---
layout: page
title: 搜索
subtitle: "查找应用、文章与术语解释。"
permalink: /zh/search/
lang: zh
nav: search
description: "在 Meow Apps Studio 全站搜索——应用、博客文章与词汇表。"
image: /assets/images/favicons/avatar.png
---

<div class="search">
  <input type="search" id="search-input" class="search__input" placeholder="输入关键词搜索…" autocomplete="off" />
  <p id="search-empty" class="search__hint">在上方输入关键词，结果会随输入实时更新。</p>
  <nav id="search-apps" class="search-apps" aria-label="我们的应用">
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
  var lang = document.documentElement.lang || "zh";
  var pagefind;

  function loadPF(cb) {
    if (pagefind) { cb(pagefind); return; }
    import("/pagefind/pagefind.js")
      .then(function (mod) { pagefind = mod; cb(pagefind); })
      .catch(function () { results.innerHTML = '<p class="search__hint">搜索索引加载失败。</p>'; });
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
          empty.textContent = "未找到“" + q + "”的相关结果。";
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
