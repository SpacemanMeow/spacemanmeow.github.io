---
name: cover-images
description: 管理文章封面图 — 原始 1920x1080 WebP、生成的 -640/-1280 缩略图、列表卡片中的 srcset、LCP 头部图片以及 CSS 宽高比。在替换封面、为新文章添加图片、排查「图片没更新」或改动卡片/图片布局时使用。
---

# 封面图系统

## 文件

- 原图：`assets/images/covers/<slug>.webp`，1920×1080 WebP。`<slug>` = 去掉 `YYYY-MM-DD-` 前缀的文章文件名。同一篇文章的所有语言共享同一张图。**原图要提交到 git。**
- 缩略图：`<slug>-640.webp`（640×360）和 `<slug>-1280.webp`（1280×720）。每次构建前由 `skills/cover-images/scripts/generate_thumbs.py` 生成；被 gitignore；绝不提交。

## 生成

`bash scripts/build.sh` 会先运行 `python3 skills/cover-images/scripts/generate_thumbs.py`（增量式：跳过已是最新的文件；缺少 Pillow 时清楚报错）。只生成图片：`python3 skills/cover-images/scripts/generate_thumbs.py`。

## 页面用法

- 列表卡片 `_includes/post-card.html`：`<img src="-640.webp" srcset="-640 640w, -1280 1280w, 原图 1920w" sizes="(max-width:768px) 92vw, 160px" alt=标题 width="1920" height="1080" loading="lazy" decoding="async">`。
- 文章/指南头部：使用原图，带 `fetchpriority="high"`，**不要** `loading="lazy"`（LCP 元素）。宽高属性必须是 `1920`/`1080`。
- CSS `.post-card__cover img`：桌面和移动端都是 `aspect-ratio: 1/1`，`object-fit: cover`，`border-radius: var(--radius)`，网格列宽 160px。
- 文章头部 CSS：`aspect-ratio: 16/9`。

## 替换封面后

1. 替换 `assets/images/covers/` 中的原始 WebP（保持 1920×1080）。
2. 运行 `SKIP_PAGEFIND=1 bash scripts/build.sh` — 这会重新生成缩略图并把原图复制进 `_site/`。
3. 在浏览器中强制刷新。预览服务器只读取 `_site/`；不重新构建的话，即使源文件已改，仍会提供旧图。

## 常见错误

- 提交了缩略图（它们是构建产物）。
- 只重新运行图片生成器而没有做完整构建。
- `width/height` 属性错误（导致 CLS），或给 LCP 头部图片加了 `loading="lazy"`。
- 新增文章却没有配套的封面 slug — 检查 D08 和图片引用是否失效。
