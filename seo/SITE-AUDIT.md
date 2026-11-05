# 网站整体教研（全站校验）规范

> **定位**：本站「大规模改动后」的唯一全站验收标准。回答一个问题：**改动之后，整个站点是否仍然正确？**
> **适用站点**：`spacemanmeow.com` 英文站（根路径）+ `/zh/` 中文站；Jekyll 4.4、双语合并构建、GitHub Pages 部署。
> **触发时机**：见 §1.1。**每次触发都必须完整跑一遍 §0 的七步，并填写 §8 教研记录表**，不得只做「改了哪一块就只验哪一块」。
> **判定原则**：P0 硬门禁全绿 + WARN 逐条给出人工结论；详见 §1.3 / §1.4。
> **基线快照日期**：2026-11-05（历史欠账已全部清零，见 §8）。所有数量以 §2 为准，数量变化必须能解释。
> **关联文档**：`SEO-OPTIMIZATION-PLAN.md`（总览）、`SEO-PLAYBOOK.md`（方法与运营红线）、`SEO-PROGRESS.md`（进度台账）、`SEO-METRICS.md`（月度指标）、`SEO-KEYWORDS.md`（关键词权威库）。本文档不替代它们，只规定「如何整体验收」。

---

## 0. 速查卡：一次完整教研

| 步 | 动作 | 命令 / 入口 | 级别 |
|---|---|---|---|
| 1 | 工作区与文件名红线 | `git status --short`；对照 §4 D14 | P0 |
| 2 | **完整构建（CI 同款，不带 `SKIP_PAGEFIND`）** | `JEKYLL_ENV=production bash scripts/build.sh` | P0 |
| 3 | 链接与资源校验 | `bundle exec htmlproofer _site --disable-external --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"` | P0 |
| 4 | 一键静态教研 | 复制 §5 脚本整段执行（在仓库根目录） | P0 |
| 5 | 产物与 SEO 产物抽验 | §4 D05 / D10 / D11 / D12 的人工抽验项 | P1 |
| 6 | 线上与人工项 | §6（GSC、Rich Results、PSI、外链、真实设备） | P1 |
| 7 | 记录 | 填写 §8 教研记录表，写明结论与基线数字变化 | P0 |

> 日常小改动（单篇文案、纯错别字）可只跑步 1–4，并用 `SKIP_PAGEFIND=1 bash scripts/build.sh` 加速；**但大规模改动的全站教研必须跑不含 `SKIP_PAGEFIND` 的完整构建**，否则 Pagefind 索引维度（D12）无法验收。
> 本地 fast 版构建命令：`SKIP_PAGEFIND=1 JEKYLL_ENV=production bash scripts/build.sh`。
> 本地 fast 版链接校验：`bundle exec htmlproofer _site --disable-external --allow-hash-href --ignore-urls "/^https?:\/\//"`。

---

## 1. 触发时机与判定原则

### 1.1 必须完整教研（P0）

以下任一情况发生，都要按 §0 跑完整流程：

- 批量内容改动：一次改动 ≥ 3 个内容文件，或跨 ≥ 2 个 App 分组；
- 结构性改动：`_layouts/`、`_includes/`、`_data/`、`_plugins/`、`assets/css/`、`assets/js/`；
- 构建与配置改动：`scripts/`、`_config.yml`、`_config_zh.yml`、`Gemfile`、`.github/workflows/`；
- 双语 / 集合 / 路由改动：新增语言、改 `collections`、改 `permalink`、改 `exclude`、目录重命名；
- 批量图片或 `alt` 改动、批量 `description` / frontmatter 改动；
- 关键词库 `SEO-KEYWORDS.md` 的结构或覆盖状态批量变更；
- 发布前（合并到 `main` / `master` 之前）的最后一次验收。

### 1.2 可简化（不视为「大规模改动」）

单篇文案微调、错别字、纯格式调整。**仍需**跑步 1–4 的构建与链接校验；教研记录表可简写为「小改动，步 1–4 通过」。

### 1.3 判定分级

| 级别 | 含义 | 处置 |
|---|---|---|
| **P0 / FAIL** | 构建失败、链接断、双语缺页、文件缺失、URL 泄漏、hreflang/sitemap 破损、关键词丢失、JSON-LD 污染 | **阻塞发布**，必须当场修复并重跑全流程 |
| **P1 / WARN** | 需人工确认或线上验证的项（外链、Pagefind、发布物白名单、性能、合规表述抽验） | 记录结论；有疑点则转 P0 |
| **P2 / BASE** | 已知历史欠账（§2.3 当前为空） | 与基线比对；**数量不得上升**；改善后更新基线 |

### 1.4 基线对账原则

站点存在若干未清理的历史欠账（§2.3）。教研脚本对它们不判 FAIL，而是输出当前值并与 §2.3 基线比较：

- `当前值 > 基线` → **FAIL，判定为本次改动引入回归，必须修复**；
- `当前值 == 基线` → `BASE`，允许通过，但需在记录表中登记「欠账仍在」；
- `当前值 < 基线` → `PASS`，视为改善，并同步更新 §2.3 与脚本中的 `BASE` 常量。

这条规则的目的：**不因历史欠账让每次教研满屏 FAIL，也不让新改动悄悄扩大欠账。**

> 2026-11-05 整改教研已把 §2.3 全部欠账清零，当前 `BASE` 为空；**所有维度均为 P0 硬门禁**，任何回升直接判 FAIL，不再有「与基线持平即可放行」的口子。

---

## 2. 站点基线快照（2026-11-05）

### 2.1 结构与数量

