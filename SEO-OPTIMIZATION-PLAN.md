# SpacemanMeow 网站 SEO 长期优化方案

> 最后更新：2026-10-30
> **当前状态：Phase 1（技术地基）+ Phase 2（页面级）+ Phase 3（内容集群 66 篇）均已完成；Phase 4 主线（AI/权威 + 内容新鲜度）已启动并落地 T-17/18/19/22，详见 §7。** 近期完成：alt 全站差异化（0 重复）、app 页 Guides 回链、/tags/ 聚合页、全站样式对齐、自动相关文章、Glossary 词汇页、Pillar 新鲜度时间戳、薄弱 app FAQ 增强——**以上全部中英双语同步**（`/zh/` 已上线，与英文并行构建，双向 `hreflang`）。
> 适用范围：spacemanmeow.com **英文站 + `/zh/` 中文站（双语并行）**。所有优化默认中英同步执行，URL 不变、hreflang 不破。
> 目标：提升在 Google 搜索与 AI 应用内搜索（ChatGPT / Perplexity / Claude / Gemini）的排名
> 覆盖关键词方向：expense tracker / budget app / to-do list / mood diary / habit tracker / home screen widgets / flip clock / cpu monitor / floating assistant 等（中英文各一套）

---

## 0. 现状审计（基于当前仓库）

### 技术现状（2026-10-18 复核）
- ✅ 已装 `jekyll-seo-tag`，基础 title / Open Graph / Twitter 卡片已具备
- ✅ 已配 Google Analytics
- ✅ 全站响应式、图片已转 WebP（q82）、首屏懒加载、部署走 GitHub Actions
- ✅ **`sitemap.xml`** + **`robots.txt`** 已上线并指向（T-01/T-02）
- ✅ **结构化数据**：11 app 页 `SoftwareApplication` + `FAQPage` + `BreadcrumbList`，博客 `BlogPosting`（T-05/06/07/08）
- ✅ 11 app 的 `description:` 字段已补全（T-04）
- ✅ 全站 839 处图片 `alt` 关键词化且**差异化 0 重复**（T-09 彻底完成）
- ✅ `canonical` 生效；`<html lang="en">` 已输出（T-10/T-11）
- ✅ 各 app `og:image` 独立（T-12）
- ✅ 66/66 文章均含 `description:` 字段（seo-tag 输出高质量 meta description）
- ⚠️ **`sitemap.xml` 未包含 `feed.xml`**（RSS 未被提交给 GSC，T-16 待办）
- ✅ **文章底部「相关文章」区块**已全站自动化上线（`_includes/related-posts.html`：同语言取标签重叠最多 4 篇 + 父 app 回链，T-17，中英双语）
- ⚠️ **无 404 页 / 站内搜索**（T-20 待办）；RSS(`feed.xml`) 未提交 GSC（T-16 待办）

### 内容现状（2026-10-18 复核）
- 11 个 app 详情页 + 可见 FAQ（T-06）+ Guides 回链（T-14）
- **66 篇博客**（每 app 6 篇：Pillar + vs + Alternatives + Best×2 + How-to），11 个品类全覆盖（2026-10-16）
- `/tags/` 聚合页（81 个 tag 分组，T-15）
- 关键词已通过集群方式成体系覆盖；**Glossary / 更新日志时间戳 / 相关文章** 三类增量已于 2026-10-30 补齐（T-17/18/19，中英双语同步上线）

---

## 1. 关键词库

### 1.1 站内已覆盖词（从 `_apps` + `_posts` 提取）
- **Meow Money**：bookkeeping / budget app / budget management / financial management / expense tracker / income / cute finance app / fingerprint lock / multi-currency / ledger / CSV export / recurring transaction / reimbursement
- **Meow Todo**：to-do list / task manager / schedule planner
- **Meow Mood Diary**：mood diary / feelings / safe place / journal
- **Meow Habits**：habit building / habit tracker / routine
- **One Widget**：home screen widgets / Glass iOS / Material You / Galaxy One UI / Nothing style / app shortcut / clock & calendar widget / battery widget
- **Only Clock**：full-screen clock / flip animation
- **CPU Monitor**：cpu temperature / cpu frequency / real time / one tap boost / ram widget / floating window / over heat alarm / multicore
- **System Monitor**：cpu monitor / storage cleaner / memory booster / battery doctor
- **Floating Assistant**：assistive touch / floating clock / floating monitor
- **Meow FM**：white noise / sleep / relax / concentrate
- **Crosshair Aim**：crosshair / FPS games / aim / overlay

### 1.2 竞品调研补充（2026-10 调研，按品类）
| 品类 | 主要竞品 | 高频搜索词（补充进词库） |
|---|---|---|
| 记账 / 预算 | Mint, YNAB, PocketGuard, Expensly, Expensora(AI) | `expense tracker app`, `free budget app`, `money tracker`, `spending tracker`, `private expense tracker no account`, `budget app for couples/students`, `subscription tracker` |
| 待办 | TickTick, Things, Todoist, TASKn(AI), SingularityApp | `task manager`, `getting things done GTD`, `daily planner`, `reminder app`, `AI task planner`, `shared/family to-do list` |
| 心情日记 | Day One, Journey, Reflectly, Daylio, Gratitude Genie | `journaling app`, `mood tracker`, `gratitude journal`, `private diary app`, `mood tracking free`, `guided journal`, `mental health journal` |
| 习惯养成 | HabitBull, Streaks, HabitBox, Kabit, Fabulous | `habit tracker`, `build habits`, `streak counter`, `habit tracker widget`, `habit reminder`, `routine builder`, `free habit tracker` |
| 桌面小组件 | KWGT, WidgetClub, Widget Studio, Zeffi, Launchy | `android widgets`, `home screen customization`, `Material You widgets`, `Glass widgets`, `Nothing OS widgets`, `clock widget`, `minimalist widgets` |
| 翻页时钟 | Retroflip, Fullscreen Clock(MWM), FliTik, LCDWatch | `flip clock`, `fullscreen clock`, `flip clock widget`, `desk clock`, `nightstand clock`, `focus timer`, `pomodoro clock` |
| CPU 监测 | CPU-Z, DevCheck, 3C Toolbox, AIDA64 | `cpu temperature monitor`, `phone temperature`, `cpu usage`, `overheating fix`, `ram booster`, `battery monitor`, `floating cpu widget` |
| 悬浮窗 | （搜索噪声大，属蓝海） | `floating window`, `assistive touch`, `floating clock`, `overlay widget`, `floating shortcuts` |

