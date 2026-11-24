# 网站整体教研（全站校验）规范

> **定位**：本站「大规模改动后」的唯一全站验收标准。回答一个问题：**改动之后，整个站点是否仍然正确？**
> **适用站点**：`spacemanmeow.com` 英文站（根路径）+ `/zh/` `/id/` `/th/` `/ms/` 四个子站；Jekyll 4.4、5 语合并构建、GitHub Pages Pages-artifact 部署。
> **触发时机**：见 §1.1。**每次触发都必须完整跑一遍 §0 的八步**，校验结果按维度在对话中输出，不得只做「改了哪一块就只验哪一块」。
> **判定原则**：P0 硬门禁全绿 + WARN 逐条给出人工结论（§1.3）；历史欠账已清零、`BASE` 恒为空，任何欠账回升直接 FAIL（§1.4）。
> **当前基线**：见 §2.1 结构快照；数量为快照非硬阈值，变化须在当次校验输出中解释。不保留历史校验记录，逐次结果见对话输出。
> **关联文档**：`SEO-OPTIMIZATION-PLAN.md`（总览）、`SEO-PLAYBOOK.md`（方法与运营红线）、`SEO-PROGRESS.md`（进度台账）、`SEO-METRICS.md`（月度指标）、`SEO-KEYWORDS.md`（关键词权威库）。本文档不替代它们，只规定「如何整体验收」。

---

## 0. 速查卡：一次完整教研

| 步 | 动作 | 命令 / 入口 | 级别 |
|---|---|---|---|
| 1 | 工作区与文件名红线 | `git status --short`；脚本 `HYGIENE-04` 维度自动检查 | P0 |
| 2 | **完整构建（CI 同款，不带 `SKIP_PAGEFIND`）** | `JEKYLL_ENV=production bash scripts/build.sh` | P0 |
| 3 | 链接与资源校验 | `bundle exec htmlproofer _site --disable-external --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"` | P0 |
| 4 | 一键静态教研（8 维度）+ 性能预算 | `python3 scripts/site_audit.py`（CI `Audit site`）+ `python3 scripts/perf_budget.py`（CI `Perf budget`） | P0 |
| 5 | **响应式布局与样式实测（D12 已自动化）** | `npm run test:visual`（Playwright：375/768/1024/1920 × 首页/应用/文章/FAQ/标签/术语/Docs 共 28 项，CI 同名 `Visual regression (D12)` 步骤）；不再用一次性临时探针 | P0 |
| 6 | 产物与 SEO 产物抽验 | §6 人工抽验项（hreflang / JSON-LD / 内链 / 索引） | P1 |
| 7 | 线上与人工项 | §6（GSC、Rich Results、PSI、外链、真实设备） | P1 |
| 8 | 输出 | 在对话中按维度输出校验项与结果、构建/链接结论及基线数字变化 | P0 |

> 日常小改动（单篇文案、纯错别字）可只跑步 1–4，并用 `SKIP_PAGEFIND=1 bash scripts/build.sh` 加速；**但大规模改动的全站教研必须跑不含 `SKIP_PAGEFIND` 的完整构建**，否则 `BLD-04` Pagefind 索引规则无法验收。
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

单篇文案微调、错别字、纯格式调整。**仍需**跑步 1–4 的构建与链接校验，并在对话中输出这几步的结果。

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

> 数量是快照不是硬阈值。新增文章/术语/语言后数量上升是正常的，但必须在当次校验输出中说明「新增了什么、各语言是否成对」。5 语均已全量交付；任一语言文章数偏差按 `I18N-03`/`I18N-04`「完整 / 分批」规则判定。

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
- `README.md` 已收敛为纯对外站点介绍，不含内部命令/路径；「语言」段与 `_data/languages.yml` 一致由 `I18N-01` 硬规则校验。

### 2.5 基线更新规则

只要修复或新增了 §2.3 任一项，或新增语言 / 集合 / 批量新增内容，**必须同步更新本文档 §2 与 §5 脚本顶部的 `BASE` 常量**，并在当次校验输出中说明变更前后数值。当前 `BASE` 为空，表示所有维度均为硬门禁。

### 2.6 多语言（N 语言）教研规则（2026-11-06 起）

