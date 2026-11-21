# 网站整体教研（全站校验）规范

> **定位**：本站「大规模改动后」的唯一全站验收标准。回答一个问题：**改动之后，整个站点是否仍然正确？**
> **适用站点**：`spacemanmeow.com` 英文站（根路径）+ `/zh/` `/id/` `/th/` `/ms/` 四个子站；Jekyll 4.4、5 语合并构建、GitHub Pages Pages-artifact 部署。
> **触发时机**：见 §1.1。**每次触发都必须完整跑一遍 §0 的八步，并填写 §8 教研记录表**，不得只做「改了哪一块就只验哪一块」。
> **判定原则**：P0 硬门禁全绿 + WARN 逐条给出人工结论（§1.3）；历史欠账已清零、`BASE` 恒为空，任何欠账回升直接 FAIL（§1.4）。
> **当前基线**：以 §8 最近一次全绿记录为准（2026-11-18：675 页 / 1292 内链 / 70×5 文章 / 27×5 术语）。数量为快照非硬阈值，变化须能解释并记入 §8。
> **关联文档**：`SEO-OPTIMIZATION-PLAN.md`（总览）、`SEO-PLAYBOOK.md`（方法与运营红线）、`SEO-PROGRESS.md`（进度台账）、`SEO-METRICS.md`（月度指标）、`SEO-KEYWORDS.md`（关键词权威库）。本文档不替代它们，只规定「如何整体验收」。

---

## 0. 速查卡：一次完整教研

| 步 | 动作 | 命令 / 入口 | 级别 |
|---|---|---|---|
| 1 | 工作区与文件名红线 | `git status --short`；对照 §4 D14 | P0 |
| 2 | **完整构建（CI 同款，不带 `SKIP_PAGEFIND`）** | `JEKYLL_ENV=production bash scripts/build.sh` | P0 |
| 3 | 链接与资源校验 | `bundle exec htmlproofer _site --disable-external --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"` | P0 |
| 4 | 一键静态教研（含 **D22 设计令牌/统一样式**：字号字重不硬编码、分割线/间距走变量） | 复制 §5 脚本整段执行（在仓库根目录） | P0 |
| 5 | **响应式布局与样式实测** | §4 D21：多视口 + 多页面类型探针，量测溢出 / 断点 / 关键元素宽度 | P0 |
| 6 | 产物与 SEO 产物抽验 | §4 D05 / D10 / D11 / D12 的人工抽验项 | P1 |
| 7 | 线上与人工项 | §6（GSC、Rich Results、PSI、外链、真实设备） | P1 |
| 8 | 记录 | 填写 §8 教研记录表，写明结论与基线数字变化 | P0 |

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
| **P0 / FAIL** | 构建失败、链接断、多语言缺页、文件缺失、URL 泄漏、hreflang/sitemap 破损、关键词丢失、JSON-LD 污染 | **阻塞发布**，必须当场修复并重跑全流程 |
| **P1 / WARN** | 需人工确认或线上验证的项（外链、Pagefind、发布物白名单、性能、合规表述抽验） | 记录结论；有疑点则转 P0 |

### 1.4 基线对账原则

历史欠账已于 2026-11-05 全部清零，§5 脚本 `BASE` 恒为空；**所有维度均为 P0 硬门禁**，任何欠账回升直接判 FAIL，不再有「与基线持平即可放行」的口子。

---

## 2. 站点基线快照（2026-11-12）

### 2.1 结构与数量

| 类别 | 数量 | 路径 |
|---|---|---|
| 文章 | **345 = 69 × 5 语（EN / ZH / ID / MS / TH）** | `_posts/*.md` / `_posts/{zh,id,ms,th}/*.md`（均同名一一对应） |
| 应用详情页 | **55 = 11 × 5 语** | `_apps/` / `_apps_{zh,id,ms,th}/` |
| 静态页 | **40 = 8 × 5 语** | `_pages/` / `_pages/{zh,id,ms,th}/` |
| Glossary 术语页 | **135 = 27 × 5 语** | `_glossary/` / `_glossary_{zh,id,ms,th}/` |
| 内容 Markdown 合计 | **575** | 上述四类 |
| 图片文件 | **533**（526 webp + 4 jpg + 1 png + 1 svg + 1 ico） | `assets/images/` |
| 模板 | 8 layouts + 13 includes | `_layouts/` / `_includes/` |
| 构建产物 | **611 个 HTML**（含 404）、sitemap **610 条 `<loc>`** | `_site/` |
| 语言 | 5（EN 根 / ZH `/zh/` / ID `/id/` / MS `/ms/` / TH `/th/`） | `scripts/i18n_postprocess.py` 日志 `Languages detected: ['en', 'id', 'ms', 'th', 'zh']` |
| 内链 | htmlproofer 检查 **1292** 条内部链接（0 failure） | 随内容增长变化 |

> 数量是快照不是硬阈值。新增文章/术语/语言后数量上升是正常的，但必须在 §8 教研记录表写明「新增了什么、各语言是否成对」。5 语均已全量交付；任一语言文章数偏差按 D03「完整 / 分批」规则判定。

### 2.2 构建与路由事实（教研时的判定依据）

1. **合并构建**：`scripts/build.sh` 先用 `_config.yml` 构建 EN 到 `_site/`，再依次用 `_config_{zh,id,th,ms}.yml` 构建各语言到临时目录 `.jekyll-<lang>`，`rsync` 到 `_site/<lang>/`，最后 `scripts/i18n_postprocess.py --url` 注入 hreflang 并覆盖写合并 `sitemap.xml`，随后生成 Pagefind 索引。
2. **集合必须分离**：Jekyll 集合始终从 `_#{label}` 目录递归读取，`collections.*.path` 只影响 URL、不影响读取目录。因此中文应用必须用独立集合 `apps_zh`（源 `_apps_zh/`），术语用 `glossary_zh`（源 `_glossary_zh/`）；否则 ZH 构建会把英文文档一并读入并映射到 `/zh/`。
3. **`exclude` 细节**：Jekyll fnmatch 的 `*` 不带 `FNM_PATHNAME`，会跨 `/` 匹配，故不能用 `_posts/*` 区分根级文章与 `_posts/zh/`；`_config_zh.yml` 用 `_posts/2*`、`_posts/1*` 按年份前缀排除英文文章，并用 `_apps/`（**带尾斜杠**）避免误伤 `_apps_zh`。不支持 `!ruby/regexp`，且目录排除用 `start_with?` 判断。
4. **URL 规则**：EN `/posts/:title/`、`/apps/:name/`、`/glossary/:name/`；ZH 全部加 `/zh/` 前缀。`_pages/*.md` 用显式 permalink，不会与 `/zh/` 冲突。
5. **hreflang / sitemap**：按「去掉语言前缀后的路径」分组；每页注入组内所有语言 + 一条 `x-default` 指向 EN；合并 sitemap 每个语言变体一条 `<url>`，并删除各语言子 sitemap `/<lang>/sitemap.xml`；`404.html` 不注入、不进 sitemap。
6. **feed / 搜索**：5 个 feed（`feed.xml` 与 `zh/id/ms/th/feed.xml`）均存在；Pagefind 索引 `_site/pagefind/` 按语言分片，`data-pagefind-body` 只索引正文；`robots.txt` 指向生产 sitemap。
7. **CI**：`.github/workflows/pages-deploy.yml` 跑 `bash scripts/build.sh` + `htmlproofer`，部署后 Ping IndexNow。教研须与 CI 同款构建；`skills/site-build-deploy/scripts/test.sh` 已改为调用 `scripts/build.sh` 的全站验收入口，可直接用于验收（见 §2.4）。

### 2.3 已知基线欠账（BASE）

