#!/usr/bin/env python3
"""为 assets/images/covers/*.webp 生成响应式缩略图，供文章列表卡片和首图使用。

- <slug>-640.webp / <slug>-640.avif    640x360   桌面卡片（160px 显示，覆盖 2x DPR）
- <slug>-1280.webp / <slug>-1280.avif  1280x720  移动端全宽卡片 / 首图预载

由 build.sh 在每次构建前调用（本地与 CI 均如此）。
缩略图是构建产物，不提交到 git（见 .gitignore）；仓库只存 1920x1080 原图，
因此换 cover 时只需提交原图，构建会自动生成对应的 640/1280 缩略图，不会遗漏。

也可本地单独运行：python3 skills/cover-images/scripts/generate_thumbs.py
已存在且不比源图旧的缩略图会跳过（增量）；Pillow 缺失时会优雅降级。
"""
import os

try:
    from PIL import Image
except ImportError:
    Image = None

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
COVERS = os.path.join(ROOT, "assets", "images", "covers")
SIZES = ((640, 360), (1280, 720))
FORMATS = (("webp", {"quality": 82, "method": 6}),
           ("avif", {"quality": 50}))


def _is_source(name):
    return name.endswith(".webp") and not any(
        name.endswith("-%d.%s" % (w, fmt)) for w, _ in SIZES for fmt, _ in FORMATS
    )


def _all_up_to_date():
    """Pillow 不可用时的降级判断：所有缩略图已存在且不旧于源图则无需生成。"""
    for name in sorted(os.listdir(COVERS)):
        if not _is_source(name):
            continue
        src_mtime = os.path.getmtime(os.path.join(COVERS, name))
        base = name[:-5]
        for w, _ in SIZES:
            for fmt, _ in FORMATS:
                dst = os.path.join(COVERS, "%s-%d.%s" % (base, w, fmt))
                if not (os.path.exists(dst) and os.path.getmtime(dst) >= src_mtime):
                    return False
    return True


def main():
    if Image is None:
        if _all_up_to_date():
            print("cover thumbs: Pillow unavailable, all thumbs up-to-date, skip")
            return
        raise SystemExit(
            "cover thumbs: Pillow (PIL) required to generate missing thumbnails. "
            "Install with: python3 -m pip install Pillow"
        )
    created = skipped = 0
    for name in sorted(os.listdir(COVERS)):
        if not _is_source(name):
            continue
        src = os.path.join(COVERS, name)
        base = name[:-5]
        src_mtime = os.path.getmtime(src)
        with Image.open(src) as raw:
            im = raw.convert("RGB")
            for w, h in SIZES:
                thumb = im.resize((w, h), Image.LANCZOS)
                for fmt, save_kwargs in FORMATS:
                    dst = os.path.join(COVERS, "%s-%d.%s" % (base, w, fmt))
                    if os.path.exists(dst) and os.path.getmtime(dst) >= src_mtime:
                        skipped += 1
                        continue
                    thumb.save(dst, fmt.upper(), **save_kwargs)
                    created += 1
    print("cover thumbs: created=%d up-to-date=%d" % (created, skipped))


if __name__ == "__main__":
    main()
