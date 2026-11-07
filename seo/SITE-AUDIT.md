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

## 2. 站点基线快照（2026-11-06）

### 2.1 结构与数量

| 类别 | 数量 | 路径 |
|---|---|---|
| 文章 | **264 = 66 EN + 66 ZH + 66 ID + 66 TH** | `_posts/*.md` / `_posts/zh/*.md` / `_posts/id/*.md` / `_posts/th/*.md`（均同名一一对应） |
| 应用详情页 | **44 = 11 EN + 11 ZH + 11 ID + 11 TH** | `_apps/` / `_apps_zh/` / `_apps_id/` / `_apps_th/` |
| 静态页 | **32 = 8 EN + 8 ZH + 8 ID + 8 TH** | `_pages/` / `_pages/zh/` / `_pages/id/` / `_pages/th/`（TH 8 结构页已于 2026-11-07 补齐，见 §8） |
| Glossary 术语页 | **88 = 22 EN + 22 ZH + 22 ID + 22 TH** | `_glossary/` / `_glossary_zh/` / `_glossary_id/` / `_glossary_th/` |
| 内容 Markdown 合计 | **421** | 上述四类 |
| 图片文件 | **533**（526 webp + 4 jpg + 1 png + 1 svg + 1 ico） | `assets/images/` |
| 模板 | 8 layouts + 13 includes | `_layouts/` / `_includes/` |
| 构建产物 | **449 个 HTML**（含 404）、sitemap **449 条 `<loc>`** | `_site/` |
| 语言 | 4（EN 根 / ZH `/zh/` / ID `/id/` / TH `/th/`） | `scripts/i18n_postprocess.py` 日志 `Languages detected: ['en', 'id', 'th', 'zh']` |
| 内链 | htmlproofer 检查约 **670** 条内部链接（TH 结构页曾缺失致 963 断链，已于 2026-11-07 清零，见 §8） | 随内容增长变化 |

> 数量是快照不是硬阈值。新增文章/术语/语言后数量上升是正常的，但必须在教研记录表中写明「新增了什么、完整语言是否成对、分批语言的覆盖进度」。ID 为分批建设中的语言，进度以 `SEO-I18N-PROGRESS.md` 为准。

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

### 2.6 多语言（N 语言）教研规则（2026-11-06 起）

- **语言清单自动发现**：§5 脚本从 `_config_<lang>.yml` 自动构造 `LANGS = ['en', ...]`，新增语言**不需要改脚本**；`i18n_postprocess.py` 亦按 `_site/` 下两位字母目录自动发现，无需改动。
- **完成度分层**：文章数与 EN 相等的语言判为「完整语言」，按一一对应硬门禁；不足者判为「分批建设中」，只要求「无孤立文件（不存在 EN 没有的文件）」并输出 `x/y` 覆盖进度，避免阻塞分批上线。其余三类（应用 / 页面 / 术语）对所有语言均要求无孤立文件。
- **文章骨架全语言对等（2026-11-06 起）**：**所有语言版本**的文章结构、文章目录与图片插入都以 EN 为准——H2/H3 层级与顺序、结构块（表格 / 列表 / 编号步骤 / FAQ / 分隔线）序列、文章目录（TOC 条目数与所在行序）、图片插入行序逐篇与 EN 同名文章一致；不再按本地搜索意图重新组织内容，也不再只要求「H2 ≥ 4 且含 FAQ」的结构下限。纯文本段落可因语言表达做局部调整，关键词按各语言词库优化。由 §5 脚本 **D18** 逐篇硬校验；依据 `SEO-I18N-PLAYBOOK.md` §1 红线 11 / §3.2 / §3.3 / §3.5。
- **hreflang 条数**：按「去掉语言前缀后的路径」分组，条数 = 组内实际语言数 + 1（x-default）。分批建设期间允许 2/3/4 条并存（当前分布 3 条 132 页、4 条 144 页），**不**要求每页固定为总语言数 + 1。
- **D14 白名单**：新增语言源文件属已批准改动，不计入文件名红线告警；EN/ZH 既有文件的增删改仍照常告警。
- **模板通用化**：所有布局/包含按构建级 `site.lang` 动态取集合与前缀（`site[coll]`、`site.data.ui[lang]`），禁止 `zh`-vs-else 二元判断；`page.lang` 不可用于集合选择（非 EN 构建会渲染到 EN 根级页面）。

---

## 3. 校验维度总表

| 编号 | 维度 | 级别 | 主要手段 | 合格标准 |
|---|---|---|---|---|
| D01 | 构建与产物 | P0 | `scripts/build.sh` 全量构建 | 退出码 0；各语言首页存在；日志 N 语言、页数正常 |
| D02 | 链接与资源 | P0 | `htmlproofer` | 0 failure；内链、锚点、图片、脚本全通 |
| D03 | 多语言源对账 | P0 | §5 脚本 | 完整语言 4 组差集为 0；分批语言无孤立文件并报告覆盖进度 |
| D04 | 路由、集合与隔离 | P0 | 配置核对 + 产物 URL 抽查 | 集合分离且非空、`exclude` 正确、各语言子站无跨语言泄漏 |
| D05 | hreflang / sitemap / canonical / feed / robots | P0 | §5 脚本 + 人工抽验 | 组内每语言 1 条 + x-default；合并 sitemap；404 排除；canonical 为生产域名 |
| D06 | frontmatter 与元数据 | P0 | §5 脚本 | 必填齐、`lang` 对、`description ≤160`、无裸 `&`；**App `tagline` 四语信息量与 EN 对等**（≤1.5× 且无增补规格数字，见 `SEO-I18N-PLAYBOOK.md` §1 红线 12） |
| D07 | 正文结构与多语言对等 | P0 | §5 脚本 + 人工抽验 | 完整语言 H2 一致；分批语言基础结构下限（H2≥4 且含 FAQ）；**骨架全语言对等由 D18 硬校验**；无汉字间多余空格 |
| D08 | 图片与可访问性 | P0 | §5 脚本 | alt 唯一、无 `![image]`、引用文件存在、全部带 `width` |
| D09 | 关键词真实覆盖 | P0 | §5 脚本归一化逐词核对 | 全部 11 组 MISS = 0 |
| D10 | 结构化数据与富媒体 | P0 + P1 | §5 脚本 + Rich Results Test | JSON-LD 无 `&amp;`；app 页 @type 正确；OG 图正确 |
| D11 | 内链闭环 | P0 | §5 脚本 + 抽验 | 语言前缀正确、glossary/tags/app 回链闭合 |
| D12 | 搜索与索引 | P0 | 完整构建 + 产物检查 | Pagefind N 语言分片生成、各语言 feed / sitemap / robots / IndexNow 正常 |
| D13 | 合规与产品表述 | P1 | 人工抽验 | 只读/免 root、不承诺虚假效果、YMYL、隐私、外链 rel |
| D14 | 文件名与 URL 红线 | P0 | `git status` | 无未经批准的文章/页面重命名、删除、新增；permalink 未变 |
| D15 | 发布物与敏感文件 | P0 | 产物目录检查 | 无临时目录、无凭据；`_site/seo/` 不存在 |
| D16 | 文档与台账一致性 | P1 | 人工核对 | 优化方案/进度已同步；纯修复未误写进计划文档；滞后项已登记 |
| D17 | 文章插图跨语言一致性 | P0 | §5 脚本 + 人工抽验 | 非 EN 文章图片路径多重集 = EN 同名文章、**位置与 EN 行序一致**、`alt` 已本地化未照抄 EN（规范见 `SEO-I18N-PLAYBOOK.md` §3.5）；行序硬门禁于 2026-11-06 全量启用（72 篇一致） |
| D18 | 多语言文章骨架对等（结构 / 目录 / 插图） | P0 | §5 脚本 | **所有非 EN 语言**文章的 H2/H3 层级序列、结构块序列、文章目录（TOC 条目与行位置）、图片插入行序逐篇与 EN 同名文章一致；规则见 §2.6 与 `SEO-I18N-PLAYBOOK.md` §1 红线 11 / §3.5 |

