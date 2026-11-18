# 内容形态融合执行计划（Blog + Docs + Glossary + App；Tools 已移除）

> **用途**：把「形态融合」方案拆成可执行的改动清单——导航怎么调、页面怎么划分、形态间怎么联动、具体补哪些文件和内容。**这是规划文档，不是执行流水**；逐次执行记录仍归 `SITE-AUDIT.md` §8。
> **依据**：2026-11 数据复盘（`SEO-METRICS.md` 2026-11）与 `SEO-PROGRESS.md` 待推进项 T-37～T-41。
> **关联**：优化项编号见 `SEO-PROGRESS.md` §2（T-42；T-43 在线工具已暂缓）；多语言红线见 `SEO-I18N-PLAYBOOK.md` §1；验收见 `SITE-AUDIT.md` D01–D20。
> **状态**：✅ Docs 形态已落地；⏸️ **在线工具形态已移除，不再落地**（2026-11-18 用户决定，下文涉及 Tools 的章节仅为历史规划参考，不代表当前站点状态）　**最后更新**：2026-11-18
> **当前实际落地**：Docs 形态（55 教程 layout→docs、5 个 `/docs/` 中心页、导航/页脚/Blog 入口）；Glossary 解决方案区 20 页（T-37）。在线工具相关页面、集合、模板、脚本、样式均已删除。
> **关键修复记录**：① 5 份 config 原裸 `docs`/`tools` exclude 会误伤同名 layout（Jekyll 按 basename 排除），已移除；② Liquid 方括号内不可用 filter，改为先 assign key；③ 教程正文已自带 TOC，docs layout 不再重复生成。
> **待办**：T-33 GSC 对 `/docs/` 请求索引；30 天后用 `gsc_export.py` 复测 Docs 形态效果。

---

## 0. 决策摘要

### 0.1 五形态与技术载体映射

| 形态 | 技术载体 | URL 形态 | 内容源 | 新建集合？ |
|---|---|---|---|---|
| **Blog** | `_posts/` + layout `post`/`guide` | `/posts/<slug>/` | 69 篇 × 5 语 | 否（现有） |
| **Docs** | `_posts/*tutorial*.md` + 新 layout `docs` + `/docs/` 中心页 | `/posts/tutorial-<app>/`（**不变**） | 11 篇 × 5 语（改造） | **否（复用）** |
| **Glossary** | `_glossary*/` + layout `glossary` | `/glossary/<slug>/` | 27 篇 × 5 语（T-37 改造） | 否（现有） |
| **App** | `_apps*/` + layout `app` | `/apps/<slug>/` | 11 篇 × 5 语 | 否（现有） |
| **Tools** | `_tools*/`（**新集合**）+ layout `tool` | `/tools/<slug>/` | 首期 1 个（预算计算器）× 5 语 | **是** |

### 0.2 两个关键架构决策

**决策 1：Docs 不新建集合，复用现有 11 篇 tutorial。**
理由：① 11 篇教程每语齐全、一一对应 11 App、已带规范产品标签（D19 已通过），重写 55 篇成本极高；② 改 layout 不改 permalink，URL 零变动，不触红线 1、不破收录；③ 不新增集合就不动 5 份配置的 `collections`/审计脚本白名单，风险最低。Docs 是「呈现形态」而非「新内容类型」——通过新 layout（章节 TOC + 上下篇 + 工具/术语导流）和 `/docs/` 中心页赋予手册感。

**决策 2：Tools 新建独立集合 `_tools*/`。**
理由：① 工具页需要专用 layout + JS 交互，与文章/结构页性质不同；② 与 `apps`/`glossary`/`release_notes` 的集合模式一致，团队已有 SOP 可复用；③ defaults 统一指定 `layout: tool` + `seo.type: WebPage`，避免 seo-tag 误判为 BlogPosting；④ 未来扩展工具数量无需改结构。

> **exclude 注意**：现有 5 份配置中的裸 `docs`、`tools`（`_config.yml` L193-194 等）排除的是**根级** `docs/`、`tools/` 目录，与带下划线的集合源目录 `_docs/`、`_tools/` 不冲突，无需为此改动；但非 EN 配置排除 EN 源时必须写 `_tools/`（**带尾斜杠**），否则会误伤 `_tools_zh/` 等同前缀目录（`SEO-I18N-PLAYBOOK.md` 红线 4）。

---

## 1. 导航结构调整

### 1.1 目标信息架构

