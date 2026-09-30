# -*- coding: utf-8 -*-
"""V9-20 R04: explore elonmuskarchive.org Agent API for interview candidates.

Plan R04 candidates: Code Conference 2016 (Swisher/Mossberg) /
Everyday Astronaut Starbase tour (filmed 2021-07-30) /
Kara Swisher Recode Decode 2018-11-02 / Satellite 2020 keynote (2020-03-09).
Output: _tmp_r04/explore.json (all raw hits kept for evidence).
"""
import json, io, time, urllib.request, urllib.parse, os

BASE = "https://elonmuskarchive.org/agents/search"
OUT = "_tmp_r04/explore.json"
UA = {"User-Agent": "musk-inc-local/8.3.0"}
os.makedirs("_tmp_r04", exist_ok=True)

QUERIES = [
    # (label, phrase, extra params)
    ("decode-2018", '"Recode Decode"', ""),
    ("decode-2018b", '"Kara Swisher"', "from=2018-10-01&to=2018-12-31"),
    ("satellite-2020", '"SATELLITE 2020"', ""),
    ("satellite-2020b", '"Satellite 2020"', "from=2020-03-01&to=2020-03-31"),
    ("ea-starbase", '"Everyday Astronaut"', ""),
    ("code-2016", '"Code Conference"', "from=2016-05-01&to=2017-12-31"),
    ("code-2016b", '"Mossberg"', "from=2016-01-01&to=2016-12-31"),
]

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(io.TextIOWrapper(r, encoding="utf-8"))

def main():
    out = {}
    for label, phrase, extra in QUERIES:
        q = urllib.parse.quote(phrase)
        u = f"{BASE}?q={q}&limit=20"
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
        for r in rs[:15]:
            print(f"   {r.get('type')} {r.get('id')} {r.get('date')} | {(r.get('title') or '')[:76]}")
        time.sleep(0.8)
    io.open(OUT, "w", encoding="utf-8").write(json.dumps(out, ensure_ascii=False, indent=1))
    print("saved ->", OUT)

if __name__ == "__main__":
    main()