**当前为空（`BASE = {}`）。** 2026-11-05 的整改教研已把建立本文档时发现的全部欠账清零（description 超长、H2 数量不一致、`lang` 缺失、关键词虚标、裸 `&`、`_site/seo/` 泄漏、Pagefind 索引缺失、图片 width 模糊 WARN），并全部升级为 §5 脚本的 P0 硬门禁（`chk`），一旦回升直接判 FAIL。逐项修复明细见 git 历史，不在本文档维护。

### 2.4 已清零的工程风险

以下历史风险均于 2026-11-07 前修复，教研时只需复核未回退，不自动放行：

- `skills/site-build-deploy/scripts/test.sh` 已改为调用 `scripts/build.sh` + CI 同款 `htmlproofer` 的全站验收入口（支持 `--fast` 跳过 Pagefind）。
- `SEO-PROGRESS.md` T-34 悬空引用已改指向 `SEO-KEYWORDS.md` §2.1 各组关键词表。
- 两个工具脚本（compress_images / md_to_html）的机器绝对路径已改为基于 `__file__` 推导，缓存就近存放。
- 文档数量口径以文件系统实测为准（文章 69 / 术语 27 / 5 语），不再写死旧值。
- `README.md` 已收敛为纯对外站点介绍，不含内部命令/路径；「语言」段与 `_data/languages.yml` 一致由 §5 D01 硬门禁校验。

### 2.5 基线更新规则

只要修复或新增了 §2.3 任一项，或新增语言 / 集合 / 批量新增内容，**必须同步更新本文档 §2 与 §5 脚本顶部的 `BASE` 常量**，并在 §8 记录表写明变更前后数值。当前 `BASE` 为空，表示所有维度均为硬门禁。

### 2.6 多语言（N 语言）教研规则（2026-11-06 起）

- **语言清单自动发现**：§5 脚本从 `_config_<lang>.yml` 自动构造 `LANGS = ['en', ...]`，新增语言**不需要改脚本**；`i18n_postprocess.py` 亦按 `_site/` 下两位字母目录自动发现，无需改动。
- **完成度分层**：文章数与 EN 相等的语言判为「完整语言」，按一一对应硬门禁；不足者判为「分批建设中」，只要求「无孤立文件（不存在 EN 没有的文件）」并输出 `x/y` 覆盖进度，避免阻塞分批上线。其余三类（应用 / 页面 / 术语）对所有语言均要求无孤立文件。
- **文章骨架全语言对等（2026-11-06 起）**：**所有语言版本**的文章结构、文章目录与图片插入都以 EN 为准——H2/H3 层级与顺序、结构块（表格 / 列表 / 编号步骤 / FAQ / 分隔线）序列、文章目录（TOC 条目数与所在行序）、图片插入行序逐篇与 EN 同名文章一致；不再按本地搜索意图重新组织内容，也不再只要求「H2 ≥ 4 且含 FAQ」的结构下限。纯文本段落可因语言表达做局部调整，关键词按各语言词库优化。由 §5 脚本 **D18** 逐篇硬校验；依据 `SEO-I18N-PLAYBOOK.md` §1 红线 11 / §3.2 / §3.3 / §3.5。
- **hreflang 条数**：按「去掉语言前缀后的路径」分组，条数 = 组内实际语言数 + 1（x-default）。5 语全部完整后每页固定 6 条（当前分布 `{6: 570}`）；分批建设期间允许 2–5 条并存，**不**要求每页固定为总语言数 + 1。
- **D14 白名单**：新增语言源文件属已批准改动，不计入文件名红线告警；EN/ZH 既有文件的增删改仍照常告警。
- **模板通用化**：所有布局/包含按构建级 `site.lang` 动态取集合与前缀（`site[coll]`、`site.data.ui[lang]`），禁止 `zh`-vs-else 二元判断；`page.lang` 不可用于集合选择（非 EN 构建会渲染到 EN 根级页面）。

---

## 3. 校验维度总表

| 编号 | 维度 | 级别 | 主要手段 | 合格标准 |
|---|---|---|---|---|
| D01 | 构建与产物 | P0 | `scripts/build.sh` 全量构建 + §5 脚本 | 退出码 0；各语言首页存在；日志 5 语言、页数正常（`LANGS >= 5`）；**`README.md`「语言」段与 `_data/languages.yml` 一致**（新增语言不漏改对外清单，见 `SEO-I18N-PLAYBOOK.md` §2.4） |
| D02 | 链接与资源 | P0 | `htmlproofer` | 0 failure；内链、锚点、图片、脚本全通 |
| D03 | 多语言源对账 | P0 | §5 脚本 | 4 个非 EN 完整语言（zh/id/th/ms）逐组差集为 0、结构页 9/9（含 docs）；分批语言无孤立文件并报告覆盖进度 |
| D04 | 路由、集合与隔离 | P0 | 配置核对 + 产物 URL 抽查 | 集合分离且非空、`exclude` 正确、各语言子站无跨语言泄漏 |
| D05 | hreflang / sitemap / canonical / feed / robots | P0 | §5 脚本 + 人工抽验 | 组内每语言 1 条 + x-default；合并 sitemap；404 排除；canonical 为生产域名 |
| D06 | frontmatter 与元数据 | P0 | §5 脚本 | 必填齐、`lang` 对、`description ≤160`、无裸 `&`；**App `tagline` 四语信息量与 EN 对等**（≤1.5× 且无增补规格数字，见 §1 红线 12）；**站点级 `tagline` 单行显示宽度** `w≤60` 且非 EN ≤ EN（见 §1 红线 13） |
| D07 | 正文结构与多语言对等 | P0 | §5 脚本 + 人工抽验 | 完整语言 H2 一致；分批语言基础结构下限（H2≥4 且含 FAQ）；**骨架全语言对等由 D18 硬校验**；无汉字间多余空格 |
| D08 | 图片与可访问性 | P0 | §5 脚本 | alt 唯一、无 `![image]`、引用文件存在、全部带 `width` |
| D09 | 关键词真实覆盖 | P0 | §5 脚本归一化逐词核对 | 全部 11 组 MISS = 0 |
| D10 | 结构化数据与富媒体 | P0 + P1 | §5 脚本 + Rich Results Test | JSON-LD 无 `&amp;`；app 页 @type 正确；OG 图正确 |
| D11 | 内链闭环 | P0 | §5 脚本 + 抽验 | 语言前缀正确、glossary/tags/app 回链闭合、Docs 形态入口（docs 导航 + docs-hub 模板）齐全 |
| D12 | 搜索与索引 | P0 | 完整构建 + 产物检查 | Pagefind N 语言分片生成、各语言 feed / sitemap / robots / IndexNow 正常；**仅完整构建下有效，`SKIP_PAGEFIND=1` 快速构建下 D12 FAIL 是已知假阳性，须重跑完整构建消除** |
| D13 | 合规与产品表述 | P1 | 人工抽验 | 只读/免 root、不承诺虚假效果、YMYL、隐私、外链 rel |
| D14 | 文件名与 URL 红线 | P0 | `git status` | 无未经批准的文章/页面重命名、删除、新增；permalink 未变 |
| D15 | 发布物与敏感文件 | P0 | 产物目录检查 | 无临时目录、无凭据；`_site/seo/` 不存在 |
| D16 | 文档与台账一致性 | P1 | 人工核对 | 遵循 `SEO-OPTIMIZATION-PLAN.md`「文档更新规则」：长期价值内容已同步、临时流水未误写（见 §4 D16） |
| D17 | 文章插图跨语言一致性 | P0 | §5 脚本 + 人工抽验 | 非 EN 文章图片路径多重集 = EN 同名文章、**位置与 EN 行序一致**、`alt` 已本地化未照抄 EN（规范见 `SEO-I18N-PLAYBOOK.md` §3.5）；行序硬门禁于 2026-11-06 全量启用（72 篇一致） |
| D18 | 多语言文章骨架对等（结构 / 目录 / 插图） | P0 | §5 脚本 | **所有非 EN 语言**文章的 H2/H3 层级序列、结构块序列、文章目录（TOC 条目与行位置）、图片插入行序逐篇与 EN 同名文章一致；规则见 §2.6 与 `SEO-I18N-PLAYBOOK.md` §1 红线 11 / §3.5 |
| D19 | 文章 tags 一致性与相关文章匹配 | P0 | §5 脚本 + 人工抽验 | 每篇 `_posts/` **文章**至少带 1 个**规范产品标签**（11 个 App 之一：Meow Todo / Meow Habits / Meow Money / Meow Mood Diary / Meow FM / Only Clock / One Widget / Crosshair Aim / System Monitor / CPU Monitor / Floating Assistant）；无产品标签变体（如 `Meow Mood` / `Meow Todo List` / `To Do List` 或多余的 `Meow ` 前缀）；`related-posts.html` 已跳过泛标签（Android / Comparison / Best Apps / App Roundup / Alternatives），这些泛标签可保留但不得作为品类归属依据 |
| D20 | Release Note 页面覆盖与内链 | P0 | §5 脚本 + 人工抽验 | 每语言 11 个 App 均有 `/apps/<slug>/release-notes/` 页面（5 语言共 55 页，permalink 由各 config 的 `release_notes[_<lang>]` 集合定义）；frontmatter 含 `layout/app_slug/app_title/google_play/app_store/lang/title` 且标题后缀本地化；正文含至少 1 条发布记录；双端 App 的简介区同时显示 Google Play 与 App Store 入口（单端只显示对应一个）；`_layouts/app.html` 底部有指向该页的内链；数据由用户直接发来的升级日志经 `skills/release-notes/scripts/update_release_notes.py` 解析生成（日志临时写入被 gitignore 的 `seo/data/`，跑完可不保留；不联网抓取），页面为生成物 |
| D21 | 响应式布局与样式一致性 | P0 | §4 D21 多视口探针 + 静态 CSS 规则核对 | 375–1920px 各视口无横向溢出；三栏断点（≥1580px）内外侧栏显隐正确、正文固定 992px、侧栏 ≥280px；普通页容器不受加宽影响；商店按钮单/双按钮等宽靠左；目录竖线与 active 线同宽；五语 UI 键一致 |
| D22 | 设计令牌与统一样式 | P0 | §5 静态脚本 | 字号仅 6 档 `--fs-sm/base/md/xl/2xl/3xl`、字重仅 3 档 `--fw-head/bold/body`；全仓源文件（含内联样式与生成器）无硬编码字号/字重；分割线/间距/圆角/阴影复用标准变量；商店按钮等共享组件单一来源（include） |

