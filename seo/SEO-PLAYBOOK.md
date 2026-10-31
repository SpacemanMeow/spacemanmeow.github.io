# SpacemanMeow SEO 方法沉淀手册（Playbook）

> **用途**：系统化沉淀可长期复用的 SEO 实践方法，按分类归纳，便于持续累积与团队传承。每条方法标注「本站落地状态」，详细进度与日期见 `SEO-PROGRESS.md`。
> **适用范围**：spacemanmeow.com 英文站（默认语言）+ `/zh/` 中文站（已上线）+ 后续可能扩展其他语言（id/ms/tl/hi 等，试点见 `SEO-PROGRESS.md` T-31）。所有方法默认**全语言同步**执行；新增语言走 `/<lang>/` 子路径、配 hreflang 与 canonical，URL 不变、不破既有关联。
> **目标**：提升在 Google 搜索 与 AI 应用内搜索（ChatGPT / Perplexity / Claude / Gemini / Copilot）的可见度。
> **最后更新**：2026-10-30
> **状态图例**：✅ 已落地　🟡 部分落地　♻️ 持续运营中　☐ 待做

---

## 0. 总览：SEO 方法分类

| 分类 | 解决什么 | 类型 | 本站整体状态 |
|---|---|---|---|
| 1. 技术 SEO | 让搜索引擎/AI 能发现、读懂、信任页面 | 多为一次性 | ✅ 已落地 |
| 2. 站内内容 SEO | 用对关键词、对结构产出被检索的内容 | 一次性 + 持续 | ✅ 已落地 + ♻️ 持续 |
| 3. 内链与信息架构 | 把内容织成主题权威网 | 一次性 + 持续 | ✅ 已落地 + ♻️ 持续 |
| 4. AI 搜索专项 | 命中 AI 概览/引用 | 多为持续 | ✅ 部分 + ♻️ 持续 |
| 5. 外部权威 | 被外部源引用（最强杠杆） | 持续（手动） | ☐ 待做 |
| 6. 国际化 i18n | 多语言覆盖 | 一次性 + 持续 | ✅ 已落地（中文） |
| 7. 度量与治理 | 用数据驱动迭代 | 持续 | ✅ 已落地 + ♻️ 持续 |

**核心心法**：SEO 是慢变量——技术改动数周见效，内容积累通常 3–6 个月起量。技术地基一次性做对，之后靠「内容新鲜度 + 内链密度 + 外部权威 + 数据迭代」长期滚动。

**本文约定**：每个方法按「目的 → 原理 → 具体落地 → 避坑 → 本站状态 → 验收」展开，便于照做与复盘。

---

## 1. 技术 SEO（Technical）

> 技术 SEO 是地基：做对了爬虫/AI 才能发现并信任你。以下多为一次性工程，做完即固化；个别项（性能、图片）需随内容增长回头复核。

### 1.1 收录基础设施（sitemap / robots / 站长工具）

- **目的**：让爬虫能发现并收录全站；把「收录清单」主动递交给搜索引擎。
- **原理**：搜索引擎靠「链接发现」+「站点地图」找到页面。没有 sitemap，深层页可能长期不被发现；不验证站长工具，则无法看到收录/报错/排名数据，等于盲飞。
- **具体落地**：
  1. `jekyll-sitemap` 插件自动生成 `sitemap.xml`（已在 `../_config.yml` 启用），部署时随 `../_site` 整体发布。**验收**：线上 `https://spacemanmeow.com/sitemap.xml` 可访问、含全量 URL（含 `/zh/`）。
  2. 根目录放 `robots.txt`：`User-agent: *` + `Allow: /` + `Sitemap: https://spacemanmeow.com/sitemap.xml`。**验收**：线上 `robots.txt` 返回 200，Sitemap 行指向正确域名（非 github.io）。
  3. Google Search Console：添加属性 `spacemanmeow.com` → 用 `../_config.yml` 的 `webmaster_verifications.google` 输出的 `<meta>` 自动验证 → 提交 sitemap。
  4. Bing Webmaster Tools：添加同域 → 导入 GSC 验证（T-23 已完成）→ 提交 sitemap；Bing 覆盖 ChatGPT/Copilot 的索引源。
  5. 提交 `feed.xml`（RSS）到 GSC/Bing「Sitemaps」位（T-16）：RSS 是独立发现源，对活跃站额外加成。
- **避坑**：① `url` 必须设为 `spacemanmeow.com`，否则 sitemap/robots 指向旧 github.io 域名；② 双语并行构建时确保部署的 sitemap 是合并版（含 `/zh/`），否则中文页不被发现；③ 部署后 GSC 显示「无法抓取」常为状态延迟，72h 内多会转成功。
- **本站状态**：✅ 已落地（T-01/02/03/16/23）；IndexNow 即时提交已接（T-24）。

