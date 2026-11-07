#!/usr/bin/env bash
#
# 全站构建 + 链接校验（与 .github/workflows/pages-deploy.yml 同款）
# 5 语合并构建：EN 根目录 + /zh/ /id/ /th/ /ms/，含 hreflang、合并 sitemap、Pagefind。
#
# 用法：
#   bash tools/test.sh           完整构建 + htmlproofer（发布前验收）
#   bash tools/test.sh --fast    跳过 Pagefind，本地快速验收
#   bash tools/test.sh -h        查看帮助
#
# 依赖：html-proofer、jekyll（bundle install）、python3。
# 全站静态教研（D01–D18）另见 seo/SITE-AUDIT.md §5 的一键脚本。

set -euo pipefail

cd "$(dirname "$0")/.."

help() {
  echo "全站构建 + 链接校验（5 语合并，与 CI 同款）"
  echo
  echo "Usage:"
  echo "   bash $0 [--fast]"
  echo
  echo "Options:"
  echo "     --fast     设置 SKIP_PAGEFIND=1，跳过搜索索引生成"
  echo "     -h, --help 显示本帮助"
  echo
  echo "验收一律用本脚本或 scripts/build.sh；单语预览请用 jekyll serve。"
}

fast=0
while (($#)); do
  case "$1" in
  --fast)
    fast=1
    shift
    ;;
  -h | --help)
    help
    exit 0
    ;;
  *)
    echo "未知参数: $1" >&2
    help >&2
    exit 1
    ;;
  esac
done

echo "==> 全站构建（EN + ZH + ID + TH + MS）"
if ((fast)); then
  JEKYLL_ENV=production SKIP_PAGEFIND=1 bash scripts/build.sh
else
  JEKYLL_ENV=production bash scripts/build.sh
fi

echo "==> htmlproofer（与 CI 同参数）"
bundle exec htmlproofer _site \
  --disable-external \
  --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/"

echo "==> 完成：_site/ 为 5 语合并产物，链接校验 0 failure"
