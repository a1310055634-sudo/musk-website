#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V9-20 R07: 拉取镜像 keynote/speech 库指定场次详情页并抽取 transcript 全文。

用法: python tools/v9r07-fetch-keynotes.py <id> [id2 ...]
输出: qa/v9-20/round-07/sources/page-<id>.html（原始页）
      qa/v9-20/round-07/sources/tr-<id>.txt（抽取文本：[mm:ss] 说话人: 段落）
"""
import re
import sys
import subprocess
from pathlib import Path

BASE = "https://elonmuskarchive.org/video/{id}"
OUT = Path("qa/v9-20/round-07/sources")
OUT.mkdir(parents=True, exist_ok=True)


def fetch(pid: str) -> str:
    dest = OUT / f"page-{pid}.html"
    if not dest.exists() or dest.stat().st_size < 5000:
        url = BASE.format(id=pid)
        r = subprocess.run(["curl", "-s", "--max-time", "60", url, "-o", str(dest)])
        if r.returncode != 0 or not dest.exists():
            raise SystemExit(f"curl failed: {url}")
    return dest.read_text(encoding="utf-8", errors="replace")


def extract(html: str) -> list:
    """返回 [(speaker, [para,...]), ...]；段落保持页面顺序。"""
    head_end = html.find("</head>")
    body = html[head_end:]
    m = re.search(r"<h2[^>]*>\s*Transcript\s*</h2>", body)
    if not m:
        return []
    body = body[m.end():]
    # transcript 区结束于主要 footer / 相关链接区，取到 </main> 或文档尾
    end = body.find("</main>")
    if end == -1:
        end = len(body)
    body = body[:end]
    items = []
    speaker = None
    # 说话人: <div class="mb-1 text-sm font-semibold text-accent">NAME</div>
    sp_re = re.compile(
        r'<div class="mb-1 text-sm font-semibold text-accent">(.*?)</div>', re.S)
    # 段落按钮: <button type="button" aria-label="Play from here" ...>…<div>text</div>…</button>
    btn_re = re.compile(
        r'<button type="button" aria-label="Play from here".*?</button>', re.S)
    pos = 0
    events = []
    for m in sp_re.finditer(body):
        events.append((m.start(), "sp", m.group(1)))
    for m in btn_re.finditer(body):
        events.append((m.start(), "btn", m.group(0)))
    events.sort(key=lambda e: e[0])
    for _, kind, val in events:
        if kind == "sp":
            speaker = re.sub(r"<[^>]+>", "", val).strip()
        else:
            seg = val
            tm = re.search(r"(\d{1,2}:)?\d{1,2}:\d{2}", seg)
            tstamp = tm.group(0) if tm else ""
            # 文本段在 button 内的最后一个 div；剥掉 timestamp span
            seg = re.sub(r"<span[^>]*>\s*(\d{1,2}:)?\d{1,2}:\d{2}\s*</span>", " ", seg)
            texts = re.findall(r"<(?:div|p)[^>]*>(.*?)</(?:div|p)>", seg, re.S)
            txt = ""
            for t in texts:
                t2 = re.sub(r"<[^>]+>", " ", t)
                t2 = re.sub(r"\s+", " ", t2).strip()
                if len(t2) > len(txt):
                    txt = t2
            if txt:
                items.append((speaker or "?", tstamp, txt))
    return items


def main():
    for pid in sys.argv[1:]:
        html = fetch(pid)
        items = extract(html)
        out = OUT / f"tr-{pid}.txt"
        with out.open("w", encoding="utf-8") as f:
            for sp, ts, txt in items:
                f.write(f"[{ts}] {sp}: {txt}\n")
        print(f"{pid}: {len(items)} paras -> {out}")


if __name__ == "__main__":
    main()