---

## 4. 逐维度检查项

### D01 构建与产物（P0）

- **检查点**：完整构建退出码为 0；`_site/index.html` 与 `_site/{zh,id,th,ms}/index.html` 均存在；日志出现 `Languages detected: ['en', 'id', 'ms', 'th', 'zh']` 与 `Processed N pages across 5 languages`；所有 `.jekyll-<lang>` 临时目录已清理；`==> Done. Combined site in _site/` 出现；`README.md`「语言」段必须列出 `_data/languages.yml` 的全部 `label` 且数量词与实际语言数一致（§5 脚本 D01 硬门禁，新增语言漏改即 FAIL）。
- **命令**：`JEKYLL_ENV=production bash scripts/build.sh`（发布前教研**不要**带 `SKIP_PAGEFIND`）。
- **合格标准**：N 与 §2.1 快照 610 相当（允许随新增内容/语言增长，须解释）。
- **失败处理**：先看是 EN 还是 ZH 阶段失败；ZH 失败优先查 `_config_zh.yml` 的 `exclude` 与集合目录名；EN 失败查 `_config.yml` 与 frontmatter 语法。

### D02 链接与资源（P0）

- **检查点**：`htmlproofer` 三 check（Images / Links / Scripts）全绿；内部链接与 hash 锚点 0 失败。
- **命令**：CI 同款见 §0 步 3。
- **合格标准**：`HTML-Proofer finished successfully.`
- **失败处理**：断链先判断是「源文件改名」还是「permalink 变化」；hash 锚点失败检查 H2/H3 是否改了文字；图片失败检查 `/assets/...` 路径大小写与扩展名。

### D03 多语言源对账（P0）

- **检查点**：各语言 `_posts` 69↔69、`_apps` 11↔11、`_pages` 8↔8、`_glossary` 27↔27，**按同名文件**一一对应（具体数值以文件系统实测为准，脚本自动发现语言与完成度）；分批建设中的语言要求无孤立文件并报告进度，见 §2.6。成对文件 `title/description/tags/image/layout` 均存在。
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
  - 每个 HTML（除 404）都有 `<!-- i18n-hreflang -->` 块，含 5 条语言 alternate + `hreflang="x-default"` 共 6 条，且 x-default 指向 EN；组内互指成环；
  - `_site/sitemap.xml` 为合并版（当前 610 条 `<loc>`），每条带 6 个 `xhtml:link` alternates；各语言 `/<lang>/sitemap.xml` 全部**不存在**；404 不在 sitemap；
  - canonical 为 `https://spacemanmeow.com/...`，非 EN 为 `.../<lang>/...`；`url` 配置未被改成 localhost；
  - `_site/feed.xml` 与 `_site/{zh,id,th,ms}/feed.xml` 共 5 个 feed 均存在、含 entry 且 `xml:lang` 与语言一致；`robots.txt` 的 Sitemap 行指向生产域名。
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
  - **站点级 `tagline`（`_config*.yml` 的 header 副标题）单行不得过长**：按显示宽度 `w`（CJK / 全角 = 2，泰文 / 拉丁 = 1）计，`w ≤ 60` 且非 EN `w ≤ w(EN)`；只写「品类 + 1–2 个形容词」的短名词短语，禁止把「致力于…」「且实用…」等额外卖点堆进副标题。规则见 §1 红线 13；`_includes/nav.html` 的 `.brand__text small` 是 `nowrap + ellipsis`，≤768px 直接隐藏。
- **手段**：§5 脚本 D06；`description >160`、裸 `&`、App tagline 信息量不对等、站点级 tagline 超宽均为硬门禁 FAIL。
- **失败处理**：补字段；压缩 description 时保留年份与 2–4 个目标词；App tagline 超限时按 EN 短句重译（只换词，不增功能点）；站点级 tagline 超限时删掉动词前缀与额外形容词，收敛回 EN 短名词短语（MS / TH 均按此返工），不要靠放宽 CSS 省略号绕过；不要为塞关键词在汉字之间插空格（见 D07）。

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

### D19 文章 tags 一致性与相关文章匹配（P0，2026-11-15 新增）

- **背景**：相关文章逻辑（`_includes/related-posts.html`）按 `tags` 标签重叠取同语言 4 篇；Jekyll `where: "tags", tag` 为**精确匹配**。一旦某篇产品的标签写法与同组其余文章不一致（如 `Meow Mood` vs `Meow Mood Diary`、`Meow Todo List` vs `Meow Todo`），同组匹配落空，会一路退到泛标签（如 `Comparison`）抓全站最新文章，导致相关文章跨品类串味。**2026-11-15 已全量修复**：Mood 组 10 篇 `Meow Mood`→`Meow Mood Diary`、Budget 教程 5 篇补 `Meow Money`；并给匹配逻辑加了「跳过泛标签」的兜底（见下）。
- **检查点**：
  1. **规范产品标签白名单**（11 个 App，每个 App 唯一）：`Meow Todo` / `Meow Habits` / `Meow Money` / `Meow Mood Diary` / `Meow FM` / `Only Clock` / `One Widget` / `Crosshair Aim` / `System Monitor` / `CPU Monitor` / `Floating Assistant`；
  2. **每篇文章** frontmatter `tags` 至少包含上述白名单中 1 个（否则无法归入任何 App 组，related-posts 退化）；
  3. **不得出现产品标签变体**：`Meow Mood` / `Meow Todo List` / `To Do List`，或以 `Meow `/`Only Clock`/`One Widget`/`Crosshair Aim`/`System Monitor`/`CPU Monitor`/`Floating Assistant` 开头却不在白名单的标签；
  4. **泛标签**（Android / Comparison / Best Apps / App Roundup / Alternatives）允许保留，但 `related-posts.html` 的跳过清单必须与这里一致——新增泛标签时两处同步改，否则会被当作品类归属依据。
