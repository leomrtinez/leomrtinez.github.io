import bibtexparser

# Charger le fichier .bib
with open("_bibliography/my_bibliography.bib") as bibfile:
    bib_database = bibtexparser.load(bibfile)

entries = bib_database.entries

# Trier par année (desc)
entries = sorted(entries, key=lambda x: x.get("year", "0"), reverse=True)

html_output = ""

for entry in entries:
    title = entry.get("title", "No title")

    authors = entry.get("author", "").replace(" and ", ", ")

    authors = authors.replace("L. Martinez", "<strong>L. Martinez</strong>")

    journal = entry.get("journal", "")
    year = entry.get("year", "")
    month = entry.get("month", "")
    doi = entry.get("doi", "")

    html_output += f"""
<div class="publication-item">
  <p class="pub-title"><strong>{title}</strong></p>
  <p class="pub-authors">{authors}</p>
  <p class="pub-venue">{journal}, {month} {year}</p>"""

    if doi:
        html_output += f"""
  https://doi.org/{doi}DOI</a>"""

    html_output += """
</div>
"""

# Écriture
with open("_includes/publications_generated.html", "w") as f:
    f.write(html_output)

print("✅ Publications générées proprement")
