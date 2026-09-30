# -*- coding: utf-8 -*-
"""V9-20 R04: locate candidate quotes inside fetched transcripts (verbatim check)."""
import io, re, glob

NEEDLES = {
    "code-conference-2016-06-01": [
        r"billions.{0,40}base reality", r"one in billions", r"simulation",
        r"fundamental farewell", r"window of opportunity", r"make life multi",
    ],
    "recode-decode-with-kara-swisher-2018-11-02": [
        r"120[- ]hour", r"funding secured", r"sleep.{0,20}factory",
        r"pain level", r"excruciating",
    ],
    "starbase-tour-with-everyday-astronaut-part-1-202": [
        r"manufacturing is underrated", r"design is overrated", r"best part is no part",
        r"Raptor", r"the thing that s", r"aluminum.{0,30}steel",
    ],
    "starbase-tour-with-everyday-astronaut-part-2-202": [
        r"best part is no part", r"best process is no process", r"physics is law",
        r"Raptor", r"weight is down the tubes", r"dollars per ton",
    ],
    "starbase-launchpad-tour-part-3-2021-07-30": [
        r"best part is no part", r"cost per", r"rapidly reusable", r"Orbit",
    ],
    "satellite-2020-keynote-2020-03-09": [
        r"astronomical discoveries", r"fully and rapidly reusable",
        r"not bankrupt", r"30 billion",
    ],
}

def show(path, pat, ctx=260):
    s = io.open(path, encoding="utf-8", errors="replace").read()
    flat = re.sub(r"\s+", " ", s)
    hits = list(re.finditer(pat, flat, re.I))
    out = []
    for m in hits[:3]:
        a, b = max(0, m.start() - ctx), min(len(flat), m.end() + ctx)
        out.append(flat[a:b])
    return len(hits), out

for fid, pats in NEEDLES.items():
    path = f"_tmp_r04/sources/{fid}.txt"
    print("=" * 20, fid)
    for p in pats:
        n, snips = show(path, p)
        print(f"  [{n}] /{p}/")
        for sn in snips:
            print(f"      ...{sn}...")
