#!/usr/bin/env python3
"""每月自动拉取 Google Search Console 全量数据并导出 CSV（突破 UI 1000 行限制）。

用法:
  # 首次运行会弹浏览器授权，自动生成 tools/gsc/token.json（已 gitignore）
  python3 tools/gsc_export.py --start 2026-10-01 --end 2026-10-31 --out tools/gsc/oct2026

  # 之后可指定 GSC 属性（域名属性用 sc-domain:spacemanmeow.com）
  python3 tools/gsc_export.py --site sc-domain:spacemanmeow.com --start 2026-11-01 --end 2026-11-30

输出:
  <out>_totals.json          整站汇总（clicks/impressions/ctr/position）
  <out>_query.csv            按搜索词（全量，分页）
  <out>_page.csv             按页面
  <out>_country.csv          按国家
  <out>_device.csv           按设备
  <out>_date.csv             按日期
  <out>_summary.json         汇总 + 各维度 Top 10（便于回填进度表）
"""
import argparse
import csv
import json
import os
import sys

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:
    sys.exit("缺少依赖，先运行: python3 -m pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib")

SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
CRED_FILE = os.path.join(os.path.dirname(__file__), "gsc", "credentials.json")
TOKEN_FILE = os.path.join(os.path.dirname(__file__), "gsc", "token.json")
ROW_LIMIT = 5000  # API 单次最大行数


def get_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(CRED_FILE, SCOPES)
        auth_url, _ = flow.authorization_url(prompt="consent")
        print("\n请在浏览器打开以下链接完成 Google 授权：\n" + auth_url + "\n", flush=True)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as f:
            f.write(creds.to_json())
        print("授权成功，token 已缓存到", TOKEN_FILE, flush=True)
    return build("searchconsole", "v1", credentials=creds)


def query_paginated(service, site, payload):
    """分页拉取某维度全部行，单页上限 ROW_LIMIT。"""
    rows = []
    start = 0
    while True:
        p = dict(payload)
        p["rowLimit"] = ROW_LIMIT
        p["startRow"] = start
        resp = service.searchanalytics().query(siteUrl=site, body=p).execute()
        batch = resp.get("rows", [])
        rows.extend(batch)
        if len(batch) < ROW_LIMIT:
            break
        start += ROW_LIMIT
    return rows


METRIC_KEYS = ["clicks", "impressions", "ctr", "position"]


def write_csv(path, rows, dims):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(dims + METRIC_KEYS)
        for r in rows:
            keys = r.get("keys", [])
            w.writerow(list(keys) + [fmt(r.get(m, 0)) for m in METRIC_KEYS])


def fmt(n):
    return round(n, 4) if isinstance(n, float) else n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="https://spacemanmeow.com/")
    ap.add_argument("--start", required=True)
    ap.add_argument("--end", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    service = get_service()
    base = {"startDate": args.start, "endDate": args.end}

    # 1) 整站汇总（无维度）
    totals = service.searchanalytics().query(
        siteUrl=args.site,
        body={**base, "rowLimit": 1},
    ).execute().get("rows", [{}])[0]
    totals_d = {
        "clicks": totals.get("clicks", 0),
        "impressions": totals.get("impressions", 0),
        "ctr": totals.get("ctr", 0),
        "position": totals.get("position", 0),
    }
    with open(args.out + "_totals.json", "w", encoding="utf-8") as f:
        json.dump(totals_d, f, indent=2, ensure_ascii=False)

    dims_map = {
        "query": ["query"],
        "page": ["page"],
        "country": ["country"],
        "device": ["device"],
        "date": ["date"],
    }
    summary = {"totals": totals_d, "top": {}}
    for name, dims in dims_map.items():
        p = {**base, "dimensions": dims}
        rows = query_paginated(service, args.site, p)
        write_csv(args.out + f"_{name}.csv", rows, dims)
        rows_sorted = sorted(rows, key=lambda r: r.get("clicks", 0), reverse=True)
        top = []
        for r in rows_sorted[:10]:
            item = {dims[i]: (r["keys"][i] if r.get("keys") else "") for i in range(len(dims))}
            item.update({m: fmt(r.get(m, 0)) for m in METRIC_KEYS})
            top.append(item)
        summary["top"][name] = top
        print(f"[ok] {name}: {len(rows)} 行 -> {args.out}_{name}.csv")

    with open(args.out + "_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print("\n==== 汇总 ====")
    print(json.dumps(totals_d, indent=2, ensure_ascii=False))
    print(f"Top queries: {len(summary['top']['query'])} shown in summary; full in CSV")


if __name__ == "__main__":
    main()