| 类别 | 数量 | 路径 |
|---|---|---|
| 文章 | **132 = 66 EN + 66 ZH** | `_posts/*.md` / `_posts/zh/*.md`（同名一一对应） |
| 应用详情页 | **22 = 11 EN + 11 ZH** | `_apps/` / `_apps_zh/` |
| 静态页 | **16 = 8 EN + 8 ZH** | `_pages/` / `_pages/zh/` |
| Glossary 术语页 | **44 = 22 EN + 22 ZH** | `_glossary/` / `_glossary_zh/` |
| 内容 Markdown 合计 | **214** | 上述四类 |
| 图片文件 | **533**（526 webp + 4 jpg + 1 png + 1 svg + 1 ico） | `assets/images/` |
| 模板 | 8 layouts + 13 includes | `_layouts/` / `_includes/` |
| 构建产物 | **229 个 HTML**（含 404）、sitemap **228 条 `<loc>`** | `_site/` |
| 语言 | 2（EN 根 / ZH `/zh/`） | `scripts/i18n_postprocess.py` 日志 `Languages detected: ['en', 'zh']` |
| 内链 | htmlproofer 检查约 **407** 条内部链接 | 随内容增长变化 |

> 数量是快照不是硬阈值。新增文章/术语后数量上升是正常的，但必须在教研记录表中写明「新增了什么、EN/ZH 是否成对」。

### 2.2 构建与路由事实（教研时的判定依据）

1. **合并构建**：`scripts/build.sh` 先用 `_config.yml` 构建 EN 到 `_site/`，再用 `_config_zh.yml` 构建 ZH 到临时目录 `.jekyll-zh`，`rsync` 到 `_site/zh/`，最后 `scripts/i18n_postprocess.py --url` 注入 hreflang 并覆盖写合并 `sitemap.xml`，随后生成 Pagefind 索引。
2. **集合必须分离**：Jekyll 集合始终从 `_#{label}` 目录递归读取，`collections.*.path` 只影响 URL、不影响读取目录。因此中文应用必须用独立集合 `apps_zh`（源 `_apps_zh/`），术语用 `glossary_zh`（源 `_glossary_zh/`）；否则 ZH 构建会把英文文档一并读入并映射到 `/zh/`。
3. **`exclude` 细节**：Jekyll fnmatch 的 `*` 不带 `FNM_PATHNAME`，会跨 `/` 匹配，故不能用 `_posts/*` 区分根级文章与 `_posts/zh/`；`_config_zh.yml` 用 `_posts/2*`、`_posts/1*` 按年份前缀排除英文文章，并用 `_apps/`（**带尾斜杠**）避免误伤 `_apps_zh`。不支持 `!ruby/regexp`，且目录排除用 `start_with?` 判断。
4. **URL 规则**：EN `/posts/:title/`、`/apps/:name/`、`/glossary/:name/`；ZH 全部加 `/zh/` 前缀。`_pages/*.md` 用显式 permalink，不会与 `/zh/` 冲突。
5. **hreflang / sitemap**：按「去掉语言前缀后的路径」分组；每页注入组内所有语言 + 一条 `x-default` 指向 EN；合并 sitemap 每个语言变体一条 `<url>`，并删除 `/zh/sitemap.xml`；`404.html` 不注入、不进 sitemap。
6. **feed / 搜索**：`feed.xml`（EN）与 `zh/feed.xml`（ZH）；Pagefind 索引 `_site/pagefind/`，`data-pagefind-body` 只索引正文；`robots.txt` 指向生产 sitemap。
7. **CI**：`.github/workflows/pages-deploy.yml` 跑 `bash scripts/build.sh` + `htmlproofer`，部署后 Ping IndexNow。教研须与 CI 同款构建，不能只跑 `tools/test.sh`（见 §2.4）。

### 2.3 已知基线欠账（BASE）

**当前为空（`BASE = {}`）。** 2026-11-05 的整改教研已把建立本文档时发现的全部欠账清零；这些项已升级为 §5 脚本的 P0 硬门禁（`chk`），一旦回升直接判 FAIL。

| 原欠账 | 原基线 | 现状 | 修复方式 |
|---|---|---|---|
| `description > 160` | 29 | **0**（最长 159） | 逐条改写，保留年份、主词与事实表述 |
| EN/ZH H2 数量不一致 | 1 | **0** | 中文教程文末重复的 FAQ 合并进原 FAQ 章节，EN/ZH 各 14 个 H2、9 个问答 |
| `lang` 缺失或与目录不符 | 1 | **0** | `_pages/search.md` 补 `lang: en` |
| 关键词虚标 | §2.1 MISS 36 | **全 11 组 MISS = 0** | Meow Money 组 10 个 EN/ZH 页面成对补 FAQ 问答，36 词全部真实落地 |
| 裸 `&` 的 description | 1 | **0** | 改写为 `and` |
| `_site/seo/` 发布内部文档 | 是 | **否** | 两份 `_config*.yml` 的 `exclude` 加 `seo/` 与 `"seo/**"` |
| Pagefind 索引缺失 | SKIP_PAGEFIND 构建 | **已生成** | 完整构建（2 语言 / 228 页 / 8704 词） |
| 图片 width 等模糊 WARN | 5 条 | **0** | §5 脚本改为精确 `chk` 判定 |

> 若未来出现无法立即清理的新欠账，按 §1.4 登记进 `BASE` 并同步本表；**不得为了让脚本少报 FAIL 而把已清零项退回 BASE**。

### 2.4 已知工程风险（教研时必须确认，不自动放行）