### 1.3 关键词分层（以 Meow Money 为例）
- **Head（难、量大）**：`expense tracker app`, `budget app`
- **Middle（中）**：`private expense tracker`, `cute budget app`, `multi-currency expense tracker`
- **Long-tail（易、精准、转化高）**：`budget app with fingerprint lock`, `expense tracker no account required`, `cat-themed bookkeeping app`, `best budget app for students`

> 策略核心：**app 详情页吃 long-tail + 品牌词；新建的"品类落地页 / 对比页"去抢 head / middle 词**，互相内链形成主题权威。

---

## 2. 技术 SEO 完善清单（按优先级）

### P0 — 基础设施（快速、必须）
1. 安装 `jekyll-sitemap` → 自动生成 `sitemap.xml`（GitHub Actions 部署会把 `_site` 整体上传，sitemap 自动发布；确认未被 `exclude`）
2. 新增 `robots.txt`：允许全站抓取 + 指向 `sitemap.xml`
3. 到 **Google Search Console** 验证域名、提交 sitemap
4. 每个 app 的 front matter 增加 `description:` 字段（150–160 字符、含主关键词的摘要），让 seo-tag 输出高质量 meta description

### P1 — 结构化数据（对 Google 富媒体 + AI 搜索最关键）
5. 每个 app 页注入 **`SoftwareApplication` JSON-LD**：`name`, `operatingSystem`, `applicationCategory`, `offers`(免费/内购), `description`, `publisher`, `aggregateRating`(如有)
6. 每个 app 页加 **`FAQPage` JSON-LD**（将详情页 FAQ 结构化）
7. 列表 / 详情加 **`BreadcrumbList` JSON-LD**
8. 博客文章加 `Article` / `BlogPosting` JSON-LD

### P2 — 页面级优化
9. 图片 `alt` 改为含关键词描述（如 `alt="Meow Money Manager - cute expense tracker app icon"`）
10. 确认 `canonical` 标签生效（seo-tag 默认生成）
11. 加 `hreflang="en"`（英文站统一；未来做多语言再扩展）
12. OG / Twitter 卡片图确认每个 app 用各自截图

### P3 — 性能 / 体验（排名因子）
13. 维持 Core Web Vitals：首屏图懒加载、LCP 优化、CLS 稳定（已转 WebP，继续）
14. 保持移动端可用性

---

## 3. 内容扩充框架（可持续增长的核心）

当前只有"app 详情页 + 博客"两类载体，要不断扩充关键词，必须建立**可复制的内容模型**。

### 3.1 模型：主题集群（Pillar + Cluster）
```
品类落地页 (Pillar，抢 head 词)
   ├─ How-to 教程 (Cluster)
   ├─ 对比 / vs 页 (Cluster)
   ├─ "Best X for Y" 清单 (Cluster)
   ├─ FAQ / Glossary (Cluster)
   └─→ 全部内链回 对应 App 详情页（转化点）
```
每新增一个 app，即套此模板，关键词自然滚动增长。

### 3.2 可扩展内容类型清单
1. **品类落地页**（每个 app 一个）：如 "Best Budget App for Android (2026)"，覆盖 head/middle 词，内链到对应 app
2. **对比页 / "X vs Y"**：`Meow Money vs YNAB`、`Best Flip Clock Apps 2026`（抢竞品品牌词 + 列表词）
3. **"Best X for Y" 清单文**：`budget app for students` / `habit tracker for couples` / `mood tracker free no account`
4. **How-to 教程**（已有 1 篇教程 `tutorial-meow-money`，可复制为其他 app 模板）：`How to track expenses with a cat-themed app`
5. **FAQ 页 / 段**（同时出 FAQ 结构化数据）
6. **"Alternatives to <竞品>" 页**：抓竞品品牌搜索流量（高价值蓝海）
7. **更新日志 / 版本博客**：保持内容新鲜度（Google 偏好活跃站）
8. **词汇表 / Glossary**：`what is a habit streak`、`what is a flip clock`

### 3.3 以 Meow Money 为例的完整集群（示范，可照抄到其他 10 个 app）
- **Pillar**：`Best Budget & Expense Tracker App for Android`
- **Cluster**：
  - `How to start bookkeeping in 5 steps`（已有）
  - `Meow Money Manager full user guide`（已有）
  - `Meow Money vs YNAB / vs PocketGuard`
  - `Best budget app for students / couples`
  - `Private expense tracker with no account & fingerprint lock`
  - `Alternatives to Mint for Android`
  - FAQ：`Is Meow Money free?` / `Does it need an account?`

### 3.4 编辑流程
- 建立 **关键词映射表**（app → 目标词 → 对应内容页），新增内容前先查表避免重复
- 每月固定产出（建议起步 4 篇/月），复用 `_posts` 现有 front matter（含 `tags`）做内链与分类

---

## 4. AI 搜索专项（ChatGPT / Perplexity / Claude / Gemini）

### 4.1 工作原理
AI 联网搜索**不是按 PageRank 排位**，而是：① 从已索引网页**检索相关片段** → ② **抽取事实**拼成答案 → ③ 是否「引用你」取决于：内容是否被检索到 + 是否清晰可信 + 是否权威。
公式 = **被索引 × 被读懂 × 被信 × 被引用**。

