# 工程上下文（供 AI / 自动化工具快速上手）

> 本文件是**给 AI 看的工程说明**，不是对外文档（对外是 `README.md`）。
> 目标：任何 AI 读取本文件后即可直接开展工作，无需用户再解释背景。
> 最后更新：2026-11-17。若与代码/SEO 文档冲突，**以代码与 `seo/SITE-AUDIT.md` / `SEO-I18N-PLAYBOOK.md` 为准**，并更新本文件。

---

## 0. 一句话定位

一个用 **Jekyll** 构建的**静态多语言 SEO 内容站**（品牌 Meow Apps Studio，域名 `spacemanmeow.com`），为 11 款 Android/iOS App 做 SEO 落地页、博客/指南、术语表、更新日志（Release Note）；5 种语言（en/zh/id/ms/th）分别构建后合并为单一 `_site/`，部署到 GitHub Pages。

---

## 1. 必须首先知道的 10 条规则（红线速查）

1. **预览只认 `_site/`**：本地 `:4000` 是 `python3 -m http.server 4000` 指向 `_site/`，无任何自动重建。任何源文件改动（文章、模板、CSS、图片）必须跑一次构建才能生效。快速预览用 `SKIP_PAGEFIND=1 bash scripts/build.sh`；**最终验收/部署必须完整构建**（否则 D12 搜索索引不能验收）。
2. **多语言集合按构建级 `site.lang` 取集合与前缀**，绝不能用 `page.lang` 拼 URL——会静默渲染到 EN 根页或报 `Cannot sort a null object`（`SEO-I18N-PLAYBOOK.md` 红线 5）。
3. **`exclude` 写法**：不支持 `!ruby/regexp`，`*` 不跨 `/`；排除英语应用目录必须写 `_apps/`（带尾斜杠），文章用 `_posts/1*`/`_posts/2*`（红线 3-4）。
4. **URL/permalink 不轻易改**：改 URL = 破坏收录；任何路由改动前查 `SEO-I18N-PLAYBOOK.md` 红线 1 与 `SITE-AUDIT.md` D01/D04。
5. **hreflang 必须成环 + x-default**：由 `scripts/i18n_postprocess.py` 自动注入，不要手工改 `<link rel="alternate">`；改结构后跑全量校验（红线 2、D05）。
6. **非英语文章骨架/目录/插图位置必须与 EN 同源同序**（红线 10-11、D17/D18）；不是另写一篇。
7. **图片**：cover 原图 1920×1080 WebP 存 `assets/images/covers/<slug>.webp` 且**必须提交**；`-640.webp`/`-1280.webp` 是 gitignore 的构建产物，由 `skills/cover-images/scripts/generate_thumbs.py` 在构建前自动生成，不提交。
8. **Release Note 页面是生成物，不手改**：源文件在 `_release_notes*/`，由 `skills/release-notes/scripts/update_release_notes.py` 从日志生成；页面顶部标注"请勿手工编辑"。
9. **禁止提交**：`seo/data/`（GSC 导出数据）与 `skills/seo-research/scripts/gsc/`（OAuth 凭据）、生成的缩略图、`.pagefind-bin/`、`.jekyll-*`；`.nojekyll` 例外；详见 `.gitignore` 与 D15。
10. **改完跑审计**：`seo/SITE-AUDIT.md` §5 内嵌一段 Python 脚本（`AUDIT-SCRIPT-START/END` 之间），构建后整段复制执行；`FAIL` 必须清零，`BASE` 应为空。

---

## 2. 目录结构与用途