- `tools/test.sh` **只做 EN 单语言构建**，不覆盖 `/zh/`、hreflang 与合并 sitemap；**不可用于全站验收**。
- `SEO-PROGRESS.md` T-34 明细引用的 `CONTENT-OPTIMIZATION-RULES.md` 在仓库中不存在（引用悬空）。
- `tools/compress_images.py`、`tools/md_to_html.py` 硬编码旧机绝对路径 `/Users/gaolitao/...`，在当前工作区不可用。
- 文档滞后：`SEO-PROGRESS.md` / `SEO-PLAYBOOK.md` 记 Glossary 为「16 条/语言」，实际 **22 条/语言**；`SEO-KEYWORDS.md` §3 口径说明仍写「仅 Crosshair Aim 组完成内容侧深度优化」，实际 **11 组关键词已全部落地**（T-34 深度优化 10 组，§2.1 于 2026-11-05 整改教研补齐）。
- `README.md` 仍是 Chirpy Starter 模板，未写本站构建命令。

### 2.5 基线更新规则

只要修复或新增了 §2.3 任一项，或新增语言 / 集合 / 批量新增内容，**必须同步更新本文档 §2 与 §5 脚本顶部的 `BASE` 常量**，并在 §8 记录表写明变更前后数值。当前 `BASE` 为空，表示所有维度均为硬门禁。

---

## 3. 校验维度总表

| 编号 | 维度 | 级别 | 主要手段 | 合格标准 |
|---|---|---|---|---|
| D01 | 构建与产物 | P0 | `scripts/build.sh` 全量构建 | 退出码 0；EN/ZH 首页存在；日志 2 语言、页数正常 |
| D02 | 链接与资源 | P0 | `htmlproofer` | 0 failure；内链、锚点、图片、脚本全通 |
| D03 | 双语源对账 | P0 | §5 脚本 | 文章/应用/页面/术语 4 组文件名差集均为 0 |
| D04 | 路由、集合与隔离 | P0 | 配置核对 + 产物 URL 抽查 | 集合分离、`exclude` 正确、`/zh/` 下无英文页泄漏 |
| D05 | hreflang / sitemap / canonical / feed / robots | P0 | §5 脚本 + 人工抽验 | 每页 3 条 alternate；合并 sitemap；404 排除；canonical 为生产域名 |
| D06 | frontmatter 与元数据 | P0 | §5 脚本 | 必填齐、`lang` 对、`description ≤160`、无裸 `&` |
| D07 | 正文结构与中英对等 | P0 | §5 脚本 + 人工抽验 | H2 一致、无汉字间多余空格、段落对应 |
| D08 | 图片与可访问性 | P0 | §5 脚本 | alt 唯一、无 `![image]`、引用文件存在、全部带 `width` |
| D09 | 关键词真实覆盖 | P0 | §5 脚本归一化逐词核对 | 全部 11 组 MISS = 0 |
| D10 | 结构化数据与富媒体 | P0 + P1 | §5 脚本 + Rich Results Test | JSON-LD 无 `&amp;`；app 页 @type 正确；OG 图正确 |
| D11 | 内链闭环 | P0 | §5 脚本 + 抽验 | 语言前缀正确、glossary/tags/app 回链闭合 |
| D12 | 搜索与索引 | P0 | 完整构建 + 产物检查 | Pagefind 索引生成、sitemap/feed/robots/IndexNow 正常 |
| D13 | 合规与产品表述 | P1 | 人工抽验 | 只读/免 root、不承诺虚假效果、YMYL、隐私、外链 rel |
| D14 | 文件名与 URL 红线 | P0 | `git status` | 无未经批准的文章/页面重命名、删除、新增；permalink 未变 |
| D15 | 发布物与敏感文件 | P0 | 产物目录检查 | 无临时目录、无凭据；`_site/seo/` 不存在 |
| D16 | 文档与台账一致性 | P1 | 人工核对 | 优化方案/进度已同步；纯修复未误写进计划文档；滞后项已登记 |

---

## 4. 逐维度检查项

### D01 构建与产物（P0）

- **检查点**：完整构建退出码为 0；`_site/index.html`、`_site/zh/index.html` 存在；日志出现 `Languages detected: ['en', 'zh']` 与 `Processed N pages across 2 languages`；`.jekyll-zh` 临时目录已清理；`==> Done. Combined site in _site/` 出现。
- **命令**：`JEKYLL_ENV=production bash scripts/build.sh`（发布前教研**不要**带 `SKIP_PAGEFIND`）。
- **合格标准**：N 与 §2.1 快照 228 相当（允许随新增内容增长，须解释）。
- **失败处理**：先看是 EN 还是 ZH 阶段失败；ZH 失败优先查 `_config_zh.yml` 的 `exclude` 与集合目录名；EN 失败查 `_config.yml` 与 frontmatter 语法。

### D02 链接与资源（P0）

- **检查点**：`htmlproofer` 三 check（Images / Links / Scripts）全绿；内部链接与 hash 锚点 0 失败。
- **命令**：CI 同款见 §0 步 3。
- **合格标准**：`HTML-Proofer finished successfully.`
- **失败处理**：断链先判断是「源文件改名」还是「permalink 变化」；hash 锚点失败检查 H2/H3 是否改了文字；图片失败检查 `/assets/...` 路径大小写与扩展名。

### D03 双语源对账（P0）

- **检查点**：`_posts` 66↔66、`_apps` 11↔11、`_pages` 8↔8、`_glossary` 22↔22，**按同名文件**一一对应；成对文件 `title/description/tags/image/layout` 均存在。
- **手段**：§5 脚本 D03。
- **失败处理**：缺哪一侧补哪一侧；新增文章必须 EN/ZH 成对提交，且 ZH 放 `_posts/zh/`。

