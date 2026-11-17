#!/usr/bin/env python3
"""从升级日志生成/更新 Release Note 页面（5 语言）。

日志由用户直接在对话中提供；seo/data/ 只是临时中转目录（已 gitignore，不长期保留）：
把收到的日志临时写入 seo/data/<app_slug>_release_note 再跑本脚本，处理完可删除。

用法：
  python3 skills/release-notes/scripts/update_release_notes.py <日志文件> [<日志文件2> ...]
  python3 skills/release-notes/scripts/update_release_notes.py                      # 处理 seo/data/*_release_note 全部文件

输入文件格式（Play Console 导出样式）：
  内部版本号 (版本名)
  <en-US>
  1. ...
  </en-US>
  <zh-CN>
  ...
  </zh-CN>

站点语言映射：en-US→en, zh-CN→zh, id→id, ms→ms, th→th。
日志文件命名：<app_slug（下划线）>_release_note，如 meow_money_manager_release_note
对应 app 目录下的 meow-money-manager（通过 _apps/*.md 的 slug 匹配，
不一致时用脚本内 SLUG_ALIASES 映射）。

**日志须自带全部 5 语言译文**（缺语言会生成空节）；收到日志后先把补全/修正的译文
直接整理进日志，再跑本脚本——不再依赖任何外部 fixes / 中间修正库。
以 "- " 开头的行渲染为上一项的子列表；多版本按版本号倒序。

本脚本不联网、不抓取；只解析本地文件并更新 _release_notes[_<lang>]/ 下的页面。
"""
import argparse
import glob
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
DATA_DIR = os.path.join(ROOT, "seo", "data")
SITE_LANGS = {"en-US": "en", "zh-CN": "zh", "id": "id", "ms": "ms", "ms-MY": "ms", "th": "th"}
LANGS = ["en", "zh", "id", "ms", "th"]
LANG_LABEL = {"en": "Release Notes", "zh": "更新日志", "id": "Catatan Rilis",
              "ms": "Nota Keluaran", "th": "บันทึกการอัปเดต"}
PLACEHOLDER = "请在此处输入或粘贴"
# 日志文件名（下划线）与 _apps slug 不一致时的映射
SLUG_ALIASES = {"meow_habit": "meow-habits", "meow_todo": "meow-todo-list",
                "meow_mood": "meow-mood-diary", "crosshair": "cross-hair"}
# 语言 → (apps 源目录, release notes 输出目录)
DIRS = {
    "en": ("_apps", "_release_notes"),
    "zh": ("_apps_zh", "_release_notes_zh"),
    "id": ("_apps_id", "_release_notes_id"),
    "ms": ("_apps_ms", "_release_notes_ms"),
    "th": ("_apps_th", "_release_notes_th"),
}


def parse_log(path):
    """解析日志文件，返回按版本降序的 [{vc, version, langs:{lang:[notes]}}]。

    兼容两种版本头：
      - "147 (11.11.1)"  → vc=147, ver=11.11.1
      - "8.0.0"           → vc=-1（按出现顺序降序，实际用序号保证排在后面）, ver=8.0.0
    """
    text = open(path, encoding="utf-8").read()
    # 版本头：数字(版本号) 或 纯版本号（x.y.z）
    head = re.compile(r"^(?:(\d+)\s+\(([^)]+)\)|(\d+(?:\.\d+)+))\s*$", re.M)
    markers = list(head.finditer(text))
    versions = []
    seq = 0
    for i, mk in enumerate(markers):
        p = text[mk.end():markers[i + 1].start() if i + 1 < len(markers) else len(text)]
        if mk.group(1):
            vc, ver = int(mk.group(1)), mk.group(2)
        else:
            vc, ver = -1000 + seq, mk.group(3)
        seq += 1
        per_lang = {}
        for tag, lang in SITE_LANGS.items():
            b = re.search(r"<%s>(.*?)</%s>" % (tag, tag), p, re.S)
            if not b:
                continue
            raw = b.group(1).strip()
            if PLACEHOLDER in raw:
                continue
            lines = [re.sub(r"^\d+\s*[.)]\s*", "", ln.strip())
                     for ln in raw.splitlines() if ln.strip()]
            lines = [ln for ln in lines if ln]
            if lines:
                per_lang[lang] = lines
        versions.append({"vc": int(vc), "version": ver, "langs": per_lang})
    versions.sort(key=lambda v: v["vc"], reverse=True)
    return versions