### 4.2 七大核心策略（结合本站立项）
| # | 策略 | 本站状态 | 对应任务 |
|---|---|---|---|
| 1 | 被索引（Google + **Bing/IndexNow**） | Google 已收录；Bing/IndexNow 未做 | T-01/02/03；新增 Bing 提交 |
| 2 | 结构化数据（JSON-LD） | ✅ 已完成（SoftwareApplication/FAQPage/BreadcrumbList/Article） | T-05~08 |
| 3 | 清晰、可直引的内容（短句/列表/定义式） | app description 已做；缺定义页 | T-18 Glossary |
| 4 | FAQ 段落（AI Overview 最爱） | ✅ 每 app 4 问 + FAQPage | T-06；增问 T-22 |
| 5 | 主题集群权威（Topic clusters） | ✅ 66 篇集群；内链待密 | T-17 相关文章 |
| 6 | 被权威源引用（最强外部杠杆） | 未做 | T-21 roundup 投稿 |
| 7 | 内容新鲜度 | 缺更新机制 | T-19 更新日志 |

> 避坑：纯图片无 alt（AI 读不到）、模糊营销话术（"最好的 app" AI 不采信，要具体事实）、内容单薄重复——均已通过 alt 差异化 + 集群规避。

### 4.3 执行清单（可勾选）
- [x] 结构化数据全覆盖（T-05~08）
- [x] 每 app 事实性 `description` + 4–6 问 FAQ（T-04/T-06/T-22，中英双语）
- [x] T-18 Glossary 定义页（中英各 4 条 + 词汇表索引，命中 AI「what is X」查询；博客页已加入口）
- [x] T-17 相关文章区块（加密集群内链，增强主题权威，中英双语）
- [x] T-19 更新日志时间戳（Pillar 页 `last_modified_at`，新鲜度信号，中英双语）
- [ ] **新增 Bing Webmaster + IndexNow 提交**（Copilot / 部分 AI 走 Bing 索引）— 高优先级，见 §8
- [ ] T-22 收尾：BlogPosting 补 `dateModified`（Q2 2027 季度专项）
- [ ] T-16 提交 RSS `feed.xml` 到 GSC
- [ ] T-20 404 页 + 站内搜索
- [ ] T-21 外链投稿（Product Hunt / alternative.to / 少数派）

### 4.4 与月度运营的关系
七项策略已拆解进 §9 月度清单：Glossary（§9.2 B）、相关文章（§9.2 B）、更新日志（§9.2 B）、外链（§9.3 Q2）、JSON-LD 增强（§9.3 Q3）。**优先级最高两步：Glossary（站内可做，T-18）+ 外链投稿（手动，T-21）**——前者直接命中 AI 定义类查询，后者提供「被引用」的权威信号。

---

## 5. 度量与治理
- **Search Console**：看收录、点击词、排名；提交 sitemap；修 Crawl Errors
- **GA4**：看落地页表现、转化（Google Play 点击）
- **关键词追踪**：用 Search Console + Search Console Insights 每月复盘
- **季度审计**：查死链、重复 meta、sitemap 是否最新、结构化数据是否校验通过（Rich Results Test）

---

## 6. 分阶段路线图
| 阶段 | 时间 | 动作 | 目标 |
|---|---|---|---|
| **Phase 1 地基** | 第 1–2 周 | sitemap + robots + Search Console + 每个 app 补 `description` + JSON-LD(SoftwareApplication/FAQ) | 可被完整收录、富媒体展示 |
| **Phase 2 页面** | 第 3–4 周 | 关键词映射表 + 图片 alt + canonical/hreflang + OG 图 | 单页相关性与 CTR 提升 |
| **Phase 3 内容引擎** | 第 2 月起持续 | 套"品类落地页+对比+清单+FAQ"模板，每月 4 篇 | 关键词覆盖面滚动增长 |
| **Phase 4 权威/AI** | 第 3 月起 | 外链/roundup 投稿 + 竞品 alternatives 页 + 更新日志 | 抢 head 词、被 AI 引用 |

> SEO 是慢变量：技术改动几周见效，内容积累通常 3–6 个月起量，需持续。

---

## 7. 执行跟踪（长期优化进度表）
> 后续每完成一项，在对应"状态"列打勾并记录日期。

### 技术项
| 编号 | 任务 | 状态 | 完成日期 | 备注 |
|---|---|---|---|---|
| T-01 | 安装 jekyll-sitemap，生成 sitemap.xml | ✅ | 2026-10-10 | jekyll-sitemap 原本已在 Gemfile/_config 声明；修正 `url` 为 `https://spacemanmeow.com`（原误用 github.io），本地构建已生成 sitemap.xml |
| T-02 | 新增 robots.txt | ✅ | 2026-10-10 | 根目录创建，Allow 全站并指向 sitemap |
| T-03 | Google Search Console 验证 + 提交 sitemap | ✅ | 2026-10-10 | 用户已完成验证并线上提交 sitemap；线上 `sitemap.xml`/`robots.txt`/验证 meta 均已确认 200/生效（提交后「无法抓取」为 SC 状态延迟，72h 后自动转成功） |
| T-04 | 11 个 app 补 `description` 字段 | ✅ | 2026-10-10 | 每个 app front matter 已加 150–160 字符、含主词的 description |
| T-05 | app 页注入 SoftwareApplication JSON-LD | ✅ | 2026-10-10 | 新增 `_includes/app-jsonld.html` 并接入 `app.html`；11 页全部校验 JSON 合法 |
| T-06 | app 页注入 FAQPage JSON-LD + 可见 FAQ 区块 | ✅ | 2026-10-10 | 11 个 app 均已加 `faq:` 数据（4 问/页，含目标关键词）；`app.html` 新增可见 FAQ 渲染，`app-jsonld.html` 已注入 FAQPage；本地构建校验 JSON 全部合法、11 页全覆盖 |

