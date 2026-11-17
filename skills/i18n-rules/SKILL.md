---
name: i18n-rules
description: 创建或编辑非英文内容、hreflang、集合、exclude 规则以及新增语言时必须遵守的多语言规则（14 条红线）。在改动任何 _posts/<lang>、_apps_<lang>、_glossary_<lang>、_pages/<lang>、_config_<lang>.yml 或语言导航前使用。
---

# 多语言规则与机制

权威来源：`seo/SEO-I18N-PLAYBOOK.md` §1（14 条红线）与 §7（历史坑）。本 skill 只是快速索引；有疑问时阅读 playbook 原文。

## 14 条红线（摘要）

1. 没有明确的重定向计划，不得更改 URL/固定链接。
2. hreflang 必须构成完整的互指集合，且 `x-default` 指向英文。
3. 集合按语言分离（`apps`/`apps_zh`/`apps_id`/…）。
4. `exclude` 规则：不用 `!ruby/regexp`；`*` 不跨 `/`；英文 App 目录要写成 `_apps/`（带尾斜杠），文章写成 `_posts/1*`/`_posts/2*`。
5. 模板按构建级 `site.lang` 分支，**绝不用** `page.lang`（否则页面会静默渲染到英文根目录，或报 `Cannot sort a null object`）。
6. 本地化的是同一篇文章 — 不要写成另一篇不同的文章。
7. 覆盖所有页面类型，而不只是文章。
8. 改动后做全站审计（见 `skills/seo-audit/SKILL.md`）。
9. 各语言之间功能/术语保持一致。
10. 插图共享同一张源图；只本地化其中文字。
11. 非英文的骨架/目录/插图位置严格跟随英文（D17/D18）。
12. App 标语非英文长度 ≤ 英文的 1.5 倍，不引入新的数值规格。
13. 站点标语可见宽度 `w ≤ 60` 且不超过英文长度。
14. Release Note：根据用户提供的日志生成 55 个页面（见 `skills/release-notes/SKILL.md`）。

## 构建如何组装各语言

- 英文配置直接写入 `_site/`。
- 其它每种语言构建到 `.jekyll-<lang>/`，然后 `rsync` 到 `_site/<lang>/`。
- `scripts/i18n_postprocess.py` 按去掉语言前缀后的 slug 对页面分组，注入 hreflang alternates + x-default，并构建合并 sitemap。它是幂等的。
- `_data/languages.yml` 驱动导航语言下拉框和 `assets/js/i18n.js`。

## 新增语言

`bash scripts/new-language.sh <code> <label> [short]` 会生成配置/目录/占位文件，但历史上总有遗漏。运行后要手动检查：glossary 的 sed 替换、`feed.path` 的前导 `/`、glossary/exclude 条目、`404.html` 中硬编码的语言、`i18n.js` 残留的双语言回退、从 zh 复制过来的页脚文案。然后做完整构建并运行 D03/D05/D06。

## 参考

详细的历史坑见 `references/pitfalls.md`。
