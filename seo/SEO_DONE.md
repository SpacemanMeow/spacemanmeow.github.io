# SEO 已落地记录（DONE）

> **用途**：归档所有已完成 / 已落地的 SEO 优化项、已并入硬门禁的措施与历月完成记录。**只供查阅，不用于排期**。
> **待做事项见**：`SEO-PROGRESS.md` §2（唯一排期依据）。
> **最后更新**：2026-11-19
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

## 3. 持续执行 / 延续项

| 编号 | 优化项 | 分类 | 结论 | 状态 |
|---|---|---|---|---|
| T-40 | 复制已验证内容模式「竞品替代 + 平台限定 + 2026 年度词」，不用 Glossary 硬打 Head 大词 | 内容 | 机制已落地，并入 T-25 长尾内容持续执行 | ♻️ |
| T-43 | 在线工具 | 内容/工具 | 暂缓，不落地工具内容与页面（2026-11-18 用户决定先删除已落地工具形态，视数据再议） | ⏸️ |

## 4. 已并入硬门禁（不再单列待做）

- T-26（Glossary FAQPage 随结构化数据维护）
- T-27（标签一致性由 D19 校验）
- T-28（Glossary ⇄ App 回链由 D11 校验）

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