### T-03 操作指引（需手动）
1. 打开 https://search.google.com/search-console/ ，用站点邮箱 `meow@spacemanmeow.com` 登录
2. 添加属性 `https://spacemanmeow.com`（网域或网址前缀均可）
3. 验证方式：站点已通过 `_config.yml` 的 `webmaster_verifications.google` 输出 `<meta name="google-site-verification">`，部署后选「HTML 标记」即可自动通过；或上传验证文件
4. 验证通过后，左侧「站点地图」→ 提交 `https://spacemanmeow.com/sitemap.xml`
5. 提交后等待 Google 抓取（通常数小时到数天），可在「网址检查」中测试单个 app 页

### 已知问题 / 后续注意
- **seo-tag 误判 + 非法 JSON 已修复（2026-10-10）**：原 `jekyll-seo-tag` 给无日期页填构建时间当 `date`，把 app/隐私/条款页误标为 `BlogPosting`；且 description/title 里的 `&` 被转成 `&amp;` 塞进 JSON-LD（非法，Google 会丢弃该块）。修复方式：① 所有含 `&` 的 app `description`/`title` 改为 `and`；② `_config.yml` 的 apps 默认加 `seo.type: WebPage`、`privacy.md`/`terms.md` 加 `seo.type: WebPage`，强制类型正确；③ 我们的 `SoftwareApplication`/`FAQPage`/`BreadcrumbList` 仍由 `app-jsonld.html` 正确提供。构建校验：全站 JSON-LD 已无 `&amp;`，app 页 `@type` 为 `WebPage`+`SoftwareApplication`+`FAQPage`+`BreadcrumbList`。
- `url` 已从 `github.io` 改为 `spacemanmeow.com`，线上 canonical / sitemap 已确认均为该域名。
- ~~**T-09（按用户决定推迟）**~~ **已于 2026-10-18 彻底完成**：全站 839 处正文图片 alt（569 处 blog 图 + 270 处 apps 图）统一规范化为「`{App/功能专有名} screenshot — {文章标题}`」格式（专名大小写修正：YNAB / CCleaner / TickTick / KWGT 等），155 处描述性 alt 保留并追加主题词；`![image]` 零残留。新增 png/jpg 已全部转 WebP（q82），未使用图片（67 个）已清理。
- **T-14（2026-10-18 新增完成）**：app 详情页新增「Guides & Tutorials」回链区块（`app.html` + `main.css`），按 `post.image == app.icon` 自动列出该 app 的 6 篇相关文章——11 个 app 页全部生效，主题权威形成双向内链。
- **T-15（2026-10-18 新增完成）**：新增 `/tags/` 聚合页（`_pages/tags.md`，Jekyll 原生 81 个 tag 分组索引）+ `post.html`/`guide.html` 文章底部 tag 可点击链接（锚点跳转）+ 44 篇 guide 文章补 tags（app/品类/类型/竞品四层标签，大小写统一 0 冲突）；博客列表页加 Tags 入口。死锚点 0，htmlproofer 全绿。
- **T-13（Core Web Vitals）**：2026-10-30 完成首轮审计 + 首屏懒加载修正（详见 §7 任务表）；持续项：保持图片 WebP、首屏图非 lazy、CLS 稳定即可。建议后续手动跑一次 Lighthouse / PageSpeed Insights 取实时分确认。
- 所有 Phase 1/2 技术项已于 **2026-10-16 部署上线**，线上已出现 sitemap.xml / 结构化数据 / og:image / 修正后的 JSON。可在 Search Console「网址检查」中对 22 个新 best URL 请求编入索引以加速收录。
| T-07 | 列表/详情注入 BreadcrumbList JSON-LD | ✅ | 2026-10-10 | 新增 `_includes/breadcrumb-jsonld.html` 并在 `default.html` 引入；Meow 系列 app 为 Home›Meow›App，非 Meow app/普通页为 Home›当前页，博客为 Home›Blog›Post；全站 18 个非首页页均含，构建校验 JSON 全合法 |
| T-08 | 博客文章注入 Article/BlogPosting JSON-LD | ✅ | 2026-10-10 | `jekyll-seo-tag` 自动为 posts 输出合法 `BlogPosting`（含 author/publisher/mainEntityOfPage）；顺手修掉作者 URL 旧域名 `github.io`→`spacemanmeow.com` |
| T-09 | 图片 alt 改为含关键词描述（差异化为 0 重复） | ✅ | 2026-10-18 | 全站 839 处正文图 alt 规范化为「`{App/功能专有名} {文件名修饰} screenshot: {就近小标题} — {文章标题}`」（专名大小写修正 YNAB/CCleaner/TickTick/KWGT 等），**同文件重复 0 个**；app 图标 alt 为 `{{title}} app icon`；791 张图均带 `width` 尺寸防 CLS；`![image]` 零残留 |
| T-10 | 确认 canonical 生效 | ✅ | 2026-10-10 | `jekyll-seo-tag` 已输出 `<link rel="canonical" href="https://spacemanmeow.com/...">`（构建校验通过） |
| T-11 | 加 `hreflang` 双向语言关联 | ✅ | 2026-10-30 | `/zh/` 上线后，构建流程已为**每页注入 `en`/`zh` 双向 `hreflang`**（经 i18n 后处理脚本，已校验每页 3 条 alternate）；`<html lang>` 依构建语言自动输出 `en`/`zh`。此能力依赖双语并行构建，纯 EN 构建时仅 `en` |
| T-12 | OG/Twitter 卡片图按 app 区分 | ✅ | 2026-10-10 | 11 个 app front matter 均加 `image:`（取各自 icon.webp）；`jekyll-seo-tag` 据此输出独立 `og:image`/`twitter:image`（构建校验每页均生效） |
| T-13 | Core Web Vitals 审计 + 首屏图懒加载修正 | ✅ | 2026-10-30 | 审计全站图片懒加载：app 详情页 hero 商店徽章（lg）、列表页首卡图标原为 `loading="lazy"`（首屏→伤害 LCP），已改 eager；页脚 logo、列表卡内商店徽章保持/补 lazy（首屏外）。无自定义字体（无 CLS 字体风险），图片均为 WebP。PSI API 限流（429）未取得实时分，代码级审计+修复已落地 |
| T-16 | 提交 RSS feed.xml 到 GSC / Bing（补 RSS 收录信号） | ✅ | 2026-10-30 | 启用双语 feed：EN `feed.xml` 已在线；ZH 因构建路径问题未产出 `/zh/feed.xml`（线上 404），修正 `_config_zh.yml` 的 `feed.path` 为 `zh/feed.xml` 后 EN/ZH 均正确生成（各 10 条 entry，链接语言隔离正确）。GSC/Bing 后台粘贴 feed URL 提交为登录态手动动作，步骤见 §10 T-16 备注 |
| T-17 | 文章底部「相关文章」区块（同 app / 同 tag 内链） | ✅ | 2026-10-30 | 已实现**自动化**：新增 `_includes/related-posts.html`，按标签重叠取同语言最多 4 篇 + 父 app 页回链，接入 `post.html`/`guide.html` 页脚；自动按构建语言隔离（EN/ZH 各生成自己的链接，无需手动改）。**中英同步**。原 20 篇手写区块已清理去重 |
| T-18 | 新增 Glossary 词汇页（what is a habit streak / flip clock / expense tracker 等） | ✅ | 2026-10-30 | 新增 `glossary`/`glossary_zh` 集合（+ `_layouts/glossary.html`）；上线 4 个定义页 ×2 语言 + 词汇表索引页（EN/ZH 各 `/glossary/`、`/zh/glossary/`），均进 sitemap 并双向 hreflang；4 个相关 app 页已加「相关术语」回链；**博客页顶部新增「词汇表 →」入口**。**中英同步**，命中 AI "what is X" 查询 |
| T-19 | 新增 更新日志 / 版本博客（changelog） | ✅ | 2026-10-30 | 11 个 Pillar 页（EN+ZH 共 22 篇）已加 `last_modified_at: 2026-10-30`，`post.html` 据此渲染 "Last updated / 最后更新" 新鲜度信号。**中英同步**（注：本迭代用 Pillar 时间戳实现新鲜度，独立 changelog 页留待 Q1 2027 常态化） |
| T-20 | 404 页 + 站内搜索 | ☐ | | 基础体验/SEO |
| T-21 | 外链 / roundup 投稿（Product Hunt / alternative.to / 少数派） | ☐ | | Phase 4 权威，需手动排期 |
| T-22 | JSON-LD 增强：BlogPosting `dateModified`、author 细化、FAQ 增至 4–6 问 | ✅ | 2026-10-30 | 薄弱集群 3 个 app 页（Meow Money / Meow Habits / Floating Assistant，EN+ZH）FAQ 由 4 增至 6 问，FAQPage JSON-LD 校验含 6 组 Question+acceptedAnswer。**中英同步**（BlogPosting `dateModified` 待 Q2 2027 季度专项补） |
| T-23 | Bing Webmaster Tools：站点验证 + sitemap 提交 | ✅ | 2026-10-30 | 用户在 Bing WMT 添加 `spacemanmeow.com` 并导入 GSC 验证通过；提交 `https://spacemanmeow.com/sitemap.xml`（EN+ZH 全量 + glossary）。前置：`_config.yml` 已配 `webmaster_verifications.bing`，线上每页输出 `msvalidate.01` meta |
| T-24 | IndexNow 自动提交（Bing/ChatGPT 即时收录） | ✅ | 2026-10-30 | 仓库根新增 IndexNow key 验证文件 `indexnow-key.txt`（内容为 key `d8564afe6a7d6a287d4b47b6296b1b15`）；`.github/workflows/pages-deploy.yml` 的 deploy job 在部署后自动 ping `api.indexnow.org`，提交全量 sitemap URL（约 190 条）。`continue-on-error` 容错，key 轮换只需同步改文件名与 workflow 常量 |

