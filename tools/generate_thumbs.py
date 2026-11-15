#!/usr/bin/env python3
"""为 assets/images/covers/*.webp 生成响应式缩略图，供文章列表卡片使用。

- <slug>-640.webp   640x360   桌面卡片（160px 显示，覆盖 2x DPR）
- <slug>-1280.webp  1280x720  移动端全宽卡片（高分屏）

用法：
  python3 tools/generate_thumbs.py

已存在且不比源图旧的缩略图会跳过（增量）。build.sh 会在构建前自动调用本脚本，
所以每次更新 cover 后只需正常 build 即可。
"""
import os
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "assets", "images", "covers")
SIZES = ((640, 360), (1280, 720))


def main():
    created = skipped = 0
    for name in sorted(os.listdir(COVERS)):
        if not name.endswith(".webp"):
            continue
        if any(name.endswith("-%d.webp" % w) for w, _ in SIZES):
            continue
        src = os.path.join(COVERS, name)
        base = name[:-5]
        src_mtime = os.path.getmtime(src)
        with Image.open(src) as im:
            im = im.convert("RGB")
            for w, h in SIZES:
                dst = os.path.join(COVERS, "%s-%d.webp" % (base, w))
                if os.path.exists(dst) and os.path.getmtime(dst) >= src_mtime:
                    skipped += 1
                    continue
                im.resize((w, h), Image.LANCZOS).save(dst, "WEBP", quality=82, method=6)
                created += 1
    print("cover thumbs: created=%d up-to-date=%d" % (created, skipped))


if __name__ == "__main__":
    main()
