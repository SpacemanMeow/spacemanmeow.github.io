# SEO 已落地记录（DONE）

> **用途**：归档所有已完成 / 已落地的 SEO 优化项、已并入硬门禁的措施与历月完成记录。**只供查阅，不用于排期**。
> **待做事项见**：`SEO-PROGRESS.md` §2（唯一排期依据）。
> **最后更新**：2026-11-22
> **语言范围**：5 语并行（EN 根 + `/zh/` `/id/` `/ms/` `/th/`）。所有已落地项默认全语言同步。
> 状态图例：✅ 已落地　♻️ 持续运营中　⏸️ 暂缓

---

## 1. 技术地基 / 一次性内容（2026-10 完成）

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

## 2. 一次性优化项（2026-11 完成）

| 编号 | 优化项 | 分类 | 结论 | 完成 |
|---|---|---|---|---|
| T-22b | BlogPosting `dateModified` / author 细化 | 结构化 | 统一 include 输出 `datePublished` / `dateModified` / author，关闭 seo-tag 重复 BlogPosting | 2026-11-18 |
| T-29 | 图片再优化（AVIF / srcset / 预载） | 性能 | 构建生成 AVIF 缩略图，卡片/首图用 `picture`，首图 `link rel=preload` | 2026-11-18 |
| T-36 | `money tracker` 独立支柱页 | 内容 | 5 语同骨架上线，词库标 `已覆盖(pillar-money-tracker)` | 2026-11-18 |
| T-37 | 治理 Glossary 高曝光零点击词（约 1736 现/2 击） | 内容/CTR | 4 个高曝光术语 × 5 语补 `app_slug`，layout 加「解决方案」导流区；`one ui` 等无关 Head 词停扩 | 2026-11-18 |
| T-38 | 按 GSC 实测词重写低 CTR 支柱页 title/description | 内容/CTR | CPU 温度页强化 `cpu temperature monitor` / 2026 / CPU-Z alternative，小组件页强化 `best widget apps for android` / custom widgets / KWGT alternative；5 语同步 | 2026-11-18 |
| T-39 | 非英语 CTR 与 hreflang | i18n/CTR | id/th 4 个高曝光术语 × 2 语改本地词 + 解决意图标题；hreflang 全站复核成环 | 2026-11-18 |
| T-41 | AI 搜索与移动优先 | AI/体验 | Glossary 加 `DefinedTerm` JSON-LD；CTA 改移动友好卡片；新支柱页沿用移动优先内链 | 2026-11-18 |
| T-42 | Docs 区 55 篇 tutorial + `/docs/` 中心页 × 5 | 内容/内链 | layout 改 `docs`、加中心页与导航入口，URL 不变；详见 `CONTENT-HUB-PLAN.md` | 2026-11-18 |
| T-44 | 文章页宽屏三栏（≥1280px） | 内链/体验 | 左 sticky 目录、中正文、右 sticky 推荐；窄屏退回单栏；5 语同步 | 2026-11-19 |
| A2 | 重写低 CTR 高曝光支柱页 title/description | 内容/CTR | `pillar-cpu-temperature`（622 现/2.1%）与 `pillar-android-home-screen-widgets`（pos 29.5）5 语重写：高 intent 竞品词前置（CPU-Z / KWGT Alternative），标题 ≤60 字符、描述 150–160 且含主词；EN/ID/MS/TH 字符全部达标，无裸 `&`。**美国市场（1524 现/1.2%）为国家切片非独立页，其低 CTR 由这两个 EN 支柱页 + Glossary 治理（T-37）承接，未单独建页。** | 2026-11-19 |
| A3 | 非英语 CTR 专项 | i18n/CTR | **hreflang 复核**：全站 675 页 / 4050 条 alternates 静态校验，语言集 `{en,zh,id,ms,th,x-default}` 齐全、目标页全存在、成环 0 异常，无需修改。**本地化标题**：ms 27 个术语页从直译式 `Apakah X?` 改为「本地词 + 解决意图」（对齐 T-39 已验证的 id 模式，如 `Tetingkap Terapung Android: Cara Kerja dan Kebenaran`、`Pengurusan Bajet: Cara Atur Bajet Harian dan Bulanan`），全部 ≤60 字符；id/th 高曝光页 T-39 已处理，不重复。移动端优先由 ≤60 字符标题（移动端 SERP 不被截断）承接。 | 2026-11-19 |
| A4 | 标签 / 主题聚合页（主题中心） | 内容/内链 | `/tags/` 从平铺标签云改为**三层主题中心**：按 App 产品（11 标签）/ 品类主题 / 内容类型分组，每组带五语本地化标题；新增共享模板 `_includes/tag-index.html` + `tag-index-group.html`，五语 tags.md 统一引用（D18 骨架一致）。入口：主导航与 footer 按要求不放（**主导航/footer 未改**）；博客列表页新增右栏标签入口，复用文章页 `aside-tags-block` 样式（无卡片背景、Tags 标题），按 `Browse by app → Browse by topic → Browse by content type` 顺序完整列出三类标签；分组逻辑抽为共享 `_includes/tag-groups.html`，与 `/tags/` 主题中心同一白名单与顺序。与文章页同口径：`container--wide` 加宽、正文固定 992px、右栏 sticky，仅 ≥1580px 显示（窄屏隐藏不挤压正文）；页头已有 `tags_index_link` 指向 `/<lang>/tags/`。D11 内链闭环通过、41 个 tag 锚点零断裂；D21 多视口无溢出；`/tags/` 基线不变（groups 41/41/47/47/48、items 290/290/292/292/292）。UI 五语补 `topics_by_app/category/type` 三键。41 个 tag 锚点零断裂；五语 groups 41/41/47/47/48、items 290/290/292/292/292 全保留；审计 75 PASS、htmlproofer 通过。未新增独立 `/topics/` 集合（避免 5 份 config 与集合分离的 P0 风险）。 | 2026-11-19 |
| A5 | Release Notes 中心页 | 内容/内链 | 11 App × 5 语共 55 页 Release Note 已上线（D20）：每 App 一个结构化聚合页、每版本作为页内条目呈现，标题后缀五语本地化；`_layouts/app.html` 底部与 `_layouts/release-note.html` 回链构成 App ⇄ Release Note 双向环链。数据由 `skills/release-notes/scripts/update_release_notes.py` 从升级日志解析生成，D20 五项硬门禁（覆盖/frontmatter/正文/标题本地化/内链）全绿。 | 2026-11-20 |
| E3 | Release Notes → 更新中心 | 内容/内链 | 与 A5 合并执行，不重复立项；随 A5 一并归档。 | 2026-11-20 |
| B3 | 新增 FAQ 问答中心 | 内容/结构化数据 | 5 语新增 `/faq/` 中心页，集中全站问答索引：每语 338 条（App front matter `faq` 11 App/51 条 + 文章正文 `faq-q` 70 篇/287 条），按「按应用 / 按指南」分组列出问题并锚点跳转到来源页答案。**零手工步骤**：新增 `_plugins/faq_index.rb` 在每次构建时自动解析文章两种 FAQ 标记（`**Q**` 与教程的 `### Q`），注入稳定 `id="faq-N"` 锚点、`page.faq_items` 与 `site.data.faq_index`；编辑 FAQ 后只需正常构建，无需再跑脚本，也不再维护生成物 `_data/faq_posts.yml`（已删除）。答案与 `FAQPage` schema 留在各自来源页：App 页复用共享 `_includes/faq-jsonld.html`，文章页由 `guide-jsonld.html` 对自身可见 FAQ 输出 schema（每篇独立，利于 PAA）；中心页只做问题索引、不重复答案、不输出 schema，页面体积从首版 245–415KB 降至 65–86KB。插件同时修复了 id/ms 的 App 答案含 `&` 被 markdownify 转成 `&amp;` 污染 schema 的问题。五语 UI 补 `faq_hub_intro/faq_hub_stats/faq_by_app/faq_by_guide/faq_link` 五键；博客页眉（`/blog/` 等）三连入口后追加 FAQ 入口，**主导航/footer 未改**（沿用 A4 口径）。CSS 新增 `.faq-hub__*` 索引列表样式，字号/字重/边框/间距全部走 D22 令牌。SITE-AUDIT：D03 结构页 9/9→10/10、`STRUCT` 加 `faq`，顺手修正 §4 D03 陈旧口径（posts 69→70、pages 8→10）。完整构建 680 页；htmlproofer 681 文件 / 2988 内链 / 0 failure（含 338×5 个 `#faq-N` 锚点）；§5 静态脚本 82 PASS / 0 FAIL（D14 1 条为新增 `faq.md` 未跟踪告警，人工确认通过）；D21 四视口（375/768/1024/1920）中心页 `scrollWidth == clientWidth`，无横向溢出，338 链接全渲染。 | 2026-11-21 |
| B2 | Glossary 扩量与解决方案区（T-18x） | 内容/内链/CTR | 实测 27 术语 × 5 语共 135 页已全部落地，台账号「20/规划 27、补 7 页」为滞后口径，本轮不新建页而是完成「定义页 → 解决中心」升级：① 五语索引页补齐 5 个此前漏列的预算术语（zero-based / envelope / rollover / sinking fund / category budget），并按 5 类问题分组（预算与金钱 / 习惯心情效率 / 时钟小组件 / 设备工具性能 / 游戏与个性化），5 语各 27 条；② 27×5 术语页标题全部从定义式 `What Is X?` 改为解决意图式（如 EN `Budget Management: Set Category Limits and Track Spending`），EN/ID/MS/TH ≤60 字符；③ `app_slug` 从 4 术语扩到 23 术语 × 5 语（共 115 页），共享 layout「解决方案」区自动输出手册 + App CTA；4 个无对应产品的平台/UI 术语按 T-37 口径不扩；④ 描述补产品方案词并按 D06 ≤160 字符精简；⑤ App 详情页与 Pillar 文章的 Related terms 链接文本全量同步为新标题（5 语各 50 条），记账类补 5 个预算术语回链（5 语各 +10 条）；⑥ 新增 `_data/glossary_pillars.yml`（app→Pillar 单一来源映射）+ `<lang>` UI `related_guide` 键，Glossary layout 自动渲染「相关指南」区块，形成 Glossary ⇄ App ⇄ Pillar 闭环。D18/D21/D22 全绿；htmlproofer 1293 内链 0 failure。 | 2026-11-21 |
| GEO-01 | 首次 GEO 体检（甲戟 7 维 29 项） | AI 搜索/基线 | 首页体检完成：55.45/100（C），29/29 项全评估，20 项待整改合并为 14 个可执行任务。基线分进 `SEO-METRICS.md`、方法进 `SEO-PLAYBOOK.md` §4.5、任务进 `SEO-PROGRESS.md` §2.G，原始数据在 `data/geo/20261122/`（被 gitignore）。体检中发现并纠正三处通用话术误判：正文占比低≠SSR、Schema error 根因是 config 相对 URL、ICP 备案不适用本站。**体检已完成，整改任务仍待做（见 §2.G）**。 | 2026-11-22 |

