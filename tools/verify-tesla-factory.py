# -*- coding: utf-8 -*-
"""R02: verify tesla-factory.jpg attribution with throttling + 429 backoff.
One search call, one batched imageinfo call, throttled thumb fetches.
Usage: python tools/verify-tesla-factory.py
"""
import json, time, urllib.error
import importlib.util, os, sys, io

_spec = importlib.util.spec_from_file_location(
    "trace_assets", os.path.join(os.path.dirname(os.path.abspath(__file__)), "trace-assets.py"))
_ta = importlib.util.module_from_spec(_spec)
sys.modules["trace_assets"] = _ta
_spec.loader.exec_module(_ta)
fetch, sig, sig_file, hamming, mse = (
    _ta.fetch, _ta.sig, _ta.sig_file, _ta.hamming, _ta.mse)

def api_slow(params, tries=4):
    for i in range(tries):
        try:
            r = _ta.api(params)
            time.sleep(4)
            return r
        except urllib.error.HTTPError as e:
            if e.code == 429 and i < tries - 1:
                wait = 20 * (i + 1)
                print(f"  429, backoff {wait}s ...")
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("api failed")

def main():
    local = "assets/tesla-factory.jpg"
    bits, pxs = sig_file(local)
    print("searching ...")
    data = api_slow({
        "action": "query", "generator": "search",
        "gsrsearch": "Tesla factory Fremont Maurizio Pesce Model S",
        "gsrnamespace": "6", "gsrlimit": "12",
        "prop": "imageinfo", "iiprop": "url|size|extmetadata", "iiurlwidth": "640",
    })
    pages = list((data.get("query", {}).get("pages", {}) or {}).values())
    if not pages:
        print("no results"); return
    # rank by perceptual distance
    ranked = []
    for p in pages:
        ii = (p.get("imageinfo") or [{}])[0]
        tu = ii.get("thumburl")
        if not tu:
            continue
        try:
            b = fetch(tu)
        except Exception as e:
            print("  thumb fail:", p.get("title", "?")[:60], repr(e)[:60]); continue
        time.sleep(2)
        cb, cpx = sig(b)
        ranked.append((hamming(bits, cb), mse(pxs, cpx), p, ii))
    ranked.sort(key=lambda x: (x[0], x[1]))
    for d, e, p, ii in ranked[:4]:
        em = ii.get("extmetadata") or {}
        g = lambda k: (em.get(k) or {}).get("value", "")
        import re as _re
        artist = _re.sub(r"<[^>]+>", "", g("Artist")).strip()
        print(f"\n#{d:4d} ham / {e:9.1f} mse  {p.get('title')}")
        print(f"     {ii.get('width')}x{ii.get('height')} | {g('LicenseShortName')} | {artist[:70]} | {g('DateTimeOriginal')[:45]}")
        print(f"     {ii.get('descriptionurl','')}")
    if ranked:
        d, e, p, ii = ranked[0]
        em = ii.get("extmetadata") or {}
        g = lambda k: (em.get(k) or {}).get("value", "")
        meta = {
            "title": p.get("title"),
            "descriptionurl": ii.get("descriptionurl"),
            "w": ii.get("width"), "h": ii.get("height"),
            "license": g("LicenseShortName"),
            "license_url": g("LicenseUrl"),
            "artist": g("Artist"),
            "credit": g("Credit"),
            "date": g("DateTimeOriginal"),
            "desc": "White Model S body on red assembly carrier, Tesla Fremont factory (2011).",
            "match": f"perceptual hamming {d} / mse {e:.0f} at 32x32 (exact if 0)",
        }
        print("\nBEST-META JSON:")
        print(json.dumps(meta, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
