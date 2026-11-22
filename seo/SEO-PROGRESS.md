# SpacemanMeow SEO 进度跟踪（Progress）

> **用途**：跟踪待做项与月度运营计划。**已落地的内容全部归档在 `SEO_DONE.md`（不用于排期）**。方法本身见 `SEO-PLAYBOOK.md`，多语言状态见 `SEO-I18N-PROGRESS.md`（唯一状态源），验收见 `SITE-AUDIT.md`。
> **最后更新**：2026-11-20
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

> **本节是唯一排期依据**。全部 ☐ 项来自 2026-11 GSC / GoatCounter 实测与技术盘点。
> **数据基线**：2026-11 展现 8280 / 点击 182 / CTR 2.20% / 平均排名 15.7；移动占 73%、chatgpt.com 引荐 3%、`/search` +1000%、Release Notes 55 页近乎零流量；5 个 Glossary 页 1736 展现仅 2 点击。详见 `SEO-METRICS.md`。
> **核心问题**：CTR 3.19%→2.20%、排名 10.3→15.7，主因是大量新页进入 20–60 位 + Glossary 抢到不相关 Head 词。
> **勾选规则**：完成即把 ☐ 改为 ✅ 并把该条移到 `SEO_DONE.md`；新增待办只加在本节。

### 2.A 提升 CTR（P0）

- [ ] **A1 12 月完整 GSC 复测 T-37 / T-38** — GSC 数据仅到 11/15；用 `../skills/seo-research/scripts/gsc_export.py` 重导完整 11 月，判断术语页治理与支柱页标题重写是否提速；结果写回 `SEO-METRICS.md` 与 `SEO_DONE.md`。

### 2.B 提升停留时长（P1）

- [x] **B3 新增 FAQ 问答中心** — 5 语 `/faq/` 中心页已上线，聚合 338 问答/语（App 51 + 文章 287）+ 统一 `FAQPage` schema，博客页眉加入口。（已完成，归档至 `SEO_DONE.md` §2）
- [ ] **B4 结构化对比矩阵页** — 非文章的**表格**形态：11 App 横向对比 + 本站 vs 竞品特征矩阵；易被 Featured Snippet / AI Overview 摘引。
- [ ] **B5 Docs 手册重组为学习路径** — 不写新文章，把 55 篇×5 语按目标重组（「3 天学会记账」「新手上手清单」），提升停留与回访。
- [ ] **B6 场景 / 问题解决页（use-case）** — 「自由职业者怎么记账」「学生如何管理时间」等，意图聚焦、转化路径短于博客。

### 2.C 提升排名与收录（P2）

- [ ] **C1 月度新鲜度机制** — 真实更新 + `dateModified` + IndexNow + GSC 请求编入索引（`SEO-PLAYBOOK.md` §2.4.2 七步），把已建机制滚动执行。
- [ ] **C2 T-32 / T-33 月度巡检** — 结构化数据月度校验 + GSC/Bing 请求索引；建立执行节奏。
- [ ] **C3 待覆盖关键词补齐** — `budgeting app`、`subscription tracker app`、竞品替代词（Expensify / PocketGuard / Goodbudget / EveryDollar）、中文准星竞品专名。`widget catatan keuangan` 因产品口径未定合规挂起，产品确认前不写入。
- [ ] **C4 回填词库数据缺口** — 多组「绝对量待 Play Console / GSC 回填」，回填后才能科学选词。
- [ ] **C5 外部权威建设** — AlternativeTo / Slant / Product Hunt / 相关 subreddit 目录与社区提交；从目录提交低成本切入。
- [ ] **C6 多语言长尾池** — id / th / ms 有曝光但 CTR 低、竞争小于英文；做真正本地化内容（非翻译）作为差异化流量池。
- [ ] **C7 PageSpeed Insights 实测** — 手动跑一次取真实分，建立 LCP / CLS 基线（`SEO-PLAYBOOK.md` §1.5 明确未做）。

### 2.D 技术基建（P0→P2）

**P0（防护性、低成本）**

