# -*- coding: utf-8 -*-
"""V9-20 R03: fetch transcript JSON for the four new cards (+ note-cited posts)
from elonmuskarchive.org Agent API; save evidence to qa/v9-20/round-03/sources/.
"""
import json, io, time, urllib.request, os

BASE = "https://elonmuskarchive.org/agents/transcript"
OUTDIR = "qa/v9-20/round-03/sources"
UA = {"User-Agent": "musk-inc-local/8.3.0"}

IDS = [
    "x-1730283187127964138",  # p2023-11-30 First Cybertruck deliveries in 2 hours!
    "x-1730342317993701521",  # note-cite: Massive congrats to the incredible Tesla team
    "x-1752455348106166598",  # p2024-01-30 Never incorporate your company in the state of Delaware
    "x-1752491924848820595",  # note-cite: Should Tesla change its state of incorporation to Texas (01-31)
    "x-1752922071229722990",  # note-cite: The public vote is unequivocally in favor of Texas (02-01)
    "x-1812256998588662068",  # p2024-07-13 I fully endorse President Trump
    "x-1941584569523732930",  # p2025-07-05 By a factor of 2 to 1 ... America Party
    "x-1942003079521472760",  # note-cite: The America Party is needed to fight the Uniparty (07-06)
]

def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(io.TextIOWrapper(r, encoding="utf-8"))

os.makedirs(OUTDIR, exist_ok=True)
for pid in IDS:
    path = f"{OUTDIR}/{pid}.json"
    if os.path.exists(path):
        print(f"skip {pid} (exists)")
        continue
    d = fetch(f"{BASE}/{pid}")
    io.open(path, "w", encoding="utf-8").write(
        json.dumps(d, ensure_ascii=False, indent=1))
    print(f"{pid} date={d.get('date')} snowflake_utc={d.get('snowflake_utc')} "
          f"text[:70]={repr((d.get('text') or '')[:70])}")
    time.sleep(0.8)
print("DONE fetch ->", OUTDIR)
