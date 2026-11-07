---
layout: page
title: Cari
subtitle: "Temukan aplikasi, artikel, dan istilah glosarium."
permalink: /id/search/
nav: search
lang: id
description: "Cari di seluruh situs Meow Apps Studio — aplikasi, artikel blog, dan istilah glosarium."
image: /assets/images/favicons/avatar.png
---

<div class="search">
  <input type="search" id="search-input" class="search__input" placeholder="Ketik kata kunci…" autocomplete="off" />
  <p id="search-empty" class="search__hint">Masukkan kata kunci di atas. Hasil muncul saat Anda mengetik.</p>
  <nav id="search-apps" class="search-apps" aria-label="{{ site.data.ui[site.lang].search_apps }}">
    {%- assign lang = site.lang | default: 'en' -%}
    {%- assign coll_apps = 'apps' -%}{%- if lang != 'en' -%}{%- assign coll_apps = 'apps_' | append: lang -%}{%- endif -%}
    {%- assign apps = site[coll_apps] | where_exp: 'a', 'a.hidden != true' | sort: 'order' -%}
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
  var lang = document.documentElement.lang || "id";
  var lp = lang === "en" ? "" : "/" + lang;
  var pagefind;

  function loadPF(cb) {
    if (pagefind) { cb(pagefind); return; }
    import("/pagefind/pagefind.js")
      .then(function (mod) { pagefind = mod; cb(pagefind); })
      .catch(function () { results.innerHTML = '<p class="search__hint">Indeks pencarian gagal dimuat.</p>'; });
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
          empty.textContent = 'Tidak ada hasil untuk “' + q + '”.';
          empty.style.display = "";
          return;
        }
        empty.style.display = "none";
        Promise.all(s.results.slice(0, 20).map(function (r) { return r.data(); }))
          .then(function (data) {
            results.innerHTML = data
              .filter(function (d) { return d.url.indexOf(lp + "/search") !== 0; })
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