- **手段**：§5 脚本 D19 两段 `chk`（变体 `chk` + 缺产品标签 `chk`）；新增文章/批量改标签后由本项硬门禁拦住。
- **失败处理**：变体标签按白名单改回（如 `Meow Mood`→`Meow Mood Diary`）；缺产品标签的补上对应 App 标签；泛标签清单与 `related-posts.html` 不同步时一并更新。

### D20 Release Note 页面覆盖与内链（P0，2026-11-17 新增）

- **背景**：每个 App 需有独立的发布记录页，URL 形如 `/apps/<slug>/release-notes/`（非英语加 `/<lang>` 前缀），App 详情页底部内链。**静态生成**：`build.sh` 不含抓取步骤。
- **数据源（唯一）**：**用户在对话中直接发来的升级日志**。`seo/data/` 只是临时中转目录（已被 `.gitignore` 忽略，不进版本控制、不要求长期维护）：收到日志后临时写入 `seo/data/<app_slug>_release_note`，处理完可不保留。日志格式为 `内部版本号 (版本名)` 或纯版本号 + `<en-US>/<zh-CN>/<id>/<ms>/<th>` 等语言标签块；占位符「请在此处输入或粘贴...」视为缺失。
- **生成命令**：`python3 skills/release-notes/scripts/update_release_notes.py [日志文件...]`（省略参数则处理 `seo/data/*_release_note` 全部）。脚本只解析本地文件、不联网；按日志文件名匹配 `_apps/<slug>.md`（命名不一致时用脚本内 `SLUG_ALIASES` 映射），直接生成 5 语言页面到 `_release_notes[_<lang>]/`。
- **译文修正/补全**：收到日志后先把补全/修正的 5 语言译文**直接整理进日志临时文件**再跑脚本——不依赖任何外部 fixes/中间修正库。日志须自带全部 5 语言内容（缺语言会生成空节，D20 会拦）。历史译文中已修正的错误包括 Apple Watch 条目遗漏、"喵咪"笔误、英文 typo 等，均已固化进现有页面；以 `- ` 开头的行渲染为上一项的子列表。
- **页面格式**：多版本按 `## 版本号` 分节，每节有序列表从 1 递增编号。
- **检查点**：
  1. 每语言 11 个 App 均有对应 release note 页（5 语言共 55 页）；source 目录 `_release_notes[_<lang>]/`，集合 `release_notes[_<lang>]`，permalink `/[ lang /]apps/:name/release-notes/`；
  2. frontmatter 含 `layout: release-note`、`app_slug`、`app_title`、`google_play`、`app_store`、`lang`、`title`，且 `title` 后缀为本地化文案（EN Release Notes / ZH 更新日志 / ID Catatan Rilis / MS Nota Keluaran / TH บันทึกการอัปเดต）；`app_store` 为 `#` 或空时不显示 App Store 入口，双端 App 则两个入口都显示；
  3. 正文至少 1 条有序列表发布记录（`1. ...`），空页视为失败；
  4. `_layouts/app.html` 底部有指向 `{{ page.url | relative_url }}release-notes/` 的内链（一处覆盖全语言）；
  5. 单端 App 的 `app_store` 用 `""`（**不要写空 `app_store:` 行**，否则 YAML 会吞掉下一行，破坏 layout 与 hreflang），双端 App 才显示两个入口；「返回应用」链接只在 `_layouts/release-note.html`，不写进页面正文。
- **手段**：§5 脚本 D20 五项硬门禁（覆盖 / frontmatter / 正文 / 标题本地化 / 内链），外加上述 YAML 空值与返回链接由人工抽验。
- **失败处理**：缺页或内容过期 → 拿到用户发来的新日志（补全 5 语言译文后）临时写入 `seo/data/<app_slug>_release_note`，重跑 `python3 skills/release-notes/scripts/update_release_notes.py` 并确认 55 页生成；某 App 确无发布记录须人工在对应 md 写明并登记，不得让空页过门禁。

### D08 图片与可访问性（P0）

- **检查点**：同文件内 `alt` **零重复**且关键词化；`![image]` 零残留；所有 `/assets/...` 引用文件真实存在；每图带 `{: width="180" .normal }` 之类宽度属性防 CLS；各语言文章图片引用与 EN 一一对应（含行序位置，见 §3.5 对应规范）；新增图片走 webp 压缩。
- **手段**：§5 脚本 D08 + `skills/cover-images/scripts/compress_images.py`（路径已改为相对脚本位置推导，见 §2.4）。
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

- **检查点**：非 EN 正文的术语链接用 `/<lang>/glossary/...`，EN 用 `/glossary/...`；EN 内容里不误带任何 `/<lang>/` 前缀；`_pages/glossary.md` 索引覆盖全部 27 条；`/tags/#<slug>` 锚点存在；每篇文章 `image == app icon` 且 App 页能列出对应 Guides；related-posts 只出同语言；外链带 `rel="noopener noreferrer"`；**Docs 形态入口闭合：`nav.yml` 含 docs 导航项，`_layouts/` 含 docs-hub 模板入口**。
- **手段**：§5 脚本 D11 + 人工抽验新增/改动文章的首段内链与底部相关推荐。
- **失败处理**：语言前缀错误会导致中文读者跳到英文页、破坏 hreflang 语义，属 P0。

### D12 搜索与索引（P0 + P1）

- **检查点**：完整构建生成 `_site/pagefind/`；搜索页能 `import("/pagefind/pagefind.js")` 并按语言检索；sitemap 与 IndexNow 使用生产 URL；404 有 `data-pagefind-ignore` 且不在 sitemap；GoatCounter 与 `.nojekyll` 正常。
- **说明**：**本维度只在完整构建下有效**。`SKIP_PAGEFIND=1` 快速构建不生成索引，脚本判 FAIL 属**已知假阳性**（见维度表 D12、§10），不是回归；**发布前教研必须完整构建一次**消除该 FAIL；CI 不设该变量，会生成索引。
- **失败处理**：Pagefind 失败先看 `.pagefind-bin/` 二进制与网络；索引缺失时搜索页会静默失效，需手动打开搜索页验证。

### D13 合规与产品表述（P1）

- **检查点**：CPU Monitor / System Monitor 类强调**只读、免 root、不承诺一键降温/加速/清理**；Floating Assistant / Crosshair Aim 强调**纯视觉叠层、不改游戏数据、不触发反作弊、权限透明**；清理/加速类词按「品类对照」诚实落地，不虚构功能；财务类（Meow Money）属 YMYL，用事实与数字、避免空泛「最好」绝对词；隐私表述与 `privacy.md` 一致。
- **手段**：人工抽验改动涉及的 App 分组的 pillar / tutorial / vs 首段。
- **失败处理**：发现与只读定位冲突的营销话术，立即改写；这是信任问题，不要留到下次。

### D14 文件名与 URL 红线（P0）

- **检查点**：`git status --short` 中，内容目录（`_posts/`、`_posts/zh/`、`_apps*/`、`_pages/`、`_glossary*/`）不得出现未经批准的 `R` / `D` / `A` / `??`；已发布页 `permalink` 不变（本站**没有 301 重定向机制**，改文件名即等于丢权重）；新增语言 URL 一旦发布不再改。
- **手段**：`git status --short` + §5 脚本 D14（无增删改判 PASS，有则 WARN 需人工确认）。
- **失败处理**：确需改名时，必须同时评估索引丢失、hreflang 分组断裂、外链与 sitemap 变化，并在记录表中写明；新增文章必须 EN + 4 语同源成对（红线 11 / D18）。