- **语言清单自动发现**：§5 脚本从 `_config_<lang>.yml` 自动构造 `LANGS = ['en', ...]`，新增语言**不需要改脚本**；`i18n_postprocess.py` 亦按 `_site/` 下两位字母目录自动发现，无需改动。
- **完成度分层**：文章数与 EN 相等的语言判为「完整语言」，按一一对应硬门禁；不足者判为「分批建设中」，只要求「无孤立文件（不存在 EN 没有的文件）」并输出 `x/y` 覆盖进度，避免阻塞分批上线。其余三类（应用 / 页面 / 术语）对所有语言均要求无孤立文件。
- **文章骨架全语言对等（2026-11-06 起）**：**所有语言版本**的文章结构、文章目录与图片插入都以 EN 为准——H2/H3 层级与顺序、结构块（表格 / 列表 / 编号步骤 / FAQ / 分隔线）序列、文章目录（TOC 条目数与所在行序）、图片插入行序逐篇与 EN 同名文章一致；不再按本地搜索意图重新组织内容，也不再只要求「H2 ≥ 4 且含 FAQ」的结构下限。纯文本段落可因语言表达做局部调整，关键词按各语言词库优化。由 `I18N-15`~`I18N-18` 逐篇硬校验；依据 `SEO-I18N-PLAYBOOK.md` §1 红线 11 / §3.2 / §3.3 / §3.5。
- **hreflang 条数**：按「去掉语言前缀后的路径」分组，条数 = 组内实际语言数 + 1（x-default）。5 语全部完整后每页固定 6 条（当前分布 `{6: 570}`）；分批建设期间允许 2–5 条并存，**不**要求每页固定为总语言数 + 1。
- **`HYGIENE-04` 白名单**：新增语言源文件属已批准改动，不计入文件名红线告警；EN/ZH 既有文件的增删改仍照常告警。
- **模板通用化**：所有布局/包含按构建级 `site.lang` 动态取集合与前缀（`site[coll]`、`site.data.ui[lang]`），禁止 `zh`-vs-else 二元判断；`page.lang` 不可用于集合选择（非 EN 构建会渲染到 EN 根级页面）。

---

## 3. 校验维度总表

校验规则按 **8 个固定维度**组织，规则 ID 以维度码开头（`BLD-01`、`I18N-05`…）。
`scripts/site_audit.py` 中每个维度对应一个 `check_*()` 函数；新增规则必须写入对应函数，
并同步更新 §4 的同名小节，禁止散落到维度外。

| 维度码 | 维度 | 规则数 | 级别 | 主要手段 | 覆盖范围 |
|---|---|---|---|---|---|
| `BLD` | 构建与产物 | 4 | P0 | 完整构建 + 产物检查 | 语言数 ≥5、feed/robots、Pagefind 索引、临时目录清理 |
| `I18N` | 多语言一致性 | 46 | P0 | 源文件对账 + 产物检查 | README 语言清单、四类文件一一对应、结构页齐备、hreflang/sitemap、XML 良构与注入块唯一、骨架与插图对等、tagline 信息量 |
| `META` | 元数据与结构化数据 | 6 | P0 | frontmatter 解析 + JSON-LD 扫描 | 必填字段、`lang`、`description ≤160`、无裸 `&`、YAML 语法、JSON-LD 无 `&amp;` |
| `CONTENT` | 内容质量与 SEO | 15 | P0 | 正文归一化 + 词库核对 | H2 结构、汉字空格、关键词覆盖、tags 规范、Release Note 五语覆盖、首页数字点、应用页四角度摘要、应用页/文章页权威来源 |
| `LINK` | 链接与导航 | 3 | P0 | 链接扫描 + 模板检查 | 内链语言前缀、Docs 形态入口、App→Release Note 内链 |
| `A11Y` | 可访问性与媒体 | 4 | P0 | 图片引用解析 | `alt` 唯一、无 `![image]`、图片存在、`width` 覆盖防 CLS |
| `DESIGN` | 设计系统与样式一致性 | 8 | P0 | CSS + 全仓源文件扫描 | 字号 6 档、字重 3 档、无硬编码、令牌齐备、分割线无硬编码色、共享 include |
| `HYGIENE` | 运维与清洁度 | 4 | P0/P1 | 产物 + `git status` | 404 不进 sitemap、`seo/` 未发布、无凭据泄漏、文件增删改红线（WARN） |