现状 4 项：Home / Meow / Blog / About（`_data/nav.yml` L5-59）。
目标 6 项：**Home / Meow / Docs / Tools / Blog / About**。

- Docs、Tools 作为一级入口，体现「手册 + 工具」的价值定位，排在 Blog 前。
- **Glossary 不占导航位**：继续从 Blog 与 Docs 页头的快捷链接进入（`_layouts/blog.html` L10 已有此模式），避免移动端下拉菜单过长。
- App 入口保持现状：Home = 全部 11 App，Meow = 喵窝系列。

### 1.2 需要改的文件

| 文件 | 改动 | 位置 |
|---|---|---|
| `_data/nav.yml` | 新增 Docs、Tools 两项（各含 5 语 `title`/`url` + `nav` 键）；更新 L2 注释的 nav 取值清单 | L1-4、L59 后 |
| `_includes/nav.html` | `active` 推断逻辑补 `docs`/`tools` 分支 | L5-17 |
| `_data/ui.yml` | 5 语各补 `docs_title`、`tools_title`、`docs_intro`、`tools_intro`、`view_manual`、`try_tool` 等键 | 各语段末尾 |
| `assets/css/main.css` | 导航区适配 6 项（gap/字号/移动端下拉项）；新增 Docs/Tools 区块（建议第 12、13 节） | L198-212、L1030-1050、文件头 L1-14 |

`nav.yml` 新增项示例（5 语均需填写，缺键会静默输出空链接）：

```yaml
- title:
    en: Docs
    zh: 使用手册
    id: Panduan
    th: คู่มือ
    ms: Panduan
  url:
    en: /docs/
    zh: /zh/docs/
    id: /id/docs/
    th: /th/docs/
    ms: /ms/docs/
  nav: docs
```

Tools 同理（`en: Tools`、`zh: 在线工具`、`id: Alat`、`th: เครื่องมือ`、`ms: Alat`；URL `/tools/` 与 `/<lang>/tools/`；`nav: tools`）。

---

## 2. 页面整体结构划分

### 2.1 URL / 目录树

```
/                          Home（app-list，全部 11 App）
/meow/                     Meow 系列（app-list）
/docs/                     【新】Docs 中心：11 App 手册卡片
/posts/tutorial-<app>/      Docs 教程（现有 55 篇，layout: post → docs）
/glossary/                 Glossary 中心（现有）
/glossary/<term>/          术语页（T-37 改造：加"解决方案"区）
/tools/                    【新】Tools 中心：工具卡片网格
/tools/<tool>/             【新】工具页（_tools/ 集合，layout: tool）
/apps/<slug>/              App 页（Guides 区 + 新增工具区）
/apps/<slug>/release-notes/ Release Note（现有）
/blog/                     Blog 索引（页头快捷链接扩展）
/<lang>/...                以上全部在 zh/id/ms/th 下有同构对应
```

### 2.2 七类页面的区块结构

**① `/docs/` 中心页**（`_pages/docs.md` + 4 语，layout `docs-hub`）
1. `page-head`：标题 + 简介 + 快捷链接（Blog · Glossary · Tools）
2. 11 App 手册卡片网格：图标 + 名称 + 一句话 + "查看手册"→对应 tutorial + 最近更新时间
3. 底部：3 条推荐术语（指向 Glossary）

**② Docs 教程页**（`_posts/*tutorial*.md`，layout `docs`）
1. 面包屑：`Docs → <App 名>` + "返回手册中心"
2. 封面 + 标题 + 更新时间（沿用现有）
3. **章节 TOC**（从 H2 生成，参考 `_layouts/guide.html`）
4. 正文（结构不动，保 D17/D18）
5. 底部三件套：上一篇/下一篇（按 `doc_order`）、"相关术语"、`tool_slug` 存在时显示"试试在线工具"
6. App CTA：由 `app_icon` 反查 App 页 + store buttons

**③ Glossary 术语页**（T-37 改造）
1. 现有定义正文不变（保骨架同序）
2. **新增"解决方案"区**：链到对应 App 页 + Docs 教程 + 相关工具（解决 640 展现 0 点击的意图错配）

**④ App 页**（改造）
1. 现有 hero / 截图 / 正文 / FAQ 不变
2. Guides 区（`_layouts/app.html` L50-64）标题改为"手册与指南"，同时列 tutorial 与 pillar 文章
3. **新增"在线工具"区**：`page.tool_slug` 存在时显示工具卡片（链到 `/tools/<slug>/`）