### D04 路由、集合与隔离（P0）

- **检查点**：
  1. `_config_zh.yml` 仍使用 `apps_zh` / `glossary_zh` 独立集合，源目录为 `_apps_zh/` / `_glossary_zh/`；
  2. `exclude` 仍含 `_apps/`（带尾斜杠）、`_posts/2*`、`_posts/1*`、`_glossary/`，且没有 `_posts/*` 这类会跨目录误伤的写法；
  3. `_site/zh/` 下**不出现**只在 EN 存在的文章 slug；EN 根路径下不出现 `/zh/` 页面；
  4. 所有 ZH 内容 URL 以 `/zh/` 开头，`<html lang="zh">`；EN 为 `lang="en"`；
  5. 新增语言时，`_data/languages.yml`、`build.sh` 的语言块、`<lang>/blog/index.html` 三处同步。
- **失败处理**：任何「英文文档被 ZH 读到并发布到 /zh/」或「中文文档泄漏到根路径」都是 P0，回到 §2.2 的分离规则修配置，**不要**靠改 permalink 硬压。

### D05 hreflang / sitemap / canonical / feed / robots（P0）

- **检查点**：
  - 每个 HTML（除 404）都有 `<!-- i18n-hreflang -->` 块，含 `hreflang="en"`、`hreflang="zh"`、`hreflang="x-default"` 共 3 条，且 x-default 指向 EN；组内互指成环；
  - `_site/sitemap.xml` 为合并版（约 228 条 `<loc>`），每条带 `xhtml:link` alternates；`/zh/sitemap.xml` **不存在**；404 不在 sitemap；
  - canonical 为 `https://spacemanmeow.com/...`，ZH 为 `.../zh/...`；`url` 配置未被改成 localhost；
  - `_site/feed.xml` 与 `_site/zh/feed.xml` 均存在且各含约 10 条 entry；`robots.txt` 的 Sitemap 行指向生产域名。
- **手段**：§5 脚本 D05 + 人工抽查 1 个文章页、1 个 app 页、1 个 glossary 页的 `<head>`。
- **失败处理**：hreflang 缺页通常是「某语言缺同名文件」（回到 D03）；sitemap 分裂说明 `i18n_postprocess.py` 没跑或 URL 分组键错误。

### D06 frontmatter 与元数据（P0）

- **检查点**：
  - 全部内容 md 必须有 `title`、`description`；文章额外 `date/layout/tags/image`；应用页额外 `icon`；静态页额外 `permalink`；`tutorial-*` 带 `author`；
  - `lang` 与目录一致；`description ≤160` 字符且含目标词；`last_modified_at` 必须伴随**真实正文改动**（只推日期无效）；
  - 文章 `image:` 必须等于目标 App 的 `icon`，否则 App⇄文章回链断裂；
  - 应用页 / 隐私 / 条款页有 `seo.type: WebPage`，避免被误判 `BlogPosting`；
  - `description` 中裸 `&` 会转 `&amp;` 污染 JSON-LD，脚本硬门禁要求为 0。
- **手段**：§5 脚本 D06；`description >160` 与裸 `&` 均为硬门禁 FAIL。
- **失败处理**：补字段；压缩 description 时保留年份与 2–4 个目标词；不要为塞关键词在汉字之间插空格（见 D07）。

### D07 正文结构与中英对等（P0）

- **检查点**：EN/ZH 成对文章 H2 数量一致、小节语义对应；中文正文**无汉字之间的多余空格**（数字/英文与汉字之间的空格是合法排版，保留）；术语统一（品牌名、竞品名大小写）；中文不是英文的机器直译；每篇有实质选型/场景/FAQ 内容。
- **手段**：§5 脚本 D07 + 人工抽验改动涉及的页面。
- **说明**：关键词库中的中文词本身带空格（如 `最佳悬浮助手 安卓`），正文已按中文排版规范去掉汉字间空格，因此**逐词核对必须用「去空格归一化」匹配**（见 D09），不能要求字面严格命中。
- **失败处理**：H2 不一致时补齐对应语言的小节；发现汉字间空格用「只删汉字间空格」的正则统一清理，不要动数字/英文两侧空格。

### D08 图片与可访问性（P0）

- **检查点**：同文件内 `alt` **零重复**且关键词化；`![image]` 零残留；所有 `/assets/...` 引用文件真实存在；每图带 `{: width="180" .normal }` 之类宽度属性防 CLS；EN/ZH 图片引用一一对应；新增图片走 webp 压缩。
- **手段**：§5 脚本 D08 + `tools/compress_images.py`（注意 §2.4 的旧机路径风险）。
- **失败处理**：重复 alt 用「原描述 + 图片文件名对应的视图标识」区分，不要只加序号凑唯一；缺图先确认是路径写错还是资源未提交。

### D09 关键词真实覆盖（P0）

- **检查点**：从 `SEO-KEYWORDS.md` 提取所有标「已覆盖」的词（含中文竞品拦截表按 `/` 拆分），去空格/去粗体/小写归一化后，在**全站内容 md 正文**中逐词核对；**§2.1–§2.11 全部 11 组必须 MISS = 0**，不再分组豁免。
- **手段**：§5 脚本 D09。
- **配套检查**：新增/升权关键词后，`SEO-KEYWORDS.md` 的「当前覆盖」列与维护日志已回写；同词不由两篇主吃（cannibalization）；目标词来自词库。
- **失败处理**：MISS 说明「台账标已覆盖但正文没落地」——要么把词自然织入正文/meta/alt，要么把状态改回「待覆盖」；**不允许只改台账状态蒙混过关**。

