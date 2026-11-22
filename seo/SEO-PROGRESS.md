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

### 2.D 技术基建（P0→P2）

**P0（防护性、低成本）**

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

### 2.G GEO 体检整改（2026-11-22 首次体检，唯一排期依据）

> **来源**：甲戟 GEO 7 维 29 项体检，总分 55.45/100（C），20 项待整改合并为 14 个可执行任务。方法见 `SEO-PLAYBOOK.md` §4.5，基线数据在 `data/geo/20261122/`（被 gitignore），指标见 `SEO-METRICS.md`。
> **与 E6 的关系**：E6（AI 搜索引用优化）是总目标，本节是它的可执行拆解；完成 GEO 任务即推进 E6，不重复立项。
> **多语言**：标注「5 语」须同步改 5 份文件（`_config*.yml` 或 `_pages/{,zh/,id/,ms/,th/}index.md` / `_apps*`），只改英文会造成 5 语不一致。
> **勾选规则**：完成即改 ✅ 并把该条移到 `SEO_DONE.md` §2；复测方法见 `SEO-PLAYBOOK.md` §4.5。
> **三条红线**：① 正文占比低≠JS 渲染，本站不要做 SSR；② 不编造数据/引用/案例；③ 通用模板的「ICP 备案/工商全称」不适用本站。

**先清小项（10–30 分钟）**

- [ ] **G01 修 WebSite JSON-LD 的 3 处 W3C error** — 5 语 `_config*.yml` 的 `social.links` 相对 URL 改绝对（`jekyll-seo-tag` 把 `/privacy/`、`/terms/`、`mailto:` 塞进 `sameAs`）。验收：`inspect-schema.py` 的 `w3c_validation.summary.errors` 从 3→0。高危。
- [ ] **G02 页脚补主体信息** — `_includes/footer.html` + 5 语 config：团队名、邮箱、更新时间、隐私/条款链接。**去掉 ICP 备案/工商全称**（海外工作室不适用）。验收：页脚四项可见。高危。

**内容骨架（决定 AI 能否转述，第一周）**

- [ ] **G03 首页补正文** — `_layouts/app-list.html` / `_includes/app-card.html`：每款应用补 2-3 句功能细节/场景/差异点，正文约 1300→4000+ 字符。**不做 SSR**。验收：`fetch-page.py` 的 `main_text_chars.raw_chars`≥4000。高危（C4.3/C7.1/C1.4）。
- [ ] **G04 二级标题首段改结论句** — 各 `_apps*/*.md`、`_posts/*.md`：首段「X 是指…/实测…」开头、150–300 字、少代词；优先最差 2 页（`/id/`、`/id/apps/meow-todo-list/`）。验收：抽 3 段遮上下文能独立读懂，`citability.average`≥65（现 18.5）。高危（C7.1/C7.2）。
- [ ] **G05 页面级 FAQ 区块** — `_layouts/app-list.html` / `app.html` 引入已有 `faq-hub.html` + `faq-jsonld.html`，每页 6-10 条真实提问。验收：首页/应用页有 FAQ 且与页内 FAQPage schema 一致。高危（C5.3）。
- [ ] **G06 补数据/事实支撑** — 5 语首页与应用页：把 "beautiful/high-quality" 换成可核对事实（`400+ icons`、`500+ widgets`、`over a decade`），有真实数字才写、没有不编。验收：带语境数字点>0（现 0）。高危（C3.2/C2.3）。
- [ ] **G07 摘要 + 多角度** — `_layouts/app-list.html` / `app.html`：开头 3-5 条要点、结尾结论；每 App 补「适合谁/怎么用/是否免费/有什么限制」四个小标题。验收：疑问链覆盖≥4 类。高危（C4.2/C5.1/C2.2）。

**可信度与解析（第二到四周）**

- [ ] **G08 补权威来源引用** — 5 语内容页：关键论断后补权威链接+年份，禁止编造（现 19 外链全是商店链接）。中（C3.1）。
- [ ] **G09 补一手数据/原创观点** — 5 语应用页/文章：开发取舍、迭代记录、真实场景、作者署名，避免 11 款句式雷同。中（C3.4）。
- [ ] **G10 参数对比表 + 案例** — `_pages/index.md` 或新建 compare 页：11 款应用对比表 + 一个真实案例。验收：页面有 `<table>`（现 0）。中（C5.2/C1.5）。
- [ ] **G11 首页 subtitle 首句给结论** — 5 语 `_pages/index.md` 的 `subtitle`：背景式改为结论式（11 款应用/覆盖品类/免费无广告）。验收：第一句即结论。中（C1.4）。
- [ ] **G13 降关键词密度** — `_layouts/app-list.html`/`app-card.html` 的 "Download" 文案场景化，密度 4.25%→<3%。中（C2.1）。
- [ ] **G16 首页模块骨架重排** — `_layouts/app-list.html`：按「是什么—列表—对比—FAQ—联系」重排（现识别 0 模块）。低（C6.3）。
- [ ] **G17 加载速度** — GitHub Pages 无 gzip 配置入口，重点图片压缩/首屏体积；TTFB 现 1212ms。低、收益最小、最后做（C6.1）。

> G12（语义多样性）、G14（段落自包含）、G15（列表表格）分别随 G03/G07、G04、G10 完成，不单独立项。

### 2.F 执行顺序（建议）

1. **第一批**：A1 → A2 → A3（数据复测 + 低 CTR 页与非英语标题重写，最直接的 CTR 杠杆）。
2. **第二批**：D1 → D2 → D3 → D4（把规则从「靠人执行」变成「机器兜底」，不改视觉）。
3. **第三批**：A4 / A5 / B3 / B4（新流量入口与内容形态，每新增形态 ×5 语并入 D11/D19）。
4. **第四批**：B1 / B2 / C1 / C2 / E1 / E6（存量资产放大 + 月度机制滚动）；**GEO 整改 G01→G02→G03→G04**（G01/G02 十分钟小项先清，再补首页正文与结论句——这是 E6 的具体落地）。
5. **持续**：C3–C7、D5–D14、E5 / E7、G05–G17（按月滚动，见 §3）。

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

