# 多语言内容扩展标准流程（i18n Expansion Playbook）

> **用途**：本站 `spacemanmeow.com` 新增任何语言、任何 App 的多语言内容时，**直接按本文档执行**，无需再向需求方确认实现细节。
> **适用**：Jekyll 4.4 多语言合并构建；默认语言 `en`（根路径），其他语言走 `/<lang>/` 子路径。
> **权威关系**：技术红线以 `SITE-AUDIT.md` 为准；关键词以 `SEO-KEYWORDS.md` 为准；SEO 方法论以 `SEO-PLAYBOOK.md` 为准；进度与台账以 `SEO-PROGRESS.md` / 本文档配套 `SEO-I18N-PROGRESS.md` 为准。本文档负责把四者串成**可重复执行的流程**。
> **最后更新**：2026-11-07
> **首个实例**：`id`（Bahasa Indonesia / 印度尼西亚；2026-11-06 完成 Phase 0–3，66/66 posts 可发布，状态见 `SEO-I18N-PROGRESS.md`），Meow Money Manager 优先。
> **第二个实例**：`th`（泰语 / Thai；2026-11-07 完成 Phase 4 全量交付，posts/apps/gloss 66/66·11/11·22/22、**结构页 8/8 已补齐**，htmlproofer 0 failure），从 `id` 骨架逐篇翻译，完整教研见 `SITE-AUDIT.md` §8。

---

## 0. 速查：新增一门语言的 12 步

| 步 | 动作 | 产出 / 命令 | 不可跳过 |
|---|---|---|---|
| 1 | **关键词先行**：用当地语言在 Google Play 与网上做本地检索 | `seo/SEO-KEYWORDS.md` 新增 `§2.N.x <语言>` 小节 | ✅ |
| 2 | 登记词库与证据 | 词层表 + 维护日志 + `§1` 索引语言范围 | ✅ |
| 3 | 生成语言配置与目录 | `bash scripts/new-language.sh <code> "<Label>" <SHORT>`，再按 §2.3 手工补齐 | ✅ |
| 4 | 补数据文件 | `_data/languages.yml` / `nav.yml` / `ui.yml` | ✅ |
| 5 | 补构建脚本 | `scripts/build.sh` 增加该语言 build + rsync 块 | ✅ |
| 6 | **模板 N 语言通用化**（仅首次新增第三语言时做一次） | 消除所有 `zh`-vs-else 二元判断，见 §2.6 | ✅（一次性） |
| 7 | 教研文档 N 语言化 | `SITE-AUDIT.md` §2/§3/§4/§5 脚本/§8 | ✅ |
| 8 | **结构页全覆盖** | `_pages/<code>/` 8 页 + `<code>/blog/index.html` + `_glossary_<code>/` 22 条 + 404 | ✅ |
| 9 | **App 页** | `_apps_<code>/` 全部 11 个 App（首页列表不得残缺） | ✅ |
| 10 | **Posts** | `_posts/<code>/`，按 App 分批推进，见 §7 | 分批 |
| 11 | 全量校验 | 完整构建 + htmlproofer + 教研脚本 + 产物抽验，见 §6 | ✅ |
| 12 | 记录 | `SEO-I18N-PROGRESS.md` + `SITE-AUDIT.md` §8 + `SEO-PROGRESS.md` | ✅ |

---

## 1. 不可协商红线（P0，违反即阻塞发布）

1. **URL 不破**：默认 `en` 保持根路径；新语言一律 `/<lang>/` 子路径。已发布页的 `permalink` 不得改动（无 301 机制，改则权重清零）。
2. **hreflang 成对/成环**：由 `scripts/i18n_postprocess.py` 统一注入，每页 = `len(langs)` 条语言 alternate + 1 条 `x-default`（指向 EN）。缺同名文件会导致整组被 Google 忽略，属 P0。
3. **集合必须按语言分离**：Jekyll 集合始终从 `_#{label}` 目录**递归**读取，`collections.*.path` **只影响 URL 前缀、不影响读取目录**。因此英文源（`_apps/`、`_glossary/`、`_posts/`、`_pages/`）与本地语言源不能共用集合标签。
   - EN：`apps` / `glossary` / `posts` / `pages`
   - 非 EN：`apps_<lang>` / `glossary_<lang>` / `posts`（沿用，`jekyll-paginate` 只认 `site.posts`）/ `pages`
   - 源目录：`_apps_<lang>/`、`_glossary_<lang>/`、`_posts/<lang>/`、`_pages/<lang>/`
