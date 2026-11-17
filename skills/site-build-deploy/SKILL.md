---
name: site-build-deploy
description: 构建、预览和部署这个多语言 Jekyll 站点。当任何源文件发生变化（文章/应用/CSS/图片/模板）、需要在本地预览验证改动、运行或排查 scripts/build.sh，或诊断 GitHub Pages 部署与 CI 失败时使用。
---

# 站点构建、预览与部署

## 核心事实（先读）

`http://localhost:4000` 上的本地预览只是一个以 `_site/` 为根目录的 `python3 -m http.server 4000`。它**没有自动重建**。每次源文件改动后都必须重新构建，预览才会反映出来。这是「我的改动没生效」最常见的原因。

## 构建命令

```bash
# 本地快速预览（跳过 Pagefind；开发阶段使用）
SKIP_PAGEFIND=1 bash scripts/build.sh

# 完整构建（最终验证 / 部署前必需）
bash scripts/build.sh
```

每次构建后，在浏览器中强制刷新（`Cmd+Shift+R`）。

## build.sh 做了什么（按顺序）

1. `python3 skills/cover-images/scripts/generate_thumbs.py` — 生成缺失的 `-640`/`-1280` WebP 缩略图（需要 Pillow）。
2. `jekyll build --config _config.yml` — 英文站点直接写入 `_site/`。
3. 对 `zh`、`id`、`th`、`ms` 中的每一种语言：`jekyll build --config _config_<lang>.yml` 构建到 `.jekyll-<lang>/`，然后 `rsync` 到 `_site/<lang>/`。
4. `python3 scripts/i18n_postprocess.py --url $SITE_URL` — 注入 hreflang/alternate/canonical 块并生成合并后的 `sitemap.xml`。
5. Pagefind 索引 — `SKIP_PAGEFIND=1` 时跳过；否则首次会下载 v1.3.0 扩展版二进制到 `.pagefind-bin/` 并缓存。

`SITE_URL` 默认为 `https://spacemanmeow.com`。

## CI / 部署

`.github/workflows/pages-deploy.yml` 在推送到 `main`/`master`（排除 `.gitignore`、`README.md`、`LICENSE`）或手动触发时运行：

checkout → Setup Pages → Ruby 3.4（bundler 缓存）→ Python 3.12 + Pillow → `JEKYLL_ENV=production SITE_URL=... bash scripts/build.sh` → htmlproofer → 上传 artifact → deploy-pages → Ping IndexNow（`indexnow-key.txt`，`continue-on-error`）。

CI 使用**完整**构建（包含 Pagefind）。如果 CI 报 `No module named 'PIL'`，说明工作流缺少 Python/Pillow 步骤 — 但缩略图是构建产物，添加依赖前先确认是否真的需要生成。

## 改动后的验证

- 预览：从 `localhost:4000` curl 改动过的页面/图片；确认 HTTP 200 且内容符合预期。
- 全站：运行 `skills/site-build-deploy/scripts/test.sh`（或 `--fast`）执行 CI 同款 htmlproofer 检查。
- SEO 验收：运行审计脚本 — 见 `skills/seo-audit/SKILL.md`。**在 `SKIP_PAGEFIND=1` 下 D12（Pagefind）会 FAIL** — 这是预期行为，不是真实错误。

## 常见错误

- 直接编辑 `_site/` — 它是生成产物，会被覆盖。
- 替换封面图或 App 截图后忘记重新构建。
- 用快速构建做最终验证，并把 D12 的 FAIL 当成回归问题。
- 改动 `scripts/build.sh` 却没有同步更新全部五个 `_config*.yml`（路由/集合前缀必须保持一致）。