## 3. 持续执行 / 延续项

| 编号 | 优化项 | 分类 | 结论 | 状态 |
|---|---|---|---|---|
| T-40 | 复制已验证内容模式「竞品替代 + 平台限定 + 2026 年度词」，不用 Glossary 硬打 Head 大词 | 内容 | 机制已落地，并入 T-25 长尾内容持续执行 | ♻️ |
| T-43 | 在线工具 | 内容/工具 | 暂缓，不落地工具内容与页面（2026-11-18 用户决定先删除已落地工具形态，视数据再议） | ⏸️ |

## 4. 已并入硬门禁（不再单列待做）

- T-26（Glossary FAQPage 随结构化数据维护）
- T-27（标签一致性由 D19 校验）
- T-28（Glossary ⇄ App 回链由 D11 校验）
- D1（审计脚本落盘 + 接入 CI + 维度化重构：2026-11-22 将 `SITE-AUDIT.md` §5 内嵌的 D01–D22 脚本抽为 `scripts/site_audit.py` 单一权威副本，加 FAIL 退出码 1；CI `pages-deploy.yml` 在 `Test site` 后新增 `Audit site` 步骤调用同一脚本。同日按用户要求把散乱的 D 编号检查重构为 **8 大维度**（BLD/I18N/META/CONTENT/LINK/A11Y/DESIGN/HYGIENE）+ 稳定规则 ID（如 `I18N-05`、`DESIGN-02`）+ `Auditor` 注册表结构；脚本按维度分组输出每条规则的名称与结果及小计；`SITE-AUDIT.md` §3/§4 同步重写为同 8 维度规则表，§4.9 规定新增规则必须落位到对应维度函数与小节，§0/§5/§7/§8 全部改为维度口径。重构后 83 项检查与原版一一对应、无遗漏；本地验证：语法编译通过、正常退出 0、注入 FAIL 退出 1；完整构建通过、htmlproofer 0 failure、workflow YAML 合法）