### 1.2 URL 规范化（canonical）

- **目的**：避免重复内容稀释权重，告诉搜索引擎「每页真正的唯一版本是哪个 URL」。
- **原理**：同一页面可能被多个 URL 访问到（少斜杠、带 `?ref=` 参数、GitHub Pages 旧域名等）。搜索引擎会把这些当成「重复内容」，分散排名权重甚至选错正版。canonical 标签就是一页声明：「认准这个网址」。
- **具体落地**：`jekyll-seo-tag` 默认给每页输出 `<link rel="canonical">`。**只需确认** `../_config.yml` 的 `url` 是 `https://spacemanmeow.com`，canonical 即自动指向正确域名。双语下 `/zh/` 页 canonical 指向 `spacemanmeow.com/zh/...`。
- **避坑**：最典型坑是 GitHub Pages 默认域名 `*.github.io` 被写进 canonical，导致 Google 把 GitHub 镜像当正版。本项目已通过改 `url` 修正（T-10）。
- **本站状态**：✅ 已落地（T-10）。

### 1.3 多语言关联（hreflang）

- **目的**：让中/英（及未来多语言）同主题页互相标注「语言版本」，避免被判定为重复内容，并把正确语言推给正确地区用户。
- **原理**：hreflang 是给搜索引擎的「这是同一内容的不同语言版」信号。缺失时，Google 可能只显示一个语言版本、或混淆受众；错误配置（如 A 说自己是 B 的 zh、B 却没回指 A）会导致回退到单版本。
- **具体落地**：
  1. 构建流程为每页注入 `en`/`zh` 双向 `hreflang`（经 i18n 后处理脚本，每页 3 条 `alternate`：x-default + en + zh）。
  2. `<html lang>` 依构建语言自动输出 `en`/`zh`，帮助辅助技术与语音搜索。
  3. 每语言独立 URL（`/`、`/zh/`）+ 各自 canonical + 各自 sitemap 区段。
- **避坑**：hreflang 必须**成对/成环**——若 A 指向 B，B 也要指回 A，否则 Google 忽略整组。本项目由后处理脚本统一生成，已校验每页 3 条 alternate。
- **本站状态**：✅ 已落地（T-11）。

### 1.4 结构化数据（JSON-LD）

- **目的**：把页面事实「机器可读」地标注出来，让 Google 富媒体展示、让 AI 搜索更易抽取（是 AI「被读懂」的关键）。
- **原理**：JSON-LD 是嵌在 `<head>` 的 JSON，声明实体的类型与属性（如「这是个 App，叫 Meow Money，免费、类别 Finance」）。Google 据此生成富媒体结果（评分星、FAQ 折叠、面包屑），AI 检索时也能直接读事实而非猜。
- **具体落地（类型与文件）**：
  - App 页 `SoftwareApplication` + `FAQPage` + `BreadcrumbList`：`_includes/app-jsonld.html` 接 `app.html`，11 页全覆盖。
  - 博客 `BlogPosting`/`Article`：`jekyll-seo-tag` 自动输出（含 author/publisher/mainEntityOfPage）。
  - 面包屑 `BreadcrumbList`：`_includes/breadcrumb-jsonld.html` 接 `default.html`。
- **避坑（本项目真实踩过的坑）**：
  1. `description`/`title` 里含 `&` 会被 seo-tag 转成 `&amp;` 塞进 JSON-LD → **非法 JSON，Google 丢弃整块**。修复：含 `&` 处一律改 `and`。
  2. 无日期页（app/隐私/条款）被 seo-tag 误填构建时间、误标为 `BlogPosting`。修复：这些页 front matter 加 `seo.type: WebPage` 强制类型正确；真正的结构化数据仍由我们的 include 提供。
  3. **验收**：用 Rich Results Test 抽验；构建产物全站 JSON-LD 应**无 `&amp;`**，app 页 `@type` 为 `WebPage`+`SoftwareApplication`+`FAQPage`+`BreadcrumbList`。
- **本站状态**：✅ 已落地（T-05/06/07/08/22）；Glossary 定义页加 `FAQPage` 待做（T-26）。

### 1.5 性能（Core Web Vitals）

- **目的**：LCP / CLS / INP 是排名因子，也影响 AI 抓取效率与用户体验（间接影响跳出/停留）。
- **原理**：Google 把 CWV 纳入排名；三大指标——LCP（最大内容绘制，首屏主图/文字加载慢则差）、CLS（布局位移，图片无尺寸会跳动）、INP（交互延迟）。任一超标会拖累排名。
- **具体落地**：
  1. **首屏图 `eager`、其余 `lazy`**：详情页 hero 商店徽章、列表首卡图标原为 `lazy` 却属首屏 → 改 `eager`（否则伤害 LCP）；页脚 logo、卡内徽章保持 `lazy`。
  2. 图片统一 WebP（q82）；关键图可加 `srcset`/`<link rel="preload">` 进一步压 LCP。
  3. 无自定义字体（无 CLS 字体风险）；每图带 `width`/`height` 防位移。