- [ ] **D1 全站审计脚本落盘 + 接入 CI** — D01–D21 脚本只嵌在 `SITE-AUDIT.md` §5 靠人工复制；CI 只跑 build + htmlproofer。抽出 `scripts/site_audit.py` 作单一权威副本，CI 加 `Audit site` 步骤，文档 §5 改为调用脚本。
- [ ] **D2 锁定依赖版本** — 无 `Gemfile.lock`（被 `.gitignore` 忽略）、Jekyll 仅 `~> 4.4`、插件零约束；提交 lockfile、收紧版本，保证构建可复现。
- [ ] **D3 A11y 键盘与动效** — 补 Skip link、全局 `:focus-visible`（当前 `.search__input:focus` 主动 `outline:none`）、`prefers-reduced-motion`、搜索结果 `aria-live`。
- [ ] **D4 搜索页 XSS 兜底** — `_pages/search.md` 用 `innerHTML` 拼接 Pagefind 结果；改 `textContent` 或转义；商店链接 `rel="noopener"` 统一为 `noopener noreferrer`。

**P1（稳健性与可观测性）**

- [ ] **D5 `i18n_postprocess.py` 解析级加固** — 加注入成功校验、缺 EN 时 x-default 告警、分组质量日志（单语言组 / 缺 EN 组）、XML 转义；纳入 D05。
- [ ] **D6 CWV / 性能门禁** — 先手动 PSI 建基线（同 C7），再在 CI 加轻量性能预算或定期 Lighthouse；图片链路已完备，此项补「度量与门禁」。
- [ ] **D7 错误与 404 监控** — 404 页加分类埋点，定期看 GSC 覆盖率；需要时接轻量错误追踪。
- [ ] **D8 `posts-lastmod-hook.rb` 技术债治理** — 缓存 git log、只对 posts 注册、`||=` 不覆盖手工 `last_modified_at`、路径 shell 转义。

**P2（体验增强）**

- [ ] **D9 PWA 装配** — 192/512 图标已存在但未引用；补 `manifest.json` + `theme-color` + Service Worker。
- [ ] **D10 安全响应头** — GitHub Pages 无法直接发头；经 Cloudflare 前置注入 CSP / HSTS / X-Content-Type-Options / Referrer-Policy。
- [ ] **D11 统一脚本入口** — 加 Makefile 或 package.json scripts，收敛分散在 `scripts/` 与 `skills/` 的 build/serve/test 入口。
- [ ] **D12 视觉回归自动化** — 把 D21 多视口探针固化为 Playwright 测试，替代一次性临时探针。
- [ ] **D13 devcontainer 补 `bundle install`** — `post-create.sh` 的 npm 分支条件永远不成立，本地依赖准备补上。
- [ ] **D14 清理遗留配置** — `.gitmodules` 声明子模块但 CI checkout 注释了 `submodules: true`；`.gitignore` 有 Chirpy 主题残留。

### 2.E 非博客流量资产（长期复利）

> 博客是「写出来才有的流量」，本节是「建一次、长期复利」的资产，多数能直接导向 App 下载。与 A/B 重复的项已标注合并执行。

- [ ] **E1 App 详情页 → 品类权威页** — `meow-money-manager` 已是全站最好页（30 击/465 现），但多数 App 页只是功能+下载按钮；整合品类关键词、场景、FAQ、对比表、截图文本化，11 App × 5 语 = 55 个高意图入口。
- [ ] **E2 Docs → 学习路径** — 同 B5，合并执行，不重复立项。
- [ ] **E4 Glossary → 问题解决中心** — 同 B2，合并执行，不重复立项。
- [ ] **E5 可下载模板 / 资源页** — 预算 CSV 模板、习惯追踪表、清单模板；收藏与外链属性强，自然导流 App。
- [ ] **E6 AI 搜索引用优化** — chatgpt.com 已占 3% 引荐；让内容「可被机器引用」——直接答案前置、`DefinedTerm` / `FAQPage` schema、清晰实体关系；不写更多文章，而是让现有内容被 LLM 摘引。
- [ ] **E7 Google Discover** — 产品更新 + AVIF 图片链路适合 Discover 流；依赖标题质量与时效性。

### 2.F 执行顺序（建议）

1. **第一批**：A1 → A2 → A3（数据复测 + 低 CTR 页与非英语标题重写，最直接的 CTR 杠杆）。
2. **第二批**：D1 → D2 → D3 → D4（把规则从「靠人执行」变成「机器兜底」，不改视觉）。
3. **第三批**：A4 / A5 / B3 / B4（新流量入口与内容形态，每新增形态 ×5 语并入 D11/D19）。
4. **第四批**：B1 / B2 / C1 / C2 / E1 / E6（存量资产放大 + 月度机制滚动）。
5. **持续**：C3–C7、D5–D14、E5 / E7（按月滚动，见 §3）。

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