**⑤ `/tools/` 中心页**（`_pages/tools.md` + 4 语，layout `tools-hub`）
1. 页头 + 快捷链接（Docs · Blog）
2. 工具卡片网格：工具名 + 一句话 + 入口

**⑥ 工具页**（`_tools/<slug>.md`，layout `tool`）
1. 页头 + 快捷链接（Docs · App）
2. **工具交互区**：`<div data-tool="<tool_type>">` + `assets/js/tools.js` 按 `tool_type` 分支渲染
3. 使用说明（H2 结构与 5 语同序）
4. 结果区 CTA："用 <App> 一键完成"→ App 页
5. 底部：相关 Docs 教程 + 相关 Glossary 词条

**⑦ Blog 索引页**（改造 `_layouts/blog.html` L10）
- 快捷链接从「Tags · Glossary」扩展为「Tags · Glossary · Docs · Tools」

---

## 3. 形态间联动设计

### 3.1 联动矩阵

| 源页面 | 目标 | 实现字段 / 方式 | 落点 |
|---|---|---|---|
| 顶部导航 | Docs / Tools 中心 | `nav.yml` 新项 | `nav.html` L73-77 |
| App 页 | Docs 教程 | `app_icon == page.icon`（现有） | `_layouts/app.html` L50-64 |
| App 页 | 工具 | `page.tool_slug` | 新增区块（§2.2④） |
| Docs 教程 | App 页 | `app_icon` 反查 `site.apps` | layout `docs` 底部 CTA |
| Docs 教程 | 工具 | front matter `tool_slug` | layout `docs` 底部 |
| Docs 教程 | 上/下篇 | `doc_order` + `doc_app` | layout `docs` |
| Docs 教程 | Glossary | `glossary_terms` | layout `docs` 底部 |
| Glossary | App / Docs / 工具 | T-37"解决方案"区 | `glossary.html` |
| 工具页 | App 页 | front matter `app_slug` | 结果区 CTA |
| 工具页 | Docs 教程 | `app_slug` → 查 tutorial | 底部 |
| Blog 页头 | Docs / Tools / Glossary | `ui.yml` 文案 | `_layouts/blog.html` L10 |
| 页脚 | 五形态入口 | `footer.html` + `ui.yml` | `footer.html` L15-26 |

### 3.2 三条关键链路（对应 11 月数据问题）

1. **零点击词 → 转化**：`budget management`（595 现 0 击）→ Glossary 页"解决方案"区 → ① 预算计算器 `/tools/budget-calculator/` → 结果 CTA → Meow Money Manager App 页；② 同区链 Docs 教程。把定义型曝光接到工具与产品。
2. **品牌词 → 手册深度**：`meow money` 品牌词（CTR 12.9%）→ App 页 Guides 区 → Docs 教程（带章节 TOC）→ 提升停留与内链深度。
3. **工具 → App 转化**：预算计算器的分配结果页给出「用 Meow Money Manager 一键记录」CTA → 直接导入 App 落地页（首期链路；后续如扩视觉化工具，可再加「结果可复制/截图 → 自然外链」路径）。

### 3.3 语言前缀规则（硬性）

所有内链按构建级 `site.lang` 生成前缀，模板统一用：

```liquid
{%- assign lang = site.lang | default: 'en' -%}
{%- assign lp = '' -%}{%- if lang != 'en' -%}{%- assign lp = '/' | append: lang -%}{%- endif -%}
<a href="{{ '/docs/' | prepend: lp | relative_url }}">…</a>
```

禁止用 `page.lang` 拼 URL（`SEO-I18N-PLAYBOOK.md` 红线 2）；`related-posts.html` 等 include 已按 `site.lang` 索引 `apps_<lang>`，新增区块沿用。

---

## 4. 内容与配置补充清单

### 4.1 配置（5 份必须同步）

| 配置 | 改动 |
|---|---|
| `_config.yml` | `collections` 加 `tools`（`output: true`、`permalink: /tools/:name/`）；`defaults` 加 `type: tools` → `layout: tool`、`seo.type: WebPage`；从 exclude 删除无用裸 `tools`（可选） |
| `_config_zh.yml` 等 4 份 | 加 `tools_<lang>` 集合（`permalink: /<lang>/tools/:name/`）；defaults对应；exclude 加 `_tools/`（**带尾斜杠**，排除 EN 源）+ 其它 3 语 `_tools_<其他语>`；保留裸 `tools` 无妨 |

