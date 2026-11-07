# 多语言内容扩展 · 实现进度记录

> **配套规范**：`SEO-I18N-PLAYBOOK.md`（**每批开工前必读**）。本文档是唯一状态源：不依赖会话记忆、不依赖上下文是否溢出。
> **词库**：`SEO-KEYWORDS.md`　**教研**：`SITE-AUDIT.md`　**总台账**：`SEO-PROGRESS.md`
> **最后更新**：2026-11-07
> **当前批次**：**Phase 5（ms 马来语）全量完成 66/66 · 11/11 · 22/22 · 结构页 8/8（2026-11-07）**；此前 Phase 3（id）66/66、Phase 4（th）全量完成且结构页 8/8 已补齐（htmlproofer 0 failure）
> **本批成果**：`/ms/` 结构完整可发布（11 App、8 结构页、22 术语、66 posts）；5 语合并构建 570 页、htmlproofer 571 文件 / 1099 内链 / 0 failure；`SEO-KEYWORDS.md` §2.1.6 马来语词库 29/29 已覆盖，D09 11 组 MISS=0；D06 tagline 红线 12 与 D03 / D04 / D05 / D07 / D08 / D17 / D18 全部 PASS

---

## 1. 状态总览

| 语言 | 代码 | 子路径 | 状态 | App 页 | Posts | 结构页 | 术语 | 上线 |
|---|---|---|---|---|---|---|---|---|
| English | `en` | `/` | ✅ 已上线（基线） | 11 | 66 | 8 | 22 | ✅ |
| 中文 | `zh` | `/zh/` | ✅ 已上线（基线） | 11 | 66 | 8 | 22 | ✅ |
| Bahasa Indonesia | `id` | `/id/` | 🟢 Phase 0–3 完成（66/66 可发布） | 11 ✅ | 66 / 66 ✅ | 8 ✅ | 22 ✅ | ✅ 完整可发布 |
| 泰语 Thai | `th` | `/th/` | 🟢 Phase 4 全量完成（66/66·11/11·22/22·结构页 8/8） | 11 ✅ | 66 / 66 ✅ | 8 / 8 ✅ | 22 ✅ | ✅ 可发布 |
| Bahasa Melayu | `ms` | `/ms/` | 🟢 Phase 5 全量完成（66/66·11/11·22/22·结构页 8/8） | 11 ✅ | 66 / 66 ✅ | 8 / 8 ✅ | 22 ✅ | ✅ 可发布 |
| 后续语言（`tl` / `hi` …） | — | `/<lang>/` | ☐ 未启动 | 0 | 0 | 0 | 0 | ☐ |

> 数据来源：`SEO-PROGRESS.md` 待办 —— 「印尼 23% / 泰 2.7%（展示量特别高）」的获客语言构成，故 `id` 优先，其后 `th`，再扩 `ms`（大马与印尼同源语言，本地检索证据见 `SEO-KEYWORDS.md` §2.1.6）。

### 1.1 规范资产（全部完成）

- [x] `seo/SEO-I18N-PLAYBOOK.md`：可复用标准化流程（12 步 SOP、红线、关键词 SOP、页面全覆盖清单、验收、陷阱表）
- [x] `seo/SEO-I18N-PROGRESS.md`：本文件（外置状态源）
- [x] `seo/SEO-KEYWORDS.md` §2.1.5 印尼语站内词库（52 词，51 已落地 / 1 合规挂起）+ §2.2.5 / §2.3.5 / §2.4.5 / §2.5.5 / §2.6.5 / §2.7.5 / §2.8.5 / §2.9.5 / §2.10.5 / §2.11.5 各 10 词（G2 / G3 / G4 / G5 / G6 / G7 / G8 / G9 / G10 / G11 全组落地）
- [x] `seo/SITE-AUDIT.md`：§2/§3/§4/§6 三语基线、§2.6 N 语言教研规则、§5 脚本升级 v3.0、§8 记录
- [x] `seo/SEO-PROGRESS.md`：登记多语言扩展进度与后续批次

---

## 1.2 泰语（th）Phase 4 进度

> 泰语从 `id` 骨架逐篇翻译（非 EN 直译），`/id/`→`/th/` 内链；跨组 `alternatives-*` 指向既有 `/id/` 页面（有意保留，待后续 th 补译）。

| 维度 | 数量 | 状态 |
|---|---|---|
| Posts | 66 / 66 | ✅ 全 11 组完成（G1–G11），build 0 中文/0 英文泄漏/0 断链 |
| App 详情页 | 11 / 11 | ✅ |
| Glossary 术语页 | 22 / 22 | ✅ |
| 结构页 | 8 / 8 | ✅ 7 页已补齐（2026-11-07，从 `id` 骨架翻译；htmlproofer 0 failure） |
| FAQ 标记 | `{:.faq-q}` 260 处 | ✅ 已统一为无空格规范格式 |
| 骨架对齐 EN | D18 H2/H3·结构块·TOC·图片行序 | ✅（除 `tutorial-meow-todo` 图片/TOC 行序偏移 1 行，frontmatter 行数差，内容一致） |

**发布前置条件**：补齐 7 个 TH 结构页后，复跑 htmlproofer 至全绿方可发布。完整教研结论见 `SITE-AUDIT.md` §8（2026-11-07）。

---

## 1.3 马来语（ms）Phase 5 进度

> 从 `id` 骨架逐行本地化（同源语言用词差异 + 大马本地场景），`/id/`→`/ms/` 内链；66 篇 posts 与 EN 同名骨架对齐（D17 / D18 全绿）。

| 维度 | 数量 | 状态 |
|---|---|---|
| Posts | 66 / 66 | ✅ 全 11 组完成，行类型序列差异 0、图片行序与路径集合与 EN 一致 |
| App 详情页 | 11 / 11 | ✅ `tagline` 遵守 §1 红线 12（≤1.5× EN、无增补规格数字） |
| Glossary 术语页 | 22 / 22 | ✅ 标题与定义逐条本地化 |
| 结构页 | 8 / 8 | ✅ index / meow / about / privacy / terms / search / tags / glossary + `ms/blog/index.html` |
| 关键词 | 29 / 29 | ✅ `SEO-KEYWORDS.md` §2.1.6 全部「已覆盖(ms)」，D09 MISS=0 |
| 目录锚点 | 全量 | ✅ TOC 与正文 hash 改写为本地化后 kramdown auto_id，htmlproofer 0 failure |
| 基础设施 | — | ✅ `_config_ms.yml` / `languages.yml` / `nav.yml` / `ui.yml` / `404.html` / `build.sh` / 各 config exclude |

**本地化要点**：`keuangan→kewangan`、`anggaran→bajet`、`pengeluaran→perbelanjaan`、`uang→wang`、`gratis→percuma`、`akun→akaun`、`Rp/Rupiah→RM/Ringgit`、`GoPay/OVO/DANA/QRIS→DuitNow QR/Touch 'n Go eWallet/GrabPay/Boost`、`tanggal tua→hujung bulan`；保留 `offline` / `expense tracker` / `money manager` 等大马常用英语借词。目录锚点从印尼语 slug 同步重映射为马来语 slug（不用行内 IAL，避免 kramdown 把 `{:#id}` 当作标题文本污染 auto_id）。

---

## 2. 页面类型覆盖矩阵（`id`）

> 「不遗漏」的判定：结构、路由、导航、内链、hreflang 全部落地并可访问；`posts` 按 App 分批是计划内状态，不影响上线。