### D15 发布物与敏感文件（P0 + WARN）

- **检查点**：`_site/` 中不含 `.jekyll-zh/`、`.pagefind-bin/`、`skills/seo-research/scripts/gsc/credentials.json`、`token.json`、缓存目录；`.nojekyll` 存在；**`_site/seo/` 不存在**（内部 SEO 文档与 `seo/data/*.csv/json` GSC 导出不得公开）。
- **手段**：§5 脚本 D15 + `find _site -maxdepth 2 -type d | sort` 抽查。
- **失败处理**：`seo/` 已加入两份 `_config*.yml` 的 `exclude`；若重新出现，先 `rm -rf _site/seo` 再完整重构建验证；敏感文件泄漏属 P0。

### D16 文档与台账一致性（P1）

- **唯一权威规则**：见 `SEO-OPTIMIZATION-PLAN.md`「文档更新规则」。只写长期价值内容（需沉淀的经验、阶段性重要进展、SOP / 规则），临时性内容与一次性改动不写入；规则或有价值内容出现即同步，避免遗漏。
- **典型写入位置**：关键词覆盖状态 / 升权 → `SEO-KEYWORDS.md`；任务进度与规划 → `SEO-PROGRESS.md`、唯一状态源 `SEO-I18N-PROGRESS.md`；月度 GSC / GoatCounter 复盘 → `SEO-METRICS.md`；新坑 / 新经验 → 对应 PLAYBOOK 或 skill `references/`。
- **教研时确认**：本轮是否有漏写的规则 / 经验 / 进展，或误写的临时流水；`BASE` 是否仍为空；教研记录表是否已填。

### D21 响应式布局与样式一致性（P0，2026-11-19 新增）

- **背景**：宽屏三栏、侧栏下限、按钮栅格、目录竖线均为 CSS 渲染结果，静态脚本无法验证真实布局。2026-11-19 一轮连续样式微调暴露三类典型回归：全局 `.page-body > .container` 加宽误伤 about 等普通页；侧栏以 `1fr` 无限压缩正文；flex `flex:1` 让单枚商店按钮撑满整行。故把「多视口实测 + 静态规则核对」固化为发布前门禁。
- **静态检查点（源码 / 产物核对）**：
  1. `_data/ui.yml` 五语键完全一致（如 `tags_title` 必须 en/zh/id/ms/th 齐备）；缺键会静默输出空白；
  2. `assets/css/main.css` 三栏断点为 `@media (min-width: 1580px)`，grid 为 `minmax(240px, 1fr) 992px minmax(280px, 1fr)`，**正文固定 992px 不收缩**；
  3. 加宽规则仅作用于 `.page-body > .container--wide`（post / guide / docs 三个 layout 的 page-body），about / tags 等普通页仍为默认 `--container: 1040px`；
  4. 侧栏商店按钮为两列 grid（`repeat(2, minmax(0, 1fr))`），单按钮占首列半宽靠左；
  5. 目录 `.toc-nav__list` 基线 `border-left: 2px`，active 项同为 2px 且 `margin-left: -2px` 左对齐。
- **浏览器实测检查点（结构性样式改动必跑）**：
  1. 视口至少覆盖 375 / 768 / 1024 / 1400 / 断点±10px（1570、1590）/ 1920；页面类型至少 3 类：文章页、普通页（about / tags）、App 详情页，外加 1 篇非 EN 文章；
  2. 每页 `document.documentElement.scrollWidth <= clientWidth + 1`（无横向溢出）；
  3. 文章页在 `<1580px` 时 `.post-aside--right` 为 `display: none`、正文单栏；`>=1580px` 时为 `display: block`、`.post__inner` 宽 992px、右栏宽 `>=280px`；
  4. 普通页 `.page-body > .container` 宽 `<=1040px`（含 1920 视口），不被三栏加宽污染；
  5. 同视口下单按钮 badge 宽度与双按钮首枚 badge 宽度差 `<=1px`，且 badge 左边缘等于右栏左边缘；
  6. 非 EN 文章与 EN 文章在相同视口下三栏宽度一致。
- **手段**：在 `_site/` 放临时探针 HTML，用多个不同宽度的 iframe 批量加载目标页（**iframe 元素宽度即 media query 判定的 viewport 宽度**），本地 `python3 -m http.server` 后以 headless Chrome `--dump-dom` 一次性导出 `<pre>` 中的 JSON 测量值，逐条对照判定；**探针与 server 用完即删**，否则 D15 判 FAIL。静态键一致性与 CSS 规则可用 shell / Python 核对。
- **失败处理**：溢出 → 定位固定宽度元素改弹性或断点；侧栏挤压正文 → 提高断点让侧栏整体隐藏，**不要给侧栏留可压缩的 `1fr`**；普通页被加宽 → 把规则限定到专用 class（如 `container--wide`）；单按钮撑满 → 用两列 grid 替代 flex `flex:1`；竖线不齐 → `margin-left` 取 border 宽度的负值。

### D22 设计令牌与统一样式（P0，2026-11-20 新增）

- **背景**：站点的字号/字重、分割线、间距、圆角、阴影、商店按钮、App 卡片等均有统一标准。历史上多次出现硬编码字号（`28px`/`26px`/`.9em`）、非标准字重（300/700 混用）、第四种字重 `--fw-light`、裸 `border`/`padding` px、以及各处重复实现按钮结构，导致视觉不一致。故把「样式必须复用统一令牌/共享组件」固化为发布前硬门禁。
- **统一标准（唯一权威，定义在 `:root`）**：
  1. **字号 6 档**：`--fs-sm:12px` / `--fs-base:14px` / `--fs-md:16px` / `--fs-xl:20px` / `--fs-2xl:24px` / `--fs-3xl:30px`；其他字号就近并到最近档，禁止新增档位；
  2. **字重 3 档**：`--fw-head:700` / `--fw-bold:600` / `--fw-body:500`（对应 `fs-3xl` / `fs-xl·2xl` / `fs-sm·base·md`），禁止硬编码数字或关键字；
  3. **分割线**：`--divider-dashed` / `--divider-solid` 及配套 `--divider-*-gap`；
  4. **间距**：`--space-1`…`--space-9`（4/6/8/10/12/16/20/24/32px）；
  5. **圆角**：`--radius-sm` / `--radius` / `--radius-lg` / `--radius-xl`；**阴影**：`--shadow-card` / `--shadow-soft`；
  6. **共享组件**：商店下载按钮只在 `_includes/store-buttons.html` 实现（文案按 `names` 参数切换：默认本地化、开发者页显示 `Google Play`/`App Store`），App 卡片只在 `_includes/app-card.html`；页面不得重复硬编码同类结构。
- **静态检查点（§5 脚本）**：① 字号变量集合恰为 6 档、字重变量集合恰为 3 档；② `assets/css/main.css` 中 `font-size`/`font-weight` 全部为 `var(--fs-*)`/`var(--fw-*)`，无硬编码；③ 全仓源文件（CSS/HTML/Liquid/Python/JS，排除 `_site*`/`.jekyll-*`/依赖）无硬编码字号字重——覆盖独立 HTML 生成器与内联样式；④ 统一令牌齐备（分割线 `--divider-*`、间距 `--space-*`、圆角 `--radius-*`、阴影 `--shadow-*`），且 border 无硬编码 hex 颜色；⑤ 商店按钮共享 include 存在。
- **判定口径**：字号/字重为**零容忍硬门禁**（必须 100% 走变量）；布局专用的固定尺寸（负 margin、`100px` 留白、边框宽度 px）允许保留，不强制全部塞进 `--space-*`，避免为达标而扭曲布局。分割线重点管**颜色**必须走 `--line`/`--divider-*`，宽度 px 不限。
- **失败处理**：出现硬编码字号/字重 → 就近替换为标准 `--fs-*`/`--fw-*` 变量；多出的字重档 → 就近并入 head/bold/body；硬编码分割线颜色 → 换成 `--line`/`--divider-*`；组件重复实现 → 抽为 `_includes/` 共享 include 并让各调用点引用。新增样式一律先复用现有令牌，确需新令牌时同步更新本节与 `:root` 定义。