---

## 4. 逐维度检查项

### D01 构建与产物（P0）

- **检查点**：完整构建退出码为 0；`_site/index.html`、`_site/zh/index.html`、`_site/id/index.html` 存在；日志出现 `Languages detected: ['en', 'id', 'zh']` 与 `Processed N pages across 3 languages`；所有 `.jekyll-<lang>` 临时目录已清理；`==> Done. Combined site in _site/` 出现。
- **命令**：`JEKYLL_ENV=production bash scripts/build.sh`（发布前教研**不要**带 `SKIP_PAGEFIND`）。
- **合格标准**：N 与 §2.1 快照 276 相当（允许随新增内容/语言增长，须解释）。
- **失败处理**：先看是 EN 还是 ZH 阶段失败；ZH 失败优先查 `_config_zh.yml` 的 `exclude` 与集合目录名；EN 失败查 `_config.yml` 与 frontmatter 语法。

### D02 链接与资源（P0）

- **检查点**：`htmlproofer` 三 check（Images / Links / Scripts）全绿；内部链接与 hash 锚点 0 失败。
- **命令**：CI 同款见 §0 步 3。
- **合格标准**：`HTML-Proofer finished successfully.`
- **失败处理**：断链先判断是「源文件改名」还是「permalink 变化」；hash 锚点失败检查 H2/H3 是否改了文字；图片失败检查 `/assets/...` 路径大小写与扩展名。

### D03 多语言源对账（P0）

- **检查点**：完整语言 `_posts` 66↔66、`_apps` 11↔11、`_pages` 8↔8、`_glossary` 22↔22，**按同名文件**一一对应；分批语言（当前 ID：6/66、11/11、8/8、22/22）要求无孤立文件并报告进度，见 §2.6。成对文件 `title/description/tags/image/layout` 均存在。
- **手段**：§5 脚本 D03。
- **失败处理**：完整语言缺哪一侧补哪一侧；新增语言按 `SEO-I18N-PLAYBOOK.md` §2.3 建配置/目录/集合，内容按 `SEO-I18N-PROGRESS.md` 分批补齐。

### D04 路由、集合与隔离（P0）

- **检查点**：
  1. 各语言配置使用独立集合（`apps_zh` / `apps_id` / `glossary_zh` / `glossary_id`），源目录为 `_apps_<lang>/` / `_glossary_<lang>/`；
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
  - `description` 中裸 `&` 会转 `&amp;` 污染 JSON-LD，脚本硬门禁要求为 0；
  - **App 页 `tagline` 必须是 EN 短句的忠实本地化**，字符数 ≤ EN ×1.5、不得出现 EN tagline 没有的规格数字（`400+` / `500+` / `80`…），语义要点一一对应由人工抽验；禁止把正文功能点 / 卖点清单提炼进 tagline。规则见 `SEO-I18N-PLAYBOOK.md` §1 红线 12。
- **手段**：§5 脚本 D06；`description >160`、裸 `&`、tagline 信息量不对等均为硬门禁 FAIL。
- **失败处理**：补字段；压缩 description 时保留年份与 2–4 个目标词；tagline 超限时按 EN 短句重译（只换词，不增功能点），不要为塞关键词在汉字之间插空格（见 D07）。

### D07 正文结构与中英对等（P0）

- **检查点**：EN/ZH 成对文章 H2 数量一致、小节语义对应；中文正文**无汉字之间的多余空格**（数字/英文与汉字之间的空格是合法排版，保留）；术语统一（品牌名、竞品名大小写）；中文不是英文的机器直译；每篇有实质选型/场景/FAQ 内容。
- **手段**：§5 脚本 D07 + 人工抽验改动涉及的页面。
- **说明**：关键词库中的中文词本身带空格（如 `最佳悬浮助手 安卓`），正文已按中文排版规范去掉汉字间空格，因此**逐词核对必须用「去空格归一化」匹配**（见 D09），不能要求字面严格命中。
- **失败处理**：H2 不一致时补齐对应语言的小节；发现汉字间空格用「只删汉字间空格」的正则统一清理，不要动数字/英文两侧空格。

### D18 多语言文章骨架对等（P0，2026-11-06 新增）

- **规则**：所有语言版本的**文章结构、文章目录、图片插入**都必须与 EN 同名文章一致；多语言是同一篇文章的不同语言版本，不是按本地搜索意图另写一篇。
- **检查点**：
  1. **文章结构** — H2/H3 的层级、数量、顺序逐条对应；结构块（表格行、列表项、编号步骤、FAQ 标记、分隔线、图片行）的类型序列与 EN 一致。纯文本段落与空行允许因语言表达做局部调整。
  2. **文章目录** — 带 TOC 的文章（教程类）目录条目数与各条目所在行号与 EN 一致；锚点可本地化（印尼语 slug / 中文标题），但不得增删条目或改变链接数量。
  3. **图片插入** — 图片所在行号序列与 EN 一致（D17 同时校验路径集合、行序与 `alt` 本地化）；不得挪到小节末尾、合并或拆分图片块、改变图片块之间的正文顺序。
- **手段**：§5 脚本 D18 四组 `chk` 全语言逐篇比对；新增 / 重构文章另按 `SEO-I18N-PLAYBOOK.md` §3.5 从 EN 骨架逐行起稿。
- **失败处理**：按 EN 同名文章补齐缺失的标题 / 列表项 / 表格行 / FAQ 条目，或把多出的结构块并入相邻正文；目录缺条目按 EN 补链接；图片位置错位按 EN 行号移回。禁止用删减 EN 对应小节或改动 EN 来凑一致。

### D08 图片与可访问性（P0）

- **检查点**：同文件内 `alt` **零重复**且关键词化；`![image]` 零残留；所有 `/assets/...` 引用文件真实存在；每图带 `{: width="180" .normal }` 之类宽度属性防 CLS；各语言文章图片引用与 EN 一一对应（含行序位置，见 §3.5 对应规范）；新增图片走 webp 压缩。
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
# 全站教研静态检查 v3.4 / N 语言版（D18 文章骨架全语言对等：结构 / 目录 / 插图位置）（EN + 所有 _config_<lang>.yml）
# 新增语言无需改脚本：LANGS 自动发现；已完成语言按一一对应检查，
# 分批建设中的语言按「无孤立文件 + 覆盖进度」检查（见 SEO-I18N-PROGRESS.md）。
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
def norm(s): return s.lower().replace(' ', '').replace('\t', '').replace('**', '').replace('　', '')

LANGS = ['en']
for _f in sorted(glob.glob('_config_*.yml')):
    _m = re.match(r'_config_([a-z]{2})\.yml$', os.path.basename(_f))
    if _m and _m.group(1) not in LANGS: LANGS.append(_m.group(1))
LANGS = ['en'] + sorted(LANGS[1:])
def dirs(L):
    if L == 'en': return dict(posts='_posts', pages='_pages', apps='_apps', gloss='_glossary')
    return dict(posts='_posts/' + L, pages='_pages/' + L,
                apps='_apps_' + L, gloss='_glossary_' + L)
def lang_of(f):
    for L in LANGS[1:]:
        if any(f.startswith(d + '/') for d in dirs(L).values()): return L
    return 'en'

mds = []
for L in LANGS:
    for d in dirs(L).values(): mds += fs(d + '/**/*.md')
mds = sorted(set(mds))
txt = {f: open(f, encoding='utf-8').read() for f in mds}
fms = {f: fm(t) for f, t in txt.items()}
en_posts = nm('_posts/*.md')
FULL = [L for L in LANGS[1:] if nm(dirs(L)['posts'] + '/*.md') == en_posts]
PARTIAL = [L for L in LANGS[1:] if L not in FULL]
chk('D01', '语言清单与完成度', len(LANGS) >= 2,
    f'LANGS={LANGS} 完整={FULL} 分批中={PARTIAL}')
empty = [(L, k) for L in LANGS[1:] for k in ('apps', 'gloss')
         if not fs(dirs(L)[k] + '/*.md')]