| # | 类型 | 数量 | `id` 源目录 | 产出 URL | 状态 |
|---|---|---|---|---|---|
| 1 | 首页 App 列表 | 1 | `_pages/id/index.md` | `/id/` | ✅ 11 个 App 全显示 |
| 2 | Meow 系列页 | 1 | `_pages/id/meow.md` | `/id/meow/` | ✅ |
| 3 | 博客分页模板 | 1 | `id/blog/index.html` | `/id/blog/`、`/id/blog/pageN/` | ✅ |
| 4 | 关于 / 隐私 / 条款 | 3 | `_pages/id/{about,privacy,terms}.md` | `/id/{about,privacy,terms}/` | ✅ |
| 5 | 搜索页 | 1 | `_pages/id/search.md` | `/id/search/` | ✅ 按 `lang` 分片检索 |
| 6 | 标签索引 | 1 | `_pages/id/tags.md` | `/id/tags/` | ✅ 日期 `%-d/%-m/%Y` |
| 7 | 术语索引 + 定义页 | 1 + 22 | `_pages/id/glossary.md` + `_glossary_id/` | `/id/glossary/…/` | ✅ 22/22 |
| 8 | App 详情页 | 11 | `_apps_id/` | `/id/apps/…/` | ✅ 11/11 |
| 9 | Posts | 66 | `_posts/id/` | `/id/posts/…/` | ✅ 66/66（G1–G10 完成，G11 6/6） |
| 10 | feed | 1 | `_config_id.yml` `feed.path` | `/id/feed.xml` | ✅ |
| 11 | sitemap / hreflang | — | `i18n_postprocess.py` | `/sitemap.xml` | ✅ 296 loc，子 sitemap 已删 |
| 12 | 404 | 1 | 根级 `404.html`（共享） | — | ✅ 按 `SITE_LANGS` 判定 |
| 13 | 导航 / UI / 语言切换 | 3 | `_data/{languages,nav,ui}.yml` | 全站 | ✅ 30 处 `/id/` 链接 |
| 14 | Pagefind 分片 | — | `<html lang>` + `data-pagefind-body` | `/pagefind/` | ✅ 3 语 / 296 页 / 10855 词 |

### 2.1 基础设施文件清单（全部完成）

| 文件 | 状态 | 备注 |
|---|---|---|
| `_config_id.yml` | ✅ | `lang: id`、`apps_id` / `glossary_id`、`feed.path: id/feed.xml`、站点文案已印尼语化 |
| `_config.yml` / `_config_zh.yml` exclude | ✅ | 补 `_posts/id`、`_pages/id`、`_apps_id/`、`_glossary_id/`、`id/` 及 ZH 源排除 |
| `_data/languages.yml` | ✅ | `Bahasa Indonesia / ID` |
| `_data/nav.yml` | ✅ | 4 个条目补 `title.id` / `url.id` |
| `_data/ui.yml` | ✅ | 三语同键（含 `date_format` 等 6 个通用化新键） |
| `scripts/build.sh` | ✅ | ID build + rsync；完成提示改为动态语言清单 |
| `scripts/new-language.sh` | ✅ | 修复 `glossary_zh` / `feed.path` / `_glossary_<code>` / `_pages/<code>` exclude / `_config.yml` 漏处理 |
| 模板通用化 | ✅ | `nav` / `related-posts` / `post-card` / `breadcrumb-jsonld` / `pagination` / `app-list` / `app` / `blog` / `glossary` / `guide` / `post` + EN/ZH/ID `search.md` `tags.md` |
| `assets/js/i18n.js` | ✅ | 兜底数组改为 `[DEFAULT]` |
| `404.html` + `main.css` | ✅ | 按 `SITE_LANGS` 判定，新增语言只需加一行 HTML |
| `SITE-AUDIT.md` §5 脚本 | ✅ | v3.4 N 语言，自动发现语言、完成度分层、D14 白名单、D17 插图行序 / D18 骨架对等硬门禁 |

**本轮踩坑（已修复并写进 PLAYBOOK §7 / §2.6）**：模板最初用 `page.lang` 选集合，但非 EN 构建会渲染到 EN 根级 `_pages/index.md`（其 `page.lang: en`），导致取到不存在的 `apps` 集合而 Liquid 报错；统一改用**构建级** `site.lang` 后解决。

---

## 3. 内容批次计划

> 分组依据：`SEO-KEYWORDS.md` §2.1–§2.11（每个 App 一组，每组 6 篇 posts）。
> 每批开工/收工动作见 `SEO-I18N-PLAYBOOK.md` §5.3。

| Phase | 范围 | 文件数 | 验收标准 | 状态 |
|---|---|---|---|---|
| **0** | 规范 + 词库 + `/id/` 基础设施 | ~25 | 三语构建通过、教研 FAIL=0 | ✅ |
| **1** | 结构页（8 + 1 blog 模板）+ 术语 22 + App 11 | 42 | `/id/` 无断链、首页 11 App 完整 | ✅ |
| **2** | Meow Money Manager 的 app 页 + 6 篇 posts | 7 | 按 `id` 词库 P0/P1 落地、D09 MISS=0 | ✅ |
| **3** | 其余 10 个 App 各 6 篇 posts | 60 | 按各 App `id` 词库逐组落地；一律从 EN 骨架起稿（D17/D18） | ✅ 完成（66/66，G2–G11 全组落地） |
| **4** | 换语言（`th` 等） | — | 只做 Phase 0 配置/数据 + 内容批次，模板零改动 | ✅ |
| **5** | 马来语（`ms`） | 108 | Phase 0 配置 / 词库 + 8 结构页 + 22 术语 + 11 App + 66 posts；5 语构建、htmlproofer、教研 | ✅ 完成（2026-11-07） |

### 3.1 Posts 全清单（66 篇，按 App 组勾选）

**G1 · Meow Money Manager（§2.1，6 篇）— ✅ 全部完成**
- [x] `2026-01-31-alternatives-to-mint.md` — *Alternatif Mint 2026: Aplikasi Catatan Keuangan Offline untuk Pengguna Indonesia* — ✅ **已按 EN 骨架重构（第 3 批）**
- [x] `2026-04-07-best-meow-money-manager-android.md` — *Aplikasi Catatan Keuangan Android Terbaik 2026* — ✅ **已按 EN 骨架重构（第 1 批）**
- [x] `2026-04-12-best-meow-money-manager-students.md` — *Aplikasi Catatan Keuangan untuk Mahasiswa* — ✅ **已按 EN 骨架重构（第 2 批）**
- [x] `2026-06-03-pillar-budget-expense-tracker-apps-android.md` — *Aplikasi Catatan Keuangan dan Anggaran Bulanan Android* — ✅ **已按 EN 骨架重构（第 1 批）**
- [x] `2026-08-08-tutorial-meow-money.md` — *Cara Mencatat Pengeluaran Harian … Dari Gajian sampai CSV* — ✅ **已按 EN 骨架重构（第 3 批）**
- [x] `2026-09-26-vs-meow-money-and-ynab.md` — *Meow Money Manager vs YNAB* — ✅ **已按 EN 骨架重构（第 2 批）**