def find_app(slug_underscore):
    """从 seo/data 文件名（下划线）找到 _apps 中的 slug（连字符）与各语言 title。"""
    slug = SLUG_ALIASES.get(slug_underscore, slug_underscore.replace("_", "-"))
    path = os.path.join(ROOT, "_apps", slug + ".md")
    if not os.path.exists(path):
        return None
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^title:\s*(.+)$", text, re.M)
    title = m.group(1).strip() if m else slug
    title = re.split(r"\s+#", title, maxsplit=1)[0].strip().strip('"\'')
    play = re.search(r"^google_play:\s*(\S+)", text, re.M)
    store = re.search(r"^app_store:\s*(\S+)", text, re.M)
    store_url = store.group(1) if store else ""
    if store_url in ("#", ""):
        store_url = ""
    return {"slug": slug, "title_en": title,
            "play": play.group(1) if play else "", "store": store_url}


def local_title(app, lang):
    """从对应语言的 _apps_<lang>/<slug>.md 取本地化标题；缺失则用英文。"""
    apps_dir = DIRS[lang][0]
    path = os.path.join(ROOT, apps_dir, app["slug"] + ".md")
    if os.path.exists(path):
        text = open(path, encoding="utf-8").read()
        m = re.search(r"^title:\s*(.+)$", text, re.M)
        if m:
            return re.split(r"\s+#", m.group(1).strip(), maxsplit=1)[0].strip().strip('"\'')
    return app["title_en"]


def build_page(app, lang, versions):
    label = LANG_LABEL[lang]
    title = local_title(app, lang) + " — " + label
    fm = [
        "---", "layout: release-note",
        "title: %s" % json.dumps(title, ensure_ascii=False),
        "app_slug: %s" % app["slug"],
        "app_title: %s" % json.dumps(local_title(app, lang), ensure_ascii=False),
        "google_play: %s" % app["play"],
        # 单端 App 必须写 app_store: ""，裸空值会让 YAML 吞掉下一行 lang，破坏 hreflang
        "app_store: %s" % (app["store"] if app["store"] else '""'),
        "lang: %s" % lang,
        "seo:", "  type: WebPage", "---", "",
    ]
    body = ["<!-- 由 skills/release-notes/scripts/update_release_notes.py 从 seo/data 日志文件生成，请勿手工编辑 -->", ""]
    versions = [v for v in versions if v["langs"].get(lang)]
    for v in versions:
        body += ["## " + v["version"], ""]
        n = 0
        for line in v["langs"][lang]:
            if line.startswith("- "):
                # 以 "- " 开头的行作为上一项的子列表项（如传感器清单），不单独编号
                if n == 0:
                    body.append(line)  # 无父项时作为独立无序列表
                else:
                    body.append("    " + line)
            else:
                n += 1
                body.append("%d. %s" % (n, line))
        body.append("")
    # 返回应用链接由 layout（release-note.html）统一提供，正文不再重复
    return "\n".join(fm + body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", help="日志文件；省略则处理 seo/data/*_release_note 全部")
    args = ap.parse_args()

    files = args.files or sorted(glob.glob(os.path.join(DATA_DIR, "*_release_note")))
    if not files:
        raise SystemExit("没有找到日志文件（seo/data/*_release_note）")

    for path in files:
        key = os.path.basename(path)
        app_key = key[:-len("_release_note")] if key.endswith("_release_note") else key
        print("== %s" % key)
        app = find_app(app_key)
        if not app:
            print("  ! 未找到对应 app（_apps/%s.md），跳过" % app_key.replace("_", "-"))
            continue
        versions = parse_log(path)
        if not versions:
            print("  ! 未解析到任何版本，跳过")
            continue
        missing = [l for l in LANGS if not any(v["langs"].get(l) for v in versions)]
        if missing:
            print("  ! 以下语言缺失（将生成仅含其它语言的页面）: %s" % ",".join(missing))
        for lang in LANGS:
            out_dir = os.path.join(ROOT, DIRS[lang][1])
            os.makedirs(out_dir, exist_ok=True)
            out = os.path.join(out_dir, app["slug"] + ".md")
            with open(out, "w", encoding="utf-8") as f:
                f.write(build_page(app, lang, versions))
        print("  -> %d 个版本 × 5 语言页面已生成" % len(versions))


if __name__ == "__main__":
    main()
