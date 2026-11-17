---
name: seo-research
description: 使用 seo/ 下的 SEO 研究资料库 — 关键词库、Google Search Console 导出、月度指标、进度台账和 Google Play ASO 记录。当被问到目标关键词、搜索表现、GSC 数据导出、更新 SEO 指标/进度或 ASO 文案时使用。
---

# SEO 研究资料库

## 文件地图

| 文件 | 用途 |
|---|---|
| `seo/SEO-OPTIMIZATION-PLAN.md` | 总体方案 / 导航枢纽 |
| `seo/SEO-PLAYBOOK.md` | 通用 SEO 方法论 |
| `seo/SEO-I18N-PLAYBOOK.md` | 多语言规则（14 条红线）— 见 `skills/i18n-rules/SKILL.md` |
| `seo/SEO-I18N-PROGRESS.md` | 多语言任务状态的唯一权威来源 |
| `seo/SEO-KEYWORDS.md` | 权威的跨语言关键词库 |
| `seo/SEO-METRICS.md` | 月度 GSC / GoatCounter 报告 |
| `seo/SEO-GOOGLE-PLAY.md` | Google Play ASO 规则 |
| `seo/SEO-PROGRESS.md` | 任务台账 — 注意：部分数量数字已过时；以文件系统核实为准 |
| `seo/SITE-AUDIT.md` | 验收规范 — 见 `skills/seo-audit/SKILL.md` |
| `seo/data/` | 被 gitignore 的工作数据（GSC CSV/JSON 导出、临时 Release Note 日志） |
| `seo/drafts/` | 工作草稿 |

## GSC 导出

`python3 skills/seo-research/scripts/gsc_export.py` 使用 `skills/seo-research/scripts/gsc/`（被 gitignore）中的 OAuth 凭据，把 `_totals/_query/_page/_country/_device/_date/_summary` 文件导出到 `skills/seo-research/scripts/gsc/`。绝不要提交凭据或导出结果。

## 工作规则

- `SEO-KEYWORDS.md` 是关键词目标的权威来源 — 不要在文章里自行编造关键词。
- `SEO-I18N-PROGRESS.md` 是多语言工作状态的唯一来源；任务变化时更新它。
- 数量以文件系统核实为准（例如英文 `_posts/` = 69、`_glossary/` = 27），不要相信过时的台账数字。
- 所有分析数据都是离线/静态的 — 站点没有后端或数据库。

## 分享 / 社交卡片

`og:image` 指向封面 WebP 的绝对 URL，`twitter:card=summary_large_image`。WebP 在 Facebook/X/Telegram 可用，但在微信/iMessage/Slack 可能不渲染；如果某平台需要卡片图，可为 `og:image` 单独准备 JPG，页面展示仍用 WebP。