4. **exclude 三条硬规则**：
   - 不支持 `!ruby/regexp`（会被当字符串）。
   - Jekyll `fnmatch` 不带 `FNM_PATHNAME`，`*` 会跨 `/` 匹配 → 不能用 `_posts/*` 区分根级文章与 `_posts/zh/`；用 `_posts/2*`、`_posts/1*` 按年份前缀排除。
   - `EntryFilter` 用 `start_with?` 判断目录排除 → 排除英文应用目录必须写 `_apps/`（**带尾斜杠**），写 `_apps` 会误伤同前缀的 `_apps_zh`、`_apps_id`。同理 `_glossary/`。
5. **禁止 `zh`-vs-else 二元硬编码**：所有模板必须按 `site.lang` 动态取集合、前缀、文案、日期格式。新增第 N 种语言时不得再改模板（见 §2.6）。
6. **关键词按各语言优化，但文章本体是同一篇**：非 EN 内容是 EN 对应文章的**语言版本**，不是另写一篇新文章；只允许优化关键词、标题用词与局部表达，当地高频但产品不具备的功能词不得写入文案。
7. **所有页面类型都要有对应语言内容**：只有 `posts` 与 `app` 不算完成；`pages` / `glossary` / `blog` 分页 / 搜索 / 标签 / 隐私 / 条款 / 关于 / 404 / nav / UI / feed / sitemap / Pagefind 分片全部要覆盖，见 §5。
8. **全站改动必须完整教研**：按 `SITE-AUDIT.md` §1.1，新增语言属 P0，必须跑全量构建 + htmlproofer + 教研脚本 + §8 记录。
9. **功能事实口径统一**：备份 = Google Drive + WebDAV（Google Play 描述不写 iCloud）；图标 = 400+；货币 = 50+；FAQ 用 `{:.faq-q}`，问句与答案之间留空行。
10. **文章插图必须与 EN 同源**：非 EN 文章的 `![...](/assets/images/...)` 图片路径集合（含重复次数）必须与 EN 同名文章完全一致，`alt` 按本语言关键词优化而非照抄 EN。详见 §3.5（D17 硬门禁）。
11. **所有语言版本的文章结构、文章目录、图片插入都以 EN 为准**：H2/H3 的层级、数量、顺序、含义逐条对应；结构块（表格 / 列表 / 编号步骤 / FAQ / 分隔线）与文章目录（TOC 条目数、所在行序）逐项对应；正文论点、对比对象、功能点、表格、FAQ 条目、数据大致一致，差异只出现在关键词、本地场景举例与表达措辞。因此图片落在**与 EN 完全相同的位置**，不要求「紧跟标题」。全语言由 `SITE-AUDIT.md` §5 **D18** 自动硬校验（D17 另校验图片集合、行序与 `alt`）。详见 §3.2 / §3.3 / §3.5。
12. **App 详情页 `tagline` 四语语义与信息量对等**：`tagline` 是 EN 短句的**忠实本地化版本**，只允许换用词、语序与本地惯用表达，**不得把正文 / `description` 里的功能点、规格数字、卖点清单提炼进 tagline**，也不得删减 EN 原有的核心信息。**只设上限、不设下限**（中文信息密度高，忠实短句天然只有 EN 的 0.2–0.7 倍字符数，属正常）。自动门禁（`SITE-AUDIT.md` §5 **D06**，逐 App 点名异常文件）：① 字符数 ≤ EN × `1.5`；② tagline 中的规格数字（如 `400+` / `500+` / `80`）集合必须是 EN tagline 数字集合的子集；③ 语义要点一一对应由人工抽验兜底。超出即视为「另写一句 SEO 长句」，破坏 hreflang 对应页内容对等与列表页卡片排版，属 P0。2026-11-07 已按此规则把 `_apps_id` / `_apps_th` 的 11 个 tagline 收敛回 EN 短句。

---

## 2. 新增语言 SOP（逐步）

### 2.1 Step 1 · 关键词先行（**先于任何文案**）

必须用**当地语言**检索，禁止用英语词翻译生成。至少完成两类证据：

1. **Google Play 当地在架标题**：`https://play.google.com/store/search?q=<当地词>&c=apps&hl=<lang>&gl=<国家码>`，记录在架 App 标题/描述里真实出现的说法。
2. **当地网页/评测/媒体**：检索「品类词 + 场景 + 年份」与「长尾功能词」，记录本地惯用表达、本地支付/生活场景词、本地竞品名。

判定规则：
- 当地用户混用英语借词时（如印尼语高频 `budget` / `expense tracker` / `money manager`），**照实收录借词**，不要强行译成纯本地语。
- 只收录产品真实具备的功能对应的词；不具备的（如银行自动同步、`QRIS` 自动导入）即使高频也**不得**写进文案。
- 证据写到词库「数据来源」列，并附检索日期与来源类型；不能只写「竞品调研」而无具体来源。

### 2.2 Step 2 · 登记词库