> 新增集合不需要改 `scripts/build.sh`（无集合白名单）与 `scripts/i18n_postprocess.py`（按去语言前缀 slug 配对）。**硬约束**：`/tools/<slug>/` 与 `/<lang>/tools/<slug>/` 去前缀后必须同 slug，否则 hreflang 无法成组（脚本不会报错，需人工抽验）。

### 4.2 模板与样式（新建/修改）

**新建**
- `_layouts/docs.html`（Docs 教程：TOC + 上下篇 + 三件套导流）
- `_layouts/docs-hub.html`、`_layouts/tools-hub.html`（中心页）
- `_layouts/tool.html`（工具页）
- `_includes/tool-*.html`（按 `tool_type` 的 UI 片段，可选）
- `assets/js/tools.js`（按 `data-tool` 分支的计算逻辑，单文件避免碎片化）

**修改**
- `_layouts/app.html`（L50-64 Guides 区改名 + 新工具区）
- `_layouts/blog.html`（L10 快捷链接扩展）
- `_includes/footer.html`（L15-26 形态入口）
- `assets/css/main.css`（导航适配 + 第 12/13 节新区块）
- `_data/nav.yml`、`_data/ui.yml`（§1.2）

### 4.3 内容清单

| 内容 | 数量 | 命名 | 关键 front matter |
|---|---|---|---|
| `/docs/` 中心页 | 1 × 5 = 5 | `_pages/docs.md`、`_pages/<lang>/docs.md` | `layout: docs-hub`、`permalink`、`lang` |
| `/tools/` 中心页 | 1 × 5 = 5 | `_pages/tools.md`、`_pages/<lang>/tools.md` | `layout: tools-hub`、`permalink`、`lang` |
| Docs 教程改造 | 11 × 5 = 55 | 现有文件**改名不改** | `layout: post → docs`；新增 `doc_order`(1-11)、`doc_app`(app slug)、可选 `tool_slug`、`glossary_terms` |
| 工具页 | 1 × 5 = 5 | `_tools/budget-calculator.md`、`_tools_<lang>/budget-calculator.md` | `title`、`description`、`lang`、`tool_type`、`app_slug`、`doc_slug`、`image` |
| 工具 OG 图 | 1 | `assets/images/tools/budget-calculator.webp` | — |

**Docs 教程新增字段示例**（加在现有 front matter 中）：

```yaml
layout: docs          # 原为 post，URL 不变
doc_order: 6          # Docs 区顺序（按 App 顺序 1-11）
doc_app: meow-money-manager   # 对应 App slug
tool_slug: budget-calculator  # 可选，有对应工具时填
glossary_terms: [what-is-a-budget, what-is-an-expense-tracker]  # 可选
```

**工具页 front matter 示例**：

```yaml
---
title: Budget Calculator
description: Split your monthly income into categories in seconds — then track it offline with Meow Money Manager.
lang: en
tool_type: budget
app_slug: meow-money-manager
doc_slug: tutorial-meow-money
image: /assets/images/tools/budget-calculator.webp
---
```

### 4.4 首期工具（基于 11 月 GSC 数据选词）

| 工具 slug | 目标词/现象 | 绑定 App | 交互 |
|---|---|---|---|
| `budget-calculator` | `budget management` 595 现 0 击（pos 60） | Meow Money Manager | 收入按类别分配、占比可视化 |

选择原则：对应一个**已有展现但 CTR 低**的词，且与一款 App 强绑定，形成「工具 → App」闭环。

> **范围**：首期只实现预算计算器一个工具（5 语共 5 页），先验证「零点击词 → 工具 → App」链路是否跑通；`crosshair` / `flip clock` 等后续工具视首期数据再决定是否扩展，不在本期范围。

---

## 5. 分阶段执行步骤（先规则、再骨架、后内容）

> 每阶段收工必须跑**完整构建**（`bash scripts/build.sh`，不能 `SKIP_PAGEFIND=1`）+ htmlproofer + `SITE-AUDIT.md` §5 审计脚本（FAIL=0、BASE 空）。改任何源文件后预览服务器不自动重建，需硬刷新。

### 阶段 0：规则与门禁先行（约 0.5 人天）
- [ ] `SITE-AUDIT.md`：结构页白名单 8→10（加 `docs`、`tools`）；`dirs(L)` 加 `tools` 类；D11 加"形态间内链闭合"检查点；D19 明确只约束 `_posts/`（工具页用 `app_slug` 替代产品标签）
- [ ] `SEO-I18N-PLAYBOOK.md` 红线 7 的页面类型覆盖清单补 Docs/Tools
- [ ] `AGENTS.md` §5 内容类型表补两行
- [ ] 验收：审计脚本结构改为 10/10 后对现状跑一次，确认无回归

