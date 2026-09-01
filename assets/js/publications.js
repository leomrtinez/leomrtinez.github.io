/* Interactive behaviour for the publication list: inline PDF viewer and
 * copy-to-clipboard on the BibTeX "Cite" panels.
 *
 * Upgrades every <a data-pdf-viewer href="..."> badge into a modal that embeds
 * the file, and leaves the badge as a plain link when the upgrade is not
 * appropriate. Install as assets/js/publications.js and load it with
 *     <script src="{{ base_path }}/assets/js/publications.js" defer></script>
 * at the end of _layouts/single.html (or in the publications page front matter).
 *
 * Design notes
 * ------------
 * - The <iframe> is created on demand and destroyed on close, so opening the
 *   page never downloads a multi-megabyte PDF the visitor did not ask for.
 * - Mobile browsers (notably iOS Safari) do not render PDFs inside an iframe;
 *   they show a blank box or force a download. On narrow viewports and on
 *   coarse-pointer devices the script therefore does nothing and lets the
 *   native link behaviour take over.
 */

(function () {
  "use strict";

  var MIN_WIDTH = 768; // below this, defer to the browser's own PDF handling

  var modal = document.getElementById("pdf-modal");
  if (!modal) return;

  var frameHost = modal.querySelector(".pdf-modal__frame");
  var titleEl = modal.querySelector(".pdf-modal__title");
  var downloadEl = modal.querySelector("#pdf-modal-download");
  var lastFocused = null;

  function canEmbed() {
    return (
      window.innerWidth >= MIN_WIDTH &&
      window.matchMedia("(pointer: fine)").matches
    );
  }

  function open(href, title) {
    lastFocused = document.activeElement;

    var iframe = document.createElement("iframe");
    iframe.src = href;
    iframe.title = title || "Document";
    iframe.setAttribute("loading", "lazy");
    frameHost.replaceChildren(iframe);

    titleEl.textContent = title || "";
    downloadEl.href = href;

    modal.hidden = false;
    document.body.classList.add("pdf-modal-open");
    modal.querySelector(".pdf-modal__close").focus();
  }

  function close() {
    modal.hidden = true;
    frameHost.replaceChildren(); // drop the iframe, stop the download
    document.body.classList.remove("pdf-modal-open");
    if (lastFocused) lastFocused.focus();
  }

  document.addEventListener("click", function (event) {
    var trigger = event.target.closest("[data-pdf-viewer]");
    if (trigger) {
      if (!canEmbed()) return; // fall through to the plain link
      event.preventDefault();
      open(trigger.getAttribute("href"), trigger.dataset.pdfTitle);
      return;
    }
    if (event.target.closest("[data-pdf-close]")) {
      event.preventDefault();
      close();
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && !modal.hidden) close();
  });
})();


/* Copy-to-clipboard for the BibTeX panels.
 *
 * The button ships hidden and is revealed only where the Clipboard API is
 * available, so it never appears as a control that does nothing. The BibTeX
 * itself is plain text in the page either way, ready to be selected by hand.
 */
(function () {
  "use strict";

  if (!navigator.clipboard) return;

  document.querySelectorAll(".pub-cite__copy").forEach(function (button) {
    button.hidden = false;
  });

  document.addEventListener("click", function (event) {
    var button = event.target.closest(".pub-cite__copy");
    if (!button) return;

    var code = button.parentElement.querySelector("code");
    if (!code) return;

    navigator.clipboard.writeText(code.textContent).then(
      function () {
        var previous = button.textContent;
        button.textContent = "Copied";
        button.classList.add("is-copied");
        window.setTimeout(function () {
          button.textContent = previous;
          button.classList.remove("is-copied");
        }, 1800);
      },
      function () {
        button.textContent = "Press Ctrl+C";
      }
    );
  });
})();