在 `seo/SEO-KEYWORDS.md` 中：
- 更新头部「语言范围」与「最后更新」；
- 在目标 App 小节新增 `§2.N.x <语言>（<code>）`，按 **Head / Middle / Long-tail / 品牌词&竞品拦截词** 四段，字段沿用 §0.3；
- 「当前覆盖」初始填 `待覆盖`，随内容落地逐条改为 `已覆盖(文件名-id)`；
- 在 `§2.N.4` 维护日志追加一行，写明检索来源、新增词、以及本地选词依据（该语言实际检索证据，而非 EN 词的逐词翻译）；
- 词库是 D09 检查的数据源，登记后 D09 MISS 统计会立即生效，故**登记与内容必须同批完成**。

### 2.3 Step 3 · 生成配置与目录

```bash
bash scripts/new-language.sh <code> "<Label>" <SHORT>
```

脚手架完成后**必须手工核对/补齐**（`scripts/new-language.sh` 已按 §8 修复，但仍逐项确认）：

| 文件 | 必须满足 |
|---|---|
| `_config_<lang>.yml` | `lang: <lang>`；`apps_<lang>` / `glossary_<lang>` 集合；`path: _pages/<lang>`、`_posts/<lang>`；`permalink: /<lang>/...` 全部；`paginate_path: /<lang>/blog/page:num`；`feed.path: <lang>/feed.xml`；`destination: _site/<lang>` |
| `exclude` | 排除 EN 根级源（`_apps/`、`_glossary/`、`_glossary/**`、`_posts/2*`、`_posts/1*`、`index.html`、`blog/`、`meow/`、`404.html` 等）与**其它所有语言的源目录**（`_apps_zh/`、`_glossary_zh/`、`_posts/zh/`、`_pages/zh/`、`zh/`、`_apps_id/` …） |
| 目录 | `_pages/<lang>/`、`_posts/<lang>/`、`_apps_<lang>/`、`_glossary_<lang>/`、`<lang>/blog/index.html` |
| `_config.yml` | 追加新语言源目录排除 |
| 其它 `_config_*.yml` | 追加新语言源目录排除（脚手架会自动做） |
| **配置内站点级可见文案** | `_config_<lang>.yml` 的 `social.links[].name`（页脚「隐私 / 条款 / 邮箱」）、`developer.title` / `developer.description` 等**必须逐项译为目标语言**。从其它语言配置复制时禁止残留源语言文案——页脚直接可见，属 P0 外观缺陷；非 zh 语言配置中出现 CJK 即视为 FAIL |

> **`feed.path` 陷阱**：配置里写成 `zh/feed.xml`（无前导 `/`），用 `s#/zh/#/id/#g` 的 sed 替换不到它，会生成 `/id/zh/feed.xml`。必须单独替换。

### 2.4 Step 4 · 数据文件

- `_data/languages.yml`：追加 `- code: <lang> / label: <本地语言名> / short: <简称>`。语言切换下拉、`window.SITE_LANGS` 自动生效。
- `_data/nav.yml`：**每个条目**补 `title.<lang>` 与 `url.<lang>`（`url.id: /id/blog/` 形式）。缺一个键 → 该导航项 `href=""`、文字空白（Liquid 静默失败）。
- `_data/ui.yml`：追加完整 `<lang>:` 块，键必须与 `en`/`zh` 对齐，另含通用化新增键：`date_format`、`updated_label`、`related_app`、`blog_intro`、`glossary_link`、`back_to_glossary`。缺键同样静默空白。

### 2.5 Step 5 · 构建脚本

`scripts/build.sh` 在 `Injecting hreflang` 之前插入：

```bash
echo "==> Building ID (/id/)"
TMP_ID=".jekyll-id"
bundle exec jekyll build --config _config_id.yml --destination "$TMP_ID"
mkdir -p _site/id
rsync -a --delete "$TMP_ID/id/" _site/id/
rm -rf "$TMP_ID"
```

`scripts/i18n_postprocess.py` **无需改动**：扫描 `_site/` 下 `^[a-z]{2}$` 顶层目录自动发现语言，自动 N 语言成环、合并 sitemap、删除各语言子 sitemap。

### 2.6 Step 6 · 模板 N 语言通用化（一次性）

在每个布局/包含文件头部统一声明：

```liquid
{% assign lang = page.lang | default: site.lang | default: 'en' %}
{% assign lp = '' %}{% if lang != 'en' %}{% assign lp = '/' | append: lang %}{% endif %}
{% assign home = '/' | prepend: lp %}
{% assign coll_apps = 'apps' %}{% if lang != 'en' %}{% assign coll_apps = 'apps_' | append: lang %}{% endif %}
{% assign coll_gloss = 'glossary' %}{% if lang != 'en' %}{% assign coll_gloss = 'glossary_' | append: lang %}{% endif %}
```

