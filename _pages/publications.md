---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap"> You can also find my most recent articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

*Last updated on June 2026*

## Articles

{% bibliography %}

## Thesis

<p>
  <strong>L. Martinez</strong>, "AC/DC : Automatic Crater Detection and Characterization",
  Université Paris-Saclay, 2025
</p>

<p>
  <button class="btn-thesis" onclick="openThesis()">
    📄 View thesis
  </button>
  |
  <a href="/files/Martinez_PhD_compressed_compressed.pdf" target="_blank">Download PDF</a>
</p>


<!-- Popup -->
<div id="thesisModal" class="modal">
  <div class="modal-content">
    <span class="close" onclick="closeThesis()">&times;</span>
    <iframe id="thesisFrame"></iframe>
  </div>
</div>

``