```
.
├── _config.yml / _config_{zh,id,ms,th}.yml   # 每语一份配置：lang/url/collections/defaults/permalink
├── _apps/  _apps_{zh,id,ms,th}/              # 每语 11 款 App 落地页（slug.md）
├── _posts/  _posts/{zh,id,ms,th}/            # EN 根 69 篇 + 每语 69 篇（共 345）
├── _glossary/  _glossary_{zh,id,ms,th}/      # 术语表（EN 27 篇，其它语对等）
├── _pages/  _pages/{zh,id,ms,th}/            # about/privacy/terms/search/tags 等结构页
├── _release_notes/  _release_notes_*/        # Release Note 生成物：每语 11 页 = 55 页
├── _layouts/                                  # default/app/post/guide/release-note/page/app-list/blog/glossary
├── _includes/                                 # nav/footer/post-card/related-posts/store-buttons/*-jsonld 等
├── assets/
│   ├── css/main.css                           # 11 个区块；:root 变量 + 深色主题覆盖（:19-94）
│   ├── js/{main,i18n,theme}.js                # 菜单/灯箱；语言切换与首访跳转；主题
│   └── images/
│       ├── covers/<slug>.webp                 # 封面原图（提交）+ -640/-1280 缩略图（生成）
│       ├── apps/<slug>/                       # icon.webp + 截图
│       └── blog/ favicons/ store/             # 博客图、站点图标、商店 badge
├── scripts/
│   ├── build.sh                               # 唯一正确构建入口（多语言 + i18n + Pagefind）
│   ├── i18n_postprocess.py                    # hreflang/canonical/sitemap 注入（build.sh 调用）
│   └── new-language.sh <code> <label> [short] # 新增语言脚手架（生成后仍需人工本地化，历史坑多）
├── seo/                                       # SEO 规范与台账（见 §6）
├── .github/workflows/pages-deploy.yml         # push main → 构建 → htmlproofer → Pages → IndexNow
├── _site/                                     # 最终产物（预览服务器只读这里）
├── AGENTS.md                                  # 本文件（全局上下文入口）
└── skills/                                    # SOP/工具/规则沉淀，全部中文（见下方 Skills 体系与 skills/README.md）
    ├── cover-images/                          # SKILL.md + scripts/: generate_thumbs / compress_images
    ├── i18n-rules/                            # SKILL.md + references/pitfalls
    ├── release-notes/                         # SKILL.md + scripts/update_release_notes + references/app-mappings
    ├── seo-audit/                             # SKILL.md + references/dimensions
    ├── seo-research/                          # SKILL.md + scripts/: gsc_export / md_to_html + gsc/ 凭据
    └── site-build-deploy/                     # SKILL.md + scripts/: run.sh / test.sh
```

其它顶层目录：`blog/` 等是历史/中间产物；`covers-backup-20261116/`、`only-clock-covers_assets/` 为空的历史残留，无构建作用。

### Skills 体系（SOP / 工具 / 规则的沉淀）

`skills/` 把「流程怎么走」按 **CodeBuddy Skill 格式**沉淀为自包含单元；本 `AGENTS.md` 负责「工程是什么」的全局上下文。用法：新对话/其他 AI 先读本文件建立上下文，再按具体任务读取对应 `SKILL.md`。索引见 `skills/README.md`。

- **格式**：每个 skill 是一个目录，核心 `SKILL.md` 带 YAML frontmatter（`name` 为英文 slug 标识，`description` 与正文**全部中文**）；可选 `references/`（补充规则/资料）、`scripts/`（工具）、`assets/`。
- **工具位置**：原 `tools/` 已删除，全部脚本迁到各 skill 的 `scripts/` 下（见上方目录树）；GSC OAuth 凭据随脚本就近存放（`skills/seo-research/scripts/gsc/` 被 gitignore），**GSC 导出数据统一放 `seo/data/`**（被 gitignore，与 Oct/Nov 数据一致）。需要脚本时优先用 `skills/*/scripts/`，不要在仓库里为一次性问题新建脚本（可用 `/tmp`）。
- **使用方式**：处理具体任务前读取对应 `SKILL.md`；若运行环境支持 `use_skill` 且已注册 `skills/` 路径，可直接触发。
- **发布**：`AGENTS.md` 与 `skills/` 已在全部 5 份 `_config*.yml` 中 `exclude`，不会被 Jekyll 收录或发布到 `_site/`。
- **维护约定**：流程/规则变化时同步更新对应 `SKILL.md`（必要时 `references/`）与本文件，保持三处一致。

| Skill | 何时读 | 核心内容 |
|---|---|---|
| `site-build-deploy` | 改源文件后验证、跑/排查构建、CI 部署 | 构建 5 步、快速/完整构建、预览机制、CI、D12 假阳性 |
| `release-notes` | 用户发来升级日志、更新 Release Note、处理 D20 | 日志→临时文件→补全 5 语→生成器→构建→审计 |
| `seo-audit` | 改动后验收、跑 D01–D20、排查维度失败 | 审计脚本提取执行、结果判读、维度速查 |
| `i18n-rules` | 新增/改非英语内容、hreflang、集合/exclude、新增语言 | 14 条红线、site.lang vs page.lang、历史坑 |
| `cover-images` | 换封面、文章配图、排查图片不更新/srcset | 原图/缩略图规格、模板引用、CSS 比例、换图流程 |
| `seo-research` | 查关键词、导出 GSC、更新 SEO 指标/台账 | GSC 导出、关键词库、指标月报、数据位置 |