统一替换规则：

| 旧写法 | 新写法 |
|---|---|
| `{% if site.lang == 'zh' %}...{% else %}...{% endif %}`（链接） | `{{ '/blog/' \| prepend: lp \| relative_url }}` |
| `site.apps_zh` / `site.apps` 二元 | `site[coll_apps]` |
| `site.glossary_zh` / `site.glossary` 二元 | `site[coll_gloss]` |
| 写死中文/英文标题 | `site.data.ui[lang].<key>` |
| `date: '%Y年%-m月%-d日'` / `'%b %-d, %Y'` 二元 | `date: site.data.ui[lang].date_format` |
| `item.url[site.lang]` / `item.title[site.lang]` | 保留（已是动态），只需 `nav.yml` 补键 |
| 面包屑 `{{ site.url }}/` / `{{ site.url }}/blog/` | `{{ site.url }}{{ home }}` / `{{ site.url }}{{ lp }}/blog/` |
| `{% if page.url != "/" %}` | `{% if page.url != home %}` |

**Liquid 限制（已核实 jekyll-4.4.1 / liquid-4.0.4 源码）**：
- `site[string]` **可用**：`site_drop.rb` 的 `[]` 会先按集合 label 返回 `docs`。前提是该语言配置里确实定义了该集合。
- 不能写 `site.collections[coll]`（`site.collections` 被暴露成数组）。
- 不能把过滤器写进方括号：`site['apps_' | append: lang]` 非法，必须先 `assign`。
- 集合名不得与 `url` / `title` / `lang` / `data` / `posts` 等 config 键同名（否则 `[]` 命中后不回退）。
- 缺键返回 `nil` 且**静默失败**（`where_exp` 得空数组，页面空白不报错）→ 必须在教研脚本加「每语言集合数 > 0」硬门禁。
- `relative_url` **只加 `baseurl`**，不加语言前缀；`/id/` 必须由 `lp` 显式拼出。

需改造的文件（首次新增第三语言时）：`_includes/nav.html`、`related-posts.html`、`post-card.html`、`breadcrumb-jsonld.html`、`pagination.html`（仅数据）、`_layouts/app-list.html`、`app.html`、`blog.html`、`glossary.html`、`guide.html`、`post.html`、`_pages/*/search.md`、`_pages/*/tags.md`、`assets/js/i18n.js`、`404.html` + `assets/css/main.css` 的 `[data-nf]` 选择器。

**无需改动**：`_layouts/default.html`（`html lang` / `{% seo %}` canonical / `data-pagefind-body` 已动态）、`_layouts/page.html`、`_includes/analytics.html`、`app-card.html`、`app-jsonld.html`、`footer.html`、`guide-jsonld.html`、`screenshots.html`、`store-buttons.html`、`webmaster-verifications.html`、`assets/js/main.js`、`theme.js`、`scripts/i18n_postprocess.py`、`_plugins/posts-lastmod-hook.rb`。

canonical 由各 `_config_<lang>.yml` 的 `permalink` 自带 `/<lang>/` 前缀自动生成，**零改动**。

### 2.7 Step 7 · 教研文档 N 语言化

`SITE-AUDIT.md` 中所有「EN+ZH / 2 语言 / 3 条 alternate / 66↔66」断言改为 N 语言：
- §2.1 基线数量、§2.2 构建与路由事实、§2.5 基线更新规则；
- §3 维度表 D01/D03/D04/D05/D07/D08/D11；
- §4 D01/D03/D04/D05/D07/D08/D11/D12/D14；
- **§5 一键脚本**：`LANGS = ['en'] + sorted(所有两位字母目录)`；`iszh()` → `lang_of(path)`；`mds` 收集所有 `_apps_<lang>/`、`_glossary_<lang>/`、`_posts/<lang>/`、`_pages/<lang>/`；D03 改 N 路集合相等；D06 `d.get('lang') == lang_of(f)`；D07 按语言比 H2；D05 断言 `len(alts) == len(LANGS)+1`；D11 按 `lp` 检查内链前缀；D12 feed / 临时目录按 `LANGS` 循环；D15 泄漏白名单覆盖所有 `.jekyll-<lang>`。
- §8 追加本次教研记录。

---

## 3. 关键词本地化 SOP 细则

### 3.1 词层与目标页型（沿用 `SEO-KEYWORDS.md` §0.1）

| 词层 | 主吃页型 | 落地位置 |
|---|---|---|
| Head（P2） | Pillar 品类页 | H1、`title`、首段、Glossary 内链 |
| Middle（P1） | Best / vs / Alternatives | 对比表、H2、年度词 |
| Long-tail（P0） | App 详情页 / How-to | `description`、功能 H3、FAQ |
| 品牌 / 竞品拦截（P0/P1） | App 页 / vs 页 | 品牌名原样保留 + 本地竞品名 |