---

## 5. 一键静态教研脚本

> **用法**：在仓库根目录整段复制执行（如 `cd "$(git rev-parse --show-toplevel)"`）；**执行前先完成一次构建**（否则产物类维度会跳过）。
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
    if L == 'en': return dict(posts='_posts', pages='_pages', apps='_apps', gloss='_glossary', rel='_release_notes')
    return dict(posts='_posts/' + L, pages='_pages/' + L,
                apps='_apps_' + L, gloss='_glossary_' + L, rel='_release_notes_' + L)
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
chk('D01', '语言清单与完成度（至少 5 语）', len(LANGS) >= 5,
    f'LANGS={LANGS} 完整={FULL} 分批中={PARTIAL}')
# D01：README 对外语言清单必须与 _data/languages.yml 同步（新增语言最易漏改的公开文案）
_labels = re.findall(r'^\s+label:\s*(.+?)\s*$',
                     open('_data/languages.yml', encoding='utf-8').read(), re.M)
_rm = re.search(r'^## 语言[ \t]*\n(.*?)(?=^## |\Z)',
                open('README.md', encoding='utf-8').read(), re.M | re.S)
_seg = _rm.group(1) if _rm else ''
_miss = [x for x in _labels if x not in _seg]
_CN = {1:'一', 2:'二', 3:'三', 4:'四', 5:'五', 6:'六', 7:'七', 8:'八', 9:'九',
       10:'十', 11:'十一', 12:'十二'}
_num = _CN.get(len(_labels), str(len(_labels)))
chk('D01', 'README 对外语言清单与 languages.yml 一致',
    bool(_labels) and not _miss and (f'{_num}个语言版本' in _seg),
    f'languages.yml {len(_labels)} 语；README 缺失 {_miss}；数量词应为「{_num}个语言版本」')
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
# D03 结构页硬门禁：每个完整语言必须含 9 个固定结构页（含 Docs 中心页；缺页会致 htmlproofer 断链，P0）
STRUCT = ['index', 'meow', 'about', 'privacy', 'terms', 'search', 'tags', 'glossary', 'docs']
for L in FULL:
    have = nm(dirs(L)['pages'] + '/*.md')
    miss = [s for s in STRUCT if (s + '.md') not in have]
    chk('D03', f'结构页 9/9 ({L})', not miss,
        f'缺失 {miss}（致 htmlproofer 断链；须与 id 骨架同源补齐，不得标记待补）')
# D06
need0 = {'title', 'description'}
bad = []
for f, d in fms.items():
    if re.match(r'^_release_notes(_[a-z]{2})?/', f): continue  # D20 单独校验其 frontmatter
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
# D06：站点级 tagline 单行显示宽度（SEO-I18N-PLAYBOOK.md §1 红线 13）
# header .brand__text small 为 nowrap + ellipsis；CJK/全角按 2 单位，泰文/拉丁按 1 单位
import unicodedata
def _w(s):
    return sum(2 if unicodedata.east_asian_width(c) in 'WF' else 1 for c in s)
def _cfg_tagline(f):
    for l in open(f, encoding='utf-8').read().split('\n'):
        if l.startswith('tagline:'):
            return re.sub(r'\s+#\s.*$', '', l[len('tagline:'):].strip()).strip().strip('"')
    return ''
_cfgs = ['_config.yml'] + ['_config_%s.yml' % L for L in LANGS[1:]]
_tw = {f: _w(_cfg_tagline(f)) for f in _cfgs if os.path.isfile(f)}
_enw = _tw.get('_config.yml', 0)
_tw_bad = [(f, w) for f, w in _tw.items() if w > 60 or (f != '_config.yml' and w > _enw)]
chk('D06', '站点级 tagline 单行显示宽度（w≤60，非 EN ≤ EN）', not _tw_bad,
    f'EN w={_enw}，各语 {sorted(_tw.items())}，异常 {_tw_bad}')
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
# D19：tags 一致性与相关文章匹配（P0；产品标签变体曾致 related-posts 跨品类，见 §4 D19）
# 规则：① 每篇【_posts/ 文章】至少带 1 个规范产品标签（11 个 App 之一）；
#       ② 不得出现产品标签变体（Meow Mood / Meow Todo List / To Do List / 多余 Meow 前缀等）；
#       ③ related-posts.html 跳过泛标签（Android/Comparison/Best Apps/App Roundup/Alternatives）。
CANON_PRODUCT = {'Meow Todo', 'Meow Habits', 'Meow Money', 'Meow Mood Diary',
                 'Meow FM', 'Only Clock', 'One Widget', 'Crosshair Aim',
                 'System Monitor', 'CPU Monitor', 'Floating Assistant'}
BRAND_PREFIX = ('Meow', 'Only Clock', 'One Widget', 'Crosshair Aim',
                'System Monitor', 'CPU Monitor', 'Floating Assistant')
_badvar, _noprod = [], []
for f, d in fms.items():
    if not f.startswith('_posts/'): continue
    raw = d.get('tags', '')
    m = re.match(r'\[(.*)\]', raw)
    tags = [x.strip() for x in m.group(1).split(',') if x.strip()] if m else []
    for tg in tags:
        if tg in ('Meow Mood', 'Meow Todo List', 'To Do List') or \
           (tg.startswith(BRAND_PREFIX) and tg not in CANON_PRODUCT):
            _badvar.append((f, tg))
    if not (set(tags) & CANON_PRODUCT):
        _noprod.append(f)
chk('D19', 'tags 无产品标签变体', not _badvar, f'异常 {len(_badvar)} {_badvar[:2]}')
chk('D19', '每篇至少带规范产品标签', not _noprod, f'缺失 {len(_noprod)} {_noprod[:2]}')
# D20：Release Note 页面覆盖与内链（P0；见 §4 D20）
# 规则：每语言 11 个 App 均有对应 release note 页；frontmatter 带 layout/app_slug/app_title/google_play；
#       正文有发布记录内容；app 详情页底部有指向 release-notes/ 的内链。
REL_LABEL = {'en': 'Release Notes', 'zh': '更新日志', 'id': 'Catatan Rilis',
             'ms': 'Nota Keluaran', 'th': 'บันทึกการอัปเดต'}
_rel_miss, _rel_badfm, _rel_empty, _rel_badtitle, _rel_badstore = [], [], [], [], []
for L in LANGS:
    app_slugs = nm(dirs(L)['apps'] + '/*.md')
    rel_slugs = nm(dirs(L)['rel'] + '/*.md')
    for s in app_slugs:
        if s not in rel_slugs: _rel_miss.append((L, s))
    for f, d in fms.items():
        if not f.startswith('_%s/' % ('release_notes' if L == 'en' else 'release_notes_' + L)): continue
        need = {'layout', 'app_slug', 'app_title', 'google_play', 'app_store', 'lang', 'title'}
        if need - set(d): _rel_badfm.append((f, ','.join(sorted(need - set(d)))))
        if not re.search(r'^\d+\.\s+\S', txt[f], re.M): _rel_empty.append(f)
        if REL_LABEL.get(L, 'Release Notes') not in d.get('title', ''): _rel_badtitle.append(f)
        # 裸 app_store: 空值会被 YAML 吞掉下一行，破坏 layout/hreflang；单端须写 app_store: ""
        if re.search(r'^app_store:[ \t]*$', txt[f], re.M): _rel_badstore.append(f)
