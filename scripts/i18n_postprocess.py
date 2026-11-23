#!/usr/bin/env python3
"""Post-build i18n processor.

Scans the combined `_site/` output, then for every HTML page:
  * injects <link rel="alternate" hreflang="..."> tags into <head> (idempotent),
  * writes a single combined sitemap.xml with xhtml:link alternates.

Language detection: the root is the default (english); any top-level
two-letter directory under _site/ (e.g. _site/zh) is treated as that language.
Pages are matched across languages by their slug (path without the language
prefix), so /posts/foo/ and /zh/posts/foo/ become alternates of each other.
"""
import os
import re
import sys
import argparse
import xml.etree.ElementTree as ET

SITE = "_site"
DEFAULT_LANG = "en"


def esc(value):
    """Escape for XML text and HTML attribute contexts (URLs may contain &)."""
    return (value.replace("&", "&amp;")
                 .replace("<", "&lt;")
                 .replace(">", "&gt;")
                 .replace('"', "&quot;"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True, help="Production site URL, e.g. https://spacemanmeow.com")
    args = ap.parse_args()
    base = args.url.rstrip("/")

    # Discover languages: default (root) + two-letter subdirs of _site
    langs = [DEFAULT_LANG]
    for name in sorted(os.listdir(SITE)):
        p = os.path.join(SITE, name)
        if os.path.isdir(p) and re.match(r"^[a-z]{2}$", name):
            langs.append(name)
    print("Languages detected:", langs)

    pages = []  # {path, lang, key, url}
    for root, _dirs, files in os.walk(SITE):
        for f in files:
            if not f.endswith(".html"):
                continue
            # 404.html 是错误页，不应进入 sitemap（否则 Google 会把它当正常页收录），也不注入 hreflang
            if f == "404.html":
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, SITE)
            parts = rel.split(os.sep)
            if parts[0] in langs and parts[0] != DEFAULT_LANG:
                lang = parts[0]
                rest = parts[1:]
            else:
                lang = DEFAULT_LANG
                rest = parts
            # URL keeps the language prefix (e.g. /zh/posts/foo/); the grouping
            # key strips it so /posts/foo/ and /zh/posts/foo/ are alternates.
            url_path = "/" + "/".join(parts)
            url_path = re.sub(r"index\.html$", "", url_path)
            if url_path == "":
                url_path = "/"
            abs_url = base + url_path
            key = ("/" + "/".join(rest)).replace("index.html", "").strip("/")
            pages.append({"path": full, "lang": lang, "key": key, "url": abs_url})

    groups = {}
    for pg in pages:
        groups.setdefault(pg["key"], []).append(pg)

    link_re = re.compile(r"<!-- i18n-hreflang -->.*?<!-- /i18n-hreflang -->", re.S)

    injected = refreshed = 0
    failures = []
    missing_en_pages = []
    for pg in pages:
        grp = groups.get(pg["key"], [])
        en = next((g for g in grp if g["lang"] == DEFAULT_LANG), None)
        if en is None:
            missing_en_pages.append(pg["path"])
            en_url = grp[0]["url"]
        else:
            en_url = en["url"]
        alts = []
        for g in grp:
            alts.append(f'  <link rel="alternate" hreflang="{g["lang"]}" href="{esc(g["url"])}" />')
        alts.append(f'  <link rel="alternate" hreflang="x-default" href="{esc(en_url)}" />')
        block = "<!-- i18n-hreflang -->\n" + "\n".join(alts) + "\n  <!-- /i18n-hreflang -->\n"

        with open(pg["path"], "r", encoding="utf-8") as fh:
            html = fh.read()
        if link_re.search(html):
            html = link_re.sub(block.strip() + "\n", html)
            refreshed += 1
        elif "</head>" in html:
            html = html.replace("</head>", block + "</head>", 1)
            injected += 1
        else:
            failures.append(pg["path"])
            continue
        with open(pg["path"], "w", encoding="utf-8") as fh:
            fh.write(html)

    # Combined sitemap: one <url> per language variant, each listing all alternates.
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
          '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for _key, grp in sorted(groups.items()):
        en_url = next((g["url"] for g in grp if g["lang"] == DEFAULT_LANG), grp[0]["url"])
        for g in grp:
            sm.append("  <url>")
            sm.append(f"    <loc>{esc(g['url'])}</loc>")
            for g2 in grp:
                sm.append(f"    <xhtml:link rel=\"alternate\" hreflang=\"{g2['lang']}\" href=\"{esc(g2['url'])}\" />")
            sm.append(f"    <xhtml:link rel=\"alternate\" hreflang=\"x-default\" href=\"{esc(en_url)}\" />")
            sm.append("  </url>")
    sm.append("</urlset>")
    sitemap_path = os.path.join(SITE, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(sm) + "\n")
    try:
        ET.parse(sitemap_path)
    except ET.ParseError as e:
        failures.append(sitemap_path + f" (XML: {e})")

    # Remove per-language sub-sitemaps to avoid duplicate submission.
    for lang in langs:
        if lang == DEFAULT_LANG:
            continue
        sp = os.path.join(SITE, lang, "sitemap.xml")
        if os.path.exists(sp):
            os.remove(sp)

    single = sorted(k for k, g in groups.items() if len(g) == 1)
    no_en = sorted(k for k, g in groups.items()
                   if not any(p["lang"] == DEFAULT_LANG for p in g))
    print(f"Groups {len(groups)} | single-language {len(single)} | missing-EN {len(no_en)}")
    if single:
        print(f"  WARN single-language groups ({len(single)}): {single[:8]}")
    if no_en:
        print(f"  WARN missing-EN groups ({len(no_en)}): {no_en[:8]}"
              " — x-default fell back to first available variant")
    if missing_en_pages:
        print(f"  WARN {len(missing_en_pages)} pages have no EN variant"
              f" (e.g. {missing_en_pages[:3]})")
    print(f"hreflang injected {injected}, refreshed {refreshed}, failed {len(failures)}")
    print(f"Processed {len(pages)} pages across {len(langs)} languages.")

    if failures:
        print(f"FATAL: post-processing failed on {len(failures)} target(s):", file=sys.stderr)
        for p in failures[:10]:
            print("  " + p, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
