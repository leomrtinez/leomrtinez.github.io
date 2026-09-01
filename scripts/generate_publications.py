#!/usr/bin/env python3
"""Generate the publication list of the academic website from a BibTeX file.

Reads ``_bibliography/my_bibliography.bib`` and writes a self-contained HTML
fragment to ``_includes/publications_generated.html``, which is then included
by the Jekyll layout of the ``publications`` page.

The output is deterministic: running the script twice on an unchanged .bib
file produces a byte-identical fragment, so the generated file can safely be
tracked in Git and reviewed in diffs.

Usage
-----
    python scripts/generate_publications.py
    python scripts/generate_publications.py --bib path/to/refs.bib --out out.html

Dependencies
------------
bibtexparser >= 1.4, < 2.0  (the 2.x API is incompatible; see README)
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

import bibtexparser

# --------------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------------

#: Author name to highlight in the author list (matched case-insensitively on
#: the surname, so both "L. Martinez" and "Leo Martinez" are caught).
HIGHLIGHT_SURNAME = "Martinez"

DEFAULT_BIB = Path("_bibliography/my_bibliography.bib")
DEFAULT_OUT = Path("_includes/publications_generated.html")

#: BibTeX month macros are unquoted identifiers ("month = jun"), so the parser
#: returns the raw three-letter string. Map them to display labels and to a
#: numeric key used for sorting.
MONTHS = {
    "jan": ("Jan", 1), "feb": ("Feb", 2), "mar": ("Mar", 3),
    "apr": ("Apr", 4), "may": ("May", 5), "jun": ("Jun", 6),
    "jul": ("Jul", 7), "aug": ("Aug", 8), "sep": ("Sep", 9),
    "oct": ("Oct", 10), "nov": ("Nov", 11), "dec": ("Dec", 12),
}

#: Minimal LaTeX -> Unicode table for accented characters commonly found in
#: author names exported by reference managers.
LATEX_ACCENTS = {
    r"\'e": "é", r"\`e": "è", r"\^e": "ê", r'\"e': "ë",
    r"\'a": "á", r"\`a": "à", r"\^a": "â", r'\"a': "ä",
    r"\'i": "í", r"\^i": "î", r'\"i': "ï",
    r"\'o": "ó", r"\^o": "ô", r'\"o': "ö",
    r"\'u": "ú", r"\`u": "ù", r"\^u": "û", r'\"u': "ü",
    r"\'c": "ć", r"\c c": "ç", r"\~n": "ñ",
}


# --------------------------------------------------------------------------
# Field cleaning
# --------------------------------------------------------------------------

def clean_latex(value: str) -> str:
    """Strip BibTeX protection braces and decode common LaTeX accents.

    BibTeX entries protect capitalisation with braces, e.g.
    ``{D}eep-learning on {M}ars``. Those braces must not reach the HTML.
    """
    for latex, char in LATEX_ACCENTS.items():
        value = value.replace("{" + latex + "}", char).replace(latex, char)
    value = value.replace("--", "\u2013")          # en dash
    value = re.sub(r"[{}]", "", value)             # remaining protection braces
    return re.sub(r"\s+", " ", value).strip()


def format_authors(raw: str, surname: str = HIGHLIGHT_SURNAME) -> str:
    """Return an HTML-escaped, comma-separated author list.

    The entry owner's name is wrapped in ``<strong>``. Splitting is done on the
    BibTeX ``" and "`` separator rather than by string replacement, so an
    author whose name legitimately contains "and" is not mangled.
    """
    authors = [clean_latex(a) for a in re.split(r"\s+and\s+", raw) if a.strip()]
    rendered = []
    for author in authors:
        if author.lower() == "others":
            rendered.append("<em>et al.</em>")
        elif surname.lower() in author.lower():
            rendered.append(f"<strong>{html.escape(author)}</strong>")
        else:
            rendered.append(html.escape(author))
    return ", ".join(rendered)


def sort_key(entry: dict) -> tuple[int, int]:
    """Sort key for reverse-chronological ordering (year, then month).

    Sorting on the raw year *string* — as a naive implementation does — happens
    to work for four-digit years but breaks ties arbitrarily and silently
    mis-sorts any entry with a missing or malformed year.
    """
    try:
        year = int(entry.get("year", "0"))
    except ValueError:
        year = 0
    month = MONTHS.get(entry.get("month", "").strip().lower()[:3], ("", 0))[1]
    return (year, month)


# --------------------------------------------------------------------------
# HTML rendering
# --------------------------------------------------------------------------

def render_entry(entry: dict) -> str:
    """Render a single BibTeX entry as an HTML block."""
    title = html.escape(clean_latex(entry.get("title", "Untitled")))
    authors = format_authors(entry.get("author", ""))
    venue = html.escape(clean_latex(entry.get("journal") or entry.get("booktitle", "")))
    year = html.escape(entry.get("year", "").strip())
    month = MONTHS.get(entry.get("month", "").strip().lower()[:3], ("", 0))[0]

    date = " ".join(part for part in (month, year) if part)
    venue_line = ", ".join(part for part in (venue, date) if part)

    parts = [
        '<div class="publication-item">',
        f'  <p class="pub-title">{title}</p>',
        f'  <p class="pub-authors">{authors}</p>',
        f'  <p class="pub-venue">{venue_line}</p>',
    ]

    # Link badges. Add further sources here (arXiv, PDF, code, data) as needed.
    badges = []
    doi = entry.get("doi", "").strip()
    if doi:
        url = f"https://doi.org/{html.escape(doi, quote=True)}"
        badges.append(
            f'<a class="pub-badge" href="{url}" target="_blank" '
            f'rel="noopener noreferrer" aria-label="DOI: {html.escape(doi)}">DOI</a>'
        )
    pdf = entry.get("pdf", "").strip()
    if pdf:
        # Progressive enhancement: the badge is a plain link to the file, so it
        # works with JavaScript disabled and on browsers with no inline PDF
        # renderer. assets/js/pdf-viewer.js upgrades it into a modal viewer.
        href = html.escape(pdf, quote=True)
        badges.append(
            f'<a class="pub-badge" href="{href}" data-pdf-viewer '
            f'data-pdf-title="{title}">PDF</a>'
        )
    if entry.get("url", "").strip():
        url = html.escape(entry["url"].strip(), quote=True)
        badges.append(
            f'<a class="pub-badge" href="{url}" target="_blank" '
            f'rel="noopener noreferrer">Publisher</a>'
        )
    if badges:
        parts.append('  <p class="pub-links">' + " ".join(badges) + "</p>")

    licence = entry.get("license", "").strip()
    if licence:
        parts.append(
            f'  <p class="pub-license">Published under {html.escape(licence)}</p>'
        )

    parts.append("</div>")
    return "\n".join(parts)


#: Shared modal, emitted once per page. It stays empty until a PDF badge is
#: activated, so no <iframe> is created (and no file downloaded) on page load.
PDF_MODAL = """<div class="pdf-modal" id="pdf-modal" hidden
     role="dialog" aria-modal="true" aria-labelledby="pdf-modal-title">
  <div class="pdf-modal__backdrop" data-pdf-close></div>
  <div class="pdf-modal__panel">
    <div class="pdf-modal__bar">
      <span class="pdf-modal__title" id="pdf-modal-title"></span>
      <a class="pub-badge" id="pdf-modal-download" href="#" download>Download</a>
      <button class="pdf-modal__close" type="button" data-pdf-close
              aria-label="Close the document">&times;</button>
    </div>
    <div class="pdf-modal__frame"></div>
  </div>
</div>"""


def build_html(entries: list[dict]) -> str:
    """Assemble the full fragment, newest publication first."""
    entries = sorted(entries, key=sort_key, reverse=True)
    blocks = [render_entry(e) for e in entries]
    header = (
        "<!-- Generated by scripts/generate_publications.py - do not edit by "
        "hand. Edit _bibliography/my_bibliography.bib and re-run the script. -->"
    )
    if any(e.get("pdf", "").strip() for e in entries):
        blocks.append(PDF_MODAL)
    return header + "\n\n" + "\n\n".join(blocks) + "\n"


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--bib", type=Path, default=DEFAULT_BIB,
                        help=f"input BibTeX file (default: {DEFAULT_BIB})")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help=f"output HTML fragment (default: {DEFAULT_OUT})")
    args = parser.parse_args(argv)

    if not args.bib.is_file():
        print(f"error: BibTeX file not found: {args.bib}", file=sys.stderr)
        return 1

    with args.bib.open(encoding="utf-8") as handle:
        database = bibtexparser.load(handle)

    if not database.entries:
        print(f"error: no entries parsed from {args.bib}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(build_html(database.entries), encoding="utf-8")

    print(f"Wrote {len(database.entries)} publications to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