- **避坑**：PSI/Lighthouse 实时分曾因 API 限流取不到——以代码级审计+修复为准，建议后续手动跑一次 PageSpeed Insights 取真实分。AVIF/`srcset` 预载为后续增强（T-29）。
- **本站状态**：✅ 审计+首屏懒加载修正已落地（T-13）；AVIF/srcset 预载待做（T-29）。

### 1.6 图片优化（alt）

- **目的**：图片是「可被读懂」的载体；alt 既承载关键词（利于图片搜索与周边正文相关性），也是 AI 读取图片信息的唯一文本通道。
- **原理**：爬虫/AI 不直接读图，靠 alt 理解图义。空 alt（`![image]`）或千篇一律的 alt 既浪费 SEO 机会，也让 AI「看不见」图。alt 还应差异化——同图同 alt 重复会被视为低质。
- **具体落地**：
  1. alt 改为含关键词描述，如 `Meow Money Manager - cute expense tracker app icon`。
  2. 专名大小写统一（YNAB / CCleaner / TickTick / KWGT…），避免同一品牌多种写法稀释。
  3. **全站差异化 0 重复**：同一文件内不出现重复 alt；描述性 alt 追加主题词。
  4. 清理 `![image]` 零残留；每图带 `width` 防 CLS。
- **本站状态**：✅ 已落地（T-09，839 处全站规范化）。

### 1.7 用户体验（404 + 站内搜索）

- **目的**：低跳出、高停留间接利好 SEO；站内搜索留住用户、提升内容曝光。
- **具体落地**：
  1. 自定义双语 `404.html`：按 `/zh/` 路径前缀切换语言，避免用户迷路。
  2. Pagefind 全文搜索：EN/ZH 独立索引（扩展版含中文分词）；`data-pagefind-body` 仅索正文；导航加搜索入口。
  3. i18n 后处理跳过 404 不进 sitemap。
- **本站状态**：✅ 已落地（T-20）。

---

## 2. 站内内容 SEO（On-page / Content）

> 技术解决「能被发现」，内容解决「值得被排上来」。本类既有一次性建设（关键词库、集群模板），也有持续动作（新鲜度、Glossary 增量）。

### 2.1 关键词研究

- **目的**：知道要覆盖哪些词、避免凭感觉写，让每篇内容都瞄准真实搜索需求。
- **原理**：搜索流量 = 覆盖的词 × 每个词的排名 × 点击率。系统化研究能把「写什么」从拍脑袋变成「按词表填空」。
- **具体落地**：
  1. **提取站内已覆盖词**：遍历 `_apps` + `_posts` 的标题/描述/tags，归纳每个 app 的核心词（见 §2.1.1）。
  2. **竞品调研补充**：对 8 大品类列出主要竞品与它们的头部搜索词（见 §2.1.1 竞品表），补进词库——这是抢竞品品牌流量的入口。
  3. **三层分层**：
     - **Head（难、量大）**：`expense tracker app`、`budget app`
     - **Middle（中）**：`private expense tracker`、`cute budget app`
     - **Long-tail（易、精准、转化高）**：`budget app with fingerprint lock`、`expense tracker no account required`
  4. 建立「app → 目标词 → 对应内容页」映射表，新增内容前先查表避免重复（cannibalization）。
- **策略核心**：app 详情页吃 long-tail + 品牌词（转化高、易排）；新建「品类落地页 / 对比页」去抢 head / middle 词（量大但难），互相内链形成主题权威。
- **本站状态**：✅ 词库已建（见 §2.1.1）；竞品调研已做。

#### 2.1.1 当前关键词库（中英各一套，持续扩充）
**站内已覆盖词**
- Meow Money：expense tracker / budget app / budget management / bookkeeping / multi-currency / ledger / CSV export / reimbursement
- Meow Todo：to-do list / task manager / schedule planner
- Meow Mood Diary：mood diary / journal / safe place
- Meow Habits：habit tracker / habit building / routine
- One Widget：home screen widgets / Material You / Galaxy One UI / Nothing style / Glass iOS / clock & calendar widget / battery widget
- Only Clock：full-screen clock / flip animation / nightstand clock
- CPU Monitor：cpu temperature / cpu frequency / ram widget / floating window / overheat alarm
- System Monitor：cpu monitor / storage cleaner / memory booster / battery doctor
- Floating Assistant：assistive touch / floating clock / floating monitor
- Meow FM：white noise / sleep / relax / concentrate
- Crosshair Aim：crosshair / FPS games / aim / overlay

