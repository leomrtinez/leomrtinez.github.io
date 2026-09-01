/* ==========================================================================
   Publication list
   Consumed by _includes/publications_generated.html, which is produced by
   scripts/generate_publications.py from _bibliography/my_bibliography.bib.

   Install: save as _sass/_publications.scss and add
       @import "publications";
   at the end of the import block in assets/css/main.scss.
   ========================================================================== */

.publication-item {
  margin-bottom: 1.6em;

  p {
    margin: 0 0 0.2em;
    line-height: 1.45;
  }
}

.pub-title {
  font-weight: 700;
  font-size: 1em;
}

.pub-authors {
  font-size: 0.9em;

  strong {
    /* The site owner's name; kept bold but not recoloured, so the emphasis
       reads as authorship rather than as a link. */
    font-weight: 700;
  }
}

.pub-venue {
  font-size: 0.85em;
  color: mix($text-color, $background-color, 65%);
}

.pub-links {
  margin-top: 0.5em !important;
}

/* Bordered link badge, sized to sit on the same baseline as the venue line. */
.pub-badge {
  display: inline-block;
  padding: 0.15em 0.7em;
  border: 1px solid mix($link-color, $background-color, 45%);
  border-radius: 3px;
  font-size: 0.75em;
  font-weight: 600;
  letter-spacing: 0.02em;
  line-height: 1.6;
  color: $link-color;
  text-decoration: none;
  transition: background-color 0.15s ease, border-color 0.15s ease;

  & + .pub-badge {
    margin-left: 0.4em;
  }

  &:hover,
  &:focus {
    background-color: mix($link-color, $background-color, 8%);
    border-color: $link-color;
    text-decoration: none;
  }

  &:focus-visible {
    outline: 2px solid $link-color;
    outline-offset: 2px;
  }
}

/* Attribution required by the article's Creative Commons licence. Sits under
   the link badges, deliberately small: it is a legal notice, not content. */
.pub-license {
  margin-top: 0.35em !important;
  font-size: 0.68em;
  line-height: 1.3;
  color: mix($text-color, $background-color, 50%);
}

@media (prefers-reduced-motion: reduce) {
  .pub-badge {
    transition: none;
  }
}

/* --------------------------------------------------------------------------
   Modal PDF viewer (assets/js/pdf-viewer.js)
   -------------------------------------------------------------------------- */

.pdf-modal[hidden] {
  display: none;
}

.pdf-modal {
  position: fixed;
  inset: 0;
  z-index: 1000;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 3vh 3vw;
}

.pdf-modal__backdrop {
  position: absolute;
  inset: 0;
  background-color: rgba(0, 0, 0, 0.55);
}

.pdf-modal__panel {
  position: relative;
  display: flex;
  flex-direction: column;
  /* LibSass (sassc, used by jekyll-sass-converter 2.x) treats min() and max()
     as Sass functions rather than passing the CSS ones through, and rejects
     mixed units. Expressed with max-width instead so it compiles on both
     LibSass and Dart Sass. */
  width: 100%;
  max-width: 1000px;
  height: 94vh;
  background-color: $background-color;
  border-radius: 4px;
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.35);
  overflow: hidden;
}

.pdf-modal__bar {
  display: flex;
  align-items: center;
  gap: 0.75em;
  padding: 0.6em 0.9em;
  border-bottom: 1px solid mix($text-color, $background-color, 15%);
}

.pdf-modal__title {
  flex: 1 1 auto;
  min-width: 0;
  font-size: 0.85em;
  font-weight: 600;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.pdf-modal__close {
  flex: none;
  padding: 0 0.3em;
  border: 0;
  background: none;
  font-size: 1.5em;
  line-height: 1;
  color: mix($text-color, $background-color, 70%);
  cursor: pointer;

  &:hover,
  &:focus-visible {
    color: $text-color;
  }
}

.pdf-modal__frame {
  flex: 1 1 auto;
  min-height: 0;

  iframe {
    display: block;
    width: 100%;
    height: 100%;
    border: 0;
  }
}

/* Prevent the page behind the modal from scrolling while it is open. */
body.pdf-modal-open {
  overflow: hidden;
}