chk('D20', '每 App 均有 Release Note 页（全语言）', not _rel_miss, f'缺失 {len(_rel_miss)} {_rel_miss[:2]}')
chk('D20', 'Release Note frontmatter 完整', not _rel_badfm, f'异常 {len(_rel_badfm)} {_rel_badfm[:2]}')
chk('D20', 'Release Note 正文含发布记录', not _rel_empty, f'空 {len(_rel_empty)} {_rel_empty[:2]}')
chk('D20', 'Release Note 标题含本地化后缀', not _rel_badtitle, f'异常 {len(_rel_badtitle)} {_rel_badtitle[:2]}')
chk('D20', 'Release Note 无裸 app_store 空值行', not _rel_badstore, f'异常 {len(_rel_badstore)} {_rel_badstore[:2]}')
# app 模板须含 release-notes 内链（一处覆盖全语言）
_app_tpl = open('_layouts/app.html', encoding='utf-8').read()
chk('D20', 'app 详情页含 Release Note 内链', 'release-notes/' in _app_tpl, 'app.html 缺内链')
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
# D11 形态间内链闭合：Docs 形态须在导航与模板中留入口
_nav_txt = open('_data/nav.yml', encoding='utf-8').read()
_tpl_txt = ''.join(open(f, encoding='utf-8').read() for f in
                   fs('_layouts/*.html') + fs('_includes/*.html'))
_hub_ok = ('nav: docs' in _nav_txt and 'docs-hub' in _tpl_txt)
chk('D11', '形态间内链入口闭合', _hub_ok,
    'docs 导航项或 docs-hub 模板入口缺失')
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

# D22 设计令牌与统一样式（P0）：字体/字重/分割线/间距/按钮等禁止硬编码，必须复用统一样式
_css = open('assets/css/main.css', encoding='utf-8').read()
_css_nocomment = re.sub(r'/\*.*?\*/', '', _css, flags=re.S)
# 1) 字号：只能 --fs-sm/base/md/xl/2xl/3xl；无硬编码 px/em/rem/%/clamp/calc
_FS = {'--fs-sm', '--fs-base', '--fs-md', '--fs-xl', '--fs-2xl', '--fs-3xl'}
_fs_def = set(re.findall(r'(--fs-[\w-]+)\s*:', _css))
chk('D22', '字号变量仅保留 6 档标准', _fs_def == _FS,
    f'定义={sorted(_fs_def)} 期望={sorted(_FS)}')
_hard_fs = re.findall(r'font-size\s*:\s*([^;]+)', _css_nocomment)
_hard_fs = [v.strip() for v in _hard_fs if 'var(--fs-' not in v]
chk('D22', '无硬编码字号（font-size 全部用 --fs-* 变量）', not _hard_fs,
    f'硬编码 {len(_hard_fs)} 处 {_hard_fs[:5]}')
# 2) 字重：只能 --fw-head/bold/body；无硬编码数字/关键字
_FW = {'--fw-head', '--fw-bold', '--fw-body'}
_fw_def = set(re.findall(r'(--fw-[\w-]+)\s*:', _css))
chk('D22', '字重变量仅保留 3 档标准', _fw_def == _FW,
    f'定义={sorted(_fw_def)} 期望={sorted(_FW)}')
_hard_fw = re.findall(r'font-weight\s*:\s*([^;]+)', _css_nocomment)
_hard_fw = [v.strip() for v in _hard_fw if 'var(--fw-' not in v]
chk('D22', '无硬编码字重（font-weight 全部用 --fw-* 变量）', not _hard_fw,
    f'硬编码 {len(_hard_fw)} 处 {_hard_fw[:5]}')
# 3) 全仓源文件（排除构建产物/依赖）无硬编码字号字重，含独立 HTML 生成器与内联样式
_srcs = []
for _pat in ('**/*.css', '**/*.html', '**/*.liquid', '**/*.py', '**/*.js'):
    _srcs += [p for p in fs(_pat) if not re.search(
        r'(^|/)(_site|_site_en|_site_zh|\.jekyll-[^/]*|node_modules|\.git|\.pagefind-bin|\.sass-cache)/', p)]
_bad_inline = []
for _p in set(_srcs):
    try: _t = open(_p, encoding='utf-8').read()
    except Exception: continue
    for _m in re.finditer(r'font-size\s*:\s*([^;}"\']+)', _t):
        if 'var(--fs-' not in _m.group(1): _bad_inline.append((_p, 'size', _m.group(1).strip()))
    for _m in re.finditer(r'font-weight\s*:\s*([^;}"\']+)', _t):
        if 'var(--fw-' not in _m.group(1): _bad_inline.append((_p, 'weight', _m.group(1).strip()))
chk('D22', '全仓源文件无硬编码字号/字重（含内联样式与生成器）', not _bad_inline,
    f'{len(_bad_inline)} 处 {_bad_inline[:5]}')
# 4) 统一样式令牌必须齐备（分割线/间距/圆角/阴影），且分割线禁止硬编码颜色
_TOKENS = ['--divider-dashed', '--divider-solid',
           '--space-1', '--space-9', '--radius-sm', '--radius-xl',
           '--shadow-card', '--shadow-soft']
_miss_tok = [t for t in _TOKENS if not re.search(re.escape(t) + r'\s*:', _css)]
chk('D22', '统一令牌齐备（分割线/间距/圆角/阴影）', not _miss_tok,
    f'缺失 {_miss_tok}')
_borders = re.findall(r'border(?:-top|-bottom|-left|-right)?\s*:\s*([^;]+)', _css_nocomment)
_hex_border = [v.strip() for v in _borders if re.search(r'#[0-9a-fA-F]{3,8}\b', v)]
chk('D22', '分割线颜色无硬编码（border 用 var(--line)/--divider-*)', not _hex_border,
    f'硬编码颜色 {len(_hex_border)} 处 {_hex_border[:5]}')
# 5) 共享组件样式只在 _includes/store-buttons.html 定义，页面源码不重复硬编码按钮结构
_btn_inc = fs('_includes/store-buttons.html')
chk('D22', '商店按钮为共享 include（单一来源）', bool(_btn_inc),
    f'_includes/store-buttons.html 存在={bool(_btn_inc)}')
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
| GSC 覆盖与点击词 | `python3 skills/seo-research/scripts/gsc_export.py` 导出，回填 `SEO-METRICS.md` | 每月（Playbook §7.1） |
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
| D18 骨架不一致 | 某语言按本地意图重写正文、漏 / 多列表项、目录增删条目、图片挪位置 | 以 EN 同名文章为骨架补齐或合并结构块，禁止改动 EN 凑一致（§4 D18） |
| D20 空节 / 缺语言 / 标题未本地化 | 日志缺某语言块、译文没进临时日志、`title` 后缀照抄 EN | 补全 5 语译文进日志→重跑生成器→完整构建→复跑审计（§4 D20、`skills/release-notes/SKILL.md`） |
| D12 在快速构建下 FAIL | `SKIP_PAGEFIND=1` 未生成 Pagefind 索引（已知假阳性） | 用完整 `bash scripts/build.sh` 重构建后复跑，不要在快速构建下当回归修 |
| D22 硬编码字号/字重 FAIL | 新增样式直接写 `28px`/`600` 等裸值，或在独立生成器/内联样式里硬编码 | 就近换成标准 `--fs-*`/`--fw-*` 变量；多出的字重档并入 head/bold/body；新令牌需同步 §4 D22 与 `:root` |
| D22 分割线硬编码颜色 / 令牌缺失 FAIL | 直接写 `border: 1px solid #eee`，或删掉了 `--divider-*`/`--space-*`/`--radius-*`/`--shadow-*` 令牌 | 颜色换成 `--line`/`--divider-*`，补齐缺失令牌；布局专用 px（负 margin、边框宽度）允许保留 |

---

## 8. 教研记录表（每次必填）