### 3.2 关键词本地化的可验收判定（结构不变的前提下）

> **前提**：多语言是**同一篇文章的不同语言版本**，不是按本地意图另写一篇。结构与内容由 EN 定，SEO 优化只作用在「用词」与「局部表达」两层。

一篇/一个 App 页视为合格，需同时满足：
1. `title` / `description` / H1 / 首段的**含义与 EN 一致**，用词采用该语言词库的 P0/P1 词，不做 EN 的逐词直译；
2. H2/H3 的层级、数量、顺序、含义与 EN **逐条对应**；正文论点、对比对象、功能点、表格、FAQ 条目、数据与 EN 一致；
3. 允许加入**当地真实场景举例**（货币、支付工具、发薪周期、生活开销类别等）作为局部表达，但不得因此改变小节主题、增删对比对象或删减内容；
4. 词库里该语言的 Head 词与 EN Head 词不必一一对应（如印尼语用 `catatan keuangan` 而非 `pelacak pengeluaran`）；竞品拦截词可**补充**当地在架竞品名，但 EN 原有竞品与对比对象必须保留；
5. 产品不具备的功能词为 0。

### 3.3 不同页型的本地化粒度（不得改变文章骨架）

| 页面类型 | 策略 | 理由 |
|---|---|---|
| **结构页**（about / privacy / terms / search / tags / meow / index / glossary 定义 / 404） | **忠实本地化**：语义准确、术语统一、UI 文案按 `_data/ui.yml`；不强行塞关键词 | 法律/术语文本要求准确，堆词反而伤 E-E-A-T |
| **App 详情页** | **EN 骨架 + 本地词**：字段顺序、截图、功能点、FAQ 数量与条目、Related terms 与 EN 一致；`description` / 首段 / FAQ 用词围绕当地 P0 词优化。**但 `tagline` 例外**：必须是 EN 短句的忠实本地化，禁止堆砌功能点 / 规格数字（见 §1 红线 12） | 承接转化，是长尾词主吃页；功能事实口径须三语一致；tagline 出现在列表卡片与详情页首屏，信息量不对等会破坏 hreflang 对等与卡片排版 |
| **Posts（Pillar / Best / vs / Alternatives / Tutorial）** | **EN 骨架的本地化版本**：H2/H3、段落顺序、对比对象、表格、FAQ、图片位置与 EN 逐项对应；仅把关键词、标题用词、场景举例与表达换成当地说法 | hreflang 对应页须内容对等；结构分化会让对应页内容不对等、图片错位、教研无法比对 |

### 3.4 front matter 模板（非 EN）

```yaml
---
layout: post            # 或 app / page / guide
title: <当地语言标题，含目标词>
description: "≤160 字符，含品牌 + P0 词，无裸 &"
date: YYYY-MM-DD HH:MM:SS +0800
last_modified_at: YYYY-MM-DD
lang: <lang>
permalink: /<lang>/posts/<slug>/   # 由 defaults 生成时可省
tags: [...]
image: /assets/images/apps/<app>/icon.webp
---
```

- `lang` 必须与目录一致（D06 硬门禁）；`_pages/<lang>/*.md` 必须有 `permalink: /<lang>/.../`。
- 内链一律 `](/<lang>/glossary/.../)`、`](/<lang>/apps/.../)`、`](/<lang>/posts/.../)`；EN 内链不得出现在非 EN 正文，非 EN 前缀不得出现在 EN 正文（D11）。
- 图片引用沿用 `/assets/...`（共享资源），带 `{: width=... }`，`alt` 站内唯一且不重复；**插图集合与 alt 本地化另见 §3.5（P0）**。
- FAQ 用 `**问句？**` + 下一行 `{:.faq-q}` + **空行** + 答案；H3 问句直接挂 `{:.faq-q}`。
- H2 数量与 EN 版一致（D07）；EN/ZH/新语言三者的 FAQ 条数建议对等，保证 JSON-LD 完整。

### 3.5 文章插图一致性（P0，2026-11-06 新增）

> **起因（已发生的错误）**：`id` 首批 6 篇 posts 按本地关键词重写正文时**漏掉了全部插图**，`/id/` 文章页只有全站共用图标；`zh` 也有 1 篇少 17 张竞品截图。`post.html` 只渲染 `{{ content }}`，正文没有 `![...]` 就不会有图；而旧教研 D08 只检查「已有图片」的 alt / width / 文件存在，**查不出「整篇没图」**。以下规则用于杜绝同类问题再次发生。

