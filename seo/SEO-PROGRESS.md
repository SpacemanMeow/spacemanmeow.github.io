# SpacemanMeow SEO 进度跟踪（Progress）

> **用途**：跟踪每条 SEO 方法的落地状态、待做项与月度运营计划。方法本身见 `SEO-PLAYBOOK.md`，多语言状态见 `SEO-I18N-PROGRESS.md`（唯一状态源），验收见 `SITE-AUDIT.md`。
> **最后更新**：2026-11-17
> **语言范围**：5 语并行（EN 根 + `/zh/` `/id/` `/ms/` `/th/`，全部全量上线）。所有优化默认全语言同步；新增语言走 `/<lang>/` 子路径、配 hreflang + canonical，URL 不变。
> 状态图例：✅ 已落地　🟢 已完成可发布　🟡 部分落地　♻️ 持续运营中　☐ 待做

---

## 0. 阅读说明

- **两类任务**：短期/一次性（技术地基、一次性内容建设，做完即固化）与长期运营（按月滚动，见 §4）。
- **文档同步范围**：本台账与 `SEO-OPTIMIZATION-PLAN.md` 只记录**优化方案/措施、进度与规划**；bug 修复、格式/一致性调整不写入。逐次执行明细见 `SITE-AUDIT.md` §8 与 git 提交历史，本文件不重复堆砌流水。

## 1. 任务总览

### 1.A 技术地基 / 一次性内容（全部完成）

| 编号 | 任务 | 分类 | 状态 | 完成 |
|---|---|---|---|---|
| T-01～T-03 | sitemap / robots / GSC 验证提交 | 技术 | ✅ | 2026-10 |
| T-04～T-08 | app description / JSON-LD（SoftwareApplication、FAQPage、Breadcrumb、BlogPosting） | 技术/内容 | ✅ | 2026-10 |
| T-09～T-13 | alt 关键词化去重 / canonical / OG 图 / CWV 首屏懒加载 / 提交 feed | 技术 | ✅ | 2026-10 |
| T-14～T-17 | App Guides 回链 / tags 聚合 / 相关文章区块 | 内链 | ✅ | 2026-10 |
| T-18 | Glossary 词汇页（现 27 条/语言） | 内容/AI | ✅ | 2026-10 起持续 |
| T-19～T-20 | Pillar 新鲜度时间戳 / 404 + 站内搜索（Pagefind 5 语分片） | 内容/体验 | ✅ | 2026-10～11 |
| T-23～T-24 | Bing WMT / IndexNow 自动提交 | 技术/AI | ✅ | 2026-10 |
| T-34 | 既有文章人工审核与完善（10 组全量复核完毕） | 内容质量 | ✅ | 2026-11-05 |

> 逐任务执行记录（含每组的关键词命中数、升权词、alt 去重数等）见 git 历史与 `SITE-AUDIT.md` §8；数量口径以文件系统实测为准。

### 1.B 长期运营任务（按月滚动）

| 编号 | 任务 | 分类 | 状态 | 频率 |
|---|---|---|---|---|
| T-18x | Glossary 词条持续扩量 | 内容/AI | ♻️ | 月度 |
| T-17x | 相关文章补全（新文 + 旧文） | 内链 | ♻️ | 月度 |
| T-19x | 更新日志（Release Note，5 语共 55 页已上线，见 D20） | 内容 | ♻️ | 随发版 |
| T-25 | 长尾内容（Best / vs / Alternatives） | 内容 | ♻️ | 月度 |
| T-32 / T-33 | 结构化数据月度校验 / GSC 请求编入索引 | 治理 | ♻️ | 月度 |
| T-21 | 外链 / roundup 投稿 | 权威 | ☐ | 季度 |
| T-22b | BlogPosting dateModified / author 细化 | 结构化 | ☐ | 规划 |
| T-29 | 图片再优化（AVIF / srcset 预载） | 性能 | ☐ | 规划 |
| T-30 | App 内官网链接加 UTM（App 侧） | 度量 | ☐ | 规划 |
| T-31 | 新增语言（`tl` / `hi` 等；id/th/ms 已全部交付） | 扩张 | ☐ | 按数据排期 |

## 2. 待做 / 候选优化清单

| 编号 | 优化项 | 分类 | 谁做 | ROI | 状态 |
|---|---|---|---|---|---|
| T-21 | 外链 / roundup 投稿（Product Hunt / alternative.to / 少数派） | 权威 | 手动 | 高 | ☐ |
| T-22b | BlogPosting dateModified / author 细化 | 结构化 | 站内 | 中 | ☐ |
| T-29 | 图片再优化（AVIF / srcset / 预载） | 性能 | 站内 | 中 | ☐ |
| T-30 | App 内官网链接加 UTM | 度量 | App 侧 | 中 | ☐ |
| T-31 | 新增语言（tl / hi） | 扩张 | 站内+人工 | 中 | ☐ 按获客数据排期 |

> 已并入 D11/D19 硬门禁、不再列为待做：T-26（Glossary FAQPage 随结构化数据维护）、T-27（标签一致性由 D19 校验）、T-28（Glossary⇄App 回链由 D11 校验）。
> **建议节奏**：先 T-29（低成本性能）→ T-21（季度外部杠杆）→ T-31（验证后扩语种）。

## 3. 月度长期运营规划

### 3.1 月度固定清单（Monthly Checklist）

**A. 技术巡检（每月第 1 周）**
- [ ] 按 `SITE-AUDIT.md` §0 完整构建 + htmlproofer，死链 / 锚点 / 图片全绿；跑 §5 教研脚本 FAIL=0
- [ ] 确认 sitemap.xml 更新、GSC 无抓取错误
- [ ] Rich Results Test 抽验 1–2 个 app 页 JSON-LD（T-32）
- [ ] PageSpeed Insights 抽 2 核心页，LCP / CLS 无回退

**B. 内容产出（全月配额）**
- [ ] Glossary 词条 ≥ 2 条（T-18x）
- [ ] 相关文章补全：当月新文 + 至少 3 篇旧文（T-17x）
- [ ] 长尾内容 ≥ 2 篇（Best / vs / Alternatives，T-25）

**C. 内链与权威**
- [ ] 新文章确认纳入 App 页回链（`image:` == 对应 App `icon`）
- [ ] 外链铺垫：月度物色 1–2 投稿目标（T-21 季度集中执行）

**D. 数据复盘（月末）**
- [ ] 更新 `SEO-METRICS.md`（`../skills/seo-research/scripts/gsc_export.py` 拉数 → 趋势表 + 月份分析）
- [ ] GSC 对当月新页与重大改版页「请求编入索引」（T-33）
- [ ] 复盘 CTR 偏低页 → 优化 `<title>` / `description`

### 3.2 当月规划

- **2026-11**（已完成，详见 `SITE-AUDIT.md` §8）：5 语预算对比文、习惯机制深对比文、清单应用深对比文三批 5 语发布；id/th/ms 全量交付收尾；文章达 69/语、术语 27/语；Release Note 55 页上线；`page.lang` 与 GSC 输出路径等口径修正。
- **待推进**：`money tracker` 独立支柱页（T-36，App 第一搜索词，当前仅在 App 集群顺带覆盖）；`widget catatan keuangan` 产品口径核实；T-21 外链投稿。