```markdown
| 日期 | 改动范围 | 构建 | htmlproofer | D03 | D05 | D06 | D09 | D12 | D17 | D18 | D19 | D20 | D21 | D22 | 基线数字变化 | WARN 结论 | 结论 | 执行人 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| YYYY-MM-DD | 简述改了哪些目录/文件、是否属 §1.1 大规模改动 | PASS/FAIL + 页数 | PASS/FAIL + 文件数/内链数 | … | … | … | … | … | … | … | … | … | PASS/FAIL + 视口/页面类型覆盖 | PASS/FAIL + 令牌/硬编码项 | 如 610→615 页 | 逐条写明 | ✅ 可发布 / ❌ 阻塞 | … |
```

**历史教研流水**：2026-11-05 至 2026-11-12 的逐次教研记录（欠账清零、5 语扩展、骨架对等硬门禁、tagline 红线、Release Note 上线等）已从本文档移出，完整过程见 git 提交历史。仅保留最近一次全绿基线用于对照：

| 日期 | 构建 | htmlproofer | 教研结果 | 基线数字 |
|---|---|---|---|---|
| 2026-11-12 | PASS（5 语 / 610 页；Pagefind 36145 词） | PASS（611 文件 / 1159 内链 / 0 failure） | 69/69 文章·11/11 应用·8/8 页面·27/27 术语 五语对称；D01–D20 全绿（D14 1 条未跟踪新文件已批准） | 610 页 / sitemap 610 loc / 6 条 hreflang × 610 页 / `BASE` 为空 |
| 2026-11-18 | PASS（5 语 / 675 页；Pagefind 37247 词） | PASS（676 文件 / 1292 内链 / 0 failure） | Docs 形态落地（`CONTENT-HUB-PLAN.md`）：+5/5 `/docs/` 中心页(8→9 结构页)、55 教程 layout→docs；在线工具形态已移除、暂不落地；T-38 两组支柱页 title/description 重写；T-39 id/th 8 个高曝光术语页本地化标题；T-22b 统一 BlogPosting `dateModified`/author；T-29 AVIF/srcset/preload；T-36 `money tracker` 5 语支柱页；T-41 Glossary `DefinedTerm` + 移动 CTA。D03 70/70 文章·9/9 结构页、D05 hreflang 675 页成环、D06 description ≤160、D09 MISS=0、D11 Docs 入口闭合、D17/D18/D19 通过；74 PASS / 1 WARN | 670→675 页 / sitemap 675 loc / 6 条 hreflang × 675 页 / `BASE` 为空；D14 1 条为 T-36 新页未跟踪告警，人工确认通过 |
| 2026-11-19 | PASS（5 语 / 675 页） | PASS（676 文件 / 1293 内链 / 0 failure） | T-44 文章页宽屏三栏（≥1280px）：左 sticky 目录（JS 从 h2/h3 生成 + 滚动高亮）、中正文、右 sticky 推荐（Related App 卡片 + 相关文章）；新增 `_includes/post-toc-aside.html`、`_includes/post-sidebar.html`，改 post/guide/docs layout + nav `SITE_UI.table_of_contents` + main.js + CSS；窄屏退回单栏、正文内手写 TOC 保留。D03/D05/D06/D09/D11/D17/D18/D19/D20 全通过；75 PASS / 0 FAIL / 0 WARN | 页/sitemap/hreflang 不变（675 / 675 / 6×675）；内链 1292→1293（新增 aside 回链） |
| 2026-11-19 | PASS（5 语 / 675 页；Pagefind 完整） | PASS（676 文件 / 1293 内链 / 0 failure） | 宽屏三栏与侧栏样式连续微调后的全量校验：正文相关文章 4→5 篇与侧栏一致；三栏断点 1400→1580px、正文固定 992px 不收缩、侧栏下限 240/280px；侧栏单按钮半宽靠左；目录基线 1→2px 对齐；容器加宽限定到 `container--wide`，about/tags 恢复 1040px；侧栏 Related Posts 下新增 Tags 区块并补齐五语 `tags_title`。D01–D20 全绿（75 PASS / 0 FAIL / 0 WARN）。**新增 D21 响应式门禁并实测**：375/768/1024/1400/1570/1590/1920 × about/文章/App页/中文文章全部无横向溢出；1570px 侧栏隐藏、1590px 显示且正文 992px / 右栏 280px；普通页容器 1040px；单/双按钮 badge 均 129px 且靠左；目录竖线 2px 对齐 | 页/sitemap/hreflang 不变（675 / 675 / 6×675）；新增 D21 维度（§0 步 5 / §3 / §4 / §8） | 675 / 675 / 6×675；`BASE` 为空 | ✅ 可发布 | — |
| 2026-11-20 | 纯台账状态迁移：A5 Release Notes 中心页（及合并执行的 E3）勾选并从 `SEO-PROGRESS.md` §2 归档至 `SEO_DONE.md` §2；无站点文件改动 | —（未触发构建） | —（未触发构建） | 沿用 2026-11-19 全绿基线（D01–D21）；A5 对应 D20 已验证：55 页 Release Note + App ⇄ Release Note 环链 | 无基线数字变化（675 页 / 1293 内链 / 675 sitemap / 6×675 hreflang） | ✅ 可发布 | — |
| 2026-11-21 | B2 Glossary 升级为「按问题分类的解决中心」（大规模改动）：5 语 `_glossary*` 共 135 术语页改解决意图标题 + 描述 + `app_slug`（4→23 术语×5 语）；5 语 `glossary.md` 索引补 5 个漏列预算术语并按 5 类问题分组（各 22→27 条）；5 语 `_apps*` + Pillar `Related terms` 链接文本同步（各 50 条）+ 记账类补 5 预算术语回链；新增 `_data/glossary_pillars.yml` + 五语 `related_guide` UI 键 + Glossary layout「相关指南」区块 | PASS（5 语 / 675 页；完整构建含 Pagefind） | PASS（676 文件 / 1293 内链 / 0 failure） | D03 术语/App/页面五语一一对应；D05 hreflang 675 页 / sitemap 675 loc；D06 description ≤160（首轮追加方案词超长 78 条已精简至达标，无裸 &）、YAML 有效；D09 MISS=0；D11 内链前缀；D17/D18/D19/D20 全通过；D22 令牌/无硬编码字号字重/共享组件全绿 | 83 PASS / 0 FAIL / 0 WARN（§5 静态脚本） | **结构性模板改动**：新增 `_data/glossary_pillars.yml` 属已批准文件变更，由 Glossary layout 读取并渲染，D14 无红线告警；`where_exp` 按 `lang` + URL 定位 Pillar 页，EN/中文产物分别验证 2 条指南链接正确、带语言前缀 | 页/sitemap/hreflang 不变（675 / 675 / 6×675）；内链 1293 不变（链接文本与分组调整，未新增 URL）；术语索引条目 22→27×5，CTA 覆盖 20→115 页 | D12 完整构建 PASS（快速构建的 FAIL 为已知假阳性，已按 §0 步 2 重跑消除） | ✅ 可发布 | AI 助手 |

> D12 在 `SKIP_PAGEFIND=1` 快速构建下的 FAIL 是已知假阳性，不计入基线；本表只登记完整构建结果。

---

## 9. 维护本文档

以下情况必须回来更新本文档，否则教研会失真：

- 站点结构、集合目录、`exclude`、`permalink` 规则变化；
- 构建脚本、i18n 注入逻辑、CI 流程变化；
- **新增语言**（D03/D04/D05 的判定要扩展为 N 语言）；
- §2.3 任一欠账被修复或新增（同步更新 `BASE` 常量与硬门禁项）；
- 新增了自动校验脚本（把其纳入 §0 步骤，避免两套口径）；
- 教研中发现新的「反复出现但脚本没覆盖」的问题（补进 §3 维度表与 §5 脚本）。
