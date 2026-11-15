#!/usr/bin/env python3
"""为 assets/images/covers/*.webp 生成响应式缩略图，供文章列表卡片使用。

- <slug>-640.webp   640x360   桌面卡片（160px 显示，覆盖 2x DPR）
- <slug>-1280.webp  1280x720  移动端全宽卡片（高分屏）

由 build.sh 在每次构建前调用（本地与 CI 均如此）。
缩略图是构建产物，不提交到 git（见 .gitignore）；仓库只存 1920x1080 原图，
因此换 cover 时只需提交原图，构建会自动生成对应的 -640/-1280 缩略图，不会遗漏。

也可本地单独运行：python3 tools/generate_thumbs.py
已存在且不比源图旧的缩略图会跳过（增量）；Pillow 缺失时会优雅降级。
"""
import os

try:
    from PIL import Image
except ImportError:
    Image = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COVERS = os.path.join(ROOT, "assets", "images", "covers")
SIZES = ((640, 360), (1280, 720))


def _all_up_to_date():
    """Pillow 不可用时的降级判断：所有缩略图已存在且不旧于源图则无需生成。"""
    for name in sorted(os.listdir(COVERS)):
        if not name.endswith(".webp"):
            continue
        if any(name.endswith("-%d.webp" % w) for w, _ in SIZES):
            continue
        src_mtime = os.path.getmtime(os.path.join(COVERS, name))
        base = name[:-5]
        for w, _ in SIZES:
            dst = os.path.join(COVERS, "%s-%d.webp" % (base, w))
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
