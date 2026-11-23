#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建产物静态性能预算 — 轻量、可复现、无需外部 API。

用法（仓库根目录，需先完成构建）：python3 scripts/perf_budget.py

PSI/Lighthouse 受配额限流（HTTP 429）时仍可运行：只检查产物体积与阻塞
资源，不追求真实 CWV 分数。阈值基于 2026-11-23 实测基线加余量；任何
一项超预算即 FAIL（退出码 1），CI 的 `Perf budget` 步骤调用本脚本。
真实 CWV 仍须按 seo/SITE-AUDIT.md §6 人工补测，不能用本脚本替代。
"""
import os
import re
import sys

SITE = "_site"
IMG_EXT = (".webp", ".avif", ".png", ".jpg", ".jpeg")
LIMITS = {
    "home_html_bytes": 100 * 1024,
    "main_css_bytes": 80 * 1024,
    "single_image_bytes": 400 * 1024,
    "home_images_bytes": 10 * 1024 * 1024,
    "asset_count": 8,
    "head_sync_scripts": 0,
}


def walk_files():
    for root, _dirs, files in os.walk(SITE):
        for f in files:
            yield os.path.join(root, f)


def kb(n):
    return f"{n / 1024:.1f} KB"


def mb(n):
    return f"{n / 1048576:.2f} MB"


def main():
    if not os.path.isdir(SITE):
        print(f"FATAL: {SITE}/ not found — run scripts/build.sh first", file=sys.stderr)
        return 1

    def size(path):
        return os.path.getsize(path) if os.path.exists(path) else 0

    html_path = os.path.join(SITE, "index.html")
    html = open(html_path, encoding="utf-8").read() if os.path.exists(html_path) else ""
    ref_imgs = set(re.findall(r'(?:src|href)="(/assets/[^"?#]+(?:\.webp|\.avif|\.png|\.jpe?g))"', html))
    ref_bytes = sum(size(os.path.join(SITE, p.lstrip("/"))) for p in ref_imgs)

    assets = [p for p in walk_files()
              if p.endswith((".js", ".css")) and "/assets/" in p]
    images = [p for p in walk_files() if p.lower().endswith(IMG_EXT)]
    largest = max((size(p) for p in images), default=0)

    head = html.split("</head>")[0] if html else ""
    sync_scripts = len(re.findall(
        r'<script(?![^>]*\b(?:defer|async|type="application/ld\+json"))[^>]*\bsrc=', head))

    values = [
        ("首页 HTML 体积", size(html_path), LIMITS["home_html_bytes"], kb, "≤ 100 KB"),
        ("主 CSS 体积", size(os.path.join(SITE, "assets/css/main.css")),
         LIMITS["main_css_bytes"], kb, "≤ 80 KB"),
        ("单张图片上限", largest, LIMITS["single_image_bytes"], kb, "≤ 400 KB"),
        ("首页引用图片总量", ref_bytes, LIMITS["home_images_bytes"], mb, "≤ 10 MB"),
        ("JS/CSS 文件数", len(assets), LIMITS["asset_count"], str, "≤ 8"),
        ("head 同步脚本数", sync_scripts, LIMITS["head_sync_scripts"], str, "= 0"),
    ]

    print("=" * 72)
    print(" 静态性能预算 / Perf budget  (基于产物，非真实 CWV)")
    print("=" * 72)
    fails = 0
    for name, value, limit, fmt, label in values:
        ok = value <= limit
        fails += 0 if ok else 1
        detail = f"{len(ref_imgs)} 张引用" if name == "首页引用图片总量" else ""
        print(f"  {'PASS' if ok else 'FAIL'}  {name:18s} {fmt(value):>12s} / {label:10s} {detail}")
    print("=" * 72)
    print(f" 汇总  {len(values) - fails} PASS / {fails} FAIL  (共 {len(values)} 项)")
    print(" 注：PSI 429 限流，真实 CWV 待配额恢复后按 SITE-AUDIT.md §6 人工补测。")
    print("=" * 72)
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
