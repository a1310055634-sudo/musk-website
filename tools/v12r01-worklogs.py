# -*- coding: utf-8 -*-
"""V12 R01: 生成两份工作册（引语 101 块核验册 + email 47 封在册核对册）。
底册：
  qa/v10-15/round-03/unmatched-itemized.tsv  （101 块，两列 id/reason_code）
  qa/v9-20/round-06/sources/emails.json      （47 封镜像 email 清单）
产出：
  qa/v12/round-01/quotes-worklog.tsv （五列 id/source/plan/note/verdict，verdict 留空）
  qa/v12/round-01/emails-worklog.tsv （六列 id/date/title/org/onsite/verdict）
只读底册、只写 qa/v12/round-01/，不碰任何页面。
"""
import io, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q_IN = os.path.join(ROOT, "qa", "v10-15", "round-03", "unmatched-itemized.tsv")
E_IN = os.path.join(ROOT, "qa", "v9-20", "round-06", "sources", "emails.json")
OUT_DIR = os.path.join(ROOT, "qa", "v12", "round-01")
DOCS = os.path.join(ROOT, "documents.html")

PLAN = {
    "other-official": "official page direct -> mirror /agents/search (first 8-12 EN words) -> EDGAR full-text",
    "earnings-call": "stockanalysis.com transcripts via WebFetch (Cloudflare blocks curl)",
    "edgar": "EDGAR full-text search (Archives, UA header required)",
    "jre": "wordpress six-part self-hosted transcript (elonmuskinterviews.wordpress.com)",
    "ted": "ted.com inline JSON field \"transcript\" (json.loads, no unicode_escape)",
}

def quotes():
    rows = []
    with io.open(Q_IN, encoding="utf-8") as f:
        header = f.readline().rstrip("\r\n").split("\t")
        assert header[:2] == ["id", "reason_code"], header
        for line in f:
            line = line.rstrip("\r\n")
            if not line.strip():
                continue
            parts = line.split("\t", 1)
            rid = parts[0]
            reason = parts[1] if len(parts) > 1 else ""
            key = reason.split("(")[0].strip()
            rows.append((rid, reason, PLAN.get(key, "mirror /agents/search + two-source")))
    out = os.path.join(OUT_DIR, "quotes-worklog.tsv")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("id\tsource\tplan\tverdict\tanchor_url\n")
        for rid, reason, plan in rows:
            f.write(f"{rid}\t{reason}\t{plan}\t\t\n")
    return len(rows)

def emails():
    data = json.load(io.open(E_IN, encoding="utf-8"))
    entries = data["entries"]
    doc_text = io.open(DOCS, encoding="utf-8").read()
    # 在册判定：documents.html 的日精度 doc id（d{YYYY-MM-DD}）与 email 日期对表
    doc_ids = set(re.findall(r'id="(d\d{4}-\d{2}-\d{2})', doc_text))
    rows = []
    for e in entries:
        date = e.get("date", "")
        onsite = "Y" if f"d{date}" in doc_ids else "?"
        rows.append((e.get("id", ""), date, e.get("title", ""), e.get("org", ""), onsite))
    out = os.path.join(OUT_DIR, "emails-worklog.tsv")
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("id\tdate\ttitle\torg\tonsite\tverdict\n")
        for r in rows:
            f.write("\t".join(r) + "\t\n")
    n_y = sum(1 for r in rows if r[4] == "Y")
    return len(rows), n_y

os.makedirs(OUT_DIR, exist_ok=True)
nq = quotes()
ne, ny = emails()
print(f"quotes-worklog.tsv: {nq} rows")
print(f"emails-worklog.tsv: {ne} rows, onsite-dated(Y)={ny}")
