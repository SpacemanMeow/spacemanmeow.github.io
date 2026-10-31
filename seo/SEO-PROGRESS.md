# SpacemanMeow SEO 进度跟踪（Progress）

> **用途**：跟踪每条 SEO 方法的落地状态、月度运营计划与进度台账。方法本身见 `SEO-PLAYBOOK.md`。
> **最后更新**：2026-10-30
> **语言范围**：英文站（默认）+ `/zh/` 中文站（已上线）+ 后续可扩展其他语言（id/ms/tl/hi 等）。所有优化默认全语言同步；新增语言走 `/<lang>/` 子路径、配 hreflang + canonical，URL 不变。
> 状态图例：✅ 已落地　🟡 部分落地　♻️ 持续运营中　☐ 待做

---

## 0. 阅读说明
- **两类任务**：
  - **短期 / 一次性**：技术地基、一次性内容建设（做完即固化）。
  - **长期运营**：需按月滚动的内容/权威/数据动作（见 §4 月度计划）。
- 已落地任务明细（§2）保留完整执行记录，便于回溯；待做项（§3）直接取自 Playbook 分类。

---

## 1. 任务总览（按分类 + 类型 + 状态）

### 1.A 短期 / 一次性任务
| 编号 | 任务 | 分类 | 状态 | 完成日期 | 备注 |
|---|---|---|---|---|---|
| T-01 | jekyll-sitemap 生成 sitemap.xml | 技术 | ✅ | 2026-10-10 | |
| T-02 | robots.txt | 技术 | ✅ | 2026-10-10 | |
| T-03 | GSC 验证 + 提交 sitemap | 技术 | ✅ | 2026-10-10 | |
| T-04 | 11 app 补 description | 内容 | ✅ | 2026-10-10 | |
| T-05 | SoftwareApplication JSON-LD | 技术 | ✅ | 2026-10-10 | |
| T-06 | FAQPage JSON-LD + 可见 FAQ | 技术 | ✅ | 2026-10-10 | 11 页 4 问 |
| T-07 | BreadcrumbList JSON-LD | 技术 | ✅ | 2026-10-10 | |
| T-08 | BlogPosting/Article JSON-LD | 技术 | ✅ | 2026-10-10 | |
| T-09 | 图片 alt 关键词化 + 差异化 0 重复 | 技术 | ✅ | 2026-10-18 | 839 处 |
| T-10 | canonical 生效 | 技术 | ✅ | 2026-10-10 | |
| T-11 | hreflang 双向 + `<html lang>` | 技术/i18n | ✅ | 2026-10-30 | `/zh/` 上线 |
| T-12 | OG/Twitter 图按 app 区分 | 技术 | ✅ | 2026-10-10 | |
| T-13 | Core Web Vitals 审计 + 首屏懒加载修正 | 技术 | ✅ | 2026-10-30 | PSI 实时分待手动取 |
| T-14 | App 页 Guides 回链区块 | 内链 | ✅ | 2026-10-18 | |
| T-15 | /tags/ 聚合页 + 标签可点击 | 内链 | ✅ | 2026-10-18 | 81 组 |
| T-16 | 提交 feed.xml 到 GSC/Bing | 技术 | ✅ | 2026-10-30 | 提交步骤见 §2 |
| T-17 | 文章底部「相关文章」区块 | 内链 | ✅ | 2026-10-30 | 自动化 |
| T-18 | Glossary 词汇页（16 条/语言） | 内容/AI | ✅ | 2026-10-30 | |
| T-19 | Pillar 新鲜度时间戳 | 内容 | ✅ | 2026-10-30 | 独立 changelog 待 Q1 |
| T-20 | 404 页 + 站内搜索 | 体验 | ✅ | 2026-10-30 | |
| T-23 | Bing WMT 验证 + sitemap | 技术/AI | ✅ | 2026-10-30 | |
| T-24 | IndexNow 自动提交 | 技术/AI | ✅ | 2026-10-30 | deploy 后 ping |