**竞品调研补充（按品类）**
| 品类 | 主要竞品 | 高频搜索词 |
|---|---|---|
| 记账/预算 | Mint, YNAB, PocketGuard, Expensify | `expense tracker app`, `free budget app`, `money tracker`, `private expense tracker no account`, `budget app for couples/students`, `subscription tracker` |
| 待办 | TickTick, Things, Todoist | `task manager`, `GTD`, `daily planner`, `reminder app`, `AI task planner`, `shared/family to-do list` |
| 心情日记 | Day One, Journey, Reflectly, Daylio | `journaling app`, `mood tracker`, `gratitude journal`, `private diary app`, `guided journal`, `mental health journal` |
| 习惯养成 | HabitBull, Streaks, Fabulous | `habit tracker`, `streak counter`, `habit tracker widget`, `habit reminder`, `routine builder`, `free habit tracker` |
| 桌面小组件 | KWGT, WidgetClub, Widget Studio | `android widgets`, `home screen customization`, `Material You widgets`, `Glass widgets`, `Nothing OS widgets`, `minimalist widgets` |
| 翻页时钟 | Retroflip, Fullscreen Clock | `flip clock`, `fullscreen clock`, `flip clock widget`, `desk clock`, `nightstand clock`, `pomodoro clock` |
| CPU 监测 | CPU-Z, DevCheck, AIDA64 | `cpu temperature monitor`, `phone temperature`, `cpu usage`, `overheating fix`, `ram booster`, `battery monitor`, `floating cpu widget` |
| 悬浮窗 | （蓝海） | `floating window`, `assistive touch`, `overlay widget`, `floating shortcuts` |

### 2.2 主题集群模型（Pillar + Cluster）

- **目的**：用「一个权威页 + 多支撑页」让搜索引擎认定你在该主题是**权威**，从而整体提升集群内所有页排名。
- **原理**：单篇内容权重有限；当多篇互链的内容围绕同一主题，搜索引擎会识别出「这个站关于 X 很专业」，把权威信号传导到每张页。Pillar 页（宽、抢大词）与 Cluster 页（深、抢长尾）相互内链，形成「簇」。
- **具体落地（可复制模板）**：
  ```
  品类落地页 (Pillar，抢 head 词)
     ├─ How-to 教程 (Cluster)
     ├─ 对比 / vs 页 (Cluster)
     ├─ "Best X for Y" 清单 (Cluster)
     ├─ FAQ / Glossary (Cluster)
     └─→ 全部内链回 对应 App 详情页（转化点）
  ```
  每新增一个 app，即套此模板（Pillar + 1 vs + 2 Best + 1 How-to + 1 Alternatives + FAQ），关键词自然滚动增长。
- **编辑流程**：用 §2.1 映射表查重 → 写内容 → 填 tags（app/品类/类型/竞品四层）→ 确认与 Pillar/App 互链 → 部署后 GSC 请求编入索引。
- **避坑**：Cluster 页必须**真链回 Pillar/App**，否则只是孤立文章；避免两篇 Cluster 抢同一词造成自相残杀（cannibalization）。
- **本站状态**：✅ 11 个 app 全套集群已建（66 篇）；覆盖情况见 `SEO-PROGRESS.md` §2（已落地明细）。

### 2.3 标题 / 元描述 / alt 规范

- **目的**：提升相关性（让对的人点进来）+ SERP 点击率（CTR，间接影响排名）。
- **原理**：`<title>` 是最强相关信号；meta `description` 不直接影响排名但决定 SERP 里的「广告文案」、直接关系 CTR；alt 承载图片相关性。三者共同决定「搜得到 + 点得进」。
- **具体落地（每页硬指标）**：
  1. **差异化 `title`**（含主词，≤ 60 字符，避免全站雷同）：如 `Meow Money: Cute Expense Tracker & Budget App for Android`。
  2. **`description`** 150–160 字符、含主词、**事实性而非营销话术**（"最好的 app" AI 不采信，写具体功能/数字）。
  3. **关键词化 alt**（见 §1.6）。
- **避坑**：description 用 `&` 会被转 `&amp;` 污染 JSON-LD（同 §1.4）；标题堆砌关键词（keyword stuffing）会被降权。
- **本站状态**：✅ 已落地（T-04/09）；**月度复盘优化 CTR** 见进度 §4.1 D（低 CTR 页重写 title/description）。

### 2.4 内容新鲜度

- **目的**：Google 偏好活跃站；新鲜度是排名信号。
- **做法**：Pillar 页加 `last_modified_at` 渲染「Last updated」时间戳；常态化发布更新日志/版本博客（changelog）。
- **本站状态**：🟡 Pillar 时间戳已落地（T-19）；独立 changelog 页待 Q1 2027 常态化。