**脚本外检查**（不由 `site_audit.py` 覆盖，见 §6）：`htmlproofer` 断链（CI `Test site` 步骤）、
D13 合规与产品表述、D16 文档台账一致性。D21 多视口实测已由 D12 的 Playwright 测试固化（见 §0 第 5 步），不再作为脚本外人工项。这些项目也在每次校验的对话输出中逐项写明结论。

---

## 4. 逐维度检查项

> 下列规则 ID 与 `scripts/site_audit.py` 中 `a.chk(...)` / `a.warn(...)` 的第二参数一一对应。
> 每次校验输出按维度分组，逐条打印 `规则ID / PASS|FAIL|WARN / 名称 / 明细`，末尾给汇总。

### 4.1 `BLD` 构建与产物

| 规则 | 检查点 | 合格标准 |
|---|---|---|
| BLD-01 | 语言清单与完成度 | `_config_<lang>.yml` 自动发现，`LANGS >= 5`；报告完整语言与分批中语言 |
| BLD-03 | feed / robots | `_site/feed.xml` 与每语 `<lang>/feed.xml`、`_site/robots.txt` 存在 |
| BLD-04 | Pagefind 索引 | `_site/pagefind/pagefind.js` 存在（**仅完整构建有效**，`SKIP_PAGEFIND=1` 下为已知假阳性） |
| BLD-05 | 临时目录清理 | 无 `.jekyll-<lang>/` 残留 |

### 4.2 `I18N` 多语言一致性

| 规则 | 检查点 | 合格标准 |
|---|---|---|
| I18N-01 | README 语言清单 | `README.md`「语言」段含 `_data/languages.yml` 全部 `label`，数量词与语言数一致 |
| I18N-02 | 集合非空 | 非 EN 各语 `apps`/`gloss` 集合非空，防 `site[coll]` 静默失败 |
| I18N-03/<集合>/<语> | 四类文件一一对应 | 文章 / 应用 / 页面 / 术语：EN 与非 EN 同名集合差集为 0 |
| I18N-04/<集合>/<语> | 分批语言无孤立文件 | 分批中的语言不得有 EN 侧不存在的文件 |
| I18N-05/<语> | 结构页齐备 | 每语含 `index/meow/about/privacy/terms/search/tags/glossary/docs/faq` 共 10 页 |
| I18N-06 | hreflang 块 | 每个产物页含 `i18n-hreflang` 标记 |
| I18N-07 | hreflang en + x-default | 每页同时含 `hreflang="en"` 与 `hreflang="x-default"` |
| I18N-08 | hreflang 条数 | 每页条数在 2 至 `语言数+1` 之间，随组内语言数变化 |
| I18N-09/<语> | 子站自身 alternate | `<lang>/` 下每页含自身 `hreflang="<lang>"` |
| I18N-10/<语> | 子 sitemap 已删 | `<lang>/sitemap.xml` 不存在（统一走合并 sitemap） |
| I18N-11 | 合并 sitemap | `_site/sitemap.xml` 含至少 1 条 `<loc>` |
| I18N-12 | 插图集合与 EN 一致 | 非 EN 文章 `/assets/images/` 路径多重集 = EN 同名文章 |
| I18N-13 | 插图章节锚点 | 每张图「所属第几个 H2 + 该 H2 内第几张」与 EN 同名文章一致（**不用绝对行号**：G18 中文补厚会合法增加行数，但图片所在章节与顺序不变） |
| I18N-14 | alt 本地化 | 非 EN 文章未照抄 EN 的 `alt` 文本 |
| I18N-15 | H2/H3 层级序列 | 与 EN 同名文章一致 |
| I18N-16 | 骨架块序列 | 表格/FAQ/分隔线序列与 EN 一致（**忽略列表项 LI/NUM**：补厚新增的列表属正文内容，不算骨架漂移） |
| I18N-17 | 目录（TOC） | TOC 条目数量与 EN 一致（条目文字随语言不同，行号因补厚可变） |
| I18N-18 | 图片插入锚点 | 与 I18N-13 共享同一检测结果，分别登记 |
| I18N-19 | App tagline 信息量 | 非 EN 长度 ≤ EN 的 1.5×，且不增补 EN 没有的规格数字 |
| I18N-20 | 站点 tagline 宽度 | 显示宽度 `w≤60`（CJK 计 2），非 EN ≤ EN |
| I18N-21 | 合并 sitemap XML 良构 | `xml.etree` 可解析；URL 中 `&` 必须转义为 `&amp;` |
| I18N-22 | x-default 唯一 | 每个 `<url>` 恰好 1 条 `hreflang="x-default"` |
| I18N-23 | hreflang 注入块唯一 | 每页 `i18n-hreflang` 开闭标记各 1 个（重复/缺失均 FAIL） |