### 1.B 长期运营任务（需月度滚动）
| 编号 | 任务 | 分类 | 状态 | 频率 | 备注 |
|---|---|---|---|---|---|
| T-18x | Glossary 词条持续扩量（≥2 条/月） | 内容/AI | ♻️ | 月度 | 已 16 条/语言，持续增 |
| T-17x | 相关文章补全（新文 + 旧文） | 内链 | ♻️ | 月度 | |
| T-19x | 更新日志/版本博客（≥1 篇/月） | 内容 | ♻️ | 月度 | 常态化新鲜度 |
| T-25 | 长尾内容 ≥2 篇/月（Best/vs/Alternatives） | 内容 | ♻️ | 月度 | |
| T-21 | 外链 / roundup 投稿 | 权威 | ☐ | 季度集中 | 手动排期 |
| T-22b | BlogPosting dateModified / author 细化 | 技术 | ☐ | Q2 2027 | |
| T-26 | Glossary 定义页加 FAQPage JSON-LD | 结构化 | ☐ | 待做 | AI 易引用 |
| T-27 | 标签词表归并 | 内链 | ☐ | 待做 | |
| T-28 | Glossary→App 反向回链 + 面包屑 | 内链 | ☐ | 待做 | |
| T-29 | 图片再优化（AVIF/srcset/预载） | 性能 | ☐ | 待做 | |
| T-30 | App 内官网链接加 UTM | 度量 | ☐ | 待做 | App 侧 |
| T-31 | 其他语种试点（id/ms/tl/hi） | 扩张 | ☐ | 待评估 | 需 ZH 数据 |
| T-32 | 结构化数据月度校验 | 治理 | ♻️ | 月度 | |
| T-33 | GSC/Bing 月度「请求编入索引」 | 治理 | ♻️ | 月度 | |
| T-34 | 既有文章人工审核与完善（`_posts` 批量生成文） | 内容质量 | ☐ | 持续（多月） | 逐批审完整度/准确性；纳入 §4.1 E |

---

## 2. 已落地任务明细（执行记录）