#### 2.4.1 Google 如何判断新鲜度（多信号，非单一日期）
> 误区：光改「最后修改日期」并不能提升新鲜度——Google 看的是**真实内容变化**。

| 信号 | 说明 |
|---|---|
| **内容实际变化** | 最重要。爬虫重抓时比对正文，发现文字/结构变了才算「更新」；只改日期盖章、正文没动，Google 能识别，几乎不加分 |
| **datePublished / dateModified** | 来自页面可见日期与 `BlogPosting`/`Article` JSON-LD 的这两个字段；Google 用于在结果中显示「X 前更新 / Updated X」，并作新鲜度参考 |
| **页面整体更新频率** | 长期稳定维护、常小幅更新的页面会积累「新鲜度信誉」 |
| **查询类型** | 对时效性敏感搜索（版本号、新品、年度榜单）新鲜度权重极高；纯定义类影响小 |
| **sitemap `<lastmod>` / 重新抓取** | 帮助 Google 知道「该页变了、快来重新评估」、加速刷新，但本身不是排名信号 |

#### 2.4.2 已发布文章如何提升新鲜度（按 ROI 排序）
1. **实质性更新内容（核心）**：给旧文补新信息——新版本功能、更新截图、`last_modified_at` 同步改 + 正文真改。Google 检测到正文变化才会重算新鲜度。
2. **让更新时间戳真实**：如 T-19，Pillar 页渲染 "Last updated"；但务必配合第 1 点，否则只是装饰。
3. **常态化发更新日志 / 版本博客（changelog）**：每次 app 发版写一条，既给站点持续活跃信号，又能内链回相关文章 / App 页（独立 changelog 页见 Q1 2027 计划）。
4. **补内链到新内容**：旧文里加指向新发布文章 / 词汇表的链接，让旧页「沾」新内容新鲜度，同时强化主题集群（§3）。
5. **刷新过时表述**：「2025 年最佳」→「2026 年」、更新下载量/评分等数字，小改也能触发重新评估。
6. **更新后主动提请抓取**：改完用 IndexNow（T-24 自动）即时通知 Bing/ChatGPT；在 GSC 对改版页「请求编入索引」（T-33 月度动作）。
7. **结构化数据同步 `dateModified`**：`BlogPosting` 的 `dateModified` 随更新改写（T-22b 计划 Q2 2027 补），让搜索结果日期准确。

> **执行纪律**：每月「更新日志 / 内容刷新」必须伴随**真实正文改动**，不能只把 `last_modified_at` 往前推。否则 Google 抓取后发现正文没变，新鲜度信号基本无效，甚至因「日期与内容不符」失去信任。
> **公式**：新鲜度 = 真实内容更新 + 准确的更新日期 + 让 Google 知道你更新了（IndexNow / 请求编入索引）。三者缺一不可。

### 2.5 Glossary 词汇表 / 定义页

- **目的**：命中 AI「what is X」类查询（AI 概览最爱抓定义式事实）；同时服务站内用户、降低术语门槛。
- **原理**：AI 搜索（尤其 Perplexity / Gemini）在回答「what is a flip clock / habit streak」时，优先摘录结构清晰的定义页。Glossary 既是「被 AI 引用」的高命中内容，又能内链回 App 页形成闭环。
- **具体落地**：
  1. 建 `glossary`/`glossary_zh` 集合（每语言 N 条定义页 + 索引页），进 sitemap + 双向 hreflang。
  2. 定义页写清：术语名、一句话定义、为什么重要、与本 app 的关系。
  3. 相关 app 页加「相关术语」回链；博客顶部加「词汇表 →」入口，导流并强化内链。
  4. **持续增量**：每月 ≥2 条（T-18x），优先补各品类核心术语。
- **避坑**：定义页若无 FAQ/结构化数据，AI 引用率会低——待 T-26 补全 `FAQPage` JSON-LD。
- **本站状态**：✅ 已落地 16 条/语言（T-18，原 4 + 新 12）；Glossary 加 FAQPage 待做（T-26）；Glossary→App 反向回链待做（T-28）。

---

## 3. 内链与信息架构（Internal Linking）

> 内链是「零成本」的权威传导器：把零散页面织成主题网，既帮爬虫发现全站，也把权重集中在转化页（App 详情页）。

### 3.1 主题集群内链（相关文章区块）

- **目的**：在每篇文章底部推荐同主题文章，延长停留、强化集群（见 §2.2）。
- **具体落地**：`_includes/related-posts.html` 按**标签重叠度**取同语言最多 4 篇 + 父 app 页回链，接入 `post.html`/`guide.html` 页脚；构建时按语言自动隔离（EN/ZH 各生成自己的链接，无需手改）。**新文自动纳入**，无维护成本。
- **避坑**：原手写区块曾重复/缺漏，已清理；确保标签体系质量（见 §3.5）才能让匹配精准。
- **本站状态**：✅ 已落地（T-17，中英双语自动隔离）；每月补全旧文（T-17x）。