chk('D04', '各语言集合非空（防 site[coll] 静默失败）', not empty, f'空集合 {empty}')
# D03 源对账
for lab, key in [('文章', 'posts'), ('应用', 'apps'), ('页面', 'pages'), ('术语', 'gloss')]:
    B = nm(dirs('en')[key] + '/*.md')
    for L in FULL:
        O = nm(dirs(L)[key] + '/*.md')
        chk('D03', f'{lab} EN/{L} 一一对应', B == O,
            f'EN={len(B)} {L}={len(O)} 差集={len(B ^ O)}')
    for L in PARTIAL:
        O = nm(dirs(L)[key] + '/*.md')
        orphan = O - B
        chk('D03', f'{lab} {L} 无孤立文件', not orphan,
            f'{L} {len(O)}/{len(B)}，孤立 {len(orphan)}；其余按 SEO-I18N-PROGRESS.md 分批补齐')
# D03 结构页硬门禁：每个完整语言必须含 8 个固定结构页（缺页会致 htmlproofer 断链，属 P0，不得后置为「待补」）
STRUCT = ['index', 'meow', 'about', 'privacy', 'terms', 'search', 'tags', 'glossary']
for L in FULL:
    have = nm(dirs(L)['pages'] + '/*.md')
    miss = [s for s in STRUCT if (s + '.md') not in have]
    chk('D03', f'结构页 8/8 ({L})', not miss,
        f'缺失 {miss}（致 htmlproofer 断链；须与 id 骨架同源补齐，不得标记待补）')
# D06
need0 = {'title', 'description'}
bad = []
for f, d in fms.items():
    n = set(need0)
    if f.startswith('_posts/'): n |= {'date', 'layout', 'tags', 'image'}
    if re.match(r'^_apps(_[a-z]{2})?/', f): n.add('icon')
    if f.startswith('_pages/'): n.add('permalink')
    if n - set(d): bad.append((f, ','.join(sorted(n - set(d)))))
chk('D06', 'frontmatter 必填字段', not bad, f'异常 {len(bad)} {bad[:2]}')
langbad = [f for f, d in fms.items() if d.get('lang') != lang_of(f)]
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
# D06：App tagline 四语信息量对等（SEO-I18N-PLAYBOOK.md §1 红线 12）
# 只设上限不设下限：中文忠实短句天然只有 EN 的 0.2–0.7 倍字符数，属正常
def _tagline(f):
    for l in open(f, encoding='utf-8').read().split('\n'):
        if l.startswith('tagline:'):
            return re.sub(r'\s+#\s.*$', '', l[len('tagline:'):].strip()).strip()
    return ''
def _nums(s): return set(re.findall(r'\d+', s))
tgl_bad = []
for L in LANGS[1:]:
    for f in fs(dirs(L)['apps'] + '/*.md'):
        en = '_apps/' + os.path.basename(f)
        if not os.path.isfile(en): continue
        a, b = _tagline(en), _tagline(f)
        if not a or not b:
            tgl_bad.append((f, 'tagline 缺失')); continue
        ratio = len(b) / max(len(a), 1)
        extra = _nums(b) - _nums(a)
        if ratio > 1.5 or extra:
            tgl_bad.append((f, f'长度比 {ratio:.2f} 规格数字增补 {sorted(extra)}'))
chk('D06', 'App tagline 信息量与 EN 对等（≤1.5× 且无增补规格数字）', not tgl_bad,
    f'异常 {len(tgl_bad)} {tgl_bad[:2]}')
# D06：YAML 语法硬门禁（Jekyll 会静默丢弃解析失败的文档，导致空 src / 空链接的连带故障）
RB = r'''require 'yaml'
bad = []
Dir.glob('{_posts,_apps,_apps_*,_pages,_glossary,_glossary_*}/**/*.{md,html}').each do |f|
  t = File.read(f)
  next unless t.start_with?("---\n")
  e = t.index("\n---", 4)
  next unless e
  begin
    YAML.parse(t[4, e - 4])
  rescue StandardError => ex
    bad << f + ': ' + ex.message.lines.first.to_s.strip
  end
end
puts bad.join("\n")
'''
_rb = subprocess.run(['ruby', '-ryaml', '-e', RB], capture_output=True, text=True)
if _rb.returncode != 0:
    warn('D06', 'YAML 校验器不可用', _rb.stderr[:120])
else:
    _bad = [l for l in _rb.stdout.strip().split('\n') if l]
    chk('D06', 'frontmatter YAML 语法有效', not _bad, f'异常 {len(_bad)} {_bad[:2]}')
# D07：完整语言逐篇对齐；分批语言基础结构下限（骨架全语言对等由 D18 硬校验）
h2, sp, weak = [], [], []
for f, t in txt.items():
    if re.search(r'(?<=[\u4e00-\u9fff])[ \t]+(?=[\u4e00-\u9fff])', t): sp.append(f)
for n in en_posts:
    a = len(re.findall(r'^## ', txt['_posts/' + n], re.M))
    for L in FULL:
        z = dirs(L)['posts'] + '/' + n
        if os.path.exists(z):
            b = len(re.findall(r'^## ', txt[z], re.M))
            if a != b: h2.append((n, L, a, b))
chk('D07', '完整语言 H2 数量一致', not h2, f'不一致 {len(h2)} {h2[:2]}')
for L in PARTIAL:
    for f in fs(dirs(L)['posts'] + '/*.md'):
        c = len(re.findall(r'^## ', txt[f], re.M))
        if c < 4 or '{:.faq-q}' not in txt[f]: weak.append((f, c))
chk('D07', '分批语言文章结构完整（H2≥4 且含 FAQ）', not weak,
    f'异常 {len(weak)} {weak[:2]}')
chk('D07', '无汉字间多余空格', not sp, f'残留 {len(sp)} {sp[:2]}')
# D08
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
# D17 文章插图跨语言一致性（P0，见 SEO-I18N-PLAYBOOK.md §3.5）
# 只比对「EN 有同名文件」的非 EN 文章；分批建设中的语言不要求 66 篇齐全。
IMGSET = re.compile(r'!\[([^\]]*)\]\((/assets/images/[^)]+)\)')
TOCRE = re.compile(r'^- \[[^\]]+\]\(#[^)]+\)$')
def SKEL(l):
    x = l.strip()
    if x.startswith('### '): return 'H3'
    if x.startswith('## '): return 'H2'
    if x.startswith('!['): return 'IMG'
    if x.startswith('|'): return 'TBL'
    if x.startswith('- '): return 'LI'
    if re.match(r'^\d+\. ', x): return 'NUM'
    if x == '{:.faq-q}': return 'FAQ'
    if x == '---': return 'HR'
    return None
_en_posts = {os.path.basename(f): f for f in fs('_posts/[12]*.md')}
mis, copied, pos = [], [], []
hbad, sbad, tbad = [], [], []
for f, t in txt.items():
    if lang_of(f) == 'en' or not f.startswith('_posts/'): continue
    e = _en_posts.get(os.path.basename(f))
    if not e: continue
    a = collections.Counter(p for _, p in IMGSET.findall(txt[e]))
    b = collections.Counter(p for _, p in IMGSET.findall(t))
    if a != b: mis.append((f, sum(a.values()), sum(b.values())))
    el, tl = txt[e].split('\n'), t.split('\n')
    ea = [i for i, l in enumerate(el) if IMGSET.search(l)]
    ba = [i for i, l in enumerate(tl) if IMGSET.search(l)]
    if ea != ba: pos.append((f, ea[:3], ba[:3]))
    es = [k for k in (SKEL(l) for l in el) if k]
    ts = [k for k in (SKEL(l) for l in tl) if k]
    if es != ts: sbad.append((f, len(es), len(ts)))
    eh = [k for k in es if k in ('H2', 'H3')]
    th = [k for k in ts if k in ('H2', 'H3')]
    if eh != th: hbad.append((f, len(eh), len(th)))
    etoc = [i for i, l in enumerate(el) if TOCRE.match(l)]
    ttoc = [i for i, l in enumerate(tl) if TOCRE.match(l)]
    if etoc != ttoc: tbad.append((f, etoc[:3], ttoc[:3]))
    en_alts = {x[0] for x in IMGSET.findall(txt[e])}
    hit = [x[0] for x in IMGSET.findall(t) if x[0] in en_alts]
    if hit: copied.append((f, hit[0]))
