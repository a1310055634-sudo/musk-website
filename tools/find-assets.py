# -*- coding: utf-8 -*-
"""R02 素材选型：falcon-heavy 定向比对 + 新素材候选清单。
用法: python tools/find-assets.py
输出: falcon 比对排名 + 新素材候选（标题/许可/作者/尺寸/缩略URL），供人工挑选下载。"""
import io, json, os, re, sys, urllib.request, urllib.parse
import importlib.util
from PIL import Image

_spec = importlib.util.spec_from_file_location(
    "trace_assets", os.path.join(os.path.dirname(os.path.abspath(__file__)), "trace-assets.py"))
_ta = importlib.util.module_from_spec(_spec)
sys.modules["trace_assets"] = _ta
_spec.loader.exec_module(_ta)
api, fetch, sig, sig_file, hamming, mse, search_files = (
    _ta.api, _ta.fetch, _ta.sig, _ta.sig_file, _ta.hamming, _ta.mse, _ta.search_files)

FALCON_TERMS = [
    "Falcon Heavy Demo Mission liftoff",
    "Falcon Heavy Demo Mission",
    "Falcon Heavy first launch",
    "Falcon Heavy lift off 2018",
]

NEW_TERMS = {
    "starship-catch": [
        "Starship booster catch tower", "Starship IFT-5 catch",
        "SpaceX Starship flight 5 booster catch", "Starship Fifth Flight catch",
    ],
    "x-hq": [
        "X headquarters San Francisco sign", "Twitter headquarters sign San Francisco",
        "X corp headquarters", "Twitter HQ signage",
    ],
    "tesla-product": [
        "Tesla Cybertruck 2023", "Tesla Model 3 2023 front",
    ],
    "gigafactory": [
        "Gigafactory Nevada aerial", "Tesla Gigafactory Texas",
    ],
    "musk-starship": [
        "Elon Musk Starship", "Elon Musk SpaceX 2024",
    ],
}

def list_candidates(key, terms, limit=6):
    seen, uniq = set(), []
    for t in terms:
        for c in search_files(t, limit=limit):
            if c["title"] not in seen:
                seen.add(c["title"])
                uniq.append(c)
    print(f"\n=== NEW {key} ===")
    for c in uniq:
        w, h = c["w"], c["h"]
        orient = "land" if w and h and w > h else ("port" if w and h and w < h else "?")
        print(f"  - {c['title']}")
        print(f"      {w}x{h} {orient} | {c['license']} | {c['artist'][:70]} | {c['date'][:40]}")

def falcon_hunt():
    path = os.path.join("assets", "falcon-heavy.jpg")
    bits, pxs = sig_file(path)
    seen, uniq = set(), []
    for t in FALCON_TERMS:
        for c in search_files(t, limit=8):
            if c["title"] not in seen:
                seen.add(c["title"])
                uniq.append(c)
    print(f"=== falcon-heavy vs {len(uniq)} candidates ===")
    scored = []
    for c in uniq:
        if not c.get("thumburl"):
            continue
        try:
            tb = fetch(c["thumburl"])
        except Exception as e:
            print("   fetch fail", c["title"], str(e)[:80])
            continue
        b2, p2 = sig(tb)
        scored.append((hamming(bits, b2), mse(pxs, p2), c))
    scored.sort(key=lambda t: (t[0], t[1]))
    for hb, ms, c in scored[:5]:
        print(f"  diff={hb:3d}bits mse={ms:8.1f} | {c['title']}")
        print(f"       {c['w']}x{c['h']} | {c['license']} | {c['artist'][:70]}")

if __name__ == "__main__":
    falcon_hunt()
    for key, terms in NEW_TERMS.items():
        list_candidates(key, terms)