1. **资源集合一致**：任何非 EN 文章，只要 EN 存在同名文件（`_posts/<YYYY-MM-DD-slug>.md`），其正文 `![...](/assets/images/...)` 的**图片路径多重集（含重复次数）必须与 EN 完全一致**。不新增、不删减、不替换为本地自制图；资源一律 `/assets/...` 绝对路径（各语言构建共享同一份 `assets`）。
2. **图片位置与 EN 完全一致**：因为目录结构（H2/H3、段落顺序）与 EN 一致，图片应落在**与 EN 相同的位置**——同一个标题之后、同一段落之后、同一个列表项之后，按行序一一对应。**不要求、也不应强行「图片紧跟标题」**：EN 中跟在段落或列表项之后的图片，本地化后保持同样位置；不得挪到小节末尾、合并/拆分图片块、改变图片块之间的正文顺序，也不得留下多余空行。
3. **IAL 必须保留**：每条引用带 `{: width="180" .normal }`（沿用 EN），否则 D08「图片 width 覆盖」FAIL。
4. **alt 按本语言关键词优化，不照抄 EN**：
   - 取 `SEO-KEYWORDS.md` 对应语言的 `§2.1.x` 词表，把功能描述换成本地高频说法。例：`id` 用 `aplikasi catatan keuangan` / `catatan keuangan harian` / `atur anggaran bulanan` / `budget per kategori` / `ekspor CSV` / `reimburse` / `buku kas`；`zh` 用「记账 / 预算 / 账单 / 导出」等中文词。
   - 产品名与专有名词保留原文（Meow Money Manager、YNAB、GoPay、OVO、DANA、QRIS、Google Drive、WebDAV、CSV、Rupiah）。
   - 同文件内 alt 必须唯一（D08）；EN 用 `: Add` / `(2)` 区分的重复截图，本地化后仍保留区分后缀。禁止残留源语言整句（如 `home screen with accounts overview`）。
5. **新增文章从 EN 骨架起稿**：分批建设期间每写 1 篇非 EN 文章，**先完整复制 EN 同名文章的结构（H2/H3、段落顺序、表格、FAQ、图片行及其原位置）**，再逐行本地化文字与 `alt`；不得另起炉灶重写，也不得先发纯文字正文留待以后补图。

**自动门禁**：`SITE-AUDIT.md` §5 的 **D17** 逐篇比对非 EN 文章与 EN 同名文章的图片路径多重集、图片行序，并检查 `alt` 未照抄 EN；**D18** 逐篇比对 H2/H3 层级序列、结构块序列、文章目录（TOC 条目与行位置）、图片插入行序；任一不一致直接 FAIL。两项门禁覆盖所有非 EN 语言，已于 2026-11-06 全量启用（72 篇一致）。

**当前状态（2026-11-06）**：
- `zh` 66/66：**符合 D17 / D18**——H2/H3 层级、结构块序列、目录条目、图片行序与 EN 一致；历史翻译的纯文本段落与空行差异不纳入硬门禁（允许局部表达调整）。
- `id` 首批 6 篇：**已完成按 EN 骨架重构（6/6）**——三批交付，逐行行类型序列、图片行号与路径序列、表格 / FAQ / 目录全部与 EN 一致，本地关键词与场景举例保留，教研全绿；进度见 `SEO-I18N-PROGRESS.md`。
- `id` 其余 60 篇（Phase 3）一律直接从 EN 骨架起稿，不再重写。

---

## 4. 页面类型全覆盖清单（不遗漏）

