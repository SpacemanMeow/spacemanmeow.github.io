# SpacemanMeow SEO 总览

- **[SEO-PLAYBOOK.md](./SEO-PLAYBOOK.md)** —— SEO 方法沉淀手册：系统化、按分类（技术 / 内容 / 内链 / AI 搜索 / 外部权威 / i18n / 治理）归纳可复用的实践方法，每条标注本站落地状态。**用于长期积累 SEO 方法论。**
- **[SEO-PROGRESS.md](./SEO-PROGRESS.md)** —— SEO 进度跟踪：任务总览（区分一次性 / 长期运营）、已落地明细、待做清单、月度运营规划（§4 checklist 化）。**用于看清哪些已做、哪些没做、按计划滚动。**
- **[SEO-METRICS.md](./SEO-METRICS.md)** —— 核心指标月度报告：每月 GSC/GoatCounter 核心趋势表 + 各月详细分析（已拆出独立维护，便于按月滚动更新）。
- **[SEO-KEYWORDS.md](./SEO-KEYWORDS.md)** —— 跨语言关键词权威库：按「语言 × 词层(Head/Middle/Long-tail) × 优先级(P0/P1/P2)」分组排序，含目标页映射与覆盖状态；新文/改文须基于本库优化文案，并随 Google Play Console / GSC 数据月度维护。**用于决定「写什么、怎么写」。**
- **[SITE-AUDIT.md](./SITE-AUDIT.md)** —— 全站整体教研（校验）规范：大规模改动后的唯一验收标准，含 16 个维度、基线快照、一键静态教研脚本与记录表。**用于回答「改动后整站是否仍然正确」。**
- **[SEO-I18N-PLAYBOOK.md](./SEO-I18N-PLAYBOOK.md)** —— 多语言内容扩展标准流程：新增语言或为某 App 补多语言内容时直接按 12 步执行，含不可协商红线、本地关键词 SOP、页面类型全覆盖清单与验收。**后续所有语言扩展按此规范执行，无需重复说明要求。**
- **[SEO-I18N-PROGRESS.md](./SEO-I18N-PROGRESS.md)** —— 多语言扩展唯一状态源：语言矩阵、页面类型覆盖、66 篇 posts 分批清单、校验记录与下一批入口。**用于防止上下文溢出导致内容质量下降或实现方式不一致。**


## 使用方式
1. 想了解「某类 SEO 该怎么做」→ 读 Playbook。
2. 想了解「当前进度 / 本月该做什么 / 填台账」→ 读 Progress。
3. 新落地一项方法：在 Playbook 对应分类补方法 + 在 Progress 标 ✅ 并填日期；长期运营项按月执行 Progress 的 §4.1 清单（并勾选 §4.2 当月规划对应月份），数据复盘同步更新 `SEO-METRICS.md` 月度报告。
4. 大规模改动后要验收整站 → 按 `SITE-AUDIT.md` 完整教研一遍并填写教研记录表。
5. 新增语言 / 为某 App 补多语言内容 → 先读 `SEO-I18N-PLAYBOOK.md` §1 与 §3，再读 `SEO-I18N-PROGRESS.md` 的「当前批次」，按批次执行并回填状态。

## 适用范围与目标
- 站點：spacemanmeow.com 英文站（默认语言）+ `/zh/` 中文站（已上线）+ `/id/` 印尼语站（2026-11-06 完成结构、全部 App / 术语 / 结构页与 Meow Money Manager 首批 6 篇 posts，其余 posts 分批中，见 `SEO-I18N-PROGRESS.md`）+ 后续语言（th/ms/tl/hi 等）。所有方法默认**全语言同步**执行；新增语言走 `/<lang>/` 子路径、配 hreflang 与 canonical，URL 不变、不破既有关联。
- 目标：提升 Google 搜索 + AI 应用内搜索（ChatGPT / Perplexity / Claude / Gemini / Copilot）可见度。

## 状态图例
✅ 已落地　🟡 部分落地　♻️ 持续运营中　☐ 待做