| 编号 | 任务 | 完成日期 | 执行记录 |
|---|---|---|---|
| T-01 | sitemap.xml | 2026-10-10 | jekyll-sitemap 原已在 ../Gemfile 与 ../_config.yml；修正 `url` 为 `https://spacemanmeow.com`（原误用 github.io），本地构建已生成 |
| T-02 | robots.txt | 2026-10-10 | 根目录创建，Allow 全站并指向 sitemap |
| T-03 | GSC 验证+提交 | 2026-10-10 | 用户已完成验证并线上提交；「无法抓取」为 SC 状态延迟，72h 后自动转成功 |
| T-04 | app description | 2026-10-10 | 11 app 加 150–160 字符含主词 description |
| T-05 | SoftwareApplication | 2026-10-10 | 新增 `_includes/app-jsonld.html` 接 `app.html`；11 页 JSON 合法 |
| T-06 | FAQPage + FAQ | 2026-10-10 | 11 app 加 `faq:` 4 问/页；`app.html` 渲染可见 FAQ；薄弱集群后增至 6 问（T-22） |
| T-07 | BreadcrumbList | 2026-10-10 | 新增 `_includes/breadcrumb-jsonld.html` 接 `default.html`；18 个非首页页含 |
| T-08 | BlogPosting | 2026-10-10 | jekyll-seo-tag 自动输出；修作者 URL 旧域名 github.io→spacemanmeow.com |
| T-09 | 图片 alt | 2026-10-18 | 839 处规范化为「{专名} screenshot: {小标题} — {标题}」；专名大小写修正；同文件重复 0；791 张带 width 防 CLS；`![image]` 零残留 |
| T-10 | canonical | 2026-10-10 | seo-tag 输出 `<link rel="canonical" href="https://spacemanmeow.com/...">` |
| T-11 | hreflang | 2026-10-30 | `/zh/` 上线后构建注入 en/zh 双向 hreflang（每页 3 条 alternate）；`<html lang>` 自动输出 |
| T-12 | OG/Twitter 图 | 2026-10-10 | 11 app 加 `image:` 取各自 icon.webp；独立 og:image/twitter:image |
| T-13 | CWV 审计 | 2026-10-30 | 审计全站懒加载：详情页 hero 商店徽章、列表首卡图标改 eager（原首屏却 lazy 伤 LCP）；页脚/卡内徽章保留 lazy；均 WebP、无自定义字体。PSI API 限流未取得实时分 |
| T-14 | Guides 回链 | 2026-10-18 | `app.html`+`main.css` 按 `post.image==app.icon` 列该 app 6 篇相关文章；11 app 全生效 |
| T-15 | /tags/ 聚合 | 2026-10-18 | `_pages/tags.md` 原生 81 组索引 + 文章底部 tag 可点击 + 44 篇 guide 补四层标签；死锚点 0，htmlproofer 绿 |
| T-16 | feed.xml 提交 | 2026-10-30 | EN `feed.xml` 在线；ZH 因路径问题未产出，修正 `../_config_zh.yml` 的 `feed.path` 为 `zh/feed.xml` 后 EN/ZH 各 10 条 entry。提交步骤（手动）：GSC「Sitemaps」粘贴 feed URL；Bing WMT 同理 |
| T-17 | 相关文章 | 2026-10-30 | `_includes/related-posts.html` 按标签重叠取同语言最多 4 篇 + 父 app 回链，接 `post.html`/`guide.html`；中英同步；原 20 篇手写区块已清理 |
| T-18 | Glossary | 2026-10-30 | `glossary`/`glossary_zh` 集合 + `_layouts/glossary.html`；16 定义页/语言 + 索引页（EN/ZH 各 `/glossary/`、`/zh/glossary/`），进 sitemap + 双向 hreflang；10 个相关 app 页加「相关术语」回链；博客顶加「词汇表」入口。中英同步 |
| T-19 | 新鲜度时间戳 | 2026-10-30 | 11 Pillar 页（EN+ZH 共 22 篇）加 `last_modified_at: 2026-10-30`，`post.html` 渲染 "Last updated/最后更新"。独立 changelog 页留 Q1 2027 |
| T-20 | 404 + 搜索 | 2026-10-30 | 根 `404.html` 双语；Pagefind 扩展版 EN/ZH 独立索引（含中文分词）；导航加搜索入口 |
| T-23 | Bing WMT | 2026-10-30 | 用户添加 `spacemanmeow.com` 并导入 GSC 验证；提交 sitemap。前置：`../_config.yml` 配 `webmaster_verifications.bing`，每页输出 `msvalidate.01` meta |
| T-24 | IndexNow | 2026-10-30 | 根加 `../indexnow-key.txt`（key `d8564afe6a7d6a287d4b47b6296b1b15`）；`../.github/workflows/pages-deploy.yml` deploy 后 ping `api.indexnow.org` 提交全量 ~190 URL；`continue-on-error` 容错 |

**已知问题与修复**
- seo-tag 误判 + 非法 JSON：原把无日期页填构建时间当 `date` 误标 `BlogPosting`，且 `&`→`&amp;` 塞进 JSON-LD 致 Google 丢弃。修复：含 `&` 处改 `and`；apps/隐私/条款加 `seo.type: WebPage`。构建校验：全站 JSON-LD 无 `&amp;`，app 页 `@type` 为 `WebPage`+`SoftwareApplication`+`FAQPage`+`BreadcrumbList`。
- `url` 已从 github.io 改为 spacemanmeow.com，线上 canonical/sitemap 均为该域名。

---

## 3. 待做 / 候选优化清单（滚动维护）
> 来源：Playbook 各分类标 ☐ 的项。每条标注类型 / 谁来做 / ROI。