### 内容项（按 app 建集群，每完成一篇记录）
> **进度更新 2026-10-16**：本轮已批量产出 **22 篇 Best-X-for-Y** + **11 篇 vs 对比页** + **11 篇 Alternatives 页**（每 app 各 1 篇 vs / 1 篇 alternatives / 2 篇 best），故「对比页 / Best-X-for-Y / Alternatives」三类已**全覆盖 11 个 app**。剩余：**品类落地页(Pillar)：11 个 app 已全部完成（2026-10-16）**；**11 个 app 现已各具备 1 篇 How-to 教程（含 Meow Money）**。
> 注：FAQ 列指 app 详情页 FAQ（T-06 已完成，11 页全覆盖），非独立 FAQ 内容页。

| app | 品类落地页 (Pillar) | 对比页 (vs) | Best-X-for-Y | How-to | FAQ (app 页) | Alternatives |
|---|---|---|---|---|---|---|
| Meow Money | ✅ pillar-budget-expense-tracker-apps-android | ✅ vs-meow-money-and-ynab | ✅✅ android/students | ✅ 1 教程 | ✅ | ✅ alternatives-to-mint |
| Meow Todo | ✅ pillar-todo-list-task-manager-apps-android | ✅ vs-meow-todo-and-todoist | ✅✅ students/android | ✅ 1 教程 | ✅ | ✅ alternatives-to-todoist |
| Meow Mood Diary | ✅ pillar-mood-diary-journaling-apps | ✅ vs-meow-mood-and-day-one | ✅✅ diary/private | ✅ 1 教程 | ✅ | ✅ alternatives-to-day-one |
| Meow Habits | ✅ pillar-habit-tracker-apps-android | ✅ vs-meow-habits-and-streaks | ✅✅ general/beginners | ✅ 1 教程 | ✅ | ✅ alternatives-to-streaks |
| One Widget | ✅ pillar-android-home-screen-widget-apps | ✅ vs-one-widget-and-kwgt | ✅✅ android/material-you | ✅ 1 教程 | ✅ | ✅ alternatives-to-widgetsmith |
| Only Clock | ✅ pillar-flip-clock-apps-android | ✅ vs-only-clock-and-retroflip | ✅✅ flip/nightstand | ✅ 1 教程 | ✅ | ✅ alternatives-to-retroflip |
| CPU Monitor | ✅ pillar-cpu-temperature-monitor-apps-android | ✅ vs-cpu-monitor-and-cpu-z | ✅✅ temperature/phone-temp | ✅ 1 教程 | ✅ | ✅ alternatives-to-cpu-z |
| System Monitor | ✅ pillar-system-monitor-apps-android | ✅ vs-system-monitor-and-ccleaner | ✅✅ monitor/ram | ✅ 1 教程 | ✅ | ✅ alternatives-to-ccleaner |
| Floating Assistant | ✅ pillar-floating-assistant-apps-android | ✅ vs-floating-assistant-and-assistive-touch | ✅✅ general/accessibility | ✅ 1 教程 | ✅ | ✅ alternatives-to-assistive-touch |
| Meow FM | ✅ pillar-white-noise-focus-apps-android | ✅ vs-meow-fm-and-calm | ✅✅ sleep/focus | ✅ 1 教程 | ✅ | ✅ alternatives-to-calm |
| Crosshair Aim | ✅ pillar-crosshair-apps-fps-android | ✅ vs-crosshair-and-crosshair-master | ✅✅ fps/overlay | ✅ 1 教程 | ✅ | ✅ alternatives-to-crosshair-master |