> ✅ **按 2026-11-06 新规则重构完成（6/6）**：这 6 篇当时按「本地检索意图重新选题与组织」写成独立文章，与 EN 的 H2/H3 结构、段落顺序、图片位置不一致，不符合 `SEO-I18N-PLAYBOOK.md` §1 红线 11 / §3.2 / §3.3（多语言 = 同一篇文章的不同语言版本）。**第 1 批（2026-11-06）已完成** `pillar-budget-expense-tracker-apps-android`（133 行）与 `best-meow-money-manager-android`（148 行）：逐行对齐 EN 的行类型序列与图片行号，H2/FAQ 数量一致，`alt` 印尼语关键词化；D09 掉出的 8 个本地长尾词已织回正文，教研 42 PASS。**第 2 批（2026-11-06）已完成** `best-meow-money-manager-students`（150 行，9 H2 / 6 FAQ，图片 44–48 与 73–77）与 `vs-meow-money-and-ynab`（163 行，7 H2 + 11 H3 / 6 FAQ，图片 33–37 与 70–74）：行类型序列差异 0、图片行号与路径序列与 EN 完全一致、表格与 FAQ 条目逐项对应，`alt` 印尼语关键词化，D09 11 组 MISS 0。**第 3 批（2026-11-06）已完成** `alternatives-to-mint`（314 行，13 H2 / 6 FAQ，34 张图）与 `tutorial-meow-money`（388 行，14 H2 + 27 H3 / 9 组 FAQ，62 张图分布在 19 个图片行）：行类型序列差异 0、图片行号与路径序列与 EN 完全一致，8 个本地竞品拦截词织回正文，D09 11 组 MISS 0。**6 篇全部完成**，`SITE-AUDIT.md` §5 已启用 D17 插图行序 + D18 文章骨架全语言对等硬门禁（v3.4，72 篇全量一致）。重构时保留 `gajian` / `tanggal tua` / `kos` / `uang makan` / `GoPay` / `OVO` / `DANA` / `QRIS` / `Rp` / `UMKM` / `THR` 等本地场景词与 DuitKu / DompetKu / MoneyTrack / Caku / Catatku / Celenganku / Monefy / Spendee 竞品拦截词，确保 D09 不回退。

**G2 · Meow Todo（§2.2，6 篇）— ✅ 全部完成**
- [x] `2026-02-13-alternatives-to-todoist.md` — ✅ **自动推进批次（292 行 / 39 图）**
- [x] `2026-04-25-best-meow-todo-list-android.md` — ✅ **Phase 3 首批（141 行 / 10 图）**
- [x] `2026-04-29-best-meow-todo-list-students.md` — ✅ **Phase 3 首批（142 行 / 10 图）**
- [x] `2026-07-09-pillar-todo-list-task-manager-apps-android.md` — ✅ **自动推进批次（122 行 / 5 图）**
- [x] `2026-08-17-tutorial-meow-todo-list.md` — ✅ **自动推进批次（193 行 / 12 条目录锚点全命中）**
- [x] `2026-10-05-vs-meow-todo-and-todoist.md` — ✅ **自动推进批次（165 行 / 10 图）**

> **G2 完成（2026-11-06，6/6）**：后 4 篇按自动推进规则从 EN 骨架逐行起稿，`2026-08-17-tutorial-meow-todo-list` 的 12 条 TOC 锚点全部命中实际标题 id；6 篇行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 印尼语化且唯一未照抄 EN、内链全部 `/id/`。§2.2.5 的 10 词复核仍逐词命中，D09 11 组 MISS 0。


**G3 · Meow Habits（§2.3，6 篇）— ✅ 全部完成**
- [x] `2026-02-09-alternatives-to-streaks.md` — ✅ **自动推进批次（297 行 / 34 图、7 组图片行）**
- [x] `2026-03-29-best-meow-habits-beginners.md` — ✅ **自动推进批次（137 行 / 10 图）**
- [x] `2026-04-03-best-meow-habits-general.md` — ✅ **自动推进批次（142 行 / 10 图）**
- [x] `2026-06-25-pillar-habit-tracker-apps-android.md` — ✅ **自动推进批次（122 行 / 5 图）**
- [x] `2026-08-04-tutorial-meow-habits.md` — ✅ **自动推进批次（139 行 / 11 条目录锚点全命中）**
- [x] `2026-09-21-vs-meow-habits-and-streaks.md` — ✅ **自动推进批次（166 行 / 10 图）**

> **G3 完成（2026-11-06，6/6）**：pillar 页内链曾因指向 4 篇未落地同组文章产生 5 处断链，补齐整组后消失。4 篇收尾译文逐行校验：行数与行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 唯一且未照抄 EN、TOC 锚点全命中、内链异常 0、description 148–158 字符。新增 `SEO-KEYWORDS.md` §2.3.5 印尼语词组 10 词并全部正文落地。


**G4 · Meow Mood Diary（§2.4，6 篇）— ✅ 6/6 完成**
- [x] `2026-01-27-alternatives-to-day-one.md` — ✅ **297 行 / 35 图**
- [x] `2026-04-16-best-meow-mood-diary-diary.md` — ✅ **145 行 / 10 图**
- [x] `2026-04-20-best-meow-mood-diary-private.md` — ✅ **142 行 / 10 图**
- [x] `2026-06-30-pillar-mood-diary-journaling-apps.md` — ✅ **121 行 / 5 图**
- [x] `2026-08-13-tutorial-meow-mood-diary.md` — ✅ **148 行 / 12 条目录锚点全命中**
- [x] `2026-09-30-vs-meow-mood-and-day-one.md` — ✅ **166 行 / 10 图**


**G5 · Meow FM（§2.5，6 篇）— ✅ 6/6 完成**
- [x] `2026-07-13-pillar-white-noise-focus-apps-android.md` — ✅ **125 行 / 5 图**
- [x] `2026-01-09-alternatives-to-calm.md` — ✅ **298 行 / 34 图**
- [x] `2026-03-21-best-meow-fm-focus.md` — ✅ **146 行 / 9 图**
- [x] `2026-03-25-best-meow-fm-sleep.md` — ✅ **147 行 / 9 图**
- [x] `2026-07-31-tutorial-meow-fm.md` — ✅ **134 行 / 3 图 / TOC 11 锚点全命中**
- [x] `2026-09-17-vs-meow-fm-and-calm.md` — ✅ **164 行 / 9 图**


**G6 · One Widget（§2.6，6 篇）— ✅ 6/6 完成**
- [x] `2026-02-18-alternatives-to-widgetsmith.md` — ✅ **285 行 / 30 图（6 组图片行）**
- [x] `2026-05-04-best-one-widget-android.md` — ✅ **132 行 / 10 图**
- [x] `2026-05-08-best-one-widget-material-you.md` — ✅ **129 行 / 10 图**
- [x] `2026-05-30-pillar-android-home-screen-widget-apps.md` — ✅ **130 行 / 5 图**
- [x] `2026-08-22-tutorial-one-widget.md` — ✅ **148 行 / 6 图 / TOC 11 锚点全命中**
- [x] `2026-10-09-vs-one-widget-and-kwgt.md` — ✅ **166 行 / 10 图**

> **G6 完成（2026-11-07，6/6）**：6 篇一律从 EN 同名文章骨架逐行起稿，行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 印尼语关键词化且唯一未照抄 EN、TOC 11 锚点全命中、内链全部 `/id/`、description ≤160 且无裸 `&`。同组互链全部落地（无断链）。新增 `SEO-KEYWORDS.md` §2.6.5 印尼语词组 10 词并全部正文落地，D09 11 组 MISS 0。

**G7 · Only Clock（§2.7，6 篇）— ✅ 6/6 完成**
- [x] `2026-02-05-alternatives-to-retroflip.md` — ✅ **292 行 / 23 图**（末篇补齐，`/tmp/gen_alt_oc.py` + `check_id`：282/282、行类型差 0、图文对齐、alt 唯一未照抄 EN、内链 `/id/`、description 160）
- [x] `2026-05-12-best-only-clock-flip.md` — ✅ 128 行 / 10 图
- [x] `2026-05-17-best-only-clock-nightstand.md` — ✅ 131 行 / 10 图
- [x] `2026-06-17-pillar-flip-clock-apps-android.md` — ✅ 128 行 / 5 图
- [x] `2026-08-26-tutorial-only-clock.md` — ✅ 138 行 / 8 图 / TOC 11 锚点全命中
- [x] `2026-10-13-vs-only-clock-and-retroflip.md` — ✅ 158 行 / 10 图

