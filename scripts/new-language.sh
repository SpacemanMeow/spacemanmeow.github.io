#!/usr/bin/env bash
# ===================================================================
#  新增一门语言的多语言脚手架。
#
#  用法: bash scripts/new-language.sh <code> <label> [short]
#    code  两位小写语言码，必须与子路径一致，如 ja / de / fr  ->  /ja/
#    label 下拉菜单显示名，如 日本語
#    short 可选简称，默认同 label
#
#  自动完成：
#   1. 基于 _config_zh.yml 生成 _config_<code>.yml（替换 lang / 集合路径 / permalink / paginate_path）
#   2. 创建 _pages/<code>/、_posts/<code>/、_apps_<code>/、<code>/blog/ 目录与博客模板、首页
#   3. 在 _data/languages.yml 追加语言项
#   4. 为所有 _config_*.yml 的 exclude 补齐「其它语言源目录」排除项（数据驱动，自动算全）
#   5. 在 scripts/build.sh 追加该语言的「构建 + rsync 合并」块
#
#  之后只需翻译内容。i18n.js 已语言无关，无需改动。
# ===================================================================
set -euo pipefail
cd "$(dirname "$0")/.."

CODE="${1:-}"; LABEL="${2:-}"; SHORT="${3:-$LABEL}"
[[ -n "$CODE" && -n "$LABEL" ]] || { echo "用法: $0 <code> <label> [short]" >&2; exit 1; }
[[ "$CODE" =~ ^[a-z]{2}$ ]] || { echo "code 必须是两位小写字母，如 ja" >&2; exit 1; }
[[ -f "_config_$CODE.yml" ]] && { echo "_config_$CODE.yml 已存在，中止" >&2; exit 1; }

echo "==> 1. 生成 _config_$CODE.yml（基于 _config_zh.yml）"
sed -e "s/^lang: zh/lang: $CODE/" \
    -e "s#path: _pages/zh#path: _pages/$CODE#" \
    -e "s#apps_zh#apps_$CODE#g" \
    -e "s#path: _posts/zh#path: _posts/$CODE#" \
    -e "s#/zh/#/$CODE/#g" \
    -e "s#_site/zh#_site/$CODE#g" \
    "_config_zh.yml" > "_config_$CODE.yml"

echo "==> 2. 创建目录与模板"
mkdir -p "_pages/$CODE" "_posts/$CODE" "_apps_$CODE" "$CODE/blog"
cat > "_pages/$CODE/index.md" <<MD
---
layout: app-list
title: PLACEHOLDER
subtitle: PLACEHOLDER
nav: home
description: "PLACEHOLDER"
image: /assets/images/favicons/avatar.png
permalink: /$CODE/
---
MD
# 博客模板需要的是 index.html（不是 .md），且不应带 permalink（让目录路径自然产生 /<code>/blog/）
cat > "$CODE/blog/index.html" <<'HTML'
---
layout: blog
title: PLACEHOLDER
subtitle: PLACEHOLDER
nav: blog
description: "PLACEHOLDER"
image: /assets/images/favicons/avatar.png
---
HTML

echo "==> 3. 更新 _data/languages.yml"
grep -q "code: $CODE$" _data/languages.yml || cat >> _data/languages.yml <<YML

- code: $CODE
  label: $LABEL
  short: $SHORT
YML

echo "==> 4. 为所有 _config_*.yml 补齐 exclude（排除其它语言源目录）"
python3 - <<PY
import re, glob
code = "$CODE"
langs = sorted({re.match(r"_config_(.*)\.yml", f).group(1) for f in glob.glob("_config_*.yml")})
print("已知语言:", langs)

def excludes_for(owner):
    ex = []
    for x in langs:
        if x == owner:
            continue
        if x == "en":
            # 英文源在根级、无前缀
            ex += ["_apps/", "_posts/1*", "_posts/2*", "index.html", "blog/", "meow/"]
        else:
            ex += [f"_posts/{x}", f"_posts/{x}/**", f"_apps_{x}", f"_apps_{x}/**", f"{x}/", f"{x}/**"]
    return sorted(set(ex))

for f in glob.glob("_config_*.yml"):
    owner = re.match(r"_config_(.*)\.yml", f).group(1)
    needed = excludes_for(owner)
    lines = open(f, encoding="utf-8").read().split("\n")
    existing = set()
    in_ex = False
    for line in lines:
        if re.match(r"^exclude:\s*$", line):
            in_ex = True
            continue
        if in_ex:
            m = re.match(r"^\s*-\s+(.*)$", line)
            if m:
                existing.add(m.group(1).strip())
            else:
                in_ex = False
    add = [e for e in needed if e not in existing]
    if not add:
        print(f"  {f}: exclude 已完整，跳过")
        continue
    res, inserted = [], False
    for line in lines:
        res.append(line)
        if not inserted and re.match(r"^exclude:\s*$", line):
            for e in add:
                res.append(f"  - {e}")
            inserted = True
    open(f, "w", encoding="utf-8").write("\n".join(res))
    print(f"  {f}: 新增 exclude {add}")
PY

echo "==> 5. 在 scripts/build.sh 追加构建块"
python3 - "$CODE" <<'PY'
import sys
code = sys.argv[1]
codeu = code.upper()
f = "scripts/build.sh"
txt = open(f, encoding="utf-8").read()
if f"==> Building {code}" in txt:
    print("  build.sh 已含该语言块，跳过")
    sys.exit(0)
block = f'''
# 新增语言 {code} (/{code}/) —— 由 scripts/new-language.sh 生成
echo "==> Building {code} (/{code}/)"
TMP_{codeu}=".jekyll-{code}"
bundle exec jekyll build --config _config_{code}.yml --destination "$TMP_{codeu}"
mkdir -p _site/{code}
rsync -a --delete "$TMP_{codeu}/{code}/" _site/{code}/
rm -rf "$TMP_{codeu}"
'''
txt = txt.replace(
    'echo "==> Injecting hreflang + combined sitemap"',
    block + 'echo "==> Injecting hreflang + combined sitemap"',
    1,
)
open(f, "w", encoding="utf-8").write(txt)
print(f"  build.sh 已追加 {code} 构建块")
PY

echo "完成。请翻译 _pages/$CODE/、_posts/$CODE/、_apps_$CODE/ 下的内容，"
echo "并替换 $CODE/blog/index.html 与 _pages/$CODE/index.md 里的 PLACEHOLDER。"