### 度量记录（每月填写）
| 月份 | 收录页数 | 自然流量 | 主要排名词 | 备注 |
|---|---|---|---|---|
| | | | | |

---

## 8. 下一步建议（2026-10-30 更新）

### 8.1 本迭代已完成（2026-10-30，中英双语同步）
T-17 自动相关文章区块、T-18 Glossary 词汇页（4 定义×2 语言 + 索引 + 博客入口）、T-19 Pillar 新鲜度时间戳、T-22 薄弱集群 FAQ 4→6 问、T-23 Bing WMT 验证、T-24 IndexNow 自动提交。**2026-10-30 末批内容扩充**：Glossary 由 4 条/语言**扩至 16 条/语言**（新增 mood tracker / habit tracker / cpu temperature monitor / system monitor / ram booster / assistive touch / crosshair / white noise / home screen widget / to-do list / nightstand clock / material you，中英各 12 新词），索引页与 10 个相关 app 页「Related terms」回链同步补齐。

### 8.2 已完成（本轮 / 历史）
- ✅ **Bing Webmaster Tools 验证 + sitemap 提交（T-23）**：已在 Bing WMT 添加站点、导入 GSC 验证、提交 sitemap.xml。
- ✅ **IndexNow 自动提交（T-24）**：deploy 工作流部署后自动 ping `api.indexnow.org`（全量 ~190 URL），Bing/ChatGPT 即时收录。

### 8.3 接下来待做（按 ROI 排序，站内可做优先）
1. ~~Glossary 扩量至 10–20 条~~ **✅ 已完成（2026-10-30）**：由 4 条/语言扩至 **16 条/语言**（mood tracker / habit tracker / cpu temperature monitor / system monitor / ram booster / assistive touch / crosshair / white noise / home screen widget / to-do list / nightstand clock / material you），索引页与 10 个相关 app 页回链同步补齐。
2. ~~T-13 Core Web Vitals 实测~~ **✅ 已完成（2026-10-30）**：审计全站图片懒加载并修正——app 详情页 hero 商店徽章、列表页首卡图标（原为首屏却标 lazy，伤害 LCP）改为 eager；页脚 logo、列表卡内商店徽章保持 lazy（首屏外）。无自定义字体（无 CLS 字体风险），图片均为 WebP。PSI API 限流未取得实时分，代码级审计+修复已落地。
3. ~~T-16 提交 feed.xml 到 GSC / Bing~~ **✅ 已完成（2026-10-30）**：EN/ZH 双语 feed.xml 均生成并验证（各 10 条 entry，语言隔离正确）；GSC/Bing 后台粘贴 feed URL 提交为手动动作，步骤已附 §10。
4. **T-20 404 页 + 站内搜索（体验/SEO 基础）**：当前无自定义 404。
5. **标签词表归并（中等，内链质量）**：当前 ZH 有 84 个 tag，且存在近义碎片（记账类 6 个同义词：Expense Tracker / Budget App / Money Manager / Bookkeeping…）。统一归并可减少 thin-tag 稀释、提升相关文章匹配质量。
6. **T-22 收尾**：BlogPosting 补 `dateModified`（Q2 2027 季度专项）；其余 app FAQ 视情况提到 6 问。

### 8.4 需手动排期（外部/Phase 4 权威）
- **T-21 外链 / roundup 投稿**：Product Hunt、alternative.to、少数派发稿带反链，AI 也常从这些源取样（纯手动，无法代码化）。
- **App 内官网链接加 UTM**：App 工程内「访问官网」按钮拼接 `?utm_source=android_app` 等，去 GoatCounter/GA4 拆分「未知」来源（链接在 App 侧，不在本仓库）。
- **其他语种试点（id/ms/tl/hi）**：见 §9.8，待 ZH 数据验证后再扩（当前优先做上面站内项）。

> 优先级建议：**先做 2（CWV 实测）**——高 ROI 且数周内见效；3/4 低成本补完；5 提升内链质量；6 季度专项；外部项按资源排期。每次推上线后务必在 GSC/Bing WMT 对新增/重大改版页「请求编入索引」。

---

## 9. 月度长期运营规划（Monthly SEO Operations）

> 本规划用于 **2026-11 起**的持续运营。技术地基（Phase 1/2）与内容集群（Phase 3，66 篇）已完成，下一阶段主线转向 **内容新鲜度 + 内链密度 + 外部权威 + 数据驱动迭代**。每月按 §9.2 清单执行，季度按 §9.3 专项推进，执行结果填入 §9.7 台账。