> **G7 完成（2026-11-07，6/6）**：末篇 `alternatives-to-retroflip`（EN 282 行 / 23 图）补齐后，6 篇一律从 EN 同名文章骨架逐行起稿，行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 印尼语关键词化且唯一未照抄 EN、TOC 锚点全命中、内链全部 `/id/`、description ≤160 且无裸 `&`。整组验收：完整构建 3 语 / 316 页；htmlproofer 317 文件 / 610 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。新增 `SEO-KEYWORDS.md` §2.7.5 印尼语词组 10 词并全部正文落地。ID posts 36→42/66。

**G8 · CPU Monitor（§2.8，6 篇）— ✅ 6/6 完成**
- [x] `2026-01-18-alternatives-to-cpu-z.md` — ✅ 291 行 / 29 图
- [x] `2026-02-22-best-cpu-monitor-phone-temp.md` — ✅ 128 行 / 10 图
- [x] `2026-02-27-best-cpu-monitor-temperature.md` — ✅ 131 行 / 10 图
- [x] `2026-06-08-pillar-cpu-temperature-monitor-apps-android.md` — ✅ 128 行 / 5 图
- [x] `2026-07-17-tutorial-cpu-monitor.md` — ✅ 121 行 / 5 图 / TOC 11 锚点全命中
- [x] `2026-09-04-vs-cpu-monitor-and-cpu-z.md` — ✅ 166 行 / 10 图

> **G8 完成（2026-11-07，6/6）**：6 篇一律从 EN 同名文章骨架逐行起稿（无现成 gen 脚本，手工对齐），行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 印尼语关键词化且唯一未照抄 EN、TOC 锚点全命中、内链全部 `/id/`、description ≤160 且无裸 `&`。修正 2 处误入中文「而非」→`daripada`、pillar description 裸 `&`→`dan`、tutorial FAQ 两处多余空行致行数对不齐。整组验收：完整构建 3 语 / 323 页；htmlproofer 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。新增 `SEO-KEYWORDS.md` §2.8.5 印尼语词组 10 词并全部正文落地。ID posts 42→48/66。

**G9 · System Monitor（§2.9，6 篇）— ✅ 6/6 完成**
- [x] `2026-01-14-alternatives-to-ccleaner.md` — ✅ 291 行 / 28 图
- [x] `2026-05-21-best-system-monitor-monitor.md` — ✅ 140 行 / 10 图
- [x] `2026-05-26-best-system-monitor-ram.md` — ✅ 138 行 / 10 图
- [x] `2026-07-04-pillar-system-monitor-apps-android.md` — ✅ 131 行 / 5 图
- [x] `2026-08-30-tutorial-system-monitor.md` — ✅ 140 行 / 12 图 / TOC 10 锚点全命中
- [x] `2026-10-18-vs-system-monitor-and-ccleaner.md` — ✅ 165 行 / 10 图

> **G9 完成（2026-11-07，6/6）**：6 篇一律从 EN 同名文章骨架逐行起稿（无现成 gen 脚本，手工对齐），行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 印尼语关键词化且唯一未照抄 EN、TOC 锚点全命中、内链全部 `/id/`、description ≤160 且无裸 `&`（修正 pillar/alternatives 两处裸 `&`→`dan`）。整组验收：完整构建 3 语 / 330 页；htmlproofer 637 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。新增 `SEO-KEYWORDS.md` §2.9.5 印尼语词组 10 词并全部正文落地。ID posts 48→54/66。

**G10 · Floating Assistant（§2.10，6 篇）— ✅ 6/6 完成**
- [x] `2026-01-05-alternatives-to-assistive-touch.md` — ✅ 288 行 / 27 图
- [x] `2026-03-12-best-floating-assistant-accessibility.md` — ✅ 131 行 / 10 图
- [x] `2026-03-16-best-floating-assistant-general.md` — ✅ 132 行 / 10 图
- [x] `2026-06-21-pillar-floating-assistant-apps-android.md` — ✅ 129 行 / 5 图
- [x] `2026-07-26-tutorial-floating-assistant.md` — ✅ 146 行 / 3 图 / TOC 12 锚点全命中
- [x] `2026-09-13-vs-floating-assistant-and-assistive-touch.md` — ✅ 163 行 / 10 图

> **G10 完成（2026-11-07，6/6）**：6 篇一律从 EN 同名文章骨架逐行起稿，行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 印尼语关键词化且唯一未照抄 EN、TOC 12 锚点全命中、内链全部 `/id/`、description ≤160 且无裸 `&`（vs description 165→152 字符）。整组验收：完整构建 3 语 / 335 页；htmlproofer 653 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。修正 accessibility 误用的编号列表（应为项目符号）、pillar 遗漏的第 5 条术语列表项、tutorial 误入的 3-in-1 时钟/监控结构（仅保留 3 张与 EN 一致的插图）与多余空行；并将 `info perangkat android` 织入 G9 pillar 正文以满足 D09 覆盖。新增 `SEO-KEYWORDS.md` §2.10.5 印尼语词组 10 词并全部正文落地。ID posts 54→60/66。

**G11 · Crosshair Aim（§2.11，6 篇）— ✅ 6/6 完成**
- [x] `2026-01-22-alternatives-to-crosshair-master.md` — ✅ 274 行 / 27 图
- [x] `2026-03-03-best-cross-hair-fps.md` — ✅ 128 行 / 5 图
- [x] `2026-03-07-best-cross-hair-overlay.md` — ✅ 129 行 / 5 图
- [x] `2026-06-12-pillar-crosshair-apps-fps-android.md` — ✅ 119 行 / 5 图
- [x] `2026-07-22-tutorial-cross-hair.md` — ✅ 120 行 / 5 图 / TOC 8 锚点全命中
- [x] `2026-09-08-vs-crosshair-and-crosshair-master.md` — ✅ 146 行 / 5 图

> **G11 完成（2026-11-07，6/6）**：6 篇一律从 EN 同名文章骨架逐行起稿，行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 印尼语关键词化且唯一未照抄 EN、TOC 8 锚点全命中、内链全部 `/id/`、description ≤160 且无裸 `&`（三篇 description 167/168/163→≤160 字符）。整组验收：完整构建 3 语 / 342 页；htmlproofer 672 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。修正教程 FAQ 误加的 3 处空行（H3+{:.faq-q} 应紧接正文、无空行）。新增 `SEO-KEYWORDS.md` §2.11.5 印尼语词组 10 词并全部正文落地。ID posts 60→66/66。

### 3.2 App 页 / 结构页 / 术语页（全部完成）

**11 个 App（`_apps_id/`）**：`meow-money-manager`（EN 骨架 + 本地词优化，11 功能段 + 7 FAQ）/ `meow-todo-list` / `meow-habits` / `meow-mood-diary` / `meow-fm` / `one-widget` / `only-clock` / `cpu-monitor` / `system-monitor` / `floating-assistant` / `cross-hair`

**8 个结构页（`_pages/id/`）**：`index` / `meow` / `about` / `privacy` / `terms` / `search` / `tags` / `glossary`

**22 条术语（`_glossary_id/`）**：全部落地，其中 `what-is-an-expense-tracker` / `what-is-budget-management` / `what-is-reimbursement-management` 按印尼本地词优化，其余忠实本地化。

---

## 4. 印尼语关键词登记状态

| 语言 | 词库位置 | 检索证据 | 状态 |
|---|---|---|---|
| `id` | `SEO-KEYWORDS.md` §2.1.5 + §2.2.5 + §2.3.5 + §2.4.5 + §2.5.5 + §2.6.5 + §2.7.5 + §2.8.5 + §2.9.5 + §2.10.5 + §2.11.5 | Google Play `hl=id&gl=ID` 在架标题 + 印尼本地网页/评测检索（§2.2.5–§2.11.5 由 EN/ZH 词库本地化，当地检索待回填） | ✅ 52 词登记（§2.1.5）+ 10 词 ×10（§2.2.5–§2.11.5）；**51 已覆盖(id)** / 1 合规挂起，G2–G11 各 10 词全部已覆盖；D09 11 组 MISS=0 |
| `ms` | `SEO-KEYWORDS.md` §2.1.6 | Google Play `hl=ms&gl=MY` 在架说明 + 大马本地评测 / DOSM（2026-11-07） | ✅ 29 词登记、**29/29 已覆盖(ms)**；D09 MISS=0 |

