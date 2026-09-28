# -*- coding: utf-8 -*-
"""R02 素材下载：按精确 Commons 文件名取 imageinfo，下载缩略图供目检。
用法: python tools/get-files.py
输出: /tmp/v7r2-review/*.jpg + 每图的完整许可元数据 JSON（assets-meta/）。"""
import json, os, sys, urllib.request, urllib.parse
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "trace_assets", os.path.join(os.path.dirname(os.path.abspath(__file__)), "trace-assets.py"))
_ta = importlib.util.module_from_spec(_spec)
sys.modules["trace_assets"] = _ta
_spec.loader.exec_module(_ta)
api, fetch = _ta.api, _ta.fetch

# 主选 + 备选（备选用于目检后择优）
FILES = [
    ("falcon-liftoff", "File:Falcon Heavy Demo Mission (39337245575).jpg"),
    ("starship-catch", "File:Starship Booster Landing on Mechzilla (54064036815).jpg"),
    ("x-hq-2022", "File:TwitterHeadquarters2022.jpg"),
    ("x-hq-2023", "File:Quo vadis, Twitter?-L1001307.jpg"),
    ("cybertruck-moab", "File:2024 Tesla Cybertruck, Moab.jpg"),
    ("cybertruck-denver", "File:2023 production-level Tesla Cybertruck on display in Denver, Colorado.jpg"),
]

OUT_REVIEW = os.path.join(os.environ.get("TEMP", "/tmp"), "v7r2-review")
OUT_META = "assets-meta"
os.makedirs(OUT_REVIEW, exist_ok=True)
os.makedirs(OUT_META, exist_ok=True)

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s or "").strip()

import re

for key, title in FILES:
    try:
        data = api({
            "action": "query", "titles": title, "prop": "imageinfo",
            "iiprop": "url|size|extmetadata", "iiurlwidth": "1200",
        })
        pages = data.get("query", {}).get("pages", {})
        page = next(iter(pages.values()), None)
        if not page or "imageinfo" not in (page or {}):
            print(f"MISS {key}: {title}")
            continue
        ii = page["imageinfo"][0]
        em = ii.get("extmetadata", {})
        meta = {
            "title": title,
            "descriptionurl": ii.get("descriptionurl"),
            "w": ii.get("width"), "h": ii.get("height"),
            "license": strip_tags(em.get("LicenseShortName", {}).get("value", "")),
            "license_url": em.get("LicenseUrl", {}).get("value", ""),
            "artist": strip_tags(em.get("Artist", {}).get("value", "")),
            "credit": strip_tags(em.get("Credit", {}).get("value", ""))[:200],
            "date": strip_tags(em.get("DateTimeOriginal", {}).get("value", "")),
            "desc": strip_tags(em.get("ImageDescription", {}).get("value", ""))[:300],
        }
        with open(os.path.join(OUT_META, key + ".json"), "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
        blob = fetch(ii["thumburl"])
        out = os.path.join(OUT_REVIEW, key + ".jpg")
        with open(out, "wb") as f:
            f.write(blob)
        print(f"OK   {key:18s} {len(blob):8d}B  {meta['w']}x{meta['h']}  {meta['license']}  | {meta['artist'][:60]}")
    except Exception as e:
        print(f"FAIL {key}: {str(e)[:120]}")

print("review dir:", OUT_REVIEW)
