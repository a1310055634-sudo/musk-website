# -*- coding: utf-8 -*-
"""R02 素材溯源：在 Wikimedia Commons 搜索候选文件，与现有 assets 图片做感知比对。
用法: python tools/trace-assets.py
输出: 每张现有图的前 3 候选（文件名/尺寸/许可/作者/差异分数）+ 新素材候选清单。"""
import json, io, os, sys, urllib.request, urllib.parse
from PIL import Image

UA = {"User-Agent": "MuskIncV7R02/1.0 (static site asset audit; contact: site owner)"}
API = "https://commons.wikimedia.org/w/api.php"

def api(params):
    params = dict(params, format="json")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def sig(img_bytes, size=(32, 32)):
    im = Image.open(io.BytesIO(img_bytes)).convert("L").resize(size)
    px = list(im.getdata())
    mean = sum(px) / len(px)
    return [1 if p > mean else 0 for p in px], px

def sig_file(path):
    with open(path, "rb") as f:
        return sig(f.read())

def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))

def mse(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b)) / len(a)

def search_files(term, limit=6):
    data = api({
        "action": "query", "generator": "search",
        "gsrsearch": term, "gsrnamespace": "6", "gsrlimit": str(limit),
        "prop": "imageinfo",
        "iiprop": "url|size|extmetadata",
        "iiurlwidth": "960",
    })
    out = []
    for pid, page in (data.get("query", {}).get("pages", {}) or {}).items():
        ii = (page.get("imageinfo") or [{}])[0]
        if not ii.get("thumburl"):
            continue
        em = ii.get("extmetadata") or {}
        def meta(k):
            v = em.get(k, {}).get("value", "") or ""
            # strip html tags crudely
            import re
            return re.sub(r"<[^>]+>", "", v).strip()[:160]
        out.append({
            "title": page.get("title", ""),
            "thumburl": ii.get("thumburl"),
            "w": ii.get("width"), "h": ii.get("height"),
            "license": meta("LicenseShortName"),
            "artist": meta("Artist"),
            "credit": meta("Credit"),
            "date": meta("DateTimeOriginal"),
        })
    return out

def compare(target_path, candidates, top=3):
    bits, pxs = sig_file(target_path)
    scored = []
    for c in candidates:
        try:
            tb = fetch(c["thumburl"])
        except Exception as e:
            print("   fetch fail", c["title"], e)
            continue
        b2, p2 = sig(tb)
        scored.append((hamming(bits, b2), mse(pxs, p2), c))
    scored.sort(key=lambda t: (t[0], t[1]))
    return scored[:top]

EXISTING = {
    "portrait.jpg": [
        "Elon Musk portrait 2018", "Elon Musk official portrait",
        "Elon Musk SpaceX portrait",
    ],
    "falcon-heavy.jpg": [
        "Falcon Heavy demo mission liftoff", "Falcon Heavy launch LC-39A",
    ],
    "tesla-factory.jpg": [
        "Tesla factory Model S assembly", "Tesla Model S factory",
        "Tesla Fremont factory assembly",
    ],
}

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for fname, terms in EXISTING.items():
        if only and only not in fname:
            continue
        path = os.path.join("assets", fname)
        print(f"\n=== {fname} ({Image.open(path).size}) ===")
        cands = []
        for t in terms:
            res = search_files(t)
            print(f"  search: {t} -> {len(res)} files")
            cands.extend(res)
        # dedup by title
        seen, uniq = set(), []
        for c in cands:
            if c["title"] not in seen:
                seen.add(c["title"])
                uniq.append(c)
        for rank, (hb, ms, c) in enumerate(compare(path, uniq), 1):
            print(f"  #{rank} diff={hb:3d}bits mse={ms:8.1f} | {c['title']}")
            print(f"       {c['w']}x{c['h']} | license={c['license']} | artist={c['artist'][:80]}")
            print(f"       date={c['date'][:60]}")