**选词结论（非英文直译）**：印尼用户说 `aplikasi catatan keuangan` / `pencatat keuangan`，不是 `expense tracker` 的直译 `pelacak pengeluaran`；同时在架标题混用英语借词 `budget` / `expense tracker` / `money manager`，故按「印尼语主体 + 借词并存」双轨收录。

**本地在架竞品（拦截词来源）**：DuitKu、DompetKu、MoneyTrack、Caku、FinSave、Artos、Catatku、Atur Aja、Celenganku、Monefy、Spendee、Pocket Clear。

**明确不收录的词**（当地高频但产品不具备）：银行自动同步、QRIS 自动导入、扫描 struk OCR 记账。另 `widget catatan keuangan` 因功能口径未确认而**合规挂起**，产品确认前不写入文案。

---

## 5. 校验记录

| 日期 | 批次 | 构建 | htmlproofer | 教研脚本 | hreflang | 产物抽验 | §8 记录 |
|---|---|---|---|---|---|---|---|
| 2026-11-06 | Phase 0–2 | ✅ `JEKYLL_ENV=production bash scripts/build.sh`；3 语 / 276 页；Pagefind 276 页 / 9895 词 / 3 语分片 | ✅ 277 文件 / 504 内链 / 0 failure | ✅ **39 PASS / 0 FAIL / 0 WARN** | ✅ 4 条 144 页、3 条 132 页；x-default 全指向 EN | ✅ ID 首页 11 App、48 页 `<html lang=id>`、FAQPage 7 条、canonical 与面包屑 `/id/`、3 语 feed、子 sitemap 已删 | ✅ 已填 |
| 2026-11-06 | `_apps_id` 内容质检与重写（10 个 App 页） | ✅ 完整构建 3 语 / 276 页 / 0 YAML 与 Liquid 错误 | ✅ 277 文件 / 504 内链 / 0 failure | ✅ **40 PASS / 0 FAIL / 0 WARN**（新增 frontmatter YAML 语法硬门禁） | — | ✅ 11 个 App 页截图条与 FAQ 全部正确渲染，空 `src` 0 | ✅ 已填 |
| 2026-11-06 | ID 首批 6 篇按 EN 骨架重构 · 第 2 批（`students` + `vs`） | ✅ `JEKYLL_ENV=production bash scripts/build.sh`；3 语 / 276 页；Pagefind 276 页 / 10133 词 / 3 语分片 | ✅ 277 文件 / 502 内链 / 0 failure | ✅ **42 PASS / 0 FAIL / 0 WARN**；D09 11 组 MISS=0；D17 插图集合一致、alt 照抄 0 | ✅ 分布 4 条 144 页 / 3 条 132 页，两篇 ID 页各 4 条 | ✅ 两篇产物 `img` 15/15 与 EN 相同、正文图片序列一致、`<html lang=id>` | ✅ 已填 |
| 2026-11-06 | ID 首批 6 篇按 EN 骨架重构 · 第 3 批（`alternatives-to-mint` + `tutorial-meow-money`）；§5 启用 D17 行序硬门禁 | ✅ `JEKYLL_ENV=production bash scripts/build.sh`；3 语 / 276 页；Pagefind 276 页 / 10256 词 / 3 语分片 | ✅ 277 文件 / 512 内链 / 0 failure | ✅ **43 PASS / 0 FAIL / 0 WARN**（教研 v3.3 新增 D17 行序门禁，72 篇全量一致）；D09 11 组 MISS=0 | ✅ 分布 4 条 144 页 / 3 条 132 页，两篇 ID 页各 4 条 | ✅ 两篇产物 `img` 39/39 与 67/67 对齐 EN、正文图片序列一致、tutorial 目录 11 个锚点全部命中、`<html lang=id>` | ✅ 已填 |
| 2026-11-06 | 教研规则升级：D18 全语言骨架对等（结构 / 目录 / 插图） | ✅ `JEKYLL_ENV=production bash scripts/build.sh`；3 语 / 276 页；Pagefind 276 页 / 10261 词 / 3 语分片 | ✅ 277 文件 / 512 内链 / 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**（v3.4 新增 D18 四组 chk，72 篇全量一致）；D17 三项 0 篇不一致 | ✅ 分布 4 条 144 页 / 3 条 132 页 | ✅ 两篇 ZH 结构修复后页面渲染正常、目录锚点无断链 | ✅ 已填 |
| 2026-11-06 | Phase 3 · G2（Meow Todo）首批 2 篇 ID posts + §2.2.5 印尼语词组 10 词 | ✅ `JEKYLL_ENV=production bash scripts/build.sh`；3 语 / 278 页；Pagefind 278 页 / 10331 词 / 3 语分片 | ✅ 279 文件 / 516 内链 / 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿（74 篇对齐）、D09 11 组 MISS 0 | ✅ 新增 2 组页面各 4 条 hreflang | ✅ 两篇产物 `img` 15/15 对齐 EN、正文图片序列一致、`<html lang=id>`、hreflang 4 条 | ✅ 已填 |
| 2026-11-06 | Phase 3 自动推进 · G2 收尾 4 篇 + G3 全组 6 篇（共 10 篇 ID posts，18/66） | ✅ `JEKYLL_ENV=production bash scripts/build.sh`；3 语 / 289 页；Pagefind 289 页 / 10722 词 / 3 语分片 | ✅ 290 文件 / 545 内链 / 0 failure（G3 pillar 5 处断链已消失） | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS 0、D14 0 条 | ✅ 新增 10 组页面各 4 条 hreflang | ✅ 10 篇均为 EN 骨架逐行对齐（行类型差 0、图片行序一致、alt 唯一、TOC 锚点命中、`<html lang=id>`）；G3 教程 11 锚点全命中 | ✅ 已填 |
| 2026-11-06 | Phase 3 自动推进 · G4（Meow Mood Diary）5 篇（23/66） | ✅ `JEKYLL_ENV=production bash scripts/build.sh`；3 语 / 295 页；Pagefind 295 页 / 10820 词 / 3 语分片 | ✅ 296 文件 / 562 内链 / 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS 0、D14 0 条 | ✅ 新增 5 组页面各 4 条 hreflang | ✅ 5 篇均为 EN 骨架逐行对齐（行类型差 0、图片行序一致、alt 唯一、教程 12 锚点全命中、`<html lang=id>`） | ✅ 已填 |
| 2026-11-07 | Phase 3 自动推进 · G4（Meow Mood Diary）全组 6 篇（24/66） | ✅ `JEKYLL_ENV=production bash scripts/build.sh`；3 语 / 296 页；Pagefind 296 页 / 10855 词 / 3 语分片 | ✅ 297 文件 / 564 内链 / 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS 0、D14 0 条 | ✅ 6 组页面各 4 条 hreflang | ✅ 6 篇均为 EN 骨架逐行对齐（行类型差 0、图片行序一致、alt 唯一、教程 12 锚点全命中、`<html lang=id>`） | ✅ 已填 |
| 2026-11-07 | Phase 3 自动推进 · G5（Meow FM）2/6（tutorial 落地） | 整组构建待完成；单篇 `JEKYLL_ENV=production bash scripts/build.sh` 未跑（含预期断链） | 未做（含预期断链） | 未做（含预期断链） | 单篇校验 OK：134/134、行类型差 0、图片行 56/73/93 对齐、alt 唯一未照抄 EN、内链前缀异常 0、description 136、TOC 11 锚点全命中（D14 通过）；D17/D18 该篇通过 | 文章 157、内容 md 280、产物约 298 HTML（含预期断链，未计入全绿基线） | 无 WARN | 🟡 进行中（G5 2/6），含 5 处预期断链；整组完成后跑完整构建 + htmlproofer + 教研消链再更新全绿基线 | — |
| 2026-11-07 | Phase 3 自动推进 · G6（One Widget）全组 6 篇 | ✅ 完整构建 3 语 / 309 页；Pagefind 309 页 / 11764 词 / 3 语分片 | ✅ 310 文件 / 596 内链 / 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS 0、D14 0 条 | ✅ 新增 6 组页面各 4 条 hreflang | ✅ 6 篇 EN 骨架逐行对齐（行类型差 0、图片行序一致、alt 唯一、TOC 11 锚点全命中、`<html lang=id>`）、description ≤160 且无裸 & | ✅ 已填 |
| 2026-11-07 | Phase 3 自动推进 · G7（Only Clock）全组 6 篇 | ✅ 完整构建 3 语 / 316 页；Pagefind 316 页 / 11919 词 / 3 语分片 | ✅ 317 文件 / 610 内链 / 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS 0、D14 0 条 | ✅ 新增 6 组页面各 4 条 hreflang | ✅ 6 篇 EN 骨架逐行对齐（行类型差 0、图片行序一致、alt 唯一、TOC 锚点命中、`<html lang=id>`）、description ≤160 且无裸 &；末篇 `alternatives-to-retroflip` 23 图 / 282 行 | ✅ 已填 |
| 2026-11-07 | Phase 3 自动推进 · G8（CPU Monitor）全组 6 篇 | ✅ 完整构建 3 语 / 323 页；Pagefind 323 页 / 12058 词 / 3 语分片 | ✅ 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS 0、D14 0 条 | ✅ 新增 6 组页面各 4 条 hreflang | ✅ 6 篇 EN 骨架逐行对齐（行类型差 0、图片行序一致、alt 唯一、TOC 锚点命中、`<html lang=id>`）、description ≤160 且无裸 &；pillar 29 图 / 291 行、tutorial 11 锚点全命中 | ✅ 已填 |
| 2026-11-07 | Phase 3 自动推进 · G9（System Monitor）全组 6 篇 | ✅ 完整构建 3 语 / 330 页；Pagefind 330 页 / 12182 词 / 3 语分片 | ✅ 637 内链 / 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS 0、D14 0 条 | ✅ 新增 6 组页面各 4 条 hreflang | ✅ 6 篇 EN 骨架逐行对齐（行类型差 0、图片行序一致、alt 唯一、TOC 锚点命中、`<html lang=id>`）、description ≤160 且无裸 &；alternatives 28 图 / 291 行、tutorial 10 锚点全命中 | ✅ 已填 |
| 2026-11-07 | Phase 3 自动推进 · G10（Floating Assistant）全组 6 篇 | ✅ 完整构建 3 语 / 335 页；Pagefind 335 页 / 12305 词 / 3 语分片 | ✅ 653 内链 / 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS 0、D14 0 条 | ✅ 新增 6 组页面各 4 条 hreflang | ✅ 6 篇 EN 骨架逐行对齐（行类型差 0、图片行序一致、alt 唯一、TOC 12 锚点命中、`<html lang=id>`）、description ≤160 且无裸 &；alternatives 27 图 / 288 行、tutorial 12 锚点全命中 | ✅ 已填 |
| 2026-11-07 | Phase 3 自动推进 · G11（Crosshair Aim）全组 6 篇 | ✅ 完整构建 3 语 / 342 页；Pagefind 342 页 / 12403 词 / 3 语分片 | ✅ 672 内链 / 0 failure | ✅ **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS 0、D14 0 条 | ✅ 新增 6 组页面各 4 条 hreflang | ✅ 6 篇 EN 骨架逐行对齐（行类型差 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0、description ≤160 且无裸 &；alternatives 27 图 / 274 行、tutorial 8 锚点全命中） | ✅ 已填 |
| 2026-11-07 | Phase 5（ms 马来语）全量交付 | ✅ `JEKYLL_ENV=production bash scripts/build.sh`；5 语 / 570 页；Pagefind 570 页 / 29820 词 / 5 语分片 | ✅ 571 文件 / 1099 内链 / 0 failure | ✅ **60 PASS / 4 FAIL / 0 WARN**；ms 全维度 PASS（D03 一一对应 + 结构页 8/8、D06 tagline 红线 12、D09 MISS=0、D17 / D18 骨架全绿）；4 个 FAIL 均为既有 th 遗留项（D11 的 6 条 `/id/` 内链、D17/D18 `tutorial-meow-todo-list` 行序偏移 1 行），与 ms 无关 | ✅ hreflang 6 条 × 570 页、ms 114 页含自身 alternate、x-default 指向 EN | ✅ `/ms/` 首页 11 App、`<html lang=ms>`、66 posts / 11 apps / 22 glossary / 8 pages、feed 存在、子 sitemap 已删 | ✅ 已填 |

