#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V9-20 R07 v3: 抽取镜像 keynote/speech 详情页 transcript（最终版）。

真实结构：<h2>Transcript</h2> 之后为说话人标签 + 若干 <button aria-label="Play from here">
块，每块含一句/多词（<span><span>word</span> </span> 重复）。按 button 整体剥标签保词序。
用法: python tools/v9r07-fetch-keynotes3.py <id> [id2 ...]
输出: qa/v9-20/round-07/sources/page-<id>.html（原始页）
      qa/v9-20/round-07/sources/tr-<id>.txt（可读全文：== Speaker == 后接段落行）
      qa/v9-20/round-07/sources/tr-<id>.joined.txt（去空白连体，关键词检索用）
"""
import re
import sys
import subprocess
from pathlib import Path
from collections import OrderedDict

BASE = "https://elonmuskarchive.org/video/{id}"
OUT = Path("qa/v9-20/round-07/sources")
OUT.mkdir(parents=True, exist_ok=True)

SP_RE = re.compile(
    r'<div class="mb-1 text-sm font-semibold text-accent">(.*?)</div>', re.S)
BTN_RE = re.compile(
    r'<button type="button" aria-label="Play from here".*?</button>', re.S)


def fetch(pid: str) -> str:
    dest = OUT / f"page-{pid}.html"
    if not dest.exists() or dest.stat().st_size < 5000:
        url = BASE.format(id=pid)
        r = subprocess.run(["curl", "-s", "--max-time", "60", url, "-o", str(dest)])
        if r.returncode != 0 or not dest.exists() or dest.stat().st_size < 5000:
            raise SystemExit(f"curl failed: {url}")
    return dest.read_text(encoding="utf-8", errors="replace")


def strip_tags(s: str) -> str:
    return re.sub(r"<[^>]+>", "", s)


def extract(html: str):
    i = html.find("Transcript</h2>")
    if i == -1:
        return OrderedDict(), "", ""
    seg = html[i:]
    events = []
    for m in SP_RE.finditer(seg):
        events.append((m.start(), "sp", strip_tags(m.group(1)).strip()))
    for m in BTN_RE.finditer(seg):
        txt = strip_tags(m.group(0))
        txt = re.sub(r"\s+", " ", txt).strip()
        events.append((m.start(), "btn", txt))
    events.sort(key=lambda e: e[0])
    speakers: OrderedDict = OrderedDict()
    joined = []
    cur = None
    for _, kind, val in events:
        if kind == "sp":
            cur = val
            speakers.setdefault(cur, [])
        elif val:
            speakers.setdefault(cur, []).append(val)
            joined.append(val)
    return speakers, "".join(joined), " ".join(joined)


def main():
    for pid in sys.argv[1:]:
        html = fetch(pid)
        speakers, joined, spaced = extract(html)
        out = OUT / f"tr-{pid}.txt"
        with out.open("w", encoding="utf-8") as f:
            for sp, paras in speakers.items():
                f.write(f"== {sp} ==\n")
                for p in paras:
                    f.write(p + "\n")
                f.write("\n")
        (OUT / f"tr-{pid}.joined.txt").write_text(joined, encoding="utf-8")
        musk = sum(len(p.split()) for s, ps in speakers.items() if "Elon Musk" in s)
        total = sum(len(p.split()) for ps in speakers.values() for p in ps)
        print(f"{pid}: speakers={len(speakers)} words={total} musk_words={musk} -> {out.name}")


if __name__ == "__main__":
    main()