### D10 结构化数据与富媒体（P0 + P1）

- **检查点**：所有 `<script type="application/ld+json">` 块中 **`&amp;` 为 0**（正确提取脚本块，不要用跨标签正则误报）；app 页 @type 为 `WebPage` + `SoftwareApplication` + `FAQPage` + `BreadcrumbList`；guide 页有 `Article`；每个 app 的 OG 图是自身 `icon.webp`；站长验证 meta 存在。
- **手段**：§5 脚本 D10 + 每月用 Google Rich Results Test 抽验 1–2 个 app 页。
- **失败处理**：`&amp;` 通常来自 frontmatter 里的裸 `&`，改写为「and」或中文顿号。

### D11 内链闭环（P0）

- **检查点**：ZH 正文的术语链接用 `/zh/glossary/...`，EN 用 `/glossary/...`；EN 内容里不误带 `/zh/`；`_pages/glossary.md` 索引覆盖全部 22 条；`/tags/#<slug>` 锚点存在；每篇文章 `image == app icon` 且 App 页能列出对应 Guides；related-posts 只出同语言；外链带 `rel="noopener noreferrer"`。
- **手段**：§5 脚本 D11 + 人工抽验新增/改动文章的首段内链与底部相关推荐。
- **失败处理**：语言前缀错误会导致中文读者跳到英文页、破坏 hreflang 语义，属 P0。

### D12 搜索与索引（P0 + P1）

- **检查点**：完整构建生成 `_site/pagefind/`；搜索页能 `import("/pagefind/pagefind.js")` 并按语言检索；sitemap 与 IndexNow 使用生产 URL；404 有 `data-pagefind-ignore` 且不在 sitemap；GoatCounter 与 `.nojekyll` 正常。
- **说明**：`SKIP_PAGEFIND=1` 构建不会生成索引，脚本直接判 FAIL（不再是 WARN）；**发布前教研必须完整构建一次**；CI 不设该变量，会生成索引。
- **失败处理**：Pagefind 失败先看 `.pagefind-bin/` 二进制与网络；索引缺失时搜索页会静默失效，需手动打开搜索页验证。

### D13 合规与产品表述（P1）

- **检查点**：CPU Monitor / System Monitor 类强调**只读、免 root、不承诺一键降温/加速/清理**；Floating Assistant / Crosshair Aim 强调**纯视觉叠层、不改游戏数据、不触发反作弊、权限透明**；清理/加速类词按「品类对照」诚实落地，不虚构功能；财务类（Meow Money）属 YMYL，用事实与数字、避免空泛「最好」绝对词；隐私表述与 `privacy.md` 一致。
- **手段**：人工抽验改动涉及的 App 分组的 pillar / tutorial / vs 首段。
- **失败处理**：发现与只读定位冲突的营销话术，立即改写；这是信任问题，不要留到下次。

### D14 文件名与 URL 红线（P0）

- **检查点**：`git status --short` 中，内容目录（`_posts/`、`_posts/zh/`、`_apps*/`、`_pages/`、`_glossary*/`）不得出现未经批准的 `R` / `D` / `A` / `??`；已发布页 `permalink` 不变（本站**没有 301 重定向机制**，改文件名即等于丢权重）；新增语言 URL 一旦发布不再改。
- **手段**：`git status --short` + §5 脚本 D14（无增删改判 PASS，有则 WARN 需人工确认）。
- **失败处理**：确需改名时，必须同时评估索引丢失、hrefang 分组断裂、外链与 sitemap 变化，并在记录表中写明；新增文章必须 EN/ZH 成对。

### D15 发布物与敏感文件（P0 + WARN）

- **检查点**：`_site/` 中不含 `.jekyll-zh/`、`.pagefind-bin/`、`tools/gsc/credentials.json`、`token.json`、缓存目录；`.nojekyll` 存在；**`_site/seo/` 不存在**（内部 SEO 文档与 `seo/data/*.csv/json` GSC 导出不得公开）。
- **手段**：§5 脚本 D15 + `find _site -maxdepth 2 -type d | sort` 抽查。
- **失败处理**：`seo/` 已加入两份 `_config*.yml` 的 `exclude`；若重新出现，先 `rm -rf _site/seo` 再完整重构建验证；敏感文件泄漏属 P0。

### D16 文档与台账一致性（P1）

- **必须同步**（属于 SEO 优化方案/措施、进度与规划）：
  - `SEO-KEYWORDS.md`：关键词覆盖状态、竞品拦截词升权、维护日志、章节结构调整；
  - `SEO-PROGRESS.md`：T-34 等任务进度、已完成组数；
  - `SEO-METRICS.md`：月度 GSC / GoatCounter 数据复盘。
- **不要同步**（bug 修复、细节 / 格式调整、一致性修复）：**不写进 `SEO-OPTIMIZATION-PLAN.md`**，也不为纯修复新增「已完成优化」条目。
- **教研时确认**：本次改动属于哪一类、台账是否正确；§2.4 的文档滞后项是否在本次被扩大；教研记录表是否已填。

---

## 5. 一键静态教研脚本

> **用法**：在仓库根目录（`/Users/glt/Documents/code/spacemanmeow.github.io`）整段复制执行；**执行前先完成一次构建**（否则产物类维度会跳过）。
> **输出**：`PASS` = 硬门禁通过；`FAIL` = 阻塞；`WARN` = 需人工确认（仅 D14 出现文件增删改时）。
> **维护**：`BASE` 当前为空；若登记新欠账，同步修改脚本顶部 `BASE` 常量与本文档 §2.3。