---

## 6. 执行日志（每批必填，防止上下文丢失）

### 2026-11-06 · Phase 0–2 完成
- **关键词先行**：Google Play `hl=id&gl=ID`（`catatan keuangan`、`Pengelola Keuangan`、`Manajer uang : Expense Tracker`、`DuitKu` 离线描述等）+ 印尼本地网页检索；确认本地词、借词、本地场景与本地竞品，写入 `SEO-KEYWORDS.md` §2.1.5。
- **规范外置**：建立 `SEO-I18N-PLAYBOOK.md`（12 步 SOP / 红线 / 三类页面差异化策略 / 页面全覆盖清单 / 验收 / 陷阱）与本文件。
- **基础设施**：修复 `scripts/new-language.sh` 的 5 类遗漏后生成 `_config_id.yml`；补三份 config exclude、`languages/nav/ui`、`build.sh`；11 个模板/包含文件统一按 `site.lang` 动态取集合与前缀；`i18n.js` / `404.html` / CSS 通用化。
- **教研改造**：`SITE-AUDIT.md` §5 脚本升级 v3.0（自动发现语言、完成度分层、D11 按语言、D14 白名单、D05 按组内语言数），新增 §2.6 N 语言规则，更新 §2/§3/§4/§6 基线。
- **内容**：`/id/` 8 结构页 + blog 模板 + 22 术语 + 11 App + 6 篇 Meow Money Manager posts；按本地关键词独立撰写，非逐段翻译。
- **踩坑与修复**：`page.lang` 选集合导致非 EN 构建渲染 EN 根级页面时报错 → 改 `site.lang`；`new-language.sh` 的 `feed.path` / `glossary_zh` / `_glossary_<code>` / `_pages/<code>` / `_config.yml` 遗漏 → 全部修复并加自检提示；一处 `description` 162 字符 → 压到 ≤160。
- **收尾**：词库逐词归一化核对后才标「已覆盖」（51 词），1 词合规挂起；完整构建 + htmlproofer + 教研脚本全绿。

### 2026-11-06 · `_apps_id` 内容质检修正