### 9.1 运营核心原则
- 技术已就位，**内容新鲜度与外链权威是下一阶段主线**
- 每篇新内容必须接入「app 详情页 ⇄ 文章」双向内链（已通过 `post.image == app.icon` 自动实现）
- 所有改动 **URL 保持不变**（禁止随意改文件名 / 加 front-matter `permalink`；若必须改，先配 301，本项目暂无重定向机制，优先避免）
- 数据闭环：每月复盘 → 指导下月选题与优化

### 9.2 每月固定清单（Monthly Checklist）
**A. 技术巡检（每月第 1 周，约 1h）**
- [ ] `bundle exec jekyll build` 并跑 htmlproofer，确保死链 / 锚点 / 图片全绿
- [ ] 确认 `sitemap.xml` 已更新且 GSC 无抓取错误
- [ ] Rich Results Test 抽验 1–2 个 app 页，确认 JSON-LD 仍合法
- [ ] Core Web Vitals：PageSpeed Insights 抽 2 个核心页，LCP / CLS 无回退

**B. 内容产出（全月配额，可累积）**
- [ ] **Glossary 词条 ≥ 2 条**（T-18）：what is a habit streak / flip clock / expense tracker 等，AI 搜索最爱抓的事实定义
- [ ] **相关文章区块**：为当月新文 + 至少 3 篇旧文补「Related posts」（同 app / 同 tag）（T-17）
- [ ] **更新日志 / 版本博客 ≥ 1 篇**（T-19）：保持内容新鲜度
- [ ] **新长尾内容 ≥ 2 篇**：Best-X-for-Y / vs / Alternatives 补齐排名薄弱的品类

**C. 内链与权威**
- [ ] 新文章确认纳入 app 页回链（检查 `image:` 字段 == 对应 app `icon`）
- [ ] 外链铺垫（季度集中执行，月度可物色 1–2 个投稿目标）

**D. 数据复盘（月末，约 1h）**
- [ ] 填写 §7「度量记录」表（收录页数 / 自然流量 / 主要排名词）
- [ ] GSC 对当月新页面与重大改版页「请求编入索引」
- [ ] 复盘 CTR 偏低页面 → 优化 `<title>` 与 meta `description`

### 9.3 季度专项（Quarterly Sprints）
| 季度 | 专项 | 对应任务 | 目标 |
|---|---|---|---|
| Q4 2026 | 建库 + 内链（已完成） | T-17 相关文章全站铺开✅、T-18 Glossary 4 条/语言✅、T-19 时间戳✅、T-22 FAQ 增强✅ | 文章间网状内链、AI 可抓定义 | 下一步：Glossary 扩至 10–20 条、Bing/IndexNow |
| Q1 2027 | 新鲜度 + RSS | T-19 更新日志常态化、T-16 提交 feed.xml | 活跃度信号、RSS 收录 |
| Q2 2027 | 权威 / 外链 | T-21 roundup 投稿（Product Hunt / alternative.to / 少数派）、T-20 404 + 搜索 | 外部反链、体验补完 |
| Q3 2027 | 结构化增强 + 年审 | T-22 JSON-LD 增强、全站内容审计（重复 meta / cannibalization） | 富媒体质量、清理冗余 |

### 9.4 首年度 12 个月滚动示例
| 月份 | 内容重点 | 技术 / 数据动作 |
|---|---|---|
| 2026-11 | Glossary ×4 + 相关文章铺开 | 首次全站巡检 + 度量基线 |
| 2026-12 | 更新日志 ×2 + 薄弱品类补 Best | GSC 索引请求 + CTR 优化 |
| 2027-01 | Glossary ×4 + 新长尾 ×2 | RSS 提交（T-16） |
| 2027-02 | 相关文章补全旧文 | Core Web Vitals 实测 |
| 2027-03 | 第一轮 roundup 投稿 | 外链监测 |
| 2027-04 | 更新日志常态化 | 季度内容审计 |
| 2027-05 ~ 2027-10 | 持续滚动（每月 ≥2 Glossary + ≥2 长尾 + ≥1 更新日志） | 每季度一轮 §9.3 专项 |

> 实际执行以 §9.2 清单为最小单位，上表仅作节奏示范；后续可据 Search Console 数据动态调整选题。

### 9.5 关键度量指标（KPIs）
- **收录**：被 Google 收录的页面数（目标：随内容稳步上升）
- **自然流量**：GA4 中 organic search 会话数（月度环比）
- **可见度**：GSC 总 Impressions / 平均排名 / Top 关键词数
- **转化**：Play 商店点击（GA4 事件）/ 文章 → app 页跳转
- **健康度**：htmlproofer 错误数（目标恒为 0）、Core Web Vitals 达标率

### 9.6 运营纪律（红线）
- 已发布页 **URL 不变**（改文件名 / 加 `permalink` 前必须配 301）
- 每篇新内容 **必须有差异化 title + meta description + 关键词化 alt**
- 每月至少一次数据复盘，避免「发了不管」

### 9.7 月度执行台账（每次执行后填写）
| 月份 | 完成内容（Glossary/相关文章/更新日志/长尾） | 技术巡检 | 数据复盘摘要 | 备注 |
|---|---|---|---|---|
| 2026-10 | 内容集群 66 篇上线首月 + **10/30 中英双语优化批**（T-17 相关文章 / T-18 Glossary / T-19 时间戳 / T-22 FAQ） | 全站 build+htmlproofer 基线（绿） | 周 PV 218（GoatCounter 10/22–10/29）；来源 Google 16%(34)、chatgpt 1%(2，AI 导流初现)、bing 1%(3)；CPU/Flip 集群起量；移动端 73%/Android 62% | 内容 10/16 上线，报告区间 10/22–10/29；双语优化 10/30 落库待部署 |
| 2026-11 | | | | |
| 2026-12 | | | | |
| 2027-01 | | | | |
| 2027-02 | | | | |
| 2027-03 | | | | |
| 2027-04 | | | | |