### 阶段 1：配置与骨架（约 1.5 人天）
- [ ] 5 份 config 加 `tools` 集合与 defaults；exclude 按 §4.1 调整
- [ ] 新建 `_tools/`、`_tools_zh/`、`_tools_id/`、`_tools_ms/`、`_tools_th/`（先放 `.gitkeep`，不提交空目录）
- [ ] 新建 4 个 layout + `tools.js` 骨架；修改 nav/ui/app/blog/footer/CSS
- [ ] 验收：完整构建通过；`_site/tools/`、`_site/<lang>/tools/` 目录生成；D01/D03/D04/D05 无 FAIL

### 阶段 2：内容落地（约 2.5 人天）
- [ ] 5 个 `/docs/` + 5 个 `/tools/` 中心页（10 页）
- [ ] 55 篇 Docs 教程改 layout + 补 front matter（批量脚本从 `/tmp` 执行，不在仓库新建脚本）
- [ ] 5 个预算计算器工具页（每语 1 页）+ 1 张 OG 图（每语正文与 EN 骨架同序）
- [ ] 验收：D05 每新页 6 条 hreflang 成环；D17/D18 骨架同序；D02 htmlproofer 0 failure；工具 JS 在 5 语均工作

### 阶段 3：联动改造（约 1 人天）
- [ ] App 页工具区、Glossary"解决方案"区（T-37）、Blog 页头扩展、Docs 底部三件套、footer 形态入口
- [ ] 验收：D11 内链闭合；人工抽验 §3.2 三条链路；移动端 6 项导航无溢出

### 阶段 4：验收与发布（约 0.5 人天）
- [ ] 完整构建 + htmlproofer + 审计脚本 FAIL=0 / BASE 空
- [ ] GSC 对 `/docs/`、`/tools/` 及 5 个预算计算器工具页请求索引（T-33）
- [ ] 回填 `SITE-AUDIT.md` §8 与 `SEO-PROGRESS.md`（T-37/T-42/T-43 标 ✅）
- [ ] 30 天后用 `gsc_export.py` 复测：重点看 `budget management` 的 CTR 变化、工具页收录与「工具 → App」链路转化

**总估算：约 6 人天**（不含 30 天后的复测）。

---

## 6. 验收、排期与红线

### 6.1 验收清单（每阶段收工）
1. `bash scripts/build.sh` 退出码 0，日志含 5 语言、`==> Done...`
2. `skills/site-build-deploy/scripts/test.sh`（CI 同款 htmlproofer）0 failure
3. `SITE-AUDIT.md` §5 审计脚本：`{PASS:N, FAIL:0, WARN:0}`、BASE 空
4. 人工抽验：每新页 hreflang 6 条且 x-default 指向 EN；工具 JS 在 5 语执行；`/docs/`、`/tools/` 中心页 5 语互链可达

### 6.2 建议执行顺序与节奏
- **阶段 0 → 1 → 2 → 3 → 4** 严格串行；阶段 2 可按「中心页 → Docs 教程批量改 → 工具页」三小批推进，每小批改完跑一次快速构建（`SKIP_PAGEFIND=1`）自检，阶段末跑完整构建。
- 与既有 T-37（Glossary 治理）、T-38（支柱页重写）并行无冲突，但**不要同时改审计脚本与内容**（避免定位问题困难）。

### 6.3 红线与风险
| 风险 | 规避 |
|---|---|
| 改 URL 破收录 | Docs 教程**只改 layout，不改文件名/permalink**；工具页为全新 URL |
| hreflang 不成环 | 5 语同 slug；去前缀后路径一致；脚本不报错需人工抽验 |
| 骨架同序 FAIL | 工具页与 Docs 教程 5 语 H2/H3、结构块、图片位置与 EN 一致（D18） |
| 产品标签缺失 | Docs 教程保留现有规范标签；工具页在 `_tools/` 不受 D19 约束，但必须填 `app_slug` |
| 审计脚本盲区 | 阶段 0 先把 `_tools/` 纳入 `dirs(L)` 与 D11，否则新集合源侧无校验 |
| 移动端导航溢出 | 6 项 + 搜索/语言/主题，在 768px 下拉菜单内纵向排列，桌面收紧 gap |
| 工具 JS 增加 LCP | `tools.js` 用 `defer`，仅在工具页加载（layout `tool` 内引入，不进 `default.html`） |