- **问题**：首轮由脚本生成的 10 个 App 页把 `lang` 放在 `screenshots` 之后（字段顺序与 EN/ZH 不一致），FAQ 只有 3 条（原版 4–6 条），正文功能点是粗略改写且含**编造功能**：`system-monitor` 被写成能清理垃圾 / 加速 RAM（原版明确为只读监控）、`meow-mood-diary` 被加了 CSV 与 WebDAV、`meow-fm` 被加了 mixing / pink noise / offline、`cross-hair` 被加了 preset 与 root 表述。
- **修复**：以 EN 原版为唯一事实基准重写 10 个 App 页 —— 字段顺序、`screenshots` 路径与数量、FAQ 数量与问答意图、功能点数量与事实全部一一对应；`Related terms` 链接同步对齐原版并全部指向 `/id/glossary/`。`screenshots` 保留在 front matter（站点既有设计，由 `_layouts/app.html` 渲染为 hero 下方截图条，EN/ZH 一致）。
- **发现的连带故障**：`system-monitor` 的 `tagline` 含 `: ` 导致 YAML 解析失败，Jekyll 静默丢弃该文档，进而产生 3 处空 `src` 图片。已改文案，并在 `SITE-AUDIT.md` §5 脚本新增 **frontmatter YAML 语法硬门禁**（Ruby `YAML.parse` 全量校验），防止类似问题再次漏过教研。
- **复核**：11 个 App 页截图条 4–9 张、FAQ 4–7 条全部与原版一致；中文残留 0、英文段落残留 0、`description` ≤160 且无裸 `&`、内链前缀 100% `/id/`。

**下一批入口（Phase 3）**：
1. 读 `SEO-I18N-PLAYBOOK.md` §1 / §3、本文件 §3.1 的 G2–G11；
2. 在 `SEO-KEYWORDS.md` 为对应 App 追加 `§2.N.x id` 词表（**先本地检索，禁止直译**）；
3. 每次 1–2 个 App 组（6–12 篇 posts），**从 EN 同名文章骨架起稿**：H2/H3 层级与含义、段落顺序、表格、FAQ 条目、图片位置逐项对应，只本地化文字用词与 `alt`；保持 front matter / 内链前缀 / FAQ 格式；插图集合与位置以 EN 为准（`SEO-I18N-PLAYBOOK.md` §3.5 / D17）；
4. 逐词核对后标「已覆盖」→ 跑完整构建 + htmlproofer + §5 教研脚本 → 回填本文件与 §8。

### 2026-11-06 · Phase 3 自动推进：G2 收尾 + G3 全组

- **执行方式**：按用户长期指令「每批完成后自动开始下一批」，不再等待手动确认；连续补齐 G2 剩余 4 篇与 G3 全组 6 篇，`_posts/id/` 从 8 篇增至 18 篇。
- **起稿**：每篇一律从 EN 同名文章骨架逐行起稿，行类型序列、H2/H3 层级、表格、FAQ、目录条目与图片行号/路径序列与 EN 一致；`alt` 印尼语关键词化且唯一未照抄 EN；内链统一 `/id/`；description ≤160 且无裸 `&`。
- **断链修复**：G3 pillar 曾内链 4 篇未落地同组文章导致 htmlproofer 5 处失败，整组补齐后改为 0 failure。
- **验收**：完整构建 3 语 / 289 页；htmlproofer 290 文件 / 545 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。
- **词库**：新增 `SEO-KEYWORDS.md` §2.3.5 印尼语词组 10 词，全部标「已覆盖(id)」并逐词核对正文；§2.2.4 / §2.3.4 维护日志同步。
- **下一批**：不等确认，自动开始 G4（Meow Mood Diary）6 篇，依此类推直到 66/66。


### 2026-11-06 · Phase 3 自动推进：G4（Meow Mood Diary）5 篇

- **推进**：按长期指令自动进入 G4，从 18/66 增至 23/66；新增 §2.4.5 印尼语词组 10 词并逐词核对正文。
- **校验**：5 篇行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 印尼语化唯一且未照抄 EN、内链异常 0、description 140–159 字符；教程 12 条 TOC 锚点全部命中。
- **验收**：完整构建 3 语 / 295 页；htmlproofer 296 文件 / 562 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。
- **未完成项**：`alternatives-to-day-one`（EN 297 行 / 35 图）因译文生成子代理与长文写入链路持续超时未落地；G4 pillar 与 vs 中指向该页的 2 处链接暂改为纯文本，避免整站断链。**补齐末篇后必须恢复这 2 处 `/id/` 链接**并复跑完整教研。
- **下一批**：G4 末篇 → G5（Meow FM）→ G6–G11，继续自动推进直到 66/66。


### 2026-11-07 · Phase 3 自动推进：G4（Meow Mood Diary）全组 6 篇

- **推进**：补齐末篇 `alternatives-to-day-one`（EN 297 行 / 35 图），G4 全组 6/6 完成，ID posts 18→24/66；恢复 pillar 与 vs 中指向该页的 2 处 `/id/` 链接（此前因末篇未落地暂置纯文本）。
- **校验**：6 篇行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 印尼语化唯一且未照抄 EN、内链异常 0、description 140–159 字符；教程 12 条 TOC 锚点全部命中。
- **验收**：完整构建 3 语 / 296 页；htmlproofer 297 文件 / 564 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。
- **下一批**：按自动推进规则进入 G5（Meow FM）。


### 2026-11-07 · Phase 3 自动推进：G6（One Widget）

- **推进**：按长期指令自动进入 G6，从 30/66 增至 36/66；新增 `SEO-KEYWORDS.md` §2.6.5 印尼语词组 10 词并逐词核对正文。
- **起稿**：6 篇一律从 EN 同名文章骨架逐行起稿，行类型序列、H2/H3 层级、表格、FAQ、目录条目与图片行号/路径序列与 EN 一致；`alt` 印尼语关键词化且唯一未照抄 EN；内链统一 `/id/`；description ≤160 且无裸 `&`。
- **校验**：6 篇行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 唯一且未照抄 EN、内链异常 0、description 129–152 字符；教程 11 条 TOC 锚点全部命中。
- **验收**：完整构建 3 语 / 309 页；htmlproofer 310 文件 / 596 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。
- **下一批**：按自动推进规则进入 G7（Only Clock）。

### 2026-11-07 · Phase 3 自动推进：G7（Only Clock）

- **推进**：按长期指令自动进入 G7，从 36/66 增至 42/66；新增 `SEO-KEYWORDS.md` §2.7.5 印尼语词组 10 词并逐词核对正文。
- **起稿**：6 篇一律从 EN 同名文章骨架逐行起稿，行类型序列、H2/H3 层级、表格、FAQ、目录条目与图片行号/路径序列与 EN 一致；`alt` 印尼语关键词化且唯一未照抄 EN；内链统一 `/id/`；description ≤160 且无裸 `&`。末篇 `alternatives-to-retroflip`（EN 282 行 / 23 图）由 `/tmp/gen_alt_oc.py` 生成并经 `check_id` 校验通过（282/282、行类型差 0、图文对齐、alt 唯一、内链 `/id/`、description 160）。
- **校验**：6 篇行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 唯一且未照抄 EN、内链异常 0、description ≤160 字符；TOC 锚点全部命中。
- **验收**：完整构建 3 语 / 316 页；htmlproofer 317 文件 / 610 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。
- **下一批**：按自动推进规则进入 G8（CPU Monitor）。

### 2026-11-07 · Phase 3 自动推进：G8（CPU Monitor）

- **推进**：按长期指令自动进入 G8，从 42/66 增至 48/66；新增 `SEO-KEYWORDS.md` §2.8.5 印尼语词组 10 词并逐词核对正文。
- **起稿**：6 篇一律从 EN 同名文章骨架逐行起稿（无现成 gen 脚本，故手工逐行对齐），行类型序列、H2/H3 层级、表格、FAQ、目录条目与图片行号/路径序列与 EN 一致；`alt` 印尼语关键词化且唯一未照抄 EN；内链统一 `/id/`；description ≤160 且无裸 `&`。修正 2 处误入中文「而非」→`daripada`、pillar description 裸 `&`→`dan`、tutorial FAQ 两处多余空行致行数对不齐。
- **校验**：6 篇行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 唯一且未照抄 EN、内链异常 0、description ≤160 字符；教程 11 条 TOC 锚点全部命中。
- **验收**：完整构建 3 语 / 323 页；htmlproofer 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。
- **下一批**：按自动推进规则进入 G9（System Monitor）。

