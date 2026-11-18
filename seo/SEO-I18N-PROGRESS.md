# 多语言内容扩展 · 状态源

> **配套规范**：`SEO-I18N-PLAYBOOK.md`（每批开工/收工必读）。本文档是**唯一状态源**：不依赖会话记忆、不依赖上下文是否溢出。
> **关联**：词库 `SEO-KEYWORDS.md`　教研 `SITE-AUDIT.md`　总台账 `SEO-PROGRESS.md`
> **最后更新**：2026-11-18　**校验基准**：2026-11-18 全站教研全绿（675 页 / 1292 内链 / D01–D20 PASS）

## 1. 当前状态（5 语全部全量上线）

| 语言 | 代码 | 子路径 | 状态 | 文章 | App | 结构页 | 术语 | Release Note |
|---|---|---|---|---|---|---|---|---|
| English | `en` | `/` | ✅ 基线 | 70 | 11 | 9 | 27 | 11 |
| 中文 | `zh` | `/zh/` | ✅ 已上线 | 70 | 11 | 9 | 27 | 11 |
| Bahasa Indonesia | `id` | `/id/` | ✅ 已上线 | 70 | 11 | 9 | 27 | 11 |
| 马来语 `ms` | `ms` | `/ms/` | ✅ 已上线 | 70 | 11 | 9 | 27 | 11 |
| 泰语 `th` | `th` | `/th/` | ✅ 已上线 | 70 | 11 | 9 | 27 | 11 |

> 数量为 2026-11-17 文件系统实测；**实测优先于任何台账数字**。5 语文章 / 应用 / 结构页 / 术语 / Release Note 完全对称，由 `SITE-AUDIT.md` D03 / D20 硬门禁校验。
> 获客语言背景：印尼 / 泰国 / 马来搜索展示量占比高，故扩展顺序为 `id` → `th` → `ms`；证据见 `SEO-KEYWORDS.md` 各语言词库。

### 1.1 页面类型覆盖（各语言一致）

首页 App 列表、Meow 系列页、博客分页、关于/隐私/条款、搜索、标签、术语索引 + 定义页、Docs 中心页、11 个 App 详情、Posts、Release Note、feed、合并 sitemap/hreflang、404、导航/UI/语言切换、Pagefind 分片——全部覆盖，逐语言必检项见 `SEO-I18N-PLAYBOOK.md` §4。**任何语言的结构页未达 9/9 不得标 ✅（D03 硬门禁）。**

### 1.2 规范资产（全部完成）

- `seo/SEO-I18N-PLAYBOOK.md`：12 步 SOP、14 条红线、关键词 SOP、页面全覆盖清单、验收、陷阱表。
- `seo/SEO-KEYWORDS.md`：5 语词库（各 App 组 `<语言>` 小节 + 概念词）。
- `seo/SITE-AUDIT.md`：D01–D20、N 语言教研规则、§5 可执行脚本（自动发现语言）。
- `seo/SEO-PROGRESS.md`：总台账。

基础设施（`_config_<lang>.yml`、各 config 的 `exclude`、`_data/{languages,nav,ui}.yml`、`404.html`、`scripts/build.sh`、`scripts/new-language.sh`、按 `site.lang` 动态取值的模板通用化、`i18n.js`）——**全部完成**，逐项修复记录见 `SEO-I18N-PLAYBOOK.md` §7；历史实现日志见 git 提交记录。

## 2. 内容与批次规则

- **分组**：`SEO-KEYWORDS.md` §2.1–§2.11，每个 App 一组（约 6 篇 posts）；结构页与术语与内容同批交付，不后置。
- **新增单篇**：走 `SEO-I18N-PLAYBOOK.md` §3.6——EN 标杆定骨架 → 词库登记借词概念词 → 各语言从 EN 骨架逐行本地化 → glossary 同步 → 校验闭环。
- **新增语言**：走 `SEO-I18N-PLAYBOOK.md` §0 十二步；`scripts/new-language.sh` 生成后必须逐项复核历史坑位（§7），全量构建 + D03/D05/D06。
- **翻译来源**：非 EN 是 EN 同一篇文章的语言版本，骨架 / 目录 / 插图位置必须与 EN 同源同序（D17/D18）；不得按本地搜索意图另写。

## 3. 每批固定动作（开工 / 收工）

**开工前**（从本文档读取，不依赖会话记忆）：
1. 读 `SEO-I18N-PLAYBOOK.md` §1 红线、§3 关键词 SOP；
2. 读本文档「当前状态」与 §5「待办」；
3. 读 `SEO-KEYWORDS.md` 对应 App × 语言小节，确认目标词；
4. 确认 `lang`、内链前缀、front matter 模板与上批一致。

**收工后**：
1. 更新本文档状态表（语言 / 数量 / 覆盖）；
2. 更新 `SEO-KEYWORDS.md` 的「当前覆盖」列与维护日志（若属优化方案/措施）；
3. 跑 `SITE-AUDIT.md` §5 完整构建 + htmlproofer + 教研脚本 + 产物抽验；
4. 更新 `SITE-AUDIT.md` §8 教研记录表（每次必填）；
5. `SEO-PROGRESS.md` 仅在属于优化方案/措施时同步，纯修复不写。

## 4. 校验基线

| 日期 | 构建 | htmlproofer | 教研结果 | 基线数字 |
|---|---|---|---|---|
| 2026-11-12 | PASS（5 语 / 610 页；Pagefind 36145 词） | PASS（611 文件 / 1159 内链 / 0 failure） | 69/69 文章·11/11 应用·8/8 页面·27/27 术语 五语对称；D01–D20 全绿 | 610 页 / sitemap 610 loc / 6 条 hreflang × 610 页 |
| 2026-11-18 | PASS（5 语 / 675 页；Pagefind 37247 词） | PASS（676 文件 / 1292 内链 / 0 failure） | 70/70 文章·11/11 应用·9/9 页面·27/27 术语 五语对称；D01–D20 PASS | 675 页 / sitemap 675 loc / 6 条 hreflang × 675 页 |

逐次执行记录（Phase 0–5、G1–G11 分批、th/ms 全量等）见 `SITE-AUDIT.md` §8 与 git 提交历史，不在本文档逐批留存。**D12 在 `SKIP_PAGEFIND=1` 快速构建下 FAIL 是已知假阳性，不计入基线。**

## 5. 待办 / 阻塞 / 风险

- **待办**：核实 `widget catatan keuangan` 产品口径后决定落地或删除词条。
- **阻塞**：无。
- **风险**：所有语言一律以 EN 骨架为准，由 D18 逐篇硬校验；新增语言沿用同套流程。Pagefind 对 zh / th / ms 不支持 stemming（仅影响词形召回，不阻断发布）。