### 4.3 `META` 元数据与结构化数据

| 规则 | 检查点 | 合格标准 |
|---|---|---|
| META-01 | frontmatter 必填 | 通用 `title/description`；文章另需 `date/layout/tags/image`；App 需 `icon`；页面需 `permalink`（Release Note 由 CONTENT 单独校验） |
| META-02 | `lang` 字段 | 每文件 `lang` 与所在目录推断的语言一致 |
| META-03 | `description` 长度 | ≤160 字符 |
| META-04 | 无裸 `&` | `description` 中 `&` 须写为 `&amp;` 或 and |
| META-05 | YAML 语法 | Ruby `YAML.parse` 解析全部 frontmatter 无异常；解析器不可用时降级 WARN |
| META-06 | JSON-LD 无 `&amp;` | 产物中所有 `<script type="application/ld+json">` 块不含 HTML 实体 |

### 4.4 `CONTENT` 内容质量与 SEO

| 规则 | 检查点 | 合格标准 |
|---|---|---|
| CONTENT-01 | H2 数量一致 | 完整语言的 H2 数与 EN 同名文章一致 |
| CONTENT-02 | 分批语言结构下限 | H2≥4 且含 `{:.faq-q}` |
| CONTENT-03 | 汉字间空格 | 无汉字之间的多余空格（禁止靠空格做分词） |
| CONTENT-04 | 关键词真实覆盖 | `SEO-KEYWORDS.md` 标「已覆盖」的 11 组词归一化后全部出现在正文 |
| CONTENT-05 | tags 无变体 | 无 `Meow Mood` / `Meow Todo List` / `To Do List` 等非规范产品标签 |
| CONTENT-06 | 规范产品标签 | 每篇文章至少含 1 个 11 App 规范标签之一 |
| CONTENT-07 | Release Note 页覆盖 | 每语 11 App 均有对应 release note 文件 |
| CONTENT-08 | RN frontmatter | 含 `layout/app_slug/app_title/google_play/app_store/lang/title` |
| CONTENT-09 | RN 正文 | 含至少 1 条 `1. xxx` 发布记录 |
| CONTENT-10 | RN 标题本地化 | 含该语「Release Notes」对应词 |
| CONTENT-11 | 无裸 `app_store:` | 空值须写 `app_store: ""`，否则吞掉下一行破坏 hreflang |
| CONTENT-12 | 首页数字点与中文事实 | 五语 `home_intro_p2` 均含带语境数字；中文文章/应用页至少 1 处本地化数字事实 |
| CONTENT-13 | 应用页多角度摘要 | 55 个应用页（11 App × 5 语）均输出 4 个 `app-angles__q` 小标题 |
| CONTENT-14 | 应用页权威来源 | 55 个应用页均输出带年份的官方/标准外链区块 |
| CONTENT-15 | 文章页权威来源 | ≥300 篇文章且 5 语均覆盖；仅关键词命中时挂接，不编造来源 |

### 4.5 `LINK` 链接与导航

| 规则 | 检查点 | 合格标准 |
|---|---|---|
| LINK-01 | 内链语言前缀 | 非 EN 内链以 `/<lang>/` 开头；EN 内链不带其他语言前缀；`/assets/`、`/pagefind/` 豁免 |
| LINK-02 | 形态间入口闭合 | `_data/nav.yml` 含 `nav: docs` 且模板含 `docs-hub` |
| LINK-03 | App→Release Note | `_layouts/app.html` 含 `release-notes/` 内链 |

### 4.6 `A11Y` 可访问性与媒体

| 规则 | 检查点 | 合格标准 |
|---|---|---|
| A11Y-01 | `alt` 唯一 | 同一文件内图片 `alt` 不重复 |
| A11Y-02 | 无 `![image]` | 无占位式图片描述 |
| A11Y-03 | 图片文件存在 | 所有 `/assets/` 引用在本地文件存在 |
| A11Y-04 | `width` 覆盖 | `/assets/` 图片引用全部带 Kramdown `width=` 属性（防 CLS） |

