# SpacemanMeow SEO 进度跟踪（Progress）

> **用途**：跟踪待做项与月度运营计划。**已落地的内容全部归档在 `SEO_DONE.md`（不用于排期）**。方法本身见 `SEO-PLAYBOOK.md`，多语言状态见 `SEO-I18N-PROGRESS.md`（唯一状态源），验收见 `SITE-AUDIT.md`。
> **最后更新**：2026-11-24
> **语言范围**：5 语并行（EN 根 + `/zh/` `/id/` `/ms/` `/th/`，全部全量上线）。所有优化默认全语言同步；新增语言走 `/<lang>/` 子路径、配 hreflang + canonical，URL 不变。
> 状态图例：✅ 已落地　🟢 已完成可发布　🟡 部分落地　♻️ 持续运营中　☐ 待做　⏸️ 暂缓

---

## 0. 阅读说明

- **文档分工**：
  - **`SEO-PROGRESS.md`（本文）**：只管**待做什么**——§2 待做清单是唯一排期依据，§3 是月度滚动节奏。
  - **`SEO_DONE.md`**：只管**已经做了什么**——所有已落地项、已并入门禁项、暂缓项、历月完成记录，供查阅不用于排期。
  - 方法见 `SEO-PLAYBOOK.md`，验收见 `SITE-AUDIT.md`，多语言状态源见 `SEO-I18N-PROGRESS.md`。
- **两类任务**：短期/一次性（技术地基、一次性内容建设，做完即固化，归档到 `SEO_DONE.md`）与长期运营（按月滚动，见 §3）。
- **文档同步范围**：本台账、`SEO_DONE.md` 与 `SEO-OPTIMIZATION-PLAN.md` 只记录**优化方案/措施、进度与规划**；bug 修复、格式/一致性调整不写入。逐次执行明细见 `SITE-AUDIT.md` §8 与 git 提交历史。
- **落地动作**：§2 每完成一项 → 勾选该条 → **把该条移到 `SEO_DONE.md` 对应分组** → 更新 `SITE-AUDIT.md` §8 与 `SEO-METRICS.md` 基线。

---

## 1. 长期运营任务（按月滚动）

| 编号 | 任务 | 分类 | 状态 | 频率 |
|---|---|---|---|---|
| T-18x | Glossary 词条持续扩量 | 内容/AI | ♻️ | 月度 |
| T-17x | 相关文章补全（新文 + 旧文） | 内链 | ♻️ | 月度 |
| T-19x | 更新日志（Release Note，5 语共 55 页已上线，见 D20） | 内容 | ♻️ | 随发版 |
| T-25 | 长尾内容（Best / vs / Alternatives） | 内容 | ♻️ | 月度 |
| T-32 / T-33 | 结构化数据月度校验 / GSC 请求编入索引 | 治理 | ♻️ | 月度 |
---

## 2. 待做清单（后续要做什么，唯一权威）



---

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

- **待推进**：详见 **§2 待做清单**（唯一排期依据）。
- **历月完成记录**：已归档至 `SEO_DONE.md` §6。
- **口径提醒**：GSC 数据仅到 11/15（API 延迟约 3 天），12 月初用同一脚本重导完整 11 月做复盘。

