# 历史多语言坑（来自 SEO-I18N-PLAYBOOK §7）

- **用了 page.lang 而不是 site.lang**：模板必须按构建级语言分支。使用 `page.lang` 会渲染到错误的根目录，并可能抛 `Cannot sort a null object`。
- **Jekyll 集合从 `_<label>` 递归读取**；`collections.*.path` 只改 URL，不改源目录。
- **exclude 正则**：不支持 `!ruby/regexp`；`*` 不跨 `/`。英文 App 目录必须写成带尾斜杠的 `_apps/`，文章写成 `_posts/1*`、`_posts/2*`。
- **new-language.sh 历史遗留**：遗漏 glossary 的 sed 替换；`feed.path` 丢失前导 `/`；未创建 glossary/exclude 条目；`404.html` 硬编码 `/zh/`；i18n.js 残留旧的双语言回退；从 zh 配置复制导致页脚是中文文案。
- **骨架漂移**：非英文文章偏离英文的 H2/H3/目录/插图位置 — D17/D18 就是为捕捉这种情况而设。
- **标签漂移**：产品标签变体会破坏相关文章匹配并拉入通用文章 — D19 就是为捕捉这种情况而设。
- **hreflang 整组跳过**：如果某组缺一种语言，i18n_postprocess 会静默跳过整组；检查生成的 HTML 中是否有 `<!-- i18n-hreflang -->` 标记。
