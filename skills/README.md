# 项目 Skills 索引

本目录把工程的 SOP、工具用法、规则按 CodeBuddy Skill 格式沉淀为独立单元。每个 skill 是一个自包含目录，核心是 `SKILL.md`（含 YAML frontmatter `name`/`description`），详细资料放在 `references/`。

**使用方式**：新对话/其他 AI 先读仓库根目录 `AGENTS.md` 建立全局上下文；处理具体任务时再按本索引读取对应 `skills/<name>/SKILL.md`。若运行环境支持 `use_skill` 且已把本目录注册为 skills 路径，可直接触发。

| Skill | 何时使用 | 核心内容 |
|---|---|---|
| `site-build-deploy` | 改任何源文件后要验证、跑构建、排查"改了没生效"、CI 部署 | 构建 5 步流程、快速/完整构建、预览机制、CI、常见假阳性 |
| `release-notes` | 用户发来升级日志、要更新 Release Note、处理 D20 | 日志→临时文件→补全译文→生成器→构建→审计全流程 |
| `seo-audit` | 改动后验收、跑 D01–D20 审计、排查 SEO 维度失败 | 审计脚本提取执行、结果判读、维度速查 |
| `i18n-rules` | 新增/修改非英语内容、hreflang、集合/exclude、新增语言 | 14 条红线、site.lang vs page.lang、历史坑 |
| `cover-images` | 换 cover、新增文章配图、排查图片不更新/srcset | 原图/缩略图规格、模板引用、CSS 比例、换图流程 |
| `seo-research` | 查关键词、导出 GSC 数据、更新 SEO 指标/台账 | GSC 导出、关键词库、指标月报、数据位置 |

维护约定：流程或规则变化时，同步更新对应 `SKILL.md`（必要时 `references/`）与根目录 `AGENTS.md`，保持三处一致。