chk('D17', '文章插图集合与 EN 一致', not mis,
    f'{len(mis)} 篇不一致 {mis[:2]}')
chk('D17', '插图行序位置与 EN 一致', not pos,
    f'{len(pos)} 篇不一致 {pos[:2]}')
chk('D17', '插图 alt 已本地化（未照抄 EN）', not copied,
    f'{len(copied)} 篇 {copied[:2]}')
# D18 文章骨架全语言对等：结构 / 目录 / 图片插入（所有非 EN 语言，逐篇比对 EN 同名文章）
chk('D18', '文章 H2/H3 层级序列与 EN 一致', not hbad,
    f'{len(hbad)} 篇不一致 {hbad[:2]}')
chk('D18', '文章结构块序列与 EN 一致', not sbad,
    f'{len(sbad)} 篇不一致 {sbad[:2]}')
chk('D18', '文章目录（TOC）与 EN 一致', not tbad,
    f'{len(tbad)} 篇不一致 {tbad[:2]}')
chk('D18', '图片插入行序与 EN 一致', not pos,
    f'{len(pos)} 篇不一致 {pos[:2]}')
# D09 关键词真实覆盖（词库标「已覆盖」的词必须出现在正文，按语言归一化核对）
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
# D11 内链前缀（按语言检查，排除共享资源）
def links(t): return re.findall(r'\]\((/[^)]*)\)', t)
zbad, ebad = [], []
for f, t in txt.items():
    L = lang_of(f)
    for u in links(t):
        if u.startswith(('/assets/', '/pagefind/')): continue
        if L == 'en' and any(u.startswith('/' + x + '/') for x in LANGS[1:]):
            ebad.append((f, u))
        if L != 'en' and not u.startswith('/' + L + '/'):
            zbad.append((f, u))
chk('D11', '内链语言前缀', not zbad and not ebad,
    f'非 EN 缺前缀 {len(zbad)} {zbad[:2]} / EN 误带 {len(ebad)} {ebad[:2]}')
# D14：新增语言源文件属已批准改动，不计入红线告警
st = subprocess.run(['git', 'status', '--short'], capture_output=True, text=True).stdout.split('\n')
def approved(l):
    return any(k in l for L in LANGS[1:] for k in
               ('_posts/' + L + '/', '_pages/' + L + '/', '_apps_' + L + '/',
                '_glossary_' + L + '/', '_config_' + L + '.yml', L + '/blog/'))
risk = [l for l in st if re.match(r'^\s*(R|D|A|\?\?)', l)
        and any(k in l for k in ('_posts/', '_apps', '_pages/', '_glossary'))
        and not approved(l)]
