#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V9-20 R07 v2: 抽取镜像 keynote/speech 详情页 transcript（逐词 span 序列化）。

按说话人分组拼词；同时产出检索用连体文本。输出摘要统计+全文 txt。
用法: python tools/v9r07-fetch-keynotes2.py <id> [id2 ...]
输出: qa/v9-20/round-07/sources/page-<id>.html（原始页）
      qa/v9-20/round-07/sources/tr-<id>.txt（可读全文，[speaker] 段落）
      qa/v9-20/round-07/sources/tr-<id>.joined.txt（去空格连体，检索用）
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
WRAP_RE = re.compile(r'<span class="whitespace-pre-wrap[^"]*">(.*?)</span>', re.S)


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
    speakers, joined = OrderedDict(), []
    pos = 0
    events = []
    for m in SP_RE.finditer(seg):
        events.append((m.start(), "sp", strip_tags(m.group(1)).strip()))
    for m in WRAP_RE.finditer(seg):
        # 只取 Transcript 区块内（下一个 h2 或文档主体前 3MB 内全部）
        events.append((m.start(), "w", strip_tags(m.group(1))))
    events.sort(key=lambda e: e[0])
    for _, kind, val in events:
        if kind == "sp":
            cur = val
            speakers.setdefault(cur, [])
        else:
            w = val.strip()
            if w:
                speakers.setdefault(cur, []).append(w)
                joined.append(w)
    return speakers, "".join(joined), " ".join(joined)


def main():
    for pid in sys.argv[1:]:
        html = fetch(pid)
        res = extract(html)
        if len(res) == 2:
            speakers, joined = res, ""
        else:
            speakers, joined, spaced = res
        out = OUT / f"tr-{pid}.txt"
        with out.open("w", encoding="utf-8") as f:
            for sp, words in speakers.items():
                f.write(f"== {sp} ({len(words)}w)\n{' '.join(words)}\n\n")
        (OUT / f"tr-{pid}.joined.txt").write_text(joined, encoding="utf-8")
        musk = sum(len(w) for s, w in speakers.items() if "Elon Musk" in s)
        print(f"{pid}: speakers={len(speakers)} words={sum(len(w) for w in speakers.values())} musk_words={musk}")


if __name__ == "__main__":
    main()
