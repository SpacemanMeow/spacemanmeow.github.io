---
layout: page
title: 标签
subtitle: 按主题浏览全部文章——从预算类应用、待办清单，到翻页时钟与 CPU 监控。
permalink: /zh/tags/
description: "按主题浏览 Meow Apps Studio 全部文章：预算应用、记账工具、待办清单、习惯养成、心情日记、桌面小组件、翻页时钟、CPU 监控等。"
---

{%- comment -%}
  Tag 聚合页：按站点文章 front matter 的 tags 自动分组（Jekyll 原生，无需插件）。
  文章底部 / 页脚的 tag 链接指向本页对应锚点（#tag-slug）。
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
        <span class="tag-index__meta">{% if site.lang == 'zh' %}{{ post.date | date: '%Y年%-m月%-d日' }}{% else %}{{ post.date | date: '%b %-d, %Y' }}{% endif %}</span>
      </li>
      {% endfor %}
    </ul>
  </section>
  {% endfor %}
</div>