<!-- AUDIT-SCRIPT-START -->
```bash
python3 - <<'PY'
# 全站教研静态检查 v2.0 / 基线 2026-11-05（BASE 已清零）
# 若未来登记新欠账，按 §1.4 恢复 base() 对账逻辑并同步 §2.3
import os, re, glob, subprocess, collections
BASE = {}
R = []
def add(lv, c, n, d=''): R.append((lv, c, n, d))
def chk(c, n, ok, d=''): add('PASS' if ok else 'FAIL', c, n, d)
def warn(c, n, d=''): add('WARN', c, n, d)
def fs(p): return sorted(glob.glob(p, recursive=True))
def nm(p): return {os.path.basename(x) for x in fs(p)}
def fm(t):
    if not t.startswith('---'): return {}
    e = t.find('\n---', 3)
    if e < 0: return {}
    d = {}
    for l in t[3:e].split('\n'):
        m = re.match(r'^([A-Za-z_][A-Za-z_0-9]*):\s*(.*)$', l)
        if m: d[m.group(1)] = m.group(2).strip()
    return d
def iszh(f): return f.startswith(('_posts/zh/', '_pages/zh/', '_apps_zh/', '_glossary_zh/'))
def norm(s): return s.lower().replace(' ', '').replace('\t', '').replace('**', '').replace('　', '')
mds = sorted(set(fs('_posts/**/*.md') + fs('_apps/**/*.md') + fs('_apps_zh/**/*.md')
                 + fs('_pages/**/*.md') + fs('_glossary/**/*.md') + fs('_glossary_zh/**/*.md')))
txt = {f: open(f, encoding='utf-8').read() for f in mds}
fms = {f: fm(t) for f, t in txt.items()}
# D03
for lab, a, b in [('文章', '_posts/*.md', '_posts/zh/*.md'),
                  ('应用', '_apps/*.md', '_apps_zh/*.md'),
                  ('页面', '_pages/*.md', '_pages/zh/*.md'),
                  ('术语', '_glossary/*.md', '_glossary_zh/*.md')]:
    A, B = nm(a), nm(b)
    chk('D03', lab + ' EN/ZH 一一对应', A == B, f'EN={len(A)} ZH={len(B)} 差集={len(A ^ B)}')
# D06
need0 = {'title', 'description'}
bad = []
for f, d in fms.items():
    n = set(need0)
    if f.startswith('_posts/'): n |= {'date', 'layout', 'tags', 'image'}
    if f.startswith(('_apps/', '_apps_zh/')): n.add('icon')
    if f.startswith('_pages/'): n.add('permalink')
    if n - set(d): bad.append((f, ','.join(sorted(n - set(d)))))
chk('D06', 'frontmatter 必填字段', not bad, f'异常 {len(bad)} {bad[:2]}')
langbad = [f for f, d in fms.items() if d.get('lang') != ('zh' if iszh(f) else 'en')]
chk('D06', 'lang 存在且与目录一致', not langbad, f'异常 {len(langbad)} {langbad[:2]}')
long, amp = [], []
for f, d in fms.items():
    v = d.get('description', '')
    if v.startswith(('>-', '>', '|')): continue
    s = v.strip('"')
    if len(s) > 160: long.append((f, len(s)))
    if '&' in s: amp.append(f)
chk('D06', 'description ≤160 字符', not long, f'超长 {len(long)} {long[:2]}')
chk('D06', 'description 无裸 &', not amp, f'{len(amp)} 处')
# D07
h2, sp = [], []
for f, t in txt.items():
    if re.search(r'(?<=[\u4e00-\u9fff])[ \t]+(?=[\u4e00-\u9fff])', t): sp.append(f)
for n in nm('_posts/*.md'):
    z = '_posts/zh/' + n
    if os.path.exists(z):
        a = len(re.findall(r'^## ', txt['_posts/' + n], re.M))
        b = len(re.findall(r'^## ', txt[z], re.M))
        if a != b: h2.append((n, a, b))
chk('D07', 'EN/ZH H2 数量一致', not h2, f'不一致 {len(h2)} {h2[:2]}')
chk('D07', '无汉字间多余空格', not sp, f'残留 {len(sp)} {sp[:2]}')
# D08：严格按紧跟图片的 {: width=... } 判定
IMGRE = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)\s*(\{:[^}]*\})?')
dup, gen, missing, nowidth, total = [], [], [], [], 0
for f, t in txt.items():
    a = IMGRE.findall(t)
    if len(a) != len(set(x[0] for x in a)): dup.append(f)
    if re.search(r'!\[image\]', t, re.I): gen.append(f)
    for alt, p, attr in a:
        if p.startswith('/assets/'):
            total += 1
            if not os.path.exists('.' + p): missing.append((f, p))
            if not attr or not re.search(r'width\s*=', attr): nowidth.append((f, p))
chk('D08', '同文件 alt 唯一', not dup, f'重复 {len(dup)} {dup[:2]}')
chk('D08', '无 ![image] 残留', not gen, f'{len(gen)}')
chk('D08', '引用图片文件存在', not missing, f'缺失 {len(missing)} {missing[:2]}')
chk('D08', '图片 width 覆盖（防 CLS）', total > 0 and not nowidth,
    f'{total} 处引用，缺 width {len(nowidth)} {nowidth[:2]}')
# D09：全部 11 组均须 MISS=0
K = open('seo/SEO-KEYWORDS.md', encoding='utf-8').read().split('\n')
sec, terms = None, collections.defaultdict(set)
for l in K:
    m = re.match(r'^## (2\.\d+) ', l)
    if m: sec = m.group(1); continue
    if l.startswith('## 3.'): sec = None; continue
    if sec is None or not l.startswith('|') or l.startswith('|---'): continue
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) >= 7 and c[0] != '关键词' and '已覆盖' in c[6]:
        for w in c[0].split('/'): terms[sec].add(w.strip())
    if len(c) == 4 and '已覆盖' in c[3]:
        for w in c[1].split('/'): terms[sec].add(w.strip())
cn = norm('\n'.join(txt.values()))
miss = sorted(w for v in terms.values() for w in v if w and norm(w) not in cn)
chk('D09', '全部关键词真实覆盖', not miss and len(terms) >= 11,
    f'{len(terms)} 组，MISS {len(miss)} {miss[:3]}')
# D11
zbad = [f for f, t in txt.items() if iszh(f) and re.search(r'\]\(/glossary/', t)]
ebad = [f for f, t in txt.items() if not iszh(f) and re.search(r'\]\(/zh/', t)]
chk('D11', '内链语言前缀', not zbad and not ebad,
    f'ZH 缺前缀 {len(zbad)} / EN 误带 {len(ebad)}')
# D14
st = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True).stdout.split('\n')
risk = [l for l in st if re.match(r'^\s*(R|D|A|\?\?)', l)
        and any(k in l for k in ('_posts/', '_apps', '_pages/', '_glossary'))]
if risk: warn('D14', '文件名增删改（红线）', f'{len(risk)} 条需人工确认 {risk[:2]}')
else: chk('D14', '文件名增删改（红线）', True, '0 条')
# 产物维度
if os.path.isdir('_site'):
    hs = fs('_site/**/*.html')
    chk('D05', '每页 hreflang 块',
        all('i18n-hreflang' in open(h, encoding='utf-8').read()
            for h in hs if os.path.basename(h) != '404.html'), f'{len(hs)} 页')
    chk('D05', 'zh 子 sitemap 已删', not os.path.exists('_site/zh/sitemap.xml'), '')
    sm = open('_site/sitemap.xml', encoding='utf-8').read() if os.path.exists('_site/sitemap.xml') else ''
    chk('D05', '合并 sitemap', len(re.findall(r'<loc>', sm)) > 0,
        f'{len(re.findall(r"<loc>", sm))} 条 loc')
    chk('D12', '404 不进 sitemap', '404' not in sm, '')
    ld = [b for h in hs for b in re.findall(
        r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',
        open(h, encoding='utf-8').read(), re.S)]
    chk('D10', 'JSON-LD 无 &amp;', not any('&amp;' in b for b in ld), f'{len(ld)} 个块')
    chk('D12', 'feed / robots',
        os.path.exists('_site/feed.xml') and os.path.exists('_site/zh/feed.xml')
        and os.path.exists('_site/robots.txt'), '')
    chk('D12', 'Pagefind 索引', os.path.isfile('_site/pagefind/pagefind.js'), '')
    chk('D15', '无临时目录残留', not os.path.isdir('.jekyll-zh'), '')
    chk('D15', '内部 seo/ 未发布', not os.path.isdir('_site/seo'),
        f'存在={os.path.isdir("_site/seo")}')
    leaks = [p for p in fs('_site/**/*') if any(k in p for k in
             ('credentials.json', 'token.json', 'pagefind-bin', 'jekyll-zh'))]
    chk('D15', '无凭据/缓存文件泄漏', not leaks, f'{len(leaks)} 个')
else:
    warn('DXX', '未构建', '请先运行 bash scripts/build.sh')
print('=== 全站教研结果 ===')
for lv, c, n, d in R: print(f'{lv:4s} {c:4s} {n:32s} {d}')
print('汇总', dict(collections.Counter(x[0] for x in R)))
PY
```
<!-- AUDIT-SCRIPT-END -->