### 4.7 `DESIGN` 设计系统与样式一致性

| 规则 | 检查点 | 合格标准 |
|---|---|---|
| DESIGN-01 | 字号档位 | `--fs-*` 恰为 `sm/base/md/xl/2xl/3xl` 六档 |
| DESIGN-02 | 无硬编码字号 | `main.css` 中 `font-size` 全部走 `var(--fs-*)` |
| DESIGN-03 | 字重档位 | `--fw-*` 恰为 `head/bold/body` 三档 |
| DESIGN-04 | 无硬编码字重 | `main.css` 中 `font-weight` 全部走 `var(--fw-*)` |
| DESIGN-05 | 全仓无硬编码 | CSS/HTML/Liquid/Python/JS 源文件（排除产物与依赖）的内联字号字重也走变量 |
| DESIGN-06 | 令牌齐备 | `--divider-dashed/-solid`、`--space-1/-9`、`--radius-sm/-xl`、`--shadow-card/-soft` 存在 |
| DESIGN-07 | 分割线颜色 | `border*` 无硬编码 hex 颜色，走 `--line`/`--divider-*` |
| DESIGN-08 | 共享组件 | `_includes/store-buttons.html` 存在（下载按钮单一来源） |

### 4.8 `HYGIENE` 运维与清洁度

| 规则 | 检查点 | 合格标准 |
|---|---|---|
| HYGIENE-01 | 404 不进 sitemap | 合并 sitemap 不含 `404` |
| HYGIENE-02 | `seo/` 未发布 | `_site/seo/` 不存在 |
| HYGIENE-03 | 无凭据/缓存泄漏 | `_site/` 下无 `credentials.json`/`token.json`/`pagefind-bin`/`.jekyll-<lang>` |
| HYGIENE-04 | 文件增删改红线 | `git status` 中文章/页面/应用/术语的增删改须人工确认；已批准的语言源变更自动豁免，否则 WARN |

### 4.9 新增规则的正确落位

1. 判断新规则属于哪个维度（上表 8 个之一）；没有合适维度时先申请新增维度并同步脚本注册表与 §3/§4。
2. 在 `scripts/site_audit.py` 对应的 `check_*()` 函数内加 `a.chk('<维度>', '<维度码>-NN', ...)`，ID 序号在本维度内递增。
3. 在本节对应维度表格加一行，写明检查点与合格标准。
4. 若规则涉及产物，先确认 `HAS_SITE` 为真再检查；快速构建假阳性须在 §7 注明，并在当次校验输出中说明。
5. 跑 `python3 scripts/site_audit.py`，确认输出中新规则出现在正确维度分组下。

---

## 5. 一键静态教研脚本

> **单一权威副本**：`scripts/site_audit.py`。本文档不再内嵌脚本；修改门禁只改脚本，CI 与本地跑的是同一份。
> **用法**：在仓库根目录执行 `python3 scripts/site_audit.py`；**执行前先完成一次构建**（否则产物类维度会跳过）。CI 的 `Audit site` 步骤调用同一脚本，出现 `FAIL` 时退出码 1、阻断部署。
> **输出**：按 §3 的 8 个维度分组，逐条打印 `规则ID / PASS|FAIL|WARN / 名称 / 明细`，末尾给各维度小计与总计。
> `PASS` = 硬门禁通过；`FAIL` = 阻塞；`WARN` = 需人工确认（仅 `HYGIENE-04` 出现文件增删改时，不阻断）。
> **维护**：`BASE` 当前为空；若登记新欠账，同步修改脚本顶部 `BASE` 常量与本文档 §2.3。