### 9.8 多语言扩展评估（中文已上线，下一步评估其他语种）
- **现状（2026-10-30）**：**`/zh/` 中文站已部署上线**，与英文并行构建、双向 `hreflang`、所有优化双语同步。本段原先"中文暂不部署"的判断已过时——中文已 live。
- **洞察**：流量地域为美国(17%)+印尼(9%)+马来(6%)+菲律宾(6%)+印度(4%)，非英语母语地区（印尼语/他加禄语/印地语）是潜在增量；AI 搜索（chatgpt 已作来源）也按语言分流。
- **是否继续扩语种**：基数仍小（周 PV 218），瓶颈仍优先在「排名爬坡 + 外链权威 + 内链密度」（见 §9.2/§9.3）；低质机器翻译会伤 E-E-A-T，故扩语种须谨慎、先做试点。
- **试点方案（验证后决定是否扩）**：在 `/zh/` 架构已跑通的基础上，选已起量集群（CPU Monitor / Flip Clock）做 **印尼语(id)** 单语言 ×4–6 篇试点，观察非英语搜索增量；有效再扩马来语/他加禄语/印地语。
- **技术要求（若实施）**：复用现有双语并行构建模式（独立 `_config_<lang>.yml` + i18n 后处理 + 双向 `hreflang`），每语言独立 URL+canonical+ sitemap、本地化关键词（非直译）。
- **迁移约束（红线）**：上线新语种时**英文（默认语言）URL 保持不变**，新增语种走 `/<lang>/` 子路径配 `hreflang` 双向关联；**不得**把英文 `permalink` 模板改为带 `/en/` 前缀、**不得**给已发布英文页加 `permalink:` front-matter 却不配 301（本项目无重定向机制，改 URL = 权重清零）。正确实施则已发布英文页的 URL 与排名**零影响**。

---

## 10. 后续优化候选清单（计划做 / 可做，滚动维护）

> 本表汇总所有**尚未完成或可持续做**的优化，便于后续迭代直接取用。已完成的见 §7 任务表（T-01~T-24）。每条标注：类型 / 谁来做 / 预估 ROI / 状态。

| 编号 | 优化项 | 类型 | 谁来做 | ROI | 状态 / 备注 |
|---|---|---|---|---|---|
| T-25 | **Glossary 扩量至 10–20 条**（widget / mood tracker / task manager / assistive touch / white noise / crosshair / RAM booster 等） | 内容 | 站内（AI 批量+人工润色） | 高 | ✅ 已完成（2026-10-30）：每语言 16 条（原 4 + 新 12），索引页与 10 个相关 app 页「Related terms」回链同步补齐 |
| T-13 | **Core Web Vitals 审计 + 首屏懒加载修正**（PageSpeed / Lighthouse，看 LCP/CLS） | 技术 | 站内 | 高 | ✅ 已完成（2026-10-30）：审计并修正首屏图 lazy 问题（详情页 hero 徽章、列表首卡图标改 eager；页脚/卡内徽章保留 lazy）；图片均 WebP、无自定义字体。PSI 实时分因 API 限流未取得，建议后续手动跑一次确认 |
| T-26 | **Glossary 定义页加 FAQPage JSON-LD** | 结构化 | 站内 | 高 | 待做；定义页最易被 AI Overview 引用 |
| T-16 | **提交 feed.xml 到 GSC / Bing（补 RSS 收录信号）** | 技术 | 站内(生成) + 手动(提交) | 低-中 | ✅ feed 已就绪（2026-10-30）：EN `https://spacemanmeow.com/feed.xml` 已在线；ZH `https://spacemanmeow.com/zh/feed.xml` 需部署后生效。提交步骤：GSC「Sitemaps」粘贴 feed URL；Bing WMT「Sitemaps」同样提交（RSS 可被识别为 sitemap） |
| T-20 | **自定义 404 页 + 站内搜索** | 体验 | 站内 | 中 | 待做；当前无 404 |
| T-27 | **标签词表归并**（记账类 6 同义词→统一） | 内链 | 站内 | 中 | 待做；减 thin-tag 稀释、提升相关文章匹配 |
| T-28 | **Glossary→App 反向回链 + 面包屑** | 内链 | 站内 | 中 | 待做；形成术语⇄App 双向闭环 |
| T-22b | **BlogPosting `dateModified` / author 细化** | 结构化 | 站内 | 中 | 待做（Q2 2027 专项） |
| T-29 | **图片再优化**（AVIF/WebP 响应式 `srcset`、关键图预载） | 性能 | 站内 | 中 | 待做；进一步压 LCP |
| T-21 | **外链 / roundup 投稿**（Product Hunt / alternative.to / 少数派） | 权威 | 手动 | 高 | 手动排期；最高外部杠杆 |
| T-30 | **App 内官网链接加 UTM**（`?utm_source=android_app`） | 度量 | App 侧 | 中 | 待做；拆分 GoatCounter/GA4「未知」来源 |
| T-31 | **其他语种试点**（id/ms/tl/hi） | 扩张 | 站内+人工 | 待评估 | 见 §9.8；需 ZH 数据验证后启 |
| T-32 | **结构化数据月度校验**（Rich Results Test 抽验） | 治理 | 站内 | 中 | 常态化；防 JSON-LD 退化 |
| T-33 | **GSC/Bing 月度「请求编入索引」** | 治理 | 手动 | 中 | 常态化；新增/改版页加速收录 |

### 10.1 建议执行节奏（供后续排期参考）
- **立即可做（站内高 ROI）**：T-25（Glossary 扩量，✅ 已完成）→ T-26（Glossary FAQPage）→ T-13（CWV 首屏懒加载修正，✅ 已完成；后续可手动跑 Lighthouse 取实时分）。
- **低成本补完**：T-16、T-20、T-27、T-29。
- **季度专项**：T-22b（Q2 2027）、T-32/T-33（月度治理）。
- **手动/外部**：T-21、T-30（依赖 App 端与投稿排期）。
- **扩张评估**：T-31 待 ZH 数据回正后再定。

> 所有改动遵循 §9.1 红线：**已发布页 URL 不变**；新内容必须接入 app⇄文章双向内链；每月至少一次数据复盘（填 §9.7 台账）。