### 3.2 /tags/ 聚合页 + 标签可点击

- **目的**：给爬虫与用户一张「全站内容地图」，集中收录长尾 tag 页、提升内链密度。
- **具体落地**：`_pages/tags.md` 原生聚合所有 tag 分组（81 组）；文章底部 tag 可点击锚点跳转；博客列表加 Tags 入口。**验收**：htmlproofer 死锚点 = 0。
- **本站状态**：✅ 已落地（T-15）。

### 3.3 App ⇄ 文章双向回链

- **目的**：形成「App 详情页 ⇄ 文章」双向闭环，把文章权重传导到转化点。
- **具体落地**：按 `post.image == app.icon` 自动判定归属——App 页「Guides & Tutorials」区块列出该 app 的 N 篇相关文章（`app.html`+`main.css`，T-14）；文章页脚经 §3.1 回链 App 详情页（T-17）。**零手动维护**。
- **避坑**：新增文章务必在 front matter 设正确 `image:` == 对应 app `icon`，否则回链断裂。
- **本站状态**：✅ 已落地（T-14/17）。

### 3.4 Glossary ⇄ App 反向回链 + 面包屑

- **目的**：补完 §2.5/§3.3 的闭环——词汇页也回链 App，并加面包屑，让术语⇄App 双向成环。
- **具体落地**：在 Glossary 详情页加「相关 App」区块 + `BreadcrumbList`（首页 › 词汇表 › 术语）。
- **本站状态**：☐ 待做（T-28）。

### 3.5 标签词表归并

- **目的**：减少 thin-tag（近义碎片各自成页、流量被稀释），提升相关文章匹配质量（§3.1）。
- **具体落地**：合并近义碎片——如记账类 6 同义词（Expense Tracker / Budget App / Money Manager / Bookkeeping…）归一到统一 tag；需同步改 `_posts` 中对应 `tags` 字段与 `/tags/` 分组。
- **避坑**：归并会改变 URL（若 tag 页有独立链接），需确认无外链依赖或配重定向。
- **本站状态**：☐ 待做（T-27）。

---

## 4. AI 搜索专项（重点）

> AI 搜索是增量红利：传统 SEO 抢「蓝色链接」，AI 搜索抢「被引用」。两者地基重合（技术/内容/内链），但 AI 更看重「被读懂、被信、被引用」。

### 4.1 工作原理

AI 联网搜索不是按 PageRank 排位，而是：① 从已索引网页**检索相关片段** → ② **抽取事实**拼成答案 → ③ 是否「引用你」取决于：内容被检索到 + 清晰可信 + 权威。
**公式 = 被索引 × 被读懂 × 被信 × 被引用**。

### 4.2 各 AI 产品搜索偏好对比（经验性）
> 不同产品的索引源、引用机制、内容偏好存在差异；下表为基于当前行业实践的经验归纳，需随产品迭代复核。

| 产品 | 索引/检索来源 | 偏好内容形式 | 被引用/入选要点 | 本站对应动作 |
|---|---|---|---|---|
| **ChatGPT（Browse/Search）** | 主要走 **Bing** 索引 | 权威、结构化、近期更新的页面；倾向引用有明确答案的段落 | 被 Bing 收录 + 有 FAQ/列表/定义；IndexNow 加速即时性 | T-23 Bing WMT、T-24 IndexNow、FAQPage |
| **Perplexity** | 实时多源检索（Bing + 直连站点） | 直给答案、要点列表、清晰事实、多源佐证 | 提供「可摘录」的事实片段；定义页/对比表极易入选 | Glossary(T-18)、对比表、FAQ |
| **Claude（Anthropic）** | 网页搜索工具（多引擎） | 长文、全面、事实密集、结构清晰 | E-E-A-T 强、主题权威；偏好可靠来源 | 主题集群、结构化数据 |
| **Google Gemini / AI Overviews** | **Google** 搜索索引 | 与 Google SEO 一致；偏好 FAQ、精选摘要、结构化数据 | FAQPage/JSON-LD、E-E-A-T、新鲜度 | T-05~08、T-22 FAQ |
| **Microsoft Copilot** | **Bing** 索引（原生） | Bing 收录优先；即时性高 | IndexNow 即时收录、Bing WMT 验证 | T-23/T-24 |
| **Google 传统搜索** | Google 索引 | 经典 SEO：标题/描述/内链/权威 | 全站技术地基 + 集群内链 | 全技术项 |

