# SpacemanMeow SEO 进度跟踪（Progress）

> **用途**：跟踪每条 SEO 方法的落地状态、待做项与月度运营计划。方法本身见 `SEO-PLAYBOOK.md`，多语言状态见 `SEO-I18N-PROGRESS.md`（唯一状态源），验收见 `SITE-AUDIT.md`。
> **最后更新**：2026-11-18
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
| T-22b | BlogPosting dateModified / author 细化 | 结构化 | ✅ 2026-11-18 | 已落地 |
| T-29 | 图片再优化（AVIF / srcset 预载） | 性能 | ✅ 2026-11-18 | 已落地 |

## 2. 待做 / 候选优化清单

| 编号 | 优化项 | 分类 | 谁做 | ROI | 状态 |
|---|---|---|---|---|---|
| T-22b | BlogPosting dateModified / author 细化：统一 include 输出 `datePublished` / `dateModified` / author，关闭 seo-tag 重复 BlogPosting | 结构化 | 站内 | 中 | ✅ 2026-11-18 |
| T-29 | 图片再优化（AVIF / srcset / 预载）：构建生成 AVIF 缩略图，卡片/首图用 `picture`，首图 `link rel=preload` | 性能 | 站内 | 中 | ✅ 2026-11-18 |
| T-36 | `money tracker` 独立支柱页：5 语同骨架上线，词库标 `已覆盖(pillar-money-tracker)` | 内容 | 站内 | 中 | ✅ 2026-11-18 |
| T-37 | 治理 Glossary 高曝光零点击词（约 1736 现/2 击）：4 个高曝光术语 × 5 语补 `app_slug`，glossary layout 加「解决方案」导流区（工具/手册/App），交还 Pillar/App 主吃；`one ui` 等无关 Head 词停扩 | 内容/CTR | 站内 | 高（P0） | ✅ 2026-11-18 |
| T-38 | 按 GSC 实测词重写低 CTR 支柱页 title/description：CPU 温度页强化 `cpu temperature monitor` / 2026 / CPU-Z alternative，小组件页强化 `best widget apps for android` / custom widgets / KWGT alternative；5 语同步，URL 与正文骨架不变 | 内容/CTR | 站内 | 高（P0） | ✅ 2026-11-18 |
| T-39 | 非英语 CTR 与 hreflang：id/th 4 个高曝光术语 × 2 语把定义式标题改为本地词 + 解决意图标题；hreflang 全站复核成环，关键词沿用 `SEO-KEYWORDS.md` 本地词表 | i18n/CTR | 站内 | 中高（P1） | ✅ 2026-11-18 |
| T-40 | 复制已验证内容模式「竞品替代 + 平台限定 + 2026 年度词」，不再用 Glossary 硬打 Head 大词 | 内容 | 站内 | 中高（P1） | ♻️ 延续 T-25 |
| T-41 | AI 搜索与移动优先：Glossary 加 `DefinedTerm` JSON-LD；解决方案 CTA 改为移动端友好卡片/按钮；新支柱页沿用移动优先内链与清晰 CTA（手机 73%、GSC mobile CTR 3.1% vs desktop 1.0%） | AI/体验 | 站内 | 中（P2） | ✅ 2026-11-18 |
| T-42 | Docs 区：55 篇 tutorial（11×5）改 layout 为 `docs` + `/docs/` 中心页 × 5 + 导航入口，URL 不变、不新建集合 | 内容/内链 | 站内 | 高 | ✅ 2026-11-18 详见 `CONTENT-HUB-PLAN.md` |
| T-43 | 在线工具：暂缓，不落地工具内容与页面（2026-11-18 用户决定先删除已落地的工具形态，后续视数据再议） | 内容/工具 | 站内 | — | ⏸️ 暂缓 |

> 已并入 D11/D19 硬门禁、不再列为待做：T-26（Glossary FAQPage 随结构化数据维护）、T-27（标签一致性由 D19 校验）、T-28（Glossary⇄App 回链由 D11 校验）。
> **建议节奏（11 月复盘后重排）**：**P0** T-37 / T-38 已完成，待 12 月 GSC 复测 → **P1** T-39 / T-40 已完成或持续执行（i18n 承接 + 已验证内容模式；T-42 Docs 形态已落地，执行见 `CONTENT-HUB-PLAN.md`；T-43 在线工具暂缓）→ **P2** T-41（AI/移动）与 T-22b / T-29 / T-36 均已在本批落地。详见 `SEO-METRICS.md` 2026-11。

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

