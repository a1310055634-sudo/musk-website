# -*- coding: utf-8 -*-
"""R02 attribution audit: perceptually match pre-existing assets (portrait.jpg,
tesla-factory.jpg) against Wikimedia Commons candidates, and dump exact
extmetadata for the best hit so captions can be verified before commit.
Usage: python tools/verify-attrib.py
"""
import json, os, sys, io, urllib.request, urllib.parse
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "trace_assets", os.path.join(os.path.dirname(os.path.abspath(__file__)), "trace-assets.py"))
_ta = importlib.util.module_from_spec(_spec)
sys.modules["trace_assets"] = _ta
_spec.loader.exec_module(_ta)
api, fetch, sig, sig_file, hamming, mse = (
    _ta.api, _ta.fetch, _ta.sig, _ta.sig_file, _ta.hamming, _ta.mse)

UA = {"User-Agent": "MuskIncV7R02/1.0 (static site asset audit; contact: site owner)"}

def info_for(title):
    """Exact-file imageinfo incl. extmetadata + a 960px thumb URL."""
    data = api({
        "action": "query", "titles": title, "prop": "imageinfo",
        "iiprop": "url|size|extmetadata", "iiurlwidth": "960",
    })
    pages = data.get("query", {}).get("pages", {})
    for _, page in pages.items():
        ii = (page.get("imageinfo") or [{}])[0]
        em = ii.get("extmetadata") or {}
        def g(k):
            return (em.get(k) or {}).get("value", "")
        return {
            "title": page.get("title"),
            "w": ii.get("width"), "h": ii.get("height"),
            "thumburl": ii.get("thumburl"),
            "descurl": ii.get("descriptionurl"),
            "license": g("LicenseShortName"),
            "artist": g("Artist"),
            "credit": g("Credit"),
            "date": g("DateTimeOriginal"),
        }
    return None

def rank(local_path, terms, top=3):
    bits, pxs = sig_file(local_path)
    cands = []
    seen = set()
    for t in terms:
        for c in _ta.search_files(t, limit=8):
            if c["title"] in seen:
                continue
            seen.add(c["title"])
            try:
                b = fetch(c["thumburl"])
                cb, cpx = sig(b)
                cands.append((hamming(bits, cb), mse(pxs, cpx), c))
            except Exception as e:
                print("  fetch fail:", c.get("title", "?")[:50], repr(e)[:80])
    cands.sort(key=lambda x: (x[0], x[1]))
    return cands[:top]

def strip_html(s):
    import re as _re
    return _re.sub(r"<[^>]+>", "", s or "").strip()

def main():
    jobs = [
        ("assets/portrait.jpg", [
            "Elon Musk portrait 2015", "Elon Musk portrait Debbie Rowe",
            "Elon Musk headshot", "Elon Musk 2015",
        ]),
        ("assets/tesla-factory.jpg", [
            "Tesla factory Fremont Model S", "Tesla Fremont assembly 2011",
            "Tesla Model S factory Maurizio Pesce", "Tesla factory body assembly",
        ]),
    ]
    for path, terms in jobs:
        print("=" * 70)
        print("LOCAL:", path)
        for dist, err, c in rank(path, terms):
            print(f"  #{dist+0:3d} ham / mse {err:8.1f}  {c['title']}")
            print(f"       {c.get('w')}x{c.get('h')} | {c.get('license')} | {strip_html(c.get('artist',''))[:60]} | {c.get('date','')}")
        # exact metadata for the single best hit
        if cands_ok := rank(path, terms, top=1):
            best = cands_ok[0][2]
            meta = info_for(best["title"])
            print("  BEST-META:", json.dumps(meta, ensure_ascii=False, indent=2)[:1200])

if __name__ == "__main__":
    main()
