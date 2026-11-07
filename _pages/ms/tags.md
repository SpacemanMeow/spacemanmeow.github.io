---
layout: page
title: Tag
subtitle: Terokai semua artikel mengikut topik — daripada aplikasi bajet dan senarai tugasan sehinggalah jam flip dan pemantau CPU.
permalink: /ms/tags/
description: "Terokai semua artikel Meow Apps Studio mengikut topik: aplikasi catatan kewangan, senarai tugasan, penjejak tabiat, widget, jam flip, dan pemantau CPU."
lang: ms
---

{%- comment -%}
  Halaman pengelompokan tag: mengelompok secara automatik berdasarkan tags pada front matter artikel (ciri terbina Jekyll).
  Pautan tag di bahagian bawah artikel menuju ke anchor #tag-slug pada halaman ini.
{%- endcomment -%}

{% assign tags_sorted = site.tags | sort %}
<div class="tag-index">
  {% for tag in tags_sorted %}
  {% assign tag_name = tag[0] %}
  {% assign tag_posts = tag[1] %}
  <section class="tag-index__group" id="{{ tag_name | slugify }}">
    <h2 class="tag-index__name">{{ tag_name }} <span class="tag-index__count">{{ tag_posts | size }}</span></h2>
    <ul class="tag-index__list">
      {% for post in tag_posts %}
      <li class="tag-index__item">
        <a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
        <span class="tag-index__meta">{{ post.date | date: site.data.ui[site.lang].date_format }}</span>
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endfor %}
</div>