---

## 3. 配置与多语言机制

- 5 份 config 均 `url: https://spacemanmeow.com`、`baseurl: ""`、`twitter.card: summary_large_image`；`lang` 与时区各异（en/zh/id 上海、ms 吉隆坡、th 曼谷）。
- 集合（collection）命名**按语言后缀区分**：EN 用 `apps`/`release_notes`/`glossary`/`pages`，其它语用 `apps_<lang>` 等；permalink EN 为 `/apps/:name/`、非 EN 为 `/<lang>/apps/:name/`。
- 构建时 EN 直接写 `_site/`，各语构建到 `.jekyll-<lang>/` 后 `rsync` 合入 `_site/<lang>/`；`_data/languages.yml` 驱动 nav 语言下拉与 `i18n.js`。
- `scripts/i18n_postprocess.py` 扫描 `_site/`，按"去掉语言前缀的 slug"把 5 个版本配成一组，给每页注入 `<!-- i18n-hreflang -->` 块（每语一条 alternate + x-default 指向 EN），并生成合并 `sitemap.xml`、删除各语子 sitemap；**幂等**。不要手工维护这些标签。
- 新增语言走 `scripts/new-language.sh`，但它历史坑多（glossary sed 漏替换、feed.path 缺前导 `/`、漏建 glossary/exclude、404 写死 `/zh/`、i18n.js 旧二语兜底），执行后必须逐项复核 `SEO-I18N-PLAYBOOK.md` §7。

---

## 4. 构建、预览与部署

**唯一正确构建入口**：`bash scripts/build.sh`
```
1) python3 skills/cover-images/scripts/generate_thumbs.py           # 缺缩略图则生成（需 Pillow）
2) jekyll build --config _config.yml          # EN → _site/
3) 逐语 jekyll build --config _config_<lang>.yml → .jekyll-<lang>/ → rsync 到 _site/<lang>/
4) python3 scripts/i18n_postprocess.py --url $SITE_URL
5) Pagefind 索引（SKIP_PAGEFIND=1 可跳过；二进制缓存在 .pagefind-bin/）
```
- 快速预览（日常）：`SKIP_PAGEFIND=1 bash scripts/build.sh`，然后浏览器硬刷新。
- CI：`.github/workflows/pages-deploy.yml` → Ruby 3.4 + Python 3.12/Pillow → `JEKYLL_ENV=production SITE_URL=https://spacemanmeow.com bash scripts/build.sh` → htmlproofer → upload artifact → deploy-pages → Ping IndexNow（`indexnow-key.txt`，失败不阻断）。
- `skills/site-build-deploy/scripts/test.sh [--fast]`：CI 同款本地验证；`skills/site-build-deploy/scripts/run.sh`：jekyll serve 开发服务器。
- 预览服务器是独立进程（`python3 -m http.server 4000` 指向 `_site/`），**不随构建重启**，构建后硬刷新即可。

---

## 5. 内容类型与关键 frontmatter

| 类型 | 数量 | 关键字段 | 备注 |
|---|---|---|---|
| App | 11 × 5 语 | title/tagline/description/icon/image/lang/series/order/google_play/app_store/screenshots/faq | tagline 非 EN ≤ EN 的 1.5 倍且无新增规格数字（红线 12） |
| Post | 69 × 5 语 | date/title/description/layout(post\|guide\|docs)/tags/image/app_icon/lang/last_modified_at | 文件 `YYYY-MM-DD-slug.md`；slug 同时用于封面命名；layout=docs 的教程构成 Docs 形态（见 CONTENT-HUB-PLAN.md） |
| Guide | 属于 post（layout=guide） | 同上 + TOC | 骨架/插图/目录以 EN 为准 |
| Docs | 11 × 5 语（复用 tutorial 文章） | layout: docs/doc_order/doc_app/可选 glossary_terms | 呈现形态，URL 不变；中心页 `/docs/`（结构页） |
| Glossary | 27 × 5 语 | layout/title/description/tags/lang | `what-is-*.md` |
| Page | 9 × 5 语 | layout/permalink/nav/lang/description | 站点结构页（含 `/docs/` 中心页） |
| Release Note | 11 × 5 语 | layout: release-note/app_slug/app_title/google_play/app_store/lang/seo.type | 生成物，勿手改 |