**输出判读**：`FAIL` 必须清零；`BASE` 当前应为空（有值说明登记了新欠账，需对照 §2.3）；`WARN` 项逐条给出人工结论并写进 §8 记录表。目标汇总：`{PASS: N, FAIL: 0, WARN: 0}`。

---

## 6. 线上与人工项（脚本无法覆盖）

| 项 | 动作 | 频次 / 入口 |
|---|---|---|
| GSC 覆盖与点击词 | `python3 tools/gsc_export.py` 导出，回填 `SEO-METRICS.md` | 每月（Playbook §7.1） |
| 结构化数据可用性 | Google Rich Results Test 抽验 1–2 个 app 页 | 每月 / 大规模改动后 |
| 性能 | PageSpeed Insights 抽验首页 + 1 篇文章 + 1 个 app 页 | 每月 |
| 外部链接有效性 | 人工打开商店链接、开发者主页；`htmlproofer` 默认 `--disable-external` 不覆盖 | 每季度 / 发布前 |
| hreflang 成环 | 线上抽查 3 组 URL 的 `<head>` 与 sitemap alternates | 大规模改动后 |
| 搜索功能 | 线上搜索页分别用中/英文关键词实际检索 | 大规模改动后 |
| IndexNow / 收录 | 确认 CI 部署后 Ping 成功、sitemap 可访问 | 发布后 |
| 真实设备 | 手机端抽查 ZH 导航、悬浮/图片排版、深色模式 | 模板或 CSS 改动后 |
| 关键词自相残杀 | 检查同词是否被两篇主吃 | 每季度（Playbook §7.2） |

---

## 7. 常见失败与修复指引