## 5. 内容形式规划判断逻辑（已验证依据）

> 对应待办见 `SEO-PROGRESS.md` §2（A4/A5/B2/B3/B4/B6/E5/E1/E6/E7）。本节保留判断依据供查阅。

- **第一梯队｜已有资产改造（ROI 最高）**
  - **Glossary 术语表**：11 月已验证需求（约 1736 展现仅 2 点击）。定义型词不随热点衰减、AI 引用友好 → 对应 B2 / E4。
  - **Release Notes 更新日志**：55 页（11 App × 5 语）近乎零流量 → 对应 A5 / E3。
  - **标签 / 主题聚合页**：`/search` +1000% 说明缺聚合入口 → 对应 A4。
- **第二梯队｜静态站友好新形式**
  - **结构化对比矩阵页**（非文章）：易拿 featured snippet 与 AI 引用 → 对应 B4。
  - **独立 FAQ 问答页**：承接 `what is / how to / which app` → 对应 B3。
  - **可下载资源 / 模板页**：收藏与外链属性强 → 对应 E5。
  - **场景 / 问题解决页（use-case）**：竞争小、意图精准、生命周期长 → 对应 B6。
- **第三梯队｜暂缓**：榜单目录页（薄内容风险）、年度数据报告（外链 magnet 但维护成本高）、视频 / 播客（静态站不适配）。
- **执行原则**：每新增一种形式要 ×5 语言，优先复用现有集合（`_glossary*` / `_release_notes*` / `_pages*`）与模板；非英语骨架与 EN 同序、内链带 `/<lang>/` 前缀、hreflang 成环，并入 D11/D19 门禁。

## 6. 历月完成记录

### 2026-11

5 语预算对比文、习惯机制深对比文、清单应用深对比文三批 5 语发布；id/th/ms 全量交付收尾；文章达 69/语、术语 27/语；Release Note 55 页上线；`page.lang` 与 GSC 输出路径等口径修正。

> 逐任务执行记录（含每组的关键词命中数、升权词、alt 去重数等）见 git 历史与 `SITE-AUDIT.md` §8；数量口径以文件系统实测为准。