**相关文章** `_includes/related-posts.html`：按同语言 tags 重叠取 ≤4 篇，跳过泛标签（Android/Comparison/Best Apps/App Roundup/Alternatives）；每篇文章至少带 1 个规范产品标签（11 个 App 之一），否则会跨品类——D19 硬门禁。

---

## 6. SEO 体系（工作的"宪法"）

| 文件 | 用途 |
|---|---|
| `seo/SEO-OPTIMIZATION-PLAN.md` | 总览与导航 |
| `seo/SEO-PLAYBOOK.md` | 通用方法论沉淀 |
| `seo/SEO-I18N-PLAYBOOK.md` | **多语言规范，§1 有 14 条红线**（最重要）；§7 记录历史陷阱 |
| `seo/SEO-I18N-PROGRESS.md` | 多语言任务唯一状态源 |
| `seo/SEO-KEYWORDS.md` | 跨语言关键词权威库 |
| `seo/SEO-METRICS.md` | GSC/GoatCounter 月报 |
| `seo/SEO-GOOGLE-PLAY.md` | Google Play ASO 规范 |
| `seo/SEO-PROGRESS.md` | 任务台账（注意：部分数量口径与实际不符，实测 EN posts=69、glossary=27） |
| **`seo/SITE-AUDIT.md`** | **验收规范**：D01–D20 维度总表 + §4 逐项检查点 + §5 内嵌可执行 Python 脚本（`AUDIT-SCRIPT-START/END` 之间整段复制执行；输出 PASS/FAIL/WARN，目标 `{PASS:N, FAIL:0, WARN:0}`，`BASE` 应为空） |

新增/改动功能后：**先更新对应维度与红线，再改代码**，最后跑构建 + 审计脚本。D20 是 Release Note 专项（覆盖/frontmatter/正文/标题本地化/内链）。

**seo/ 文档更新规则**（权威见 `seo/SEO-OPTIMIZATION-PLAN.md`「文档更新规则」）：只写长期价值内容——需沉淀的经验、阶段性重要进展、SOP/规则；临时性内容与一次性改动不写入；规则或有价值内容出现即当场同步，避免遗漏。D16 人工核对此项。

---

## 7. Release Note 系统（最常被要求改动的部分）

- **5 个集合** `_release_notes{,_zh,_id,_ms,_th}/` 各 11 页 → `/[lang/]apps/<slug>/release-notes/`，共 55 页。
- **数据源**：用户在对话中直接发来的升级日志（不再维护 `seo/data/` 里的文件；该目录已 gitignore，仅临时中转，跑完可不保留）。
- **生成器** `skills/release-notes/scripts/update_release_notes.py`：
  - 日志格式：`内部版本号 (版本名)` 或纯版本号 + `<en-US>/<zh-CN>/<id>/<ms>/<th>` 等标签块；**日志须自带全部 5 语言译文**（缺语言会生成空节、D20 会拦）；以 `- ` 开头的行渲染为上一项的子列表。
  - 日志名 → app slug：默认下划线转连字符，不一致时用脚本内 `SLUG_ALIASES`（meow_habit→meow-habits、meow_todo→meow-todo-list、meow_mood→meow-mood-diary、crosshair→cross-hair）。
  - 用法：`python3 skills/release-notes/scripts/update_release_notes.py [日志文件...]`，省略参数则处理 `seo/data/*_release_note` 全部。
- **收到新日志时的处理流程**（用户会把日志直接贴给你）：
  1. 写到 `seo/data/<app_slug（下划线）>_release_note`（临时文件）；
  2. **把用户日志中缺失的语言按其它语言准确翻译补全，并修正不准确/语法错误的译文**，直接整理进这个临时日志（不再有任何外部 fixes 文件）；
  3. 跑 `python3 skills/release-notes/scripts/update_release_notes.py` → 构建 → 跑审计脚本确认 D20 全 PASS；
  4. 临时文件可删除。
- `_layouts/release-note.html`：本地化简介区（三行：说明 / Google Play / App Store），双端 App 才显示第二入口；底部返回 App 链接在 layout 中统一提供（正文已去掉，避免重复）。
- `_layouts/app.html` 底部内链到本语言 Release Note 页。
- 规则位置：`SEO-I18N-PLAYBOOK.md` 红线 14、`SITE-AUDIT.md` D20。