**D. 数据复盘（月末）**
- [ ] 更新 `SEO-METRICS.md`（`../skills/seo-research/scripts/gsc_export.py` 拉数 → 趋势表 + 月份分析）
- [ ] GSC 对当月新页与重大改版页「请求编入索引」（T-33）
- [ ] 复盘 CTR 偏低页 → 优化 `<title>` / `description`

### 3.2 当月规划

- **2026-11**（已完成，详见 `SITE-AUDIT.md` §8）：5 语预算对比文、习惯机制深对比文、清单应用深对比文三批 5 语发布；id/th/ms 全量交付收尾；文章达 69/语、术语 27/语；Release Note 55 页上线；`page.lang` 与 GSC 输出路径等口径修正。
- **待推进（11 月数据复盘后，优化项明细与编号见 §2，数据详见 `SEO-METRICS.md` 2026-11）**：
  - **P0**：T-37 术语页曝光治理、T-38 低 CTR 支柱页 5 语 title/description 重写均已完成，待 12 月 GSC 复测。
  - **P1**：T-39 id/th 本地化标题与 hreflang 复核完成，T-40 复制已验证内容模式（竞品替代 + 平台限定 + 2026）持续执行。
  - **P2**：T-41 AI 搜索与移动优先（chatgpt.com 引荐 3%、GSC mobile CTR 是 desktop 的 3 倍）。
  - **排期项**：T-29 性能、T-36 `money tracker` 支柱页、`widget catatan keuangan` 产品口径核实。
  - **口径提醒**：GSC 数据仅到 11/15（API 延迟约 3 天），12 月初用同一脚本重导完整 11 月做复盘。
- **内容形式规划（长期获流量，除文章/应用页外，按优先级）**：
  - **第一梯队｜已有资产改造（ROI 最高）**
    - **Glossary 术语表**：11 月已验证需求（约 1736 展现仅 2 点击）。定义型词不随热点衰减、AI 引用友好；标题/描述补解决方案词 + 明确产品 CTA + Pillar/App 互链，复用已有 FAQPage schema。
    - **Release Notes 更新日志**：55 页（11 App × 5 语）目前近乎零流量。做结构化 changelog 中心页 + 每版本独立可索引 + App⇄Release Note 环链，吃「品牌 + 版本 + 新功能」长尾与更新带来的新鲜度信号。
    - **标签 / 主题聚合页**：`/search` 访问 +1000% 说明用户有探索需求但缺聚合入口；把 tags 做成「主题中心」承接中词并导向对应 App。
  - **第二梯队｜值得新增的静态站友好形式**
    - **结构化对比矩阵页**（非文章）：如「7 款记账 App 功能对照表」，比对比文章更易拿 featured snippet 与 AI 引用；复用 5 语模板。
    - **独立 FAQ 问答页**：基于 Glossary 扩展为「问题 → 简短答案 → 产品入口」，复用 FAQPage schema，承接 `what is / how to / which app` 类查询。
    - **可下载资源 / 模板页**：预算 CSV 模板、习惯追踪表、清单模板等；收藏与外链属性强，自然导流到对应 App。
    - **场景 / 问题解决页（use-case）**：如「学生怎么记账」「手机发热怎么办」，竞争小、意图精准、生命周期长。
  - **第三梯队｜暂缓**：榜单目录页（薄内容风险）、年度数据报告（外链 magnet 但维护成本高）、视频 / 播客（静态站不适配）。
  - **执行顺序**：Glossary 改造 → Release Notes 中心页 → FAQ / 对比矩阵 → 模板资源。每新增一种形式要 ×5 语言，优先复用现有集合（`_glossary*` / `_release_notes*` / `_pages*`）与模板；非英语骨架与 EN 同序、内链带 `/<lang>/` 前缀、hreflang 成环，并入 D11/D19 门禁。
