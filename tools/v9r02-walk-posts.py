# -*- coding: utf-8 -*-
"""V9-20 R02: walk elonmuskarchive.org Agent API for all 2020/2021 posts."""
import json, io, time, urllib.request, sys

BASE = "https://elonmuskarchive.org/agents/index"
FIELDS = "id,date,title,url"
OUT = "_tmp_r02/posts-all-{}.json"

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "musk-inc-local/8.2.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(io.TextIOWrapper(r, encoding="utf-8"))

def walk_year(year):
    all_entries = []
    for month in range(1, 13):
        offset = 0
        while True:
            url = (f"{BASE}?type=posts&year={year}&month={month:02d}&list=1&limit=1000"
                   f"&fields={FIELDS}&sort=date_asc&offset={offset}")
            d = fetch(url)
            entries = d.get("entries", [])
            all_entries.extend(entries)
            nxt = d.get("nextUrl")
            if not nxt or not entries:
                break
            offset += len(entries)
            time.sleep(0.4)
        time.sleep(0.3)
    # de-dup by id, keep order
    seen, uniq = set(), []
    for e in all_entries:
        if e["id"] not in seen:
            seen.add(e["id"])
            uniq.append(e)
    io.open(OUT.format(year), "w", encoding="utf-8").write(
        json.dumps(uniq, ensure_ascii=False, indent=1))
    dates = [e["date"] for e in uniq]
    print(f"{year}: raw={len(all_entries)} uniq={len(uniq)} "
          f"first={dates[0] if dates else '-'} last={dates[-1] if dates else '-'}")
    return uniq

if __name__ == "__main__":
    for y in (2020, 2021):
        walk_year(y)
