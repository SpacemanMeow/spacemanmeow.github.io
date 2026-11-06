---
layout: page
title: Tag
subtitle: Jelajahi semua artikel berdasarkan topik — mulai dari aplikasi anggaran dan daftar tugas hingga jam flip dan pemantau CPU.
permalink: /id/tags/
description: "Jelajahi semua artikel Meow Apps Studio berdasarkan topik: aplikasi catatan keuangan, daftar tugas, pelacak kebiasaan, widget, jam flip, dan pemantau CPU."
lang: id
---

{%- comment -%}
  Halaman pengelompokan tag: mengelompokkan otomatis berdasarkan tags pada front matter artikel (fitur bawaan Jekyll).
  Tautan tag di bagian bawah artikel menuju ke anchor #tag-slug pada halaman ini.
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
