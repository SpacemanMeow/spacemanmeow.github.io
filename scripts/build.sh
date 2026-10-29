#!/usr/bin/env bash
#
# 多语言合并构建脚本。
# 先构建英文站（根目录 -> _site/），再构建各语言并合并到 /<lang>/ 子目录，
# 最后注入 hreflang 并生成合并 sitemap。
#
# 关键点：每个语言的 permalink 自带 /<lang>/ 前缀（保证 page.url / canonical 正确），
# 因此构建时使用临时目录，再把其中的 /<lang>/ 部分拷入 _site/<lang>/，
# 避免 jekyll 清空 _site/ 时把英文站一起删掉。
#
# 用法： bash scripts/build.sh
#
set -euo pipefail
cd "$(dirname "$0")/.."

SITE_URL="${SITE_URL:-https://spacemanmeow.com}"
TMP_ZH=".jekyll-zh"

echo "==> Building EN (root)"
bundle exec jekyll build --config _config.yml

# 新增语言时，复制 _config_zh.yml 为 _config_<code>.yml 并改好源目录/子路径，
# 然后复制下面的 ZH 代码块（把 _config_zh.yml / $TMP_ZH / _site/zh 换成对应值）：
echo "==> Building ZH (/zh/)"
bundle exec jekyll build --config _config_zh.yml --destination "$TMP_ZH"
mkdir -p _site/zh
rsync -a --delete "$TMP_ZH/zh/" _site/zh/
rm -rf "$TMP_ZH"

# echo "==> Building JA (/ja/)"
# TMP_JA=".jekyll-ja"
# bundle exec jekyll build --config _config_ja.yml --destination "$TMP_JA"
# mkdir -p _site/ja
# rsync -a --delete "$TMP_JA/ja/" _site/ja/
# rm -rf "$TMP_JA"

echo "==> Injecting hreflang + combined sitemap"
python3 scripts/i18n_postprocess.py --url "$SITE_URL"

echo "==> Done. Combined site in _site/ (EN at root, ZH at /zh/)"
