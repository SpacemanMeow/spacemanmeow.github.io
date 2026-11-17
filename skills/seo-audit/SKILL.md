---
name: seo-audit
description: 通过提取并执行 seo/SITE-AUDIT.md 中内嵌的 Python 脚本来运行全站 SEO 验收审计（D01–D20 维度）。在任何内容/模板/路由改动后、验证构建是否通过站点规则时，或某个 SEO 维度失败时使用。
---

# SEO 审计（SITE-AUDIT.md）

## 何时运行

在对内容、模板、配置、路由、多语言、图片或 Release Note 做任何改动之后。也在宣布任务完成之前。先做完整构建 — 见 `skills/site-build-deploy/SKILL.md`。

## 如何运行审计脚本

`seo/SITE-AUDIT.md` 在标记 `<!-- AUDIT-SCRIPT-START -->` 与 `<!-- AUDIT-SCRIPT-END -->` 之间包含一段完整的 Python 脚本（目前约在第 337–729 行）。提取 `<<'PY'` 与结尾 `PY` 之间的代码，然后从仓库根目录执行：

```bash
python3 - <<'PY'
import io, sys
s = open('seo/SITE-AUDIT.md', encoding='utf-8').read()
py = s.split('<!-- AUDIT-SCRIPT-START -->')[1].split('<!-- AUDIT-SCRIPT-END -->')[0].split("<<'PY'")[1].rsplit('PY', 1)[0]
buf = io.StringIO(); old = sys.stdout; sys.stdout = buf
try:
    exec(py)
except Exception as e:
    sys.stdout = old; print('ERROR', repr(e)); sys.exit(1)
sys.stdout = old
out = buf.getvalue()
for line in out.splitlines():
    if line.startswith('FAIL') or line.startswith('汇总'):
        print(line)
PY
```

排查失败时阅读完整输出，而不只是汇总。

## 输出解读

- 每项检查带维度代码输出 `PASS` / `FAIL` / `WARN`。
- `BASE` 必须为空 — 非空值表示已登记的已知欠账（见 SITE-AUDIT §2.3）。
- 目标：`{PASS: N, FAIL: 0, WARN: 0}`。
- 已知假阳性：**在 `SKIP_PAGEFIND=1` 快速构建下 D12（Pagefind 索引）会 FAIL**。重新完整构建即可消除。

## 维度一览

| 代码 | 领域 |
|---|---|
| D01 | 构建产物 / 站点结构 |
| D02 | 链接 |
| D03 | 多语言数量核对 |
| D04 | 路由隔离 |
| D05 | hreflang / sitemap / canonical |
| D06 | frontmatter / 标语 |
| D07 | 正文内容 |
| D08 | 图片 / 无障碍 |
| D09 | 关键词 |
| D10 | JSON-LD |
| D11 | 内链 |
| D12 | 搜索索引（Pagefind） |
| D13 | 合规 |
| D14 | 文件名红线 |
| D15 | 敏感文件 |
| D16 | 进度台账一致性 |
| D17 | 跨语言插图一致性 |
| D18 | 与英文的骨架/目录/插图位置一致性 |
| D19 | 标签一致性与相关文章匹配 |
| D20 | Release Note 覆盖与内链 |

每个维度的详细检查点在 SITE-AUDIT §4。最常触发的规则见 `references/dimensions.md`。

## 失败之后

修复底层源码/配置（绝不要改生成的 `_site/`），重新构建并再次运行审计。添加新规则时，要同时写入维度表（§3）、§4 说明和 §5 脚本 — 然后更新 `AGENTS.md` 和相应的 skill。
