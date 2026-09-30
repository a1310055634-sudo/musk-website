# -*- coding: utf-8 -*-
"""V9-20 R04: fetch official transcripts from elonmuskarchive.org Agent API.

Four plan-R04 candidates (all anchored in the mirror's interview library):
  satellite-2020-keynote-2020-03-09 / starbase tour part 1-3 (2021-07-30) /
  code-conference-2016-06-01 / recode-decode-with-kara-swisher-2018-11-02.
Output: _tmp_r04/sources/<id>.json + one .txt excerpt each.
"""
import json, io, os, time, urllib.request

UA = {"User-Agent": "musk-inc-local/8.3.0"}
OUT = "_tmp_r04/sources"
os.makedirs(OUT, exist_ok=True)

ids = [
    "satellite-2020-keynote-2020-03-09",
    "starbase-tour-with-everyday-astronaut-part-1-2021-07-30",
    "starbase-tour-with-everyday-astronaut-part-2-2021-07-30",
    "starbase-launchpad-tour-part-3-2021-07-30",
    "code-conference-2016-06-01",
    "recode-decode-with-kara-swisher-2018-11-02",
]

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(io.TextIOWrapper(r, encoding="utf-8"))

def main():
    for i in ids:
        try:
            d = fetch(f"https://elonmuskarchive.org/agents/transcript/{i}")
        except Exception as e:
            print(f"[{i}] FETCH FAIL: {e}")
            time.sleep(1.0)
            continue
        io.open(f"{OUT}/{i}.json", "w", encoding="utf-8").write(
            json.dumps(d, ensure_ascii=False, indent=1))
        # transcript body: try common fields
        body = None
        for k in ("transcript", "text", "content", "body", "transcriptText"):
            v = d.get(k)
            if isinstance(v, str) and len(v) > 200:
                body = v
                break
        keys = ",".join(d.keys())
        print(f"[{i}] keys={keys}")
        print(f"    date={d.get('date')} title={str(d.get('title'))[:60]}")
        if body:
            io.open(f"{OUT}/{i}.txt", "w", encoding="utf-8").write(body)
            print(f"    transcript chars={len(body)}")
        else:
            # dump structure of non-str transcript fields for inspection
            for k, v in d.items():
                if isinstance(v, list):
                    print(f"    {k}: list[{len(v)}] sample={str(v[:2])[:150]}")
        time.sleep(0.8)

if __name__ == "__main__":
    main()