**已接入的 11 个 App 与版本数**（2026-11-17）：meow-money-manager 31、cpu-monitor 19、only-clock 12、meow-habits 10、system-monitor 10、floating-assistant 9、meow-todo-list 8、cross-hair 8、meow-fm 5、meow-mood-diary 3、one-widget 3。

---

## 8. Cover 图片系统

- 原图：1920×1080 WebP，`assets/images/covers/<slug>.webp`，slug 取自文章文件名（去日期前缀），同一文章多语言共用。**原图必须提交 git**。
- 缩略图：`<slug>-640.webp`（640×360）与 `<slug>-1280.webp`（1280×720），由 `skills/cover-images/scripts/generate_thumbs.py` 在构建前增量生成，gitignore、不提交。
- 列表卡片 `_includes/post-card.html`：`<img src="-640" srcset="-640 640w, -1280 1280w, 原图 1920w" sizes="(max-width:768px) 92vw, 160px" loading="lazy" decoding="async" width="1920" height="1080">`。
- 文章/指南头图：原图 + `fetchpriority="high"`，**不加 lazy**（LCP 元素）。
- CSS `.post-card__cover img`：桌面与移动端均 `aspect-ratio: 1/1`、`object-fit: cover`、圆角 `var(--radius)`；列宽 160px。
- **换 cover 后必须重新构建**，预览服务器只读 `_site/`。

---

## 9. 常见任务与正确姿势

| 任务 | 做法 |
|---|---|
| 改了图片/文章/CSS 要看效果 | `SKIP_PAGEFIND=1 bash scripts/build.sh` → 硬刷新 |
| 用户发来升级日志 | 按 §7 流程整理进临时日志（补全 5 语译文）→ 跑生成器 → 构建 → 审计 |
| 新增文章 | 按 EN 骨架写 `_posts/`，非 EN 同源本地化（红线 11）；带规范产品标签；`image` 指向封面；跑 D18/D19 |
| 新增 App | 5 语各加 `_apps*/<slug>.md` + 图标/截图 + 封面；补齐全套页面/导航；必要时改 `SLUG_ALIASES` |
| 新增语言 | `scripts/new-language.sh` 后逐项复核（§3 坑位），全量构建 + D03/D05/D06 |
| 改 URL/permalink | 先查红线 1；改后必须全量构建 + 审计 + 考虑 301/重定向 |
| 验证线上分享卡片 | 公网 URL + Facebook Debugger / LinkedIn Post Inspector / Telegram @WebpageBot；WebP 在微信/iMessage 兼容性有限（必要时另备 JPG 作 og:image） |
| 跑全站审计 | 从 `seo/SITE-AUDIT.md` 的 `AUDIT-SCRIPT-START/END` 之间提取 Python 整段执行；FAIL=0 才算过 |

---

## 10. 已知坑与口径差异（避免踩坑）

- `SKIP_PAGEFIND=1` 会让 D12 报 FAIL——这是快速预览的正常现象，不是真问题；最终验收必须完整构建。
- SEO 进度文档里的数量口径可能滞后（记 66 posts/22 glossary，实测 69/27）；以文件系统实测为准。
- 模板按 `site.lang` 分支，不要改成 `page.lang`。
- 有序列表源码现在用显式 `1. 2. 3.`（不是全 `1.` 懒编号）；`- ` 开头行必须缩进 4 空格，否则会被渲染成 `2. ○ xxx`。
- 双端 App 的 `app_store: "#"` 视为无入口；生成 Release Note 页时 `app_store` 为空要写成 `""`，否则 YAML 粘连会吞掉 layout 与 hreflang。
- README 的「语言」段须与 `_data/languages.yml` 一致（D01）。
- 外部 AI/工具不要修改 `_site/`（生成物）；不要在仓库里新建临时脚本解决一次性问题——优先用 `skills/*/scripts/` 下的现有脚本，必要时写在 `/tmp`。

---

## 11. 环境提示

- 本地预览：`http://localhost:4000`（独立 http.server 进程，根目录 `_site/`）。
- 构建依赖：Ruby 3.4 + Bundler（`bundle install`）、Python 3 + Pillow（缩略图）、Node/Pagefind（CI 自动下载到 `.pagefind-bin/`）。
- 静态站无后端；没有数据库；所有 SEO/分析数据靠 `skills/seo-research/scripts/gsc_export.py` 导出到 gitignore 目录。
- 仓库含 `.gitmodules`（`assets/lib` 为 Chirpy 主题静态资源 submodule），常规工作不涉及。
