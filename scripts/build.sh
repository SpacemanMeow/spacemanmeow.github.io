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

echo "==> Building Pagefind search index"
# 本地预览时可用 SKIP_PAGEFIND=1 跳过（下载 57MB 二进制 + 索引 216 页很慢，纯改 CSS/模板无需）
if [ -n "${SKIP_PAGEFIND:-}" ]; then
  echo "⏭️ SKIP_PAGEFIND=1，跳过搜索索引生成（本地预览加速）"
elif command -v pagefind >/dev/null 2>&1; then
  pagefind --site _site
else
  PF_VER="1.3.0"
  PF_DIR=".pagefind-bin"
  OS=$(uname -s)
  ARCH=$(uname -m)
  case "$OS" in
    Linux)  TARGET="x86_64-unknown-linux-musl" ;;
    Darwin) TARGET="x86_64-apple-darwin" ;;
    *)      TARGET="" ;;
  esac
  if [ "$OS" = "Darwin" ] && [ "$ARCH" = "arm64" ]; then TARGET="aarch64-apple-darwin"; fi
  if [ -n "$TARGET" ] && [ ! -x "$PF_DIR/pagefind" ]; then
    URL="https://github.com/CloudCannon/pagefind/releases/download/v${PF_VER}/pagefind_extended-v${PF_VER}-${TARGET}.tar.gz"
    if curl -fsSL "$URL" -o /tmp/pagefind.tar.gz; then
      mkdir -p "$PF_DIR"
      tar -xzf /tmp/pagefind.tar.gz -C "$PF_DIR"
      # 扩展版二进制名为 pagefind_extended，统一重命名为 pagefind 以便后续调用
      if [ -f "$PF_DIR/pagefind_extended" ]; then mv "$PF_DIR/pagefind_extended" "$PF_DIR/pagefind"; fi
    else
      echo "⚠️ 无法下载 Pagefind 二进制，跳过搜索索引生成（部署环境会生成）"
    fi
  fi
  if [ -x "$PF_DIR/pagefind" ]; then
    "$PF_DIR/pagefind" --site _site
    # 保留缓存二进制（已在 .gitignore），下次构建复用，避免重复下载 57MB
  else
    echo "⚠️ Pagefind 不可用，跳过搜索索引（搜索功能在部署环境会生成）"
  fi
fi

echo "==> Done. Combined site in _site/ (EN at root, ZH at /zh/)"
