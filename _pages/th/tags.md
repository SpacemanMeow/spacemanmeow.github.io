---
layout: page
title: แท็ก
subtitle: สำรวจบทความทั้งหมดตามหัวข้อ — ตั้งแต่แอปงบประมาณและรายการสิ่งที่ต้องทำ ไปจนถึงนาฬิกาฝาพับและตัวตรวจสอบ CPU
permalink: /th/tags/
description: "สำรวจบทความทั้งหมดของ Meow Apps Studio ตามหัวข้อ: แอปบันทึกการเงิน รายการสิ่งที่ต้องทำ ตัวติดตามนิสัย วิดเจ็ต นาฬิกาฝาพับ และตัวตรวจสอบ CPU"
lang: th
---

{%- comment -%}
  หน้าจัดกลุ่มแท็ก: จัดกลุ่มอัตโนมัติตาม tags ใน front matter ของบทความ (ฟีเจอร์ built-in ของ Jekyll)
  ลิงก์แท็กที่ด้านล่างบทความจะเชื่อมไปยัง anchor #tag-slug บนหน้านี้
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