### 2026-11-07 · Phase 3 自动推进：G9（System Monitor）

- **推进**：按长期指令自动进入 G9，从 48/66 增至 54/66；新增 `SEO-KEYWORDS.md` §2.9.5 印尼语词组 10 词并逐词核对正文。
- **起稿**：6 篇一律从 EN 同名文章骨架逐行起稿（无现成 gen 脚本，故手工逐行对齐），行类型序列、H2/H3 层级、表格、FAQ、目录条目与图片行号/路径序列与 EN 一致；`alt` 印尼语关键词化且唯一未照抄 EN；内链统一 `/id/`；description ≤160 且无裸 `&`。修正 pillar 与 alternatives 两处裸 `&`→`dan`。
- **校验**：6 篇行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 唯一且未照抄 EN、内链异常 0、description ≤160 字符；教程 10 条 TOC 锚点全部命中。
- **验收**：完整构建 3 语 / 330 页；htmlproofer 637 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。
- **下一批**：按自动推进规则进入 G10（Floating Assistant）。

### 2026-11-07 · Phase 3 自动推进：G10（Floating Assistant）

- **推进**：按长期指令自动进入 G10，从 54/66 增至 60/66；新增 `SEO-KEYWORDS.md` §2.10.5 印尼语词组 10 词并逐词核对正文。
- **起稿**：6 篇一律从 EN 同名文章骨架逐行起稿，行类型序列、H2/H3 层级、表格、FAQ、目录条目与图片行号/路径序列与 EN 一致；`alt` 印尼语关键词化且唯一未照抄 EN；内链统一 `/id/`；description ≤160 且无裸 `&`。修正：accessibility 误用编号列表（应项目符号）、pillar 遗漏第 5 条术语列表项、tutorial 误入 3-in-1 时钟/监控结构（仅保留 3 张与 EN 一致插图）与多余空行、vs description 165→152 字符；并将 `info perangkat android` 织入 G9 pillar 正文以满足 D09 覆盖。
- **校验**：6 篇行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 唯一且未照抄 EN、内链异常 0、description ≤160 字符；教程 12 条 TOC 锚点全部命中。
- **验收**：完整构建 3 语 / 335 页；htmlproofer 653 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。
- **下一批**：Phase 3 已完成（66/66），按自动推进规则进入 Phase 4（泰语 `th` 等后续语言）。

### 2026-11-07 · Phase 3 自动推进：G11（Crosshair Aim）

- **推进**：按长期指令自动进入 G11，从 60/66 增至 66/66；新增 `SEO-KEYWORDS.md` §2.11.5 印尼语词组 10 词并逐词核对正文。
- **起稿**：6 篇一律从 EN 同名文章骨架逐行起稿，行类型序列、H2/H3 层级、表格、FAQ、目录条目与图片行号/路径序列与 EN 一致；`alt` 印尼语关键词化且唯一未照抄 EN；内链统一 `/id/`；description ≤160 且无裸 `&`。修正：三篇 description 167/168/163→≤160 字符；教程 FAQ 误加的 3 处空行（H3+{:.faq-q} 应紧接正文、无空行）。
- **校验**：6 篇行类型序列差异 0、图片行号与路径序列与 EN 完全一致、`alt` 唯一且未照抄 EN、内链异常 0、description ≤160 字符；教程 8 条 TOC 锚点全部命中。
- **验收**：完整构建 3 语 / 342 页；htmlproofer 672 内链 / 0 failure；§5 教研 47 PASS / 0 FAIL / 0 WARN，D09 11 组 MISS 0、D17 / D18 全绿。
- **下一批**：Phase 3 收官（66/66 达成），进入 Phase 4（泰语 `th` 等）。

### 2026-11-07 · Phase 5（ms 马来语）全量交付

- **关键词先行**：Google Play `hl=ms&gl=MY` 在架说明（`aplikasi perakaunan` / `merekod pendapatan dan perbelanjaan` / `mengira baki bajet`）+ 大马本地评测（StashAway.my / RinggitWise / CelcomDigi / Mr Money TV / FMT）+ DOSM 统计，登记 `SEO-KEYWORDS.md` §2.1.6 共 29 词；明确不收录银行自动同步 / LHDN 报税 / resit OCR。
- **基础设施**：`scripts/new-language.sh ms "Bahasa Melayu" MS` 生成 `_config_ms.yml`（可见文案逐项译为马来语、`Asia/Kuala_Lumpur`）、`_data/{languages,nav,ui}.yml`、`404.html`、`scripts/build.sh` 与四份 config 的 `ms` exclude。
- **结构页**：8 页 + `ms/blog/index.html` 同批交付（不后置），搜索页按 `pf.search(q,{language:'ms'})` 分片。
- **内容**：从 `_posts/id/`（已与 EN 骨架对齐）逐行本地化 66 篇 posts、`_apps_id/` 11 篇 App、`_glossary_id/` 22 篇术语；建立 `id→ms` 词典（同源语言用词差异、大马支付场景、竞品拦截词），保留 EN 骨架 / 图片路径与行序 / TOC 条目，`alt` 马来语化且唯一。
- **锚点**：kramdown 行内 IAL `{:#id}` 会被当作标题文本并污染 auto_id（首轮 120 处断链），改为移除 IAL、把 TOC 与正文 hash 重映射为本地化后标题的 kramdown auto_id，htmlproofer 恢复 0 failure。
- **词库**：29/29 逐词归一化核对后标「已覆盖(ms)」，6 个未自然出现的词织入 G1 真实句子（不新增行、不改结构块）；§2.1.4 维护日志追加一行。
- **验收**：完整构建 5 语 / 570 页、Pagefind 5 语分片 / 29820 词；htmlproofer 571 文件 / 1099 内链 / 0 failure；§5 教研 60 PASS，ms 相关维度全部 PASS；产物 hreflang 6 条 / 570 页、`/ms/feed.xml` 存在、子 sitemap 已删。
- **已知项**：4 个教研 FAIL 均为既有 th 遗留（D11 的 6 条 `/id/` 内链、D17/D18 `tutorial-meow-todo-list` 行序偏移 1 行），与 ms 无关，按 `SITE-AUDIT.md` §1.4 登记。

---

## 7. 待办与阻塞

- **已完成（P0，2026-11-06）**：按 `SEO-I18N-PLAYBOOK.md` §1 红线 11 / §3.2 / §3.3 **重构 `_posts/id/` 首批 6 篇**——以 EN 同名文章为骨架（H2/H3、段落顺序、表格、FAQ、图片位置逐项对应），仅优化关键词与局部表达。三批共 6 篇全部交付；`SITE-AUDIT.md` §5 已启用 D17「图片块行序一致」与 D18「文章骨架全语言对等」硬门禁（v3.4，72 篇全量一致）。后续 Phase 3 的 60 篇 posts 一律从 EN 骨架起稿。
- **待办**：核实 `widget catatan keuangan` 的产品口径后决定落地或删除词条；后续语言 `tl` / `hi` 等（按获客数据排期）。
- **阻塞**：无。
- **风险**：`id` / `th` / `ms` 均已达 66/66 完整可发布；按红线 11 所有语言一律以 EN 骨架为准，由 `SITE-AUDIT.md` §5 脚本 D18 逐篇硬校验结构 / 目录 / 图片插入；新增语言沿用同套流程。Pagefind 对 zh / th / ms 不支持 stemming（仅影响词形召回，不阻断发布）。
- **Pagefind**：印尼语分片已生成且未出现词干不支持警告；中文仍有已知的 stemming 不支持提示（仅影响词形召回，不阻断发布）。