**共性结论**：① 索引源分 Google 系 vs Bing 系——两者都要覆盖（Bing 经 IndexNow 即时提交）；② 引用机制不同（Perplexity 多源摘录、ChatGPT 单源引用、Gemini 融入概览）；③ **定义/FAQ/列表**是最稳的「被引用」内容形式；④ 新鲜度与权威是跨产品共性。

### 4.3 七大核心策略

| # | 策略 | 具体落地 | 对应任务 | 状态 |
|---|---|---|---|---|
| 1 | 被索引（Google + Bing/IndexNow） | sitemap + 站长工具 + IndexNow 自动 ping（deploy 后） | T-01/02/03/23/24 | ✅ |
| 2 | 结构化数据（JSON-LD） | SoftwareApplication/FAQPage/Breadcrumb/BlogPosting | T-05~08 | ✅ |
| 3 | 清晰、可直引的内容 | 短句/列表/定义式写法；Glossary 定义页 | T-18 Glossary | ✅ |
| 4 | FAQ 段落 | 每 app 4–6 问 + FAQPage；命中 AI Overview | T-06/22 | ✅ |
| 5 | 主题集群权威 | 相关文章区块 + 双向回链织网 | T-17 | ✅ |
| 6 | 被权威源引用 | roundup/外链投稿（见 §5） | T-21 | ☐ |
| 7 | 内容新鲜度 | 时间戳 + changelog（见 §2.4） | T-19 | 🟡 |

### 4.4 避坑清单

- 纯图片无 alt（AI 读不到）→ 已用 alt 差异化规避（§1.6）。
- 模糊营销话术（"最好的 app" AI 不采信）→ 改用具体事实、数字、功能。
- 内容单薄/重复 → 已用集群 + Glossary 规避（§2.2/§2.5）。
- 定义页无 FAQ/结构化 → 待 T-26 补 FAQPage。
- 只在 Google 做收录、忽略 Bing → 损失 ChatGPT/Copilot 流量；本项目已用 IndexNow 覆盖。

---

## 5. 外部权威（Off-page）

> 外部权威是「被信/被引用」的最强杠杆，也是最难、最慢的一项——靠手动 outreach，无法纯代码化。但有它就从「自己说好」升级到「别人说你好」。

### 5.1 外链 / roundup 投稿

- **目的**：被权威站引用 = 最强信任信号，直接提升域名权威（Domain Authority），并常是 AI 取样源之一。
- **具体落地（渠道）**：
  1. **Product Hunt**：发 app 新版本，带官网链接。
  2. **alternative.to**：在竞品（Mint/YNAB/TickTick/Day One…）的「Alternatives」里收录 Meow 系列，留官网。
  3. **少数派 / 相关垂直媒体**：写「安卓记账 app 横评」类稿件，自然嵌入链接。
  4. **内容杠杆**：把站内高质量对比/清单文（如「Best Budget App for Android 2026」）主动投递给 roundup 站点。
- **避坑**：买链/垃圾目录会触发惩罚；只做**相关、自然**的提及。外链质量 >> 数量。
- **本站状态**：☐ 待做（T-21，纯手动排期，季度集中推进）。

### 5.2 被权威源引用（mentions）

- **目的**：不一定要超链，品牌被权威源文字提及也利于 E-E-A-T。
- **具体落地**：在行业社区（Reddit 相关版块、专业论坛）以真实经验分享出现；参与媒体选题征集。与 §5.1 同源，建立行业存在感。

### 5.3 App 内官网链接加 UTM

- **目的**：拆分 GoatCounter/GA4 的「未知」来源，量化 App 内导流效果，反哺内容选题。
- **具体落地**：App 工程内「访问官网」按钮拼接 `?utm_source=android_app&utm_medium=inapp`（链接在 App 侧，不在本仓库）。**验收**：GA4 中能看到 `android_app` 来源会话。
- **本站状态**：☐ 待做（T-30，依赖 App 端改动）。

---

## 6. 国际化（i18n）

> 多语言 = 把已验证的 SEO 模型复制到新语言市场。核心是「架构可复制、URL 不破、hreflang 成对」。

### 6.1 双语并行构建模式

- **目的**：在不破坏英文站的前提下，新增语言市场。
- **具体落地**：
  1. 独立 `../_config_<lang>.yml`（如 `_config_zh.yml`）+ i18n 后处理脚本；并行构建产出 `/<lang>/` 子目录。
  2. 每语言独立 URL + canonical + sitemap 区段 + 双向 hreflang（见 §1.3）。
  3. **本地化关键词**（非直译）：如中文词要按中文搜索习惯选，而非翻译英文词。
- **避坑**：新语言 URL 一旦发布就别改；改则权重清零（见 §8 红线）。
- **本站状态**：✅ `/zh/` 已上线，与英文并行构建、所有优化双语同步（T-11/16/17/18/19/22）。

### 6.2 语种扩展评估

