# SpacemanMeow 网站 SEO 长期优化方案

> 最后更新：2026-10-10
> **当前状态：Phase 1（技术地基）已完成，详见 §7 执行跟踪表。** 下一步进入 Phase 2（页面级优化）与 Phase 3（内容引擎）。
> 适用范围：spacemanmeow.com（英文站，`lang: en`）
> 目标：提升在 Google 搜索与 AI 应用内搜索（ChatGPT / Perplexity / Claude / Gemini）的排名
> 覆盖关键词方向：expense tracker / budget app / to-do list / mood diary / habit tracker / home screen widgets / flip clock / cpu monitor / floating assistant 等

---

## 0. 现状审计（基于当前仓库）

### 技术现状
- ✅ 已装 `jekyll-seo-tag`（`{% seo %}` 位于 `_layouts/default.html`），基础 title / Open Graph / Twitter 卡片已具备
- ✅ 已配 Google Analytics（`_config.yml` 的 `google:` ID）
- ✅ 全站响应式、图片已转 WebP、部署走 GitHub Actions
- ❌ **无 `sitemap.xml`**（未安装 `jekyll-sitemap`）
- ❌ **无 `robots.txt`**
- ❌ **无结构化数据（JSON-LD）**，Google 无法识别"这是一个 App"
- ❌ 每个 app 的 front matter 只有 `title` / `tagline`，**缺少 `description` 字段** → seo-tag 只能取正文前段作 description，质量差
- ❌ 图片 `alt="{{ page.title }}"`（仅英文标题），缺少关键词
- ❌ 无 canonical、无 `hreflang`、无面包屑

### 内容现状
- 11 个 app 详情页（英文，单页内容偏薄）
- 仅 2 篇博客（均为 Meow Money 的教程），内容面极窄
- 关键词目前散落在 title / tagline / 正文，**缺乏成体系的关键词映射与内容集群**

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
4. **How-to 教程**（已有 2 篇，复制模板）：`How to track expenses with a cat-themed app`
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

AI 应用内搜索本质 = 抓取已索引的可信网页并抽取事实。杠杆最高的是：
- **结构化数据**（§2 P1）：让 AI 明确"这是安卓记账 App、免费、支持多币种"
- **清晰的事实性描述**：每个 app 用 2–3 句说清"它是什么、为谁、独特点"
- **FAQ 段落**：AI Overview / 精选摘要最爱抓 FAQ
- **被行业 roundup 引用**：到 少数派 / Product Hunt / alternative.to 发稿带反链（AI 也常从这些源取样）
- 内容保持**常更新**（博客时间戳新鲜度有帮助）

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
| T-03 | Google Search Console 验证 + 提交 sitemap | ⏳ 需手动 | | 见下方「T-03 操作指引」；`_config.yml` 已配 `webmaster_verifications.google`，部署后页面含验证 meta 标签 |
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
- jekyll-seo-tag 在 app 页会额外输出 `BlogPosting` 类型 JSON-LD，当 description 含 `&` 时会被转义成 `&amp;`（非法 JSON）。当前以 app 页的 `SoftwareApplication` 块为准（已校验合法）；如需彻底修复，可在 `app.html` 覆盖 `{% seo %` 或关闭自动类型。列入后续观察项。
- `url` 已从 `github.io` 改为 `spacemanmeow.com`，部署后请确认线上 canonical / sitemap 均为该域名。
- 注意：Phase 1 的修改尚未推送到远程仓库与部署，需在本地验证满意后提交并触发 Actions 部署，Search Console 才能抓到新 sitemap / 结构化数据。
| T-07 | 列表/详情注入 BreadcrumbList JSON-LD | ☐ | | |
| T-08 | 博客文章注入 Article/BlogPosting JSON-LD | ☐ | | |
| T-09 | 图片 alt 改为含关键词描述 | ☐ | | |
| T-10 | 确认 canonical 生效 | ☐ | | |
| T-11 | 加 hreflang="en" | ☐ | | |
| T-12 | OG/Twitter 卡片图按 app 区分 | ☐ | | |
| T-13 | 维持 Core Web Vitals（懒加载/LCP/CLS） | ☐ | | |

### 内容项（按 app 建集群，每完成一篇记录）
| app | 品类落地页 | 对比页 | Best-X-for-Y | How-to | FAQ | Alternatives |
|---|---|---|---|---|---|---|
| Meow Money | ☐ | ☐ | ☐ | ✅✅(已有2) | ☐ | ☐ |
| Meow Todo | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Meow Mood Diary | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Meow Habits | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| One Widget | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Only Clock | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| CPU Monitor | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| System Monitor | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Floating Assistant | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Meow FM | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |
| Crosshair Aim | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |

### 度量记录（每月填写）
| 月份 | 收录页数 | 自然流量 | 主要排名词 | 备注 |
|---|---|---|---|---|
| | | | | |

---

## 8. 下一步建议

**Phase 1（技术地基）已于 2026-10-10 完成**，包含：sitemap + robots + `url` 修正 + 11 个 app 的 `description` + `SoftwareApplication` JSON-LD（全部校验合法）。

**接下来建议按顺序推进：**
1. **提交并部署**：将本次改动 commit 并触发 GitHub Actions，使线上出现 sitemap.xml / robots.txt / 结构化数据；随后完成 **T-03** Search Console 验证与提交。
2. **Phase 2（页面级，P2）**：T-09 图片 `alt` 关键词化、T-10 确认 canonical、T-11 `hreflang="en"`、T-12 各 app OG 卡片图、T-07/T-08 BreadcrumbList 与博客 Article JSON-LD。
3. **Phase 3（内容引擎）**：按 §3 模板为每个 app 建「品类落地页 + 对比页 + Best-X-for-Y + FAQ」，并在 app front matter 加 `faq:` 自动产出 FAQPage 结构化数据（T-06 收尾）。
4. **Phase 4（权威/AI）**：外链 / roundup 投稿 + 竞品 alternatives 页 + 更新日志。

完成后，配合 §3 模板持续产内容，排名会稳步提升。
