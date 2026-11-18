# 高频触发的审计维度

## D03 / D05 — 多语言与 hreflang

- 每种语言的每个页面都必须有对应版本；hreflang 集合 = 5 种语言 + 指向英文的 `x-default`。
- hreflang 由 `scripts/i18n_postprocess.py` 自动注入。绝不要手工编辑 `<link rel="alternate">`。
- 如果某组缺失某一语言，脚本会静默跳过整组 — 检查 `_site/` 中缺少 `<!-- i18n-hreflang -->` 标记的页面。

## D06 — frontmatter / 标语

- 根据页面类型必需 `title`、`description`、`lang`、`layout`、`image`。
- 非英文的 App 标语长度必须 ≤ 英文的 1.5 倍，且不得引入新的数值规格。
- README 的语言列表必须与 `_data/languages.yml` 一致。

## D12 — Pagefind

- 只在完整构建上有意义。`SKIP_PAGEFIND=1` 必然产生 FAIL。

## D14 — 文件名

- 内容文件名中不得出现大写字母、空格或特殊字符；文章使用 `YYYY-MM-DD-slug.md`。

## D15 — 敏感文件

- 不得提交：`seo/data/`（GSC 导出数据）、`skills/seo-research/scripts/gsc/`（OAuth 凭据）、生成的缩略图、`.pagefind-bin/`、`.jekyll-*`。
- `AGENTS.md` 和 `skills/` 是内部文档 — 已在全部五个 `_config*.yml` 中排除。

## D17 / D18 — 跨语言一致性

- 非英文文章要镜像英文文章的 H2/H3 顺序、目录条目/行位置、插图插入顺序。
- 插图使用同一张源图，只本地化其中文字。

## D19 — 标签

- 每篇文章至少带 1 个规范产品标签（11 个 App）。不得出现 `Meow Mood` / `Meow Todo List` / `To Do List` 之类的变体。
- `related-posts.html` 会跳过通用标签；其跳过列表要与规范标签列表保持同步。

## D20 — Release Note

- 55 个页面（11 个 App × 5 种语言），frontmatter 含 `app_store`，正文至少 1 条发布记录、本地化标题后缀，App 详情页链接到自己的 Release Note。
- 见 `skills/release-notes/SKILL.md`。