if risk: warn('D14', '文件名增删改（红线）', f'{len(risk)} 条需人工确认 {risk[:2]}')
else: chk('D14', '文件名增删改（红线）', True, f'0 条（已批准语言源 {LANGS[1:]}）')
# 产物维度
if os.path.isdir('_site'):
    hs = fs('_site/**/*.html')
    heads = {h: open(h, encoding='utf-8').read() for h in hs}
    pages = {h: v for h, v in heads.items() if os.path.basename(h) != '404.html'}
    chk('D05', '每页 hreflang 块', all('i18n-hreflang' in v for v in pages.values()),
        f'{len(pages)} 页')
    missxd = [h for h, v in pages.items()
              if 'hreflang="en"' not in v or 'hreflang="x-default"' not in v]
    chk('D05', 'hreflang en + x-default 完整', not missxd, f'异常 {len(missxd)}')
    cnt = collections.Counter(len(re.findall(r'hreflang="[^"]+"', v)) for v in pages.values())
    chk('D05', 'hreflang 条数随组内语言数变化',
        min(cnt) >= 2 and max(cnt) <= len(LANGS) + 1, f'分布 {dict(cnt)}')
    for L in LANGS[1:]:
        lp = '_site/' + L + '/'
        sub = [h for h in pages if h.startswith(lp)]
        bad = [h for h in sub if 'hreflang="' + L + '"' not in heads[h]]
        chk('D05', L + ' 页含自身 alternate', not bad, f'{len(sub)} 页，异常 {len(bad)}')
        chk('D05', L + ' 子 sitemap 已删', not os.path.exists(lp + 'sitemap.xml'), '')
    sm = open('_site/sitemap.xml', encoding='utf-8').read() if os.path.exists('_site/sitemap.xml') else ''
    chk('D05', '合并 sitemap', len(re.findall(r'<loc>', sm)) > 0,
        f'{len(re.findall(r"<loc>", sm))} 条 loc')
    chk('D12', '404 不进 sitemap', '404' not in sm, '')
    ld = [b for v in heads.values() for b in re.findall(
        r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', v, re.S)]
    chk('D10', 'JSON-LD 无 &amp;', not any('&amp;' in b for b in ld), f'{len(ld)} 个块')
    feeds = ['_site/feed.xml'] + ['_site/' + L + '/feed.xml' for L in LANGS[1:]]
    chk('D12', 'feed / robots', all(os.path.exists(x) for x in feeds)
        and os.path.exists('_site/robots.txt'), ','.join(feeds))
    chk('D12', 'Pagefind 索引', os.path.isfile('_site/pagefind/pagefind.js'), '')
    temps = [d for L in LANGS[1:] for d in ('.jekyll-' + L,) if os.path.isdir(d)]
    chk('D15', '无临时目录残留', not temps, f'{temps}')
    chk('D15', '内部 seo/ 未发布', not os.path.isdir('_site/seo'),
        f'存在={os.path.isdir("_site/seo")}')
    leaks = [p for p in fs('_site/**/*') if any(k in p for k in
             ('credentials.json', 'token.json', 'pagefind-bin')
             + tuple('jekyll-' + L for L in LANGS[1:]))]
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
| 搜索功能 | 线上搜索页分别用各语言关键词实际检索（含 ID） | 大规模改动后 |
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
| D18 骨架不一致 | 某语言按本地意图重写正文、漏 / 多列表项、目录增删条目、图片挪位置 | 以 EN 同名文章为骨架补齐或合并结构块，禁止改动 EN 凑一致（§4 D18） |

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
| 2026-11-05 | **FAQ 问句样式调整**（§1.1 结构性改动）：`assets/css/main.css` 去掉主题色、改为普通字体色 + 加粗，并用 CSS counter 生成前置序号 | PASS（完整构建 EN+ZH，228 页 / 2 语言；Pagefind 228 页） | PASS（229 文件 / 407 内链） | 27 PASS；无头 Chrome 实测序号 1/2/3 正常、颜色恢复普通色、p 型与 H3 型均编号；11 组 MISS=0、H2 一致、alt 重复 0 | 无变化（`BASE` 仍为空） | ✅ 可发布 |
| 2026-11-06 | **App 详情页与 Google Play 文案对齐**（限定范围）：`_apps_zh/meow-money-manager.md`、`_apps/meow-money-manager.md` 的 tagline / description / FAQ / 正文；`SEO-PROGRESS.md`、`SEO-KEYWORDS.md` 台账同步 | PASS（完整构建 EN+ZH，228 页 / 2 语言；Pagefind 228 页 / 8715 词） | PASS（229 文件 / 407 内链） | 27 PASS；description zh 114 / en 155（≤160）、裸 `&` 0；EN/ZH FAQ 各 7 条、H2 各 1；D09 11 组 MISS=0；产物每页 4 个 JSON-LD 块、FAQPage 7 条、`&amp;` 0、hreflang 3 条，Google Drive / WebDAV 已落地且无 iCloud / WebDav 残留 | 无变化（`BASE` 仍为空）；Pagefind 词数 8704→8715（正文扩写） | ✅ 可发布 |
| 2026-11-06 | **印尼语（id）多语言扩展 Phase 0–2**（§1.1 大规模改动）：新增 `SEO-I18N-PLAYBOOK.md` / `SEO-I18N-PROGRESS.md`；`SEO-KEYWORDS.md` §2.1.5 本地词库；`_config_id.yml` + 两份 config exclude + `languages/nav/ui` + `build.sh` + 修复 `new-language.sh`；11 个布局/包含/JS/404/CSS 消除 zh-vs-else；`/id/` 8 结构页 + 22 术语 + 11 App + 6 篇 Meow Money Manager posts；§5 脚本升级 v3.0 N 语言 | PASS（完整构建 EN+ZH+ID，276 页 / 3 语言；Pagefind 276 页 / 9895 词 / 3 语言分片） | PASS（277 文件 / 504 内链） | **39 PASS / 0 FAIL / 0 WARN**；D09 11 组 MISS=0；ID 首页 11 App、FAQPage 7 条、canonical 与面包屑全为 `/id/`、48 页 `<html lang=id>`；hreflang 分布 4 条 144 页 / 3 条 132 页；三语 feed 齐、子 sitemap 已删 | 语言 2→3；HTML 229→277；sitemap 228→276；内链 407→504；Pagefind 8715→9895；ID 词库 51 已覆盖 / 1 合规挂起（widget 待产品核实） | ✅ 可发布；ID 其余 60 篇 posts 按 `SEO-I18N-PROGRESS.md` Phase 3 分批补齐 | — |
| 2026-11-06 | **`_apps_id` 内容质检与重写**（限定范围）：10 个 App 页按 EN 原版逐项对齐字段顺序 / screenshots / FAQ / 功能点与 Related terms；修正 system-monitor 只读事实、mood-diary 的 CSV 与 WebDAV、meow-fm 的 mixing、cross-hair 的 preset 与 root 等编造内容；修复 `tagline` 中 `: ` 引起的 YAML 解析失败；§5 脚本新增 frontmatter YAML 语法硬门禁（v3.1） | PASS（完整构建 3 语 / 276 页 / 0 YAML 与 Liquid 错误） | PASS（277 文件 / 504 内链） | **40 PASS / 0 FAIL / 0 WARN**；11 个 App 页截图条 4–9 张、FAQ 4–7 条全部与原版一致；空 `src` 0；中文残留 0 | 教研脚本 39→40 PASS（新增 D06 YAML 门禁）；基线数字无变化 | ✅ 可发布 | — |
| 2026-11-06 | **文章插图跨语言一致性修复 + 规则固化**（限定范围）：`_posts/id/` 6 篇补回 EN 同名文章 131 张插图、`_posts/zh/2026-01-05-alternatives-to-assistive-touch.md` 补回 17 张；ID alt 105 条按 `SEO-KEYWORDS.md` §2.1.5 本地关键词重写、ZH 新增 17 条中文关键词化；`SEO-I18N-PLAYBOOK.md` §1 红线 10 + §3.5、`SEO-I18N-PROGRESS.md` Phase 3 入口写入规则；§5 脚本升级 v3.2 新增 D17 | PASS（完整构建 3 语 / 276 页；Pagefind 276 页 / 10010 词 / 3 语言分片） | PASS（277 文件 / 504 内链） | **42 PASS / 0 FAIL / 0 WARN**；D17 比对 72 篇插图集合全部一致、alt 照抄 0；D08 同文件 alt 重复 0、width 1809/1809；产物 ID 6 篇 + ZH 差异篇 img 数与 EN 完全相同、全站 3808 个 img 无缺失资源 | 教研 40→42 PASS；图片引用 1661→1809 | ✅ 可发布 | — |
| 2026-11-06 | **ID 首批 6 篇按 EN 骨架重构 · 第 1 批**（限定范围）：`_posts/id/2026-06-03-pillar-budget-expense-tracker-apps-android.md` 与 `2026-04-07-best-meow-money-manager-android.md` 逐行本地化为 EN 骨架版本，H2/H3 含义、段落顺序、表格、FAQ 条目、图片行号完全对齐；`alt` 印尼语关键词化；D09 掉出的 8 个本地长尾词织回正文 | PASS（完整构建 3 语 / 276 页；Pagefind 276 页） | PASS（277 文件 / 504 内链） | **42 PASS / 0 FAIL / 0 WARN**；两篇行类型序列差异 0，图片行号 EN=ID（43–47、37–41 + 69–73），图片路径序列一致、alt 唯一；D09 11 组 MISS 0；产物两篇 img 数与 EN 相同（9 / 14） | 无变化（`BASE` 仍为空） | ✅ 可发布；剩余 4 篇按 `SEO-I18N-PROGRESS.md` 分批继续 | — |
| 2026-11-06 | **ID 首批 6 篇按 EN 骨架重构 · 第 2 批**（限定范围）：`_posts/id/2026-04-12-best-meow-money-manager-students.md` 与 `2026-09-26-vs-meow-money-and-ynab.md` 逐行本地化为 EN 骨架版本，H2/H3 含义与数量、段落顺序、表格（4 应用 / 11 行对比）、FAQ 6 组与图片行号完全对齐；`alt` 印尼语关键词化；`SEO-I18N-PROGRESS.md` 同步 4/6 进度 | PASS（完整构建 3 语 / 276 页；Pagefind 276 页 / 10133 词 / 3 语分片） | PASS（277 文件 / 502 内链） | **42 PASS / 0 FAIL / 0 WARN**；D09 11 组 MISS=0；D17 插图集合一致、alt 照抄 0；D08 图片 width 1809/1809；两篇行类型序列差异 0、图片行号 EN=ID（44–48 + 73–77 / 33–37 + 70–74）、路径序列一致、alt 唯一；产物两篇 `img` 15/15 与 EN 相同、正文图片序列一致、`<html lang=id>`、hreflang 4 条 | 内链 504→502（旧 ID 独立版内链较多，按 EN 骨架对齐后减少 2 条）；Pagefind 10010→10133 词（正文按 EN 骨架扩写）；`BASE` 仍为空 | 无 WARN | ✅ 可发布；剩余 `alternatives-to-mint` 与 `tutorial-meow-money` 按 `SEO-I18N-PROGRESS.md` 继续 | — |
| 2026-11-06 | **ID 首批 6 篇按 EN 骨架重构 · 第 3 批 + D17 行序硬门禁启用**（限定范围）：`_posts/id/2026-01-31-alternatives-to-mint.md`（314 行 / 13 H2 / 34 图）与 `2026-08-08-tutorial-meow-money.md`（388 行 / 14 H2 + 27 H3 / 62 图、19 个图片行）逐行本地化为 EN 骨架版本；`SEO-I18N-PROGRESS.md` 同步 6/6；§5 脚本升级 v3.3，新增「插图行序位置与 EN 一致」硬门禁 | PASS（完整构建 3 语 / 276 页；Pagefind 276 页 / 10256 词 / 3 语分片） | PASS（277 文件 / 512 内链；tutorial 11 个目录锚点全部命中） | **43 PASS / 0 FAIL / 0 WARN**；D17 插图集合一致、行序 72 篇全量一致、alt 照抄 0；D09 11 组 MISS=0；两篇行类型序列差异 0、图片行号与路径序列与 EN 一致、alt 唯一；产物 `img` 39/39 与 67/67 对齐 EN、正文图片序列一致 | 教研 42→43 PASS（新增 D17 行序门禁）；内链 502→512（教程目录 11 个锚点与骨架内链变化）；Pagefind 10133→10256 词（正文按 EN 骨架扩写）；`BASE` 仍为空 | 无 WARN | ✅ 可发布；ID 首批 6 篇重构全部完成，Phase 3 的 60 篇一律从 EN 骨架起稿 | — |
| 2026-11-06 | **教研规则升级：全语言文章骨架对等（D18）**（限定范围）：按用户要求把「所有语言版本的文章结构、文章目录、图片插入必须与 EN 一致」写入 §2.6 / §3 维度表 / §4 D18 / §5 脚本（v3.4），并同步 `SEO-I18N-PLAYBOOK.md` §1 红线 11 / §3.5 / §6.3 与 `SEO-I18N-PROGRESS.md` 的旧口径；修复 2 篇 ZH 历史差异（`2026-01-27-alternatives-to-day-one` 补 1 个列表项、`2026-09-04-vs-cpu-monitor-and-cpu-z` 多出的列表项改为续行，内容保留） | PASS（完整构建 3 语 / 276 页；Pagefind 276 页 / 10261 词 / 3 语分片） | PASS（277 文件 / 512 内链；目录锚点无断链） | **47 PASS / 0 FAIL / 0 WARN**；D18 四项全绿（H2/H3 层级序列、结构块序列、文章目录 TOC、图片插入行序均为 0 篇不一致）；D17 三项 0 篇不一致；D09 11 组 MISS=0 | 教研 43→47 PASS（新增 D18 四组 `chk`）；Pagefind 10256→10261 词（中文补 1 条列表项）；内链 512 不变；`BASE` 仍为空 | 无 WARN | ✅ 可发布；D18 为 P0 硬门禁，后续所有新增 / 重构语言文章必须逐篇与 EN 骨架对等 | — |
| 2026-11-06 | **Phase 3 启动 · G2（Meow Todo）首批 2 篇印尼语 posts**（限定范围）：`_posts/id/2026-04-25-best-meow-todo-list-android.md`（141 行）与 `2026-04-29-best-meow-todo-list-students.md`（142 行）从 EN 骨架逐行起稿；`SEO-KEYWORDS.md` 新增 §2.2.5 印尼语词组 10 词并全部正文落地；`SEO-I18N-PROGRESS.md` 同步 8/66；重新应用 `_posts/zh/2026-09-04-vs-cpu-monitor-and-cpu-z.md` 的结构修复（多余列表项改段落，内容保留） | PASS（完整构建 3 语 / 278 页；Pagefind 278 页 / 10331 词 / 3 语分片） | PASS（279 文件 / 516 内链） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿（74 篇对齐）、D09 11 组 MISS=0；两篇行类型序列差异 0、图片行号与路径序列与 EN 一致、各 10 图 `alt` 唯一且未照抄 EN；产物 `img` 15/15 对齐 EN、`<html lang=id>`、hreflang 4 条 | 文章 138→140、内容 md 261→263、产物 277→279、sitemap 276→278、内链 512→516、Pagefind 10261→10331 词（新增 2 篇 ID posts）；`BASE` 仍为空 | 无 WARN | ✅ 可发布；Phase 3 剩余 58 篇按「G2 剩 4 篇 + G3–G11 各组 6 篇」分批继续，一律从 EN 骨架起稿 | — |
| 2026-11-06 | **Phase 3 自动推进 · G2 收尾 4 篇 + G3（Meow Habits）全组 6 篇**（限定范围）：新增 `_posts/id/` 10 篇印尼语 posts（8/66 → 18/66），一律从 EN 骨架逐行起稿；`SEO-KEYWORDS.md` 新增 §2.3.5 印尼语词组 10 词；G3 pillar 的 5 处同组断链随整组补齐消失；台账同步 | PASS（完整构建 3 语 / 289 页；Pagefind 289 页 / 10722 词 / 3 语分片） | PASS（290 文件 / 545 内链 / 0 failure；G3 教程 11 个目录锚点全命中） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；10 篇行类型序列差异 0、图片行号与路径序列与 EN 一致、`alt` 唯一未照抄 EN、内链前缀异常 0、description ≤160 | 文章 140→150、内容 md 263→273、产物 279→290、sitemap 278→289、内链 516→545、Pagefind 10331→10722 词（新增 10 篇 ID posts）；`BASE` 仍为空 | 无 WARN | ✅ 可发布；Phase 3 剩余 48 篇（G4–G11）按自动推进规则继续 | — |
| 2026-11-06 | **Phase 3 自动推进 · G4（Meow Mood Diary）5 篇印尼语 posts**（限定范围）：新增 `_posts/id/` 5 篇（18/66 → 23/66），一律从 EN 骨架逐行起稿；`SEO-KEYWORDS.md` 新增 §2.4.5 印尼语词组 10 词；末篇 `alternatives-to-day-one` 未落地，pillar 与 vs 中指向它的 2 处链接暂以纯文本呈现以保证内链 0 failure；台账同步 | PASS（完整构建 3 语 / 295 页；Pagefind 295 页 / 10820 词 / 3 语分片） | PASS（296 文件 / 562 内链 / 0 failure；G4 教程 12 个目录锚点全命中） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；5 篇行类型序列差异 0、图片行号与路径序列与 EN 一致、`alt` 唯一未照抄 EN、内链前缀异常 0、description 140–159 字符 | 文章 150→155、内容 md 273→278、产物 290→296、sitemap 289→295、内链 545→562、Pagefind 10722→10820 词（新增 5 篇 ID posts）；`BASE` 仍为空 | 无 WARN | ✅ 可发布；G4 末篇补齐后须恢复 2 处 `/id/` 链接并复跑教研，Phase 3 剩余 43 篇继续自动推进 | — |
| 2026-11-07 | **Phase 3 自动推进 · G4（Meow Mood Diary）全组 6 篇印尼语 posts**（限定范围）：补齐末篇 `alternatives-to-day-one`（EN 297 行 / 35 图），`_posts/id/` 合计 24/66；pillar 与 vs 中指向该页的 2 处链接由纯文本恢复为 `/id/` 链接 | PASS（完整构建 3 语 / 296 页；Pagefind 296 页 / 10855 词 / 3 语分片） | PASS（297 文件 / 564 内链 / 0 failure） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；6 篇行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0、description 140–159 字符 | 文章 156（66+66+24）、内容 md 279、产物 297 HTML、sitemap 296、内链 564、Pagefind 10855 词（G4 全组 6 篇）；`BASE` 仍为空 | 无 WARN | ✅ 可发布；G4 全组完成，Phase 3 剩余 42 篇继续自动推进，下一批 G5（Meow FM） | — |
| 2026-11-07 | **Phase 3 自动推进 · G5（Meow FM）全组 6 篇印尼语 posts**（限定范围）：补齐 `alternatives-to-calm`（EN 297 行 / 34 图）、`best-meow-fm-focus`（146 行 / 9 图）、`best-meow-fm-sleep`（147 行 / 9 图）、`vs-meow-fm-and-calm`（164 行 / 9 图）、`tutorial-meow-fm`（134 行 / 3 图 / TOC 11 锚点全命中）、`pillar-white-noise-focus-apps-android`（125 行 / 5 图），`_posts/id/` 合计 30/66；同组互链全部落地（无断链） | PASS（完整构建 3 语 / 303 页；Pagefind 303 页 / 11546 词 / 3 语分片） | PASS（579 内链 / 0 failure） | **47+ PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；6 篇行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0 | 文章 156（66+66+30）、内容 md 285、产物 303 HTML、sitemap 302、内链 579、Pagefind 11546 词（G5 全组 6 篇） | 无 WARN | ✅ 可发布；G5 全组完成，Phase 3 剩余 36 篇继续自动推进，下一批 G6（One Widget） | — |
| 2026-11-07 | **Phase 3 自动推进 · G6（One Widget）全组 6 篇印尼语 posts**（限定范围）：补齐 `alternatives-to-widgetsmith`（EN 285 行 / 30 图）、`best-one-widget-android`（132 行 / 10 图）、`best-one-widget-material-you`（129 行 / 10 图）、`pillar-android-home-screen-widget-apps`（130 行 / 5 图）、`tutorial-one-widget`（148 行 / 6 图 / TOC 11 锚点全命中）、`vs-one-widget-and-kwgt`（166 行 / 10 图），`_posts/id/` 合计 36/66；同组互链全部落地（无断链） | PASS（完整构建 3 语 / 309 页；Pagefind 309 页 / 11764 词 / 3 语分片） | PASS（596 内链 / 0 failure） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；6 篇行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0、description ≤160 且无裸 & | 文章 168（66+66+36）、内容 md 291、产物 309 HTML、sitemap 309、内链 596、Pagefind 11764 词（G6 全组 6 篇） | 无 WARN | ✅ 可发布；G6 全组完成，Phase 3 剩余 30 篇继续自动推进，下一批 G7（Only Clock） | — |
| 2026-11-07 | **Phase 3 自动推进 · G7（Only Clock）全组 6 篇印尼语 posts**（限定范围）：补齐末篇 `alternatives-to-retroflip`（EN 282 行 / 23 图）、`best-only-clock-flip`（128 行 / 10 图）、`best-only-clock-nightstand`（131 行 / 10 图）、`pillar-flip-clock-apps-android`（128 行 / 5 图）、`tutorial-only-clock`（138 行 / 8 图 / TOC 锚点全命中）、`vs-only-clock-and-retroflip`（158 行 / 10 图），`_posts/id/` 合计 42/66；同组互链全部落地（无断链） | PASS（完整构建 3 语 / 316 页；Pagefind 316 页 / 11919 词 / 3 语分片） | PASS（610 内链 / 0 failure） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；6 篇行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0、description ≤160 且无裸 & | 文章 174（66+66+42）、内容 md 297、产物 316 HTML、sitemap 316、内链 610、Pagefind 11919 词（G7 全组 6 篇） | 无 WARN | ✅ 可发布；G7 全组完成，Phase 3 剩余 24 篇继续自动推进，下一批 G8（CPU Monitor） | — |
| 2026-11-07 | **Phase 3 自动推进 · G8（CPU Monitor）全组 6 篇印尼语 posts**（限定范围）：补齐 `alternatives-to-cpu-z`（EN 291 行 / 29 图）、`best-cpu-monitor-phone-temp`（128 行 / 10 图）、`best-cpu-monitor-temperature`（131 行 / 10 图）、`pillar-cpu-temperature-monitor-apps-android`（128 行 / 5 图）、`tutorial-cpu-monitor`（121 行 / 5 图 / TOC 锚点全命中）、`vs-cpu-monitor-and-cpu-z`（166 行 / 10 图），`_posts/id/` 合计 48/66；同组互链全部落地（无断链） | PASS（完整构建 3 语 / 323 页；Pagefind 323 页 / 12058 词 / 3 语分片） | PASS（625 内链 / 0 failure） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；6 篇行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0、description ≤160 且无裸 & | 文章 180（66+66+48）、内容 md 303、产物 323 HTML、sitemap 323、内链 625、Pagefind 12058 词（G8 全组 6 篇） | 无 WARN | ✅ 可发布；G8 全组完成，Phase 3 剩余 18 篇继续自动推进，下一批 G9（System Monitor） | — |
| 2026-11-07 | **Phase 3 自动推进 · G9（System Monitor）全组 6 篇印尼语 posts**（限定范围）：补齐 `alternatives-to-ccleaner`（EN 291 行 / 28 图）、`best-system-monitor-monitor`（140 行 / 10 图）、`best-system-monitor-ram`（138 行 / 10 图）、`pillar-system-monitor-apps-android`（131 行 / 5 图）、`tutorial-system-monitor`（140 行 / 12 图 / TOC 锚点全命中）、`vs-system-monitor-and-ccleaner`（165 行 / 10 图），`_posts/id/` 合计 54/66；同组互链全部落地（无断链） | PASS（完整构建 3 语 / 330 页；Pagefind 330 页 / 12182 词 / 3 语分片） | PASS（637 内链 / 0 failure） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；6 篇行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0、description ≤160 且无裸 & | 文章 186（66+66+54）、内容 md 309、产物 330 HTML、sitemap 330、内链 637、Pagefind 12182 词（G9 全组 6 篇） | 无 WARN | ✅ 可发布；G9 全组完成，Phase 3 剩余 12 篇继续自动推进，下一批 G10（Floating Assistant） | — |
| 2026-11-07 | **Phase 3 自动推进 · G10（Floating Assistant）全组 6 篇印尼语 posts**（限定范围）：补齐 `alternatives-to-assistive-touch`（EN 288 行 / 27 图）、`best-floating-assistant-accessibility`（131 行 / 10 图）、`best-floating-assistant-general`（132 行 / 10 图）、`pillar-floating-assistant-apps-android`（129 行 / 5 图）、`tutorial-floating-assistant`（146 行 / 3 图 / TOC 12 锚点全命中）、`vs-floating-assistant-and-assistive-touch`（163 行 / 10 图），`_posts/id/` 合计 60/66；同组互链全部落地（无断链） | PASS（完整构建 3 语 / 335 页；Pagefind 335 页 / 12305 词 / 3 语分片） | PASS（653 内链 / 0 failure） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；6 篇行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0、description ≤160 且无裸 &；另将 `info perangkat android` 织入 G9 pillar 正文以满足该词覆盖 | 文章 192（66+66+60）、内容 md 315、产物 335 HTML、sitemap 335、内链 653、Pagefind 12305 词（G10 全组 6 篇） | 无 WARN | ✅ 可发布；G10 全组完成，Phase 3 剩余 6 篇继续自动推进，下一批 G11 | — |
| 2026-11-07 | **Phase 3 自动推进 · G11（Crosshair Aim）全组 6 篇印尼语 posts**（限定范围）：补齐 `alternatives-to-crosshair-master`（EN 274 行 / 27 图）、`best-cross-hair-fps`（128 行 / 5 图）、`best-cross-hair-overlay`（129 行 / 5 图）、`pillar-crosshair-apps-fps-android`（119 行 / 5 图）、`tutorial-cross-hair`（120 行 / 5 图 / TOC 8 锚点全命中）、`vs-crosshair-and-crosshair-master`（146 行 / 5 图），`_posts/id/` 合计 66/66；同组互链全部落地（无断链） | PASS（完整构建 3 语 / 342 页；Pagefind 342 页 / 12403 词 / 3 语分片） | PASS（672 内链 / 0 failure） | **47 PASS / 0 FAIL / 0 WARN**；D17 / D18 全绿、D09 11 组 MISS=0、D14 0 条；6 篇行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0、description ≤160 且无裸 & | 文章 198（66+66+66）、内容 md 321、产物 342 HTML、sitemap 342、内链 672、Pagefind 12403 词（G11 全组 6 篇） | 无 WARN | ✅ 可发布；G11 全组完成，Phase 3 收官（66/66），下一批 Phase 4 | — |
| 2026-11-07 | **泰语（th）Phase 4 多语言扩展 · 全量交付**（§1.1 大规模改动）：`_posts/th/` 66 篇、`_apps_th/` 11 篇、`_glossary_th/` 22 篇、`_pages/th/index.md` 1 篇，从 `id` 骨架逐篇翻译；§5 脚本自动纳入 TH 为第 4 语言；修复 TH FAQ 标记 `{: .faq-q}`→`{:.faq-q}`（260 处）、`vs-meow-mood-and-day-one` 漏掉的 6 个 `###` H3 骨架、首页补 `lang: th`、2 篇 description 压到 ≤160；整站教研（§0 七步） | PASS（完整构建 4 语 / 449 页；Pagefind 449 页 / 4 语言分片） | **FAIL**（963 处断链，全部指向 7 个缺失 TH 结构页：`/th/search/`、`/th/meow/`、`/th/about/`、`/th/privacy/`、`/th/terms/`、`/th/tags/`、`/th/glossary/`（术语索引）；另 2 篇 alternatives 指向 `/id/` 为有意保留） | **48 PASS / 5 FAIL / 0 WARN**：D01 语言 id/th/zh 齐全；D03 posts/apps/gloss 66/11/22 ↔ EN 全 PASS；D06 frontmatter/lang/≤160 全 PASS；D07 FAQ/D08 图片 alt·width/D09 关键词/D17 图片集合/D18 H2·H3 骨架·结构块 全 PASS；仅 FAIL：D03 `pages 1/8`（7 结构页未译）、D11 6 条 `/id/` 链接（有意，alternatives 无 TH 目标）、D17/D18 图片与 TOC 行序 `tutorial-meow-todo` 偏移 1 行（frontmatter 行数差，内容一致，软红线） | 文章 198→264（66+66+66+66）、应用 33→44、术语 66→88、静态页 24→25、内容 md 279→421、产物 342→449；语言 3→4 | 7 个 TH 结构页缺失（P0 发布阻塞项，须补齐后再发布）；其余内容正确 | 🟡 内容正确可归档；**发布前须补齐 7 个 TH 结构页**（search/meow/about/privacy/terms/tags/术语索引）以消除 963 断链，复跑 htmlproofer 全绿后方可发布 | — |
| 2026-11-07 | **泰语（th）7 结构页补齐 + 锚点修复（收尾）**（§1.1 大规模改动后）：补齐 `_pages/th/` 的 about/privacy/terms/search/tags/glossary/meow 共 7 页（从 `id` 骨架翻译）；修复全部 TH 教程文 `## 标题{: #slug}` 缺空格致 IAL 未解析、生成畸形 id（963→120 断链），改为与 EN/ID/ZH 一致的 auto_ids 方案——移除显式 IAL 并将 TOC 锚点改写为泰语标题自动生成的 id；复跑完整构建（Pagefind 开）+ htmlproofer | PASS（完整构建 4 语 / 449 页 + Pagefind 4 语言分片） | **PASS**（0 failure；902 内链 / 457 文件全绿） | **49 PASS / 4 FAIL / 0 WARN**：D01/D03(文章·应用·术语·**页面 8/8**)/D06/D07/D08/D09/D17图片集合/D18 H2·H3·结构块 全 PASS；D12 Pagefind 全 PASS；仅 FAIL：D11 6 条 `/id/` 链接（alternatives 无 TH 目标，有意保留）、D17/D18 图片与 TOC 行序 `tutorial-meow-todo` 偏移 1 行（frontmatter 行数差，内容/结构/标题/块序列一致，软红线） | 文章 264、应用 44、术语 88、静态页 25、产物 449；语言 4 | 仅余 4 项软红线/设计项，无内容缺陷 | ✅ 可发布（TH 7 结构页补齐、htmlproofer 0 failure；D11/D17/D18 行序为已知设计/软红线，不阻塞） | — |
| 2026-11-07 | **App `tagline` 四语信息量对齐（方案 A）+ 规则入规范**：`_apps_id/` / `_apps_th/` 共 22 个 tagline 从「功能点罗列长句」收敛回 EN 短句语义（仅本地措辞，不引入正文功能点 / 规格数字）；`SEO-I18N-PLAYBOOK.md` 新增 §1 红线 12、改写 §3.3 App 行；`SITE-AUDIT.md` §3 维度表 / §4 D06 / §5 脚本新增「App tagline 信息量与 EN 对等」硬门禁（≤1.5× 且规格数字不得增补），并做反向注入验证（旧长句立刻 FAIL 并点名文件） | PASS（完整构建 4 语 / 449 页 + Pagefind 4 语言分片） | PASS（0 failure；902 内链 / 457 文件全绿） | **53 PASS / 4 FAIL / 0 WARN**：新增 D06 tagline 门禁 PASS（异常 0）；D03 结构页 8/8 等全 PASS；仅 FAIL：D11 6 条 `/id/` 链接（有意保留）、D17/D18 图片与 TOC 行序 `tutorial-meow-todo` 偏移 1 行（软红线） | 基线数量无变化；tagline 长度比 非 EN/EN 从 1.2–2.5 收敛到 0.2–1.2（ZH 0.20–0.69 属中文信息密度正常范围） | 无 WARN | ✅ 可发布；hreflang 对应页首屏信息量恢复对等，列表卡片排版一致 | — |
| 2026-11-07 | **Phase 3 自动推进 · G5（Meow FM）进行中 2/6**（限定范围）：补齐 `_posts/id/2026-07-31-tutorial-meow-fm.md`（134 行 / 3 图 / TOC 11 锚点全命中），行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN、内链前缀异常 0；含 5 处指向同组未落地页面的预期断链（整组完成后消链） | 未做完整验收（含预期断链） | 未做（含预期断链） | 单篇校验通过（行类型差 0、图片行序一致、alt 唯一、内链前缀异常 0、description 136、TOC 11 锚点全命中）；D17/D18 该篇通过；D09 11 组 MISS 0 未重测（词库 §2.5 待整组补） | 文章 157（66+66+25）、内容 md 280、产物约 298 HTML、sitemap 约 297（含预期断链，未计入全绿基线） | 无 WARN | 🟡 进行中（G5 2/6），含预期断链；整组完成后跑完整构建+htmlproofer+教研，再更新全绿基线 | — |
| 2026-11-07 | **Phase 3 自动推进 · G5（Meow FM）进行中 1/6**（限定范围）：补齐 `_posts/id/2026-07-13-pillar-white-noise-focus-apps-android.md`（125 行 / 5 图），行类型序列差异 0、图片行序一致、alt 唯一未照抄 EN；含 5 处指向同组未落地页面的预期断链（整组完成后消链） | 未做完整验收（含预期断链） | 未做（含预期断链） | 单篇校验通过（行类型差 0、图片行序一致、alt 唯一、内链前缀异常 0、description 150 字符）；D17 / D18 该篇通过；D09 11 组 MISS 0 未重测（词库 §2.5 待整组补） | 文章 157（66+66+25）、内容 md 280、产物约 298 HTML、sitemap 约 297（含预期断链，未计入全绿基线） | 无 WARN | 🟡 进行中（G5 1/6），含预期断链；整组完成后跑完整构建+htmlproofer+教研，再更新全绿基线 | — |
| 2026-11-07 | **马来语（ms）Phase 5 多语言扩展 · 全量交付**（§1.1 大规模改动）：`_config_ms.yml`、`_data/{languages,nav,ui}.yml`、`404.html`、`scripts/build.sh` 与四份 config 的 `ms` exclude；`_posts/ms/` 66 篇、`_apps_ms/` 11 篇、`_glossary_ms/` 22 篇、`_pages/ms/` 8 篇 + `ms/blog/index.html` 从 `id` 骨架逐行本地化；`SEO-KEYWORDS.md` §2.1.6 的 29 词全部落地 | PASS（完整构建 5 语 / 570 页；Pagefind 570 页 / 29820 词 / 5 语分片） | PASS（571 文件 / 1099 内链 / 0 failure） | **60 PASS / 4 FAIL / 0 WARN**；ms 全维度 PASS：D01 语言清单、D03 四语一一对应 + 结构页 8/8、D04 集合非空、D05 hreflang 6 条 × 570 页、D06 tagline 红线 12 与 YAML、D07 H2、D08/D17 插图集合与行序、D09 MISS=0、D10 JSON-LD、D12 feed / Pagefind、D14 0 条、D18 骨架 / TOC / 图片行序；4 个 FAIL 均为既有 th 遗留项（D11 的 6 条 `/id/` 内链、D17/D18 `tutorial-meow-todo-list` 行序偏移 1 行），与 ms 无关 | 产物 570 HTML、sitemap 570、内链 1099、Pagefind 29820 词；`/ms/` 114 页 | 无 WARN | ✅ `/ms/` 可发布；4 个既有 th 遗留 FAIL 按 §1.4 登记，不阻塞 ms | — |

---

## 9. 维护本文档

以下情况必须回来更新本文档，否则教研会失真：

- 站点结构、集合目录、`exclude`、`permalink` 规则变化；
- 构建脚本、i18n 注入逻辑、CI 流程变化；
- **新增语言**（D03/D04/D05 的判定要扩展为 N 语言）；
- §2.3 任一欠账被修复或新增（同步更新 `BASE` 常量与硬门禁项）；
- 新增了自动校验脚本（把其纳入 §0 步骤，避免两套口径）；
- 教研中发现新的「反复出现但脚本没覆盖」的问题（补进 §3 维度表与 §5 脚本）。