| # | 页面类型 | 源目录 | 产出 URL | 必检 |
|---|---|---|---|---|
| 1 | 首页（App 列表） | `_pages/<lang>/index.md` | `/<lang>/` | 11 个 App 全显示；`layout: app-list` 取 `site[coll_apps]` |
| 2 | Meow 系列页 | `_pages/<lang>/meow.md` | `/<lang>/meow/` | 导航高亮 |
| 3 | 博客分页 | `<lang>/blog/index.html` | `/<lang>/blog/`、`/<lang>/blog/page2/` | `jekyll-paginate` 必须根级模板；`paginate_path` 带前缀 |
| 4 | 关于 / 隐私 / 条款 | `_pages/<lang>/about.md` `privacy.md` `terms.md` | `/<lang>/{about,privacy,terms}/` | 页脚 `social.links` 指向本语言 |
| 5 | 搜索 | `_pages/<lang>/search.md` | `/<lang>/search/` | `lang: <lang>` 在 front matter；`pf.search(q,{language:lang})`；结果过滤 `d.url.indexOf(lp + '/search') !== 0`；App 图标区用 `site[coll_apps]` |
| 6 | 标签索引 | `_pages/<lang>/tags.md` | `/<lang>/tags/` | 日期用 `site.data.ui[lang].date_format` |
| 7 | 术语索引 + 22 条定义 | `_pages/<lang>/glossary.md` + `_glossary_<lang>/` | `/<lang>/glossary/.../` | 22 条内链全部指向 `/<lang>/glossary/`，不得 404 |
| 8 | 11 个 App 详情 | `_apps_<lang>/` | `/<lang>/apps/.../` | `lang: <lang>`；FAQ 7 组；JSON-LD 完整；内链前缀 |
| 9 | Posts | `_posts/<lang>/` | `/<lang>/posts/.../` | 与 EN 同名 slug 一一对应（D03） |
| 10 | feed | `_config_<lang>.yml` `feed.path` | `/<lang>/feed.xml` | 存在且含 entry |
| 11 | sitemap / hreflang | `i18n_postprocess.py` | `/sitemap.xml` | 合并版；子 sitemap 删除；404 不进 |
| 12 | 404 | 根级 `404.html`（共享） | — | 按 `SITE_LANGS` 判断首段语言，显示对应文案 |
| 13 | 导航 / UI / 语言切换 | `_data/nav.yml` `ui.yml` `languages.yml` | 全站 | 每个 key 都有 `<lang>`；下拉含新语言 |
| 14 | Pagefind 分片 | `<html lang>` `data-pagefind-body` | `/pagefind/` | `pf.search(q,{language:'<lang>'})` 能命中 |

---

## 5. 分批实施与进度记录（防上下文溢出）

### 5.1 为什么必须分批

一次新增语言涉及 100+ 内容文件（`66 posts + 11 apps + 8 pages + 22 glossary + 1 blog 模板 + 1 配置`）。上下文溢出会导致：后半批文件质量下降、front matter 字段不一致、内链前缀混用、关键词落地走样。因此**必须**按批次推进，并把状态外置到 `SEO-I18N-PROGRESS.md`。

### 5.2 批次划分原则

- **Phase 0**：流程/进度文档 + 词库 + 基础设施（配置、数据、脚本、模板通用化、教研文档）。**一次做完、全语言复用**。
- **Phase 1**：结构页 + 全部 App 页（首页完整性所必需）+ 首个 App 的 posts。
- **Phase N**：按 App 逐个补齐 posts（`SEO-KEYWORDS.md` §2.2–§2.11 每节对应一个 App 集群，约 6 篇/组）。
- **Phase N+1（换语言）**：只做 Phase 0 的配置/数据部分 + **全部内容批次**，模板不再改。但**结构页（8 页：index/meow/about/privacy/terms/search/tags/glossary）+ `<lang>/blog/index.html` + 404 必须作为与内容同批的强制交付**：从首个非 EN 语言（`id`）的对应骨架逐篇翻译，**不得标记为「待补」后置**。`SEO-I18N-PROGRESS.md` 中该语言 `pages` 列未达 `8/8` 前，**整行不得标 ✅**（见 §1 P0 #7、§4）。验收以 §5 脚本 D03「结构页 8/8」硬门禁全绿为通过判据——任何 `1/8`、`7/8` 均为阻塞 FAIL，不允许作为「已知项」挂起。

### 5.3 每批固定动作（开工 / 收工）

开工前（从 `SEO-I18N-PROGRESS.md` 读取，**不依赖会话记忆**）：
1. 读 `SEO-I18N-PLAYBOOK.md` §1 红线、§3 关键词 SOP；
2. 读 `SEO-I18N-PROGRESS.md` 的「当前批次」「已完成清单」「待办」；
3. 读 `SEO-KEYWORDS.md` 对应 App × 语言小节，确认本批目标词；
4. 确认 `lang`、内链前缀、front matter 模板与上批一致。

收工后：
1. 更新 `SEO-I18N-PROGRESS.md`：勾选文件、写覆盖词、写校验结果、写剩余待办与下一批入口；
2. 更新 `SEO-KEYWORDS.md` 的「当前覆盖」列与维护日志；
3. 跑 §6 验收；
4. 更新 `SEO-PROGRESS.md` 与 `SITE-AUDIT.md` §8（仅当属于优化方案/措施，见文档同步范围规则）。

---

## 6. 验收清单

### 6.1 构建

```bash
cd /Users/glt/Documents/code/spacemanmeow.github.io
JEKYLL_ENV=production bash scripts/build.sh       # 完整（含 Pagefind）
SKIP_PAGEFIND=1 bash scripts/build.sh             # 本地快速预览
bundle exec htmlproofer _site --disable-external  # 或项目既有参数
```

日志应出现 `Languages detected: ['en', 'zh', '<lang>']`、`Processed N pages across 3 languages`、`==> Done. Combined site in _site/`。

### 6.2 教研脚本

