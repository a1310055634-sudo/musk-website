# -*- coding: utf-8 -*-
"""V9-20 R03: batch exact-phrase search on elonmuskarchive.org Agent API.

Candidates (plan R03): Delaware ruling response / Cybertruck delivery day /
Trump endorsement (mandated) / Grok versions / 2025 events.
Output: _tmp_r03/search-results.json (all raw hits kept for evidence).
"""
import json, io, time, urllib.request, urllib.parse

BASE = "https://elonmuskarchive.org/agents/search"
OUT = "_tmp_r03/search-results.json"
UA = {"User-Agent": "musk-inc-local/8.3.0"}

QUERIES = [
    # (label, phrase, extra params)
    ("trump-endorse", '"I fully endorse President Trump"', ""),
    ("delaware-never", '"Never incorporate your company in the state of Delaware"', ""),
    ("delaware-vote-tx", '"Should Tesla change its state of incorporation to Texas"', ""),
    ("cybertruck-day", '"Cybertruck"', "from=2023-11-30&to=2023-12-01"),
    ("grok3", '"Grok 3"', "from=2025-02-01&to=2025-03-01"),
    ("america-party", '"America Party"', "from=2025-06-01&to=2025-07-31"),
]

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(io.TextIOWrapper(r, encoding="utf-8"))

def main():
    out = {}
    for label, phrase, extra in QUERIES:
        q = urllib.parse.quote(phrase)
        u = f"{BASE}?q={q}&type=posts&limit=20"
        if extra:
            u += "&" + extra
        try:
            d = fetch(u)
        except Exception as e:
            print(f"[{label}] FETCH FAIL: {e}")
            out[label] = {"error": str(e)}
            time.sleep(1.0)
            continue
        rs = d.get("results", [])
        out[label] = {"phrase": phrase, "extra": extra,
                      "total": d.get("total"), "hits": rs}
        print(f"[{label}] total={d.get('total')} phrase={phrase} {extra}")
        for r in rs[:12]:
            print(f"   {r.get('id')} {r.get('date')} | {(r.get('title') or '')[:80]}")
        time.sleep(0.8)
    io.open(OUT, "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=1))
    print("saved", OUT)

if __name__ == "__main__":
    main()
