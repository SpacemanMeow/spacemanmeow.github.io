---
name: release-notes
description: 根据用户在对话中直接提供的升级日志生成或更新 11 个 App × 5 种语言的 Release Note 页面。当用户发送 *_release_note 日志、要求新增/更新更新日志，或 SITE-AUDIT D20 失败时使用。
---

# Release Note 工作流

## 范围

55 个生成页面，分布于 `_release_notes/`、`_release_notes_zh/`、`_release_notes_id/`、`_release_notes_ms/`、`_release_notes_th/`。固定链接：`/[lang/]apps/<slug>/release-notes/`。这些页面是**生成产物** — 绝不要手工编辑。

## 真实数据源

用户**直接在对话中**发送升级日志。`seo/data/` 只是一个被 gitignore 的**临时中转目录** — 把日志写到这里、处理它，之后可以删除。不存在外部的 fixes/映射文件；日志本身必须包含全部五种语言。

## 流程（按顺序执行）

1. 把日志写到 `seo/data/<app_slug_underscore>_release_note`。
   - 格式：`内部版本号 (版本名)` 或纯版本号如 `8.0.0`，后跟语言块 `<en-US>`、`<zh-CN>`、`<id>`、`<ms>`、`<th>`。
   - 以 `- ` 开头的行会作为上一个条目的嵌套子列表渲染。
2. **在日志内部补全译文。** 用户发来的日志通常只有英文或英文+中文。把缺失的语言准确翻译出来，并直接在日志文件中修正不准确/语法错误的文本。五种语言必须齐全 — 缺一种会产生空栏目，D20 会失败。
3. **运行生成器**：
   ```bash
   python3 skills/release-notes/scripts/update_release_notes.py                 # 处理 seo/data/ 中的所有日志
   python3 skills/release-notes/scripts/update_release_notes.py seo/data/xxx_release_note   # 只处理单个日志
   ```
   脚本会把日志文件名映射到 app slug（下划线 → 连字符，四处不一致通过脚本内的 `SLUG_ALIASES` 处理），并从 `_apps*/<slug>.md` 读取每个 App 的本地化标题以及 Google Play / App Store 链接。
4. **构建并验证**：
   ```bash
   SKIP_PAGEFIND=1 bash scripts/build.sh
   # curl 5 种语言的 URL；确认 HTTP 200 且版本数符合预期
   # 运行 SITE-AUDIT 脚本；D20 必须全部 PASS
   ```
5. 可选：删除 `seo/data/` 中的临时日志。

## 关键规则

- 绝不要再引入外部的映射/fixes 文件 — 译文只存在于日志和生成页面中。
- `app_store: "#"` 或为空表示单平台；此时 Release Note 布局只显示 Google Play 链接。不要写一个空的 `app_store:` 行 — 要用 `app_store: ""`，否则 YAML 会把下面一行合并进来，破坏布局和 hreflang。
- 多版本页面使用 `## <version>` 小节，并显式使用 `1. 2. 3.` 编号。
- App 详情页在 `_layouts/app.html` 中链接到自己的 Release Note；「返回应用」链接只放在 `_layouts/release-note.html`（不要加到页面正文里）。

## 参考

App slug 别名和当前版本数见 `references/app-mappings.md`。