**输出判读**：先看每个维度的小计，再逐条读 `FAIL`；`FAIL` 必须清零；`BASE` 当前应为空（有值说明登记了新欠账，需对照 §2.3）；`WARN` 项在对话输出中逐条给出人工结论。目标汇总：`{PASS: N, FAIL: 0, WARN: 0}`。

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
| `I18N-07`~`I18N-11` hreflang 少一条 / sitemap 分裂 | 某语言缺同名文件，或 `i18n_postprocess.py` 未执行 | 补对应语言文件；重跑完整构建 |
| `CONTENT-04` 关键词 MISS | 台账标「已覆盖」但词没进正文 | 织入正文/meta/alt，或把状态改回「待覆盖」 |
| `META-03` `description >160` 上升 | 新写入的 description 过长 | 压缩到 ≤160，保留年份与 2–4 个目标词 |
| `A11Y-01` alt 重复 | 批量生成图用了同一 alt | 用「原描述 + 图片文件名对应视图」区分 |
| `CONTENT-03` 汉字间多余空格 | 为逐词匹配硬塞分词空格 | 只删汉字间空格，改用归一化核对 |
| `META-06` JSON-LD 报 `&amp;` | frontmatter 裸 `&` | 改写为 and / 顿号；确认是脚本块内命中而非正文误报 |
| `htmlproofer` 断链（脚本外） | 文件改名、permalink 变化、锚点文字改动 | 恢复文件名或补 301（本站无重定向机制，优先恢复） |
| `HYGIENE-02` `_site/seo/` 出现 | `seo/` 的 `exclude` 被误删，或旧产物残留 | 恢复两份配置的 `seo/` 排除，`rm -rf _site/seo` 后完整重构建 |
| `I18N-15`~`I18N-18` 骨架不一致 | 某语言按本地意图重写正文、漏 / 多列表项、目录增删条目、图片挪位置 | 以 EN 同名文章为骨架补齐或合并结构块，禁止改动 EN 凑一致（§4.2 I18N） |
| `CONTENT-07`~`CONTENT-11` Release Note 空节 / 缺语言 / 标题未本地化 | 日志缺某语言块、译文没进临时日志、`title` 后缀照抄 EN | 补全 5 语译文进日志→重跑生成器→完整构建→复跑审计（§4.4 CONTENT、`skills/release-notes/SKILL.md`） |
| `CONTENT-12`/`CONTENT-13` 数字点或四角度 FAIL | 首页缺带语境数字、`_data/app_angles.yml` 漏 App、布局未输出四标题 | 用应用页已有的真实数字补五语 `home_intro_p2`；核对 App slug 映射并确保 11 App × 5 语均输出四标题→完整构建→复跑审计（§4.4 CONTENT） |
| `CONTENT-14`/`CONTENT-15` 权威来源 FAIL | `_data/authoritative_sources.yml` 缺来源或年份、`_data/app_sources.yml` 漏 App、关键词未命中 | 只补已核验的官方文档/标准及明确年份；核对 App 来源映射与 `content-sources.html` 关键词；完整构建→复跑审计（§4.4 CONTENT） |
| `BLD-04` 在快速构建下 FAIL | `SKIP_PAGEFIND=1` 未生成 Pagefind 索引（已知假阳性） | 用完整 `bash scripts/build.sh` 重构建后复跑，不要在快速构建下当回归修 |
| `DESIGN-02`/`DESIGN-04` 硬编码字号/字重 FAIL | 新增样式直接写 `28px`/`600` 等裸值，或在独立生成器/内联样式里硬编码 | 就近换成标准 `--fs-*`/`--fw-*` 变量；多出的字重档并入 head/bold/body；新令牌需同步 §4.7 与 `:root` |
| `DESIGN-06`/`DESIGN-07` 分割线硬编码颜色 / 令牌缺失 FAIL | 直接写 `border: 1px solid #eee`，或删掉了 `--divider-*`/`--space-*`/`--radius-*`/`--shadow-*` 令牌 | 颜色换成 `--line`/`--divider-*`，补齐缺失令牌；布局专用 px（负 margin、边框宽度）允许保留 |

---

## 8. 维护本文档

以下情况必须回来更新本文档，否则教研会失真：

- 站点结构、集合目录、`exclude`、`permalink` 规则变化；
- 构建脚本、i18n 注入逻辑、CI 流程变化；
- **新增语言**（`I18N-01`~`I18N-11` 的判定自动扩展为 N 语言，无需改脚本）；
- §2.3 任一欠账被修复或新增（同步更新 `BASE` 常量与硬门禁项）；
- 新增了自动校验脚本（把其纳入 §0 步骤，避免两套口径）；
- 教研中发现新的「反复出现但脚本没覆盖」的问题（补进 §3 维度表与 §5 脚本）。
- 校验结果只在对话中输出，不在本文档或其他文件留存记录。