按 `SITE-AUDIT.md` §5 整段执行，目标 `{PASS: N, FAIL: 0, WARN: 0}`；`D14` 有 WARN 时逐条给人工结论并写 §8。

### 6.3 产物抽验（每语言）

- `_site/<lang>/index.html` 存在，`<html lang="<lang>">`；
- 每页 `<!-- i18n-hreflang -->` 块含 `len(langs)+1` 条 alternate，x-default 指向 EN；
- canonical 为 `https://spacemanmeow.com/<lang>/...`；
- `_site/<lang>/feed.xml` 存在；`_site/<lang>/sitemap.xml` **不存在**；
- `_site/<lang>/` 下无 EN slug 泄漏；EN 根路径下无 `/<lang>/` 页面；
- 每个 App 页 JSON-LD 块数、`FAQPage` 条数与 EN 一致，无 `&amp;` 污染；
- 每篇文章 H2/H3 的层级、数量、顺序、含义与 EN 逐条对应，FAQ 条目与表格数据一致（同一篇文章的不同语言版本）；
- 每篇文章的**文章目录（TOC 条目数与位置）**、结构块（列表 / 表格 / 编号步骤 / FAQ）序列与 EN 一致，由 §5 脚本 D18 自动校验；
- 每篇文章图片块的**数量与行序位置**与 EN 一致（同一标题 / 段落 / 列表项之后），`alt` 已本地化；
- 导航、`/search/`、`/tags/`、`/blog/`、面包屑链接全部带 `/<lang>/`；
- 404 页首段语言判定正确；
- Pagefind 分片存在且 `pf.search` 用该语言能命中。

---

## 7. 已知陷阱与修复记录

| 陷阱 | 现象 | 修复 |
|---|---|---|
| `scripts/new-language.sh` 未替换 `glossary_zh` | 中文术语页被发到 `/id/glossary/` | sed 增加 `glossary_zh` → `glossary_<code>`、`_glossary_zh` → `_glossary_<code>` |
| `feed.path: zh/feed.xml` 无前导 `/` | sed 的 `s#/zh/#/id/#g` 漏替换 → `/id/zh/feed.xml` | 单独 sed 替换 `feed.path` |
| 脚手架不建 `_glossary_<code>/`、不生成其 exclude | 术语集合为空 / 中文术语被读入 | `mkdir` + `excludes_for()` 补 `_glossary_<code>`、`_pages/<code>` |
| `_config.yml` 未排除新语言源 | EN 站把新语言文档也读进来 | 补 `_posts/<lang>`、`_pages/<lang>`、`_apps_<lang>/`、`_glossary_<lang>/`、`<lang>/` |
| 模板 `zh`-vs-else | 新语言链接回 EN、App 列表空、日期英文、面包屑错 | §2.6 通用化 |
| `site[coll]` 静默失败 | 页面空白但不报错 | 教研脚本加「每语言集合数 > 0」硬门禁 |
| `_apps` 前缀排除 | 误伤 `_apps_zh` / `_apps_id` | 一律带尾斜杠 `_apps/` |
| `fnmatch` 跨 `/` | `_posts/*` 无法区分根级与子目录 | `_posts/2*` / `_posts/1*` |
| `404.html` 写死 `/zh/` | 新语言 404 显示英文 | 用 `SITE_LANGS` + 首段路径判断 |
| `i18n.js` 兜底 `[DEFAULT,"zh"]` | 注入失败时语言切换只有两语言 | 改为 `[DEFAULT]` |
| Pagefind 词干 | 部分语言检索召回偏低 | 实测后用 extended 版二进制；不臆断配置 |
| 词库登记早于内容 | D09 MISS 上升 | 词库与内容同批完成、同批校验 |
| 模板用 `page.lang` 选集合 | 非 EN 构建会渲染到 EN 根级 `_pages/index.md`（其 `page.lang: en`），`site['apps']` 返回 nil，`sort` 报 `Cannot sort a null object` | 集合/前缀/UI 一律用**构建级** `site.lang`；`page.lang` 只用于内容语言标记 |
| 从 `zh` 配置复制新语言（如 `th`） | 页脚 `social.links` 第三项残留中文「邮箱」，前两项已本地化却漏一项 | 按 §2.3 逐项本地化 `social.links` / `developer`；收工前扫描非 zh 的 `_config_<lang>.yml` 与 `_pages/<lang>/` 的 CJK 残留（注释除外），并在产物页脚抽验三项文字 |

---

## 8. 文档维护

- 新增语言后，更新本文档 §0 首个实例列表、§4 清单数量、`SEO-I18N-PROGRESS.md` 语言矩阵。
- 若 `scripts/new-language.sh` 再次改进，同步更新 §2.3 与 §7。
- 若发现新的 `zh` 残留，补进 §2.6 与 §7，并在 §8 记录教研结论。