| 现象 | 常见原因 | 修复 |
|---|---|---|
| ZH 构建报文档冲突 / `/zh/` 下出现英文页 | 集合目录复用、`exclude` 写法退化为 `_posts/*` 或 `_apps` 无尾斜杠 | 回到 §2.2 分离规则；`_apps/`、`_posts/2*`、`_posts/1*` |
| hreflang 少一条 / sitemap 分裂 | 某语言缺同名文件，或 `i18n_postprocess.py` 未执行 | 补对应语言文件；重跑完整构建 |
| 关键词 MISS | 台账标「已覆盖」但词没进正文 | 织入正文/meta/alt，或把状态改回「待覆盖」 |
| `description >160` 上升 | 新写入的 description 过长 | 压缩到 ≤160，保留年份与 2–4 个目标词 |
| alt 重复 | 批量生成图用了同一 alt | 用「原描述 + 图片文件名对应视图」区分 |
| 汉字间多余空格 | 为逐词匹配硬塞分词空格 | 只删汉字间空格，改用归一化核对 |
| JSON-LD 报 `&amp;` | frontmatter 裸 `&` | 改写为 and / 顿号；确认是脚本块内命中而非正文误报 |
| htmlproofer 断链 | 文件改名、permalink 变化、锚点文字改动 | 恢复文件名或补 301（本站无重定向机制，优先恢复） |
| `_site/seo/` 出现 | `seo/` 的 `exclude` 被误删，或旧产物残留 | 恢复两份配置的 `seo/` 排除，`rm -rf _site/seo` 后完整重构建 |
| `tools/test.sh` 全绿但线上 ZH 异常 | 该脚本只构建 EN | 教研一律用 `scripts/build.sh` |

---

## 8. 教研记录表（每次必填）

```markdown
| 日期 | 改动范围 | 构建 | htmlproofer | D03 | D05 | D06 | D07 | D08 | D09 | D10 | D11 | D12 | D15 | 基线数字变化 | WARN 结论 | 结论 | 执行人 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | 简述改了哪些目录/文件、是否属 §1.1 大规模改动 | PASS/FAIL + 页数 | PASS/FAIL + 文件数/内链数 | … | … | … | … | … | … | … | … | … | … | 如 desc>160 29→29 | 逐条写明 | ✅ 可发布 / ❌ 阻塞 | … |
```

**本次基线登记（2026-11-05，建立本文档时的首次教研）**：

| 日期 | 改动范围 | 构建 | htmlproofer | 关键结果 | 基线数字 | 结论 |
|---|---|---|---|---|---|---|
| 2026-11-05 | 新建全站教研规范；此前完成 10 组 T-34、中文空格清理、alt 去重、关键词库重编号 | PASS（EN+ZH，229 页 / 2 语言） | PASS（229 文件 / 407 内链） | D03/D05/D08/D10/D11/D12 全 PASS；10 组关键词 MISS=0；汉字间空格 0；alt 重复 0；JSON-LD `&amp;` 0 | desc>160=29、H2 不一致=1、lang 缺失=1、§2.1 MISS=36 | ✅ 基线成立，欠账按 §1.4 管控 |
| 2026-11-05 | **整改教研**（§1.1 大规模改动）：29 条 description、`_pages/search.md`、Mood 裸 `&`、Meow Money 组 10 篇 EN/ZH 正文、中文教程 FAQ 合并、两份 `_config*.yml` 排除 `seo/` | PASS（完整构建 EN+ZH，228 页 / 2 语言；Pagefind 228 页 / 8704 词） | PASS（229 文件 / 407 内链） | D03/D05/D06/D07/D08/D09/D10/D11/D12/D14/D15 全 PASS；11 组关键词 MISS=0；汉字间空格 0；alt 重复 0；图片 width 1661/1661；JSON-LD `&amp;` 0 | desc>160 29→0、H2 不一致 1→0、lang 缺失 1→0、§2.1 MISS 36→0、裸 `&` 1→0、`_site/seo/` 有→无 | ✅ 欠账清零，`BASE` 置空，全部升级为硬门禁；可发布 |
| 2026-11-05 | **FAQ 呈现修复**（§1.1 大规模改动）：132 个内容文件的 FAQ 问句挂 `{:.faq-q}` 并插入空行分隔答案；`assets/css/main.css` 新增主题色与间距规则 | PASS（完整构建 EN+ZH，228 页 / 2 语言；Pagefind 228 页 / 8704 词） | PASS（229 文件 / 407 内链） | 27 PASS；产物 132 页含 `faq-q`（其中 22 页为 H3 型）、IAL 文本残留 0、CSS 规则已进 `_site`；11 组 MISS=0、汉字间空格 0、H2 一致、alt 重复 0 | 无变化（`BASE` 仍为空） | ✅ 可发布 |
| 2026-11-05 | **guide 导语间距修复**（§1.1 结构性改动）：`assets/css/main.css` 新增 `.guide__lead` 的 `margin-top` | PASS（完整构建 EN+ZH，228 页 / 2 语言；Pagefind 228 页） | PASS（229 文件 / 407 内链） | 27 PASS；产物 CSS 含 `.guide__lead`、110 页含该元素；11 组 MISS=0、H2 一致、alt 重复 0 | 无变化（`BASE` 仍为空） | ✅ 可发布 |

---

## 9. 维护本文档

以下情况必须回来更新本文档，否则教研会失真：

- 站点结构、集合目录、`exclude`、`permalink` 规则变化；
- 构建脚本、i18n 注入逻辑、CI 流程变化；
- **新增语言**（D03/D04/D05 的判定要扩展为 N 语言）；
- §2.3 任一欠账被修复或新增（同步更新 `BASE` 常量与硬门禁项）；
- 新增了自动校验脚本（把其纳入 §0 步骤，避免两套口径）；
- 教研中发现新的「反复出现但脚本没覆盖」的问题（补进 §3 维度表与 §5 脚本）。