| 编号 | 优化项 | 分类 | 谁来做 | ROI | 状态 |
|---|---|---|---|---|---|
| T-21 | 外链/roundup 投稿（Product Hunt/alternative.to/少数派） | 权威 | 手动 | 高 | ☐ |
| T-22b | BlogPosting dateModified / author 细化 | 结构化 | 站内 | 中 | ☐（Q2 2027） |
| T-26 | Glossary 定义页加 FAQPage JSON-LD | 结构化 | 站内 | 高 | ☐（AI 易引用） |
| T-27 | 标签词表归并 | 内链 | 站内 | 中 | ☐ |
| T-28 | Glossary→App 反向回链 + 面包屑 | 内链 | 站内 | 中 | ☐ |
| T-29 | 图片再优化（AVIF/srcset/预载） | 性能 | 站内 | 中 | ☐ |
| T-30 | App 内官网链接加 UTM | 度量 | App 侧 | 中 | ☐ |
| T-31 | 其他语种试点（id/ms/tl/hi） | 扩张 | 站内+人工 | 待评估 | ☐（需 ZH 数据） |
| T-32 | 结构化数据月度校验 | 治理 | 站内 | 中 | ♻️ 月度 |
| T-33 | GSC/Bing 月度「请求编入索引」 | 治理 | 手动 | 中 | ♻️ 月度 |
| T-34 | 既有文章人工审核与完善（`_posts` 批量生成文，逐批审） | 内容质量 | 人工 | 中-高 | ☐（多月） |

**建议节奏**：先 T-26（Glossary FAQPage，站内高 ROI）→ T-27/29（低成本补完）→ T-21（季度外部杠杆）→ T-31（验证后扩语种）。

## 4. 月度长期运营规划

### 4.1 月度固定清单（Monthly Checklist）
**A. 技术巡检（每月第 1 周，约 1h）**
- [ ] `bundle exec jekyll build` + htmlproofer，死链/锚点/图片全绿
- [ ] 确认 sitemap.xml 更新、GSC 无抓取错误
- [ ] Rich Results Test 抽验 1–2 个 app 页 JSON-LD 合法（T-32）
- [ ] PageSpeed Insights 抽 2 核心页，LCP/CLS 无回退

**B. 内容产出（全月配额，可累积）**
- [ ] **Glossary 词条 ≥ 2 条**（T-18x）：what is … 类，AI 搜索最爱
- [ ] **相关文章补全**：当月新文 + 至少 3 篇旧文补 Related posts（T-17x）
- [ ] **更新日志 / 版本博客 ≥ 1 篇**（T-19x）
- [ ] **新长尾内容 ≥ 2 篇**：Best-X-for-Y / vs / Alternatives 补薄弱品类（T-25）

**C. 内链与权威**
- [ ] 新文章确认纳入 app 页回链（检查 `image:` == 对应 app `icon`）
- [ ] 外链铺垫（季度集中执行，月度物色 1–2 投稿目标）

**D. 数据复盘（月末，约 1h）**
- [ ] 更新 **[SEO-METRICS.md](./SEO-METRICS.md)** 月度报告（运行 `../tools/gsc_export.py` 拉取数据 → 填趋势表 + 新增月份分析小节）
- [ ] GSC 对当月新页与重大改版页「请求编入索引」（T-33）
- [ ] 复盘 CTR 偏低页 → 优化 `<title>` 与 meta `description`

**E. 内容质量审核（持续多月，逐批推进）**
- [ ] 人工审核并完善既有文章（T-34）：每月推进一批 `_posts` 批量生成文，核对完整度/准确性，补数据、修正表述、统一术语

### 4.2 当月规划的事情

- **2026-11**
  - [ ] Glossary ×4（T-18x）
  - [ ] 相关文章铺开（T-17x）
  - [ ] 首次全站巡检（T-32：build + htmlproofer + sitemap/JSON-LD 校验 + PSI）
  - [ ] 度量基线：拉取 GSC + GoatCounter，回填 `SEO-METRICS.md`（§4.1 D）
