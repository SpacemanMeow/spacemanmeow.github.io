---
layout: page
title: Search
subtitle: "Find apps, articles and glossary terms."
permalink: /search/
nav: search
description: "Search across Meow Apps Studio — apps, blog posts, and glossary terms."
image: /assets/images/favicons/avatar.png
---

<div class="search">
  <input type="search" id="search-input" class="search__input" placeholder="Type to search…" autocomplete="off" />
  <p id="search-empty" class="search__hint">Enter a keyword above. Results update as you type.</p>
  <nav id="search-apps" class="search-apps" aria-label="Our apps">
    {%- if site.lang == 'zh' -%}
      {%- assign apps = site.apps_zh | where_exp: 'a', 'a.hidden != true' | sort: 'order' -%}
    {%- else -%}
      {%- assign apps = site.apps | where_exp: 'a', 'a.hidden != true' | sort: 'order' -%}
    {%- endif -%}
    {%- for app in apps -%}
    <a class="search-apps__item" href="{{ app.url | relative_url }}" title="{{ app.title }}">
      <img class="search-apps__icon" src="{{ app.icon | relative_url }}" alt="{{ app.title }}" width="64" height="64" loading="lazy" />
      <span class="search-apps__label">{{ app.title }}</span>
    </a>
    {%- endfor -%}
  </nav>
  <div id="search-results" class="search__results"></div>
</div>

<script>
(function () {
  var input = document.getElementById("search-input");
  var results = document.getElementById("search-results");
  var empty = document.getElementById("search-empty");
  var apps = document.getElementById("search-apps");
  var lang = document.documentElement.lang || "en";
  var pagefind;

  function loadPF(cb) {
    if (pagefind) { cb(pagefind); return; }
    import("/pagefind/pagefind.js")
      .then(function (mod) { pagefind = mod; cb(pagefind); })
      .catch(function () { results.innerHTML = '<p class="search__hint">Search index failed to load.</p>'; });
  }

  function debounce(fn, ms) { var t; return function () { clearTimeout(t); t = setTimeout(fn, ms); }; }

  var run = debounce(function () {
    var q = input.value.trim();
    if (!q) { results.innerHTML = ""; empty.style.display = ""; apps.style.display = ""; return; }
    apps.style.display = "none";
    loadPF(function (pf) {
      pf.search(q, { language: lang }).then(function (s) {
        if (!s.results.length) {
          results.innerHTML = "";
          empty.textContent = 'No results for “' + q + '”.';
          empty.style.display = "";
          return;
        }
        empty.style.display = "none";
        Promise.all(s.results.slice(0, 20).map(function (r) { return r.data(); }))
          .then(function (data) {
            results.innerHTML = data
              .filter(function (d) { return d.url.indexOf("/search") !== 0; })
              .map(function (d) {
                var title = (d.meta && d.meta.title) || d.url;
                return '<a class="search__item" href="' + d.url + '">' +
                  '<span class="search__item-title">' + title + "</span>" +
                  (d.excerpt ? '<span class="search__item-excerpt">' + d.excerpt + "</span>" : "") +
                  "</a>";
              }).join("");
          });
      });
    });
  }, 200);

  input.addEventListener("input", run);
  input.focus();
})();
</script>