- **洞察**：流量地域含印尼/马来/菲律宾/印度等非英语区，是潜在增量；AI 搜索也按语言分流。
- **原则**：低质机器翻译伤 E-E-A-T，须谨慎；先做试点。
- **试点**：在 `/zh/` 架构上，选已起量集群（CPU Monitor / Flip Clock）做**印尼语(id)** ×4–6 篇试点，观察非英语搜索增量；有效再扩马来语/他加禄语/印地语。
- **红线**：英文（默认语言）URL 保持不变；新语种走 `/<lang>/` 子路径配 hreflang；不得改已发布英文页 `permalink` 却不配 301（本项目无重定向机制）。
- **本站状态**：☐ 待评估（T-31，需 ZH 数据验证后启）。

---

## 7. 度量与治理

> 「发了不管」是 SEO 最大浪费。用数据闭环指导「下个月写什么、改什么」。

### 7.1 工具与 KPI

- **工具**：
  - **Search Console**：收录数、点击词、平均排名、覆盖率报错（最核心）。
  - **GA4**：落地页表现、organic 会话、转化（Play 点击、文章→App 跳转）。
  - **PageSpeed Insights / Lighthouse**：CWV 实测分。
  - **GoatCounter**（本站轻量分析）：来源细分、AI 引流初现（chatgpt 已作来源）。
- **GSC 全量数据自动拉取（脚本）**：`../tools/gsc_export.py` 通过 Search Console API 分页拉取**全量**搜索词/页面/国家/设备/日期（单次上限 5000 行，绕过 UI 导出 1000 行限制），输出 CSV + 汇总 JSON，供回填 **[SEO-METRICS.md](./SEO-METRICS.md)** 月度报告。
  - 首次运行：`python3 ../tools/gsc_export.py --site sc-domain:spacemanmeow.com --start YYYY-MM-01 --end YYYY-MM-DD --out data/<yyyymm>` → 弹浏览器授权，自动生成 `../tools/gsc/token.json`（已 gitignore，后续免登录）。
  - 之后每月换日期重跑即可；结果 CSV/JSON 均在 `data/`（已 gitignore）。
  - 属性为**域名属性**，故 `--site` 用 `sc-domain:spacemanmeow.com`（URL 形式 `https://spacemanmeow.com/` 会 403）。
- **KPI（月度跟踪）**：
  - 收录页数（目标：随内容稳步上升）
  - 自然流量（organic 会话，月度环比）
  - 可见度（Impressions / 平均排名 / Top 关键词数）
  - 转化（Play 点击 / 文章→App 跳转）
  - 健康度（htmlproofer 错误 = 0、CWV 达标率）
- **验收/记录**：更新 **[SEO-METRICS.md](./SEO-METRICS.md)** 月度报告（趋势表 + 月份分析小节）。

### 7.2 季度审计

- **目的**：定期体检，防止技术债累积。
- **具体落地（每季度）**：
  1. 死链/锚点检查（htmlproofer 全绿）。
  2. 重复 meta / title / description 核查（避免 cannibalization）。
  3. sitemap 是否最新、结构化数据是否通过 Rich Results Test。
  4. 关键词自相残杀审查（两页抢同词 → 合并或差异化）。
  5. 全站内容健康度复盘。

### 7.3 常态化治理任务

- **结构化数据月度校验**（T-32）：Rich Results Test 抽验 1–2 个 app 页，防 JSON-LD 退化（尤其改版后）。
- **GSC/Bing 月度「请求编入索引」**（T-33）：对当月新页/重大改版页主动提请，加速收录。
- **本站状态**：✅ 机制已建，待月度滚动执行（见 `SEO-PROGRESS.md` §4 月度清单）。

---

## 8. 运营红线（Rules）

> 这些是不可逾越的约束，违反会直接损失排名/权重。

1. **已发布页 URL 不变**：改文件名 / 加 `permalink` 前必须配 301；本项目暂无重定向机制，优先避免改 URL。
2. **每篇新内容必须有**：差异化 `title` + meta `description` + 关键词化 `alt`（见 §2.3/§1.6）。
3. **每篇新内容必须接入 app⇄文章双向内链**：检查 `image:` == 对应 app `icon`（见 §3.3）。
4. **每月至少一次数据复盘**：更新 `SEO-METRICS.md` 月度报告（运行 `../tools/gsc_export.py` 拉数 → 填趋势表 + 新增月份分析），避免「发了不管」（见 §7.1）。
5. **所有改动中英同步**：URL / hreflang / canonical 不被破坏（见 §1.3/§6.1）。
6. **新增语言走 `/<lang>/` 子路径**：不得改英文默认 URL、不得无 301 改已发布页 `permalink`（见 §6.2）。
7. **新鲜度必须伴随真实内容改动**：只改日期无效且伤信任（见 §2.4 纪律）。
