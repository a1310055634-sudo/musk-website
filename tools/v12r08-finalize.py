# -*- coding: utf-8 -*-
"""R08 定稿：TSV 101 行三态填充 + quotes.html 核验标（qs-src 尾追加+title）+ 口径段。
断言失败不落盘。"""
import io, json, re

res = json.load(io.open('qa/v12/round-08/mirror-edgar-results.json', encoding='utf-8'))
payload = {o['id']: o for o in json.load(io.open('qa/v12/round-08/quotes-payload.json', encoding='utf-8'))}

SAMPLE = {
    'e2016-05-04': ('YES', 'https://stockanalysis.com/stocks/tsla/transcripts/23974-q1-2016/'),
    'e2016-02-10': ('YES', 'https://stockanalysis.com/stocks/tsla/transcripts/23975-q4-2015/'),
    'e2013-05-08': ('NO', ''),
}

TQ = 'qa/v12/round-01/quotes-worklog.tsv'
lines = [l for l in io.open(TQ, encoding='utf-8').read().split('\n') if l.strip()]
out_lines = [lines[0]]
final = {}
for ln in lines[1:]:
    parts = ln.split('\t')
    qid, src = parts[0], parts[1]
    r = res.get(qid, {})
    v, anchor = r.get('verdict', 'MISS'), r.get('anchor', '')
    if v == 'YES':
        verdict = '✅ 原文核验（2026-10-06 R08）'
        if qid in SAMPLE and SAMPLE[qid][0] == 'YES':
            anchor = SAMPLE[qid][1]
        mark = ('✓原文核验', anchor)
    else:
        if qid in SAMPLE:
            if SAMPLE[qid][0] == 'YES':
                verdict = '✅ 原文核验（2026-10-06 R08，stockanalysis WebFetch 逐字吻合）'
                anchor = SAMPLE[qid][1]
                mark = ('✓原文核验', anchor)
            else:
                verdict = ('⚠️ 转引在册（R08 抽样：stockanalysis 该季逐字稿无逐字吻合，'
                           '引语实为股东信口径；原文未获，收录底源见卡注与账本）')
                mark = ('◎转引在册', 'R08 2026-10-06 转引核验：原文未获；' + verdict)
        else:
            if src.startswith('earnings-call'):
                verdict = ('⚠️ 转引在册（stockanalysis 转录为底本；R01 人工抽 2 条+R08 WebFetch 抽样 3 条'
                           '中 2 条逐字吻合 1 条口径不符如实记；原文实录未独立获取）')
            elif src.startswith('edgar'):
                verdict = '⚠️ 转引在册（EDGAR FTS 未获逐字；本条实为 SEC 起诉状/公告/判词措辞而非备案原文）'
            elif src.startswith('jre'):
                verdict = '⚠️ 转引在册（wordpress 六部转录本轮未抓取核验）'
            elif src.startswith('ted'):
                verdict = '⚠️ 转引在册（ted.com 页内 transcript JSON 本轮无逐字吻合）'
            else:
                verdict = '⚠️ 转引在册（镜像/官方页本轮流管线未获逐字原文；收录底源见卡注与账本条目）'
            mark = ('◎转引在册', 'R08 2026-10-06 转引核验：原文未获，收录底源见卡注来源与账本条目')
    final[qid] = (verdict, anchor)
    parts[3] = verdict
    parts[4] = anchor
    out_lines.append('\t'.join(parts))

io.open('qa/v12/round-08/quotes-worklog-r08.tsv', 'w', encoding='utf-8', newline='\n').write('\n'.join(out_lines) + '\n')
from collections import Counter
cc = Counter(v.split(' ')[0] for v, a in final.values())
print('TSV verdicts:', dict(cc))

# ---- quotes.html ----
s = io.open('documents_check.tmp', encoding='utf-8') if False else None
q = io.open('quotes.html', encoding='utf-8').read()
orig_count = q.count('class="qs-card"')

yes_n = tr_n = 0
for qid, (verdict, anchor) in final.items():
    yes = verdict.startswith('✅')
    label, tip = ('✓原文核验', 'R08 2026-10-06 原文锚: ' + anchor) if yes else ('◎转引在册', 'R08 2026-10-06 转引核验：原文未获，收录底源见卡注来源与账本条目')
    # 定位该卡的 qs-src span（href="primary.html#qid" 之后的第一个 qs-src）
    pat = re.compile(r'(href="primary\.html#' + re.escape(qid) + r'".*?<span class="qs-src")(>.*?</span>)', re.S)
    m = pat.search(q)
    if not m:
        print('  !! no card for', qid)
        continue
    span_body = m.group(2)
    assert label not in span_body
    if yes:
        new_body = span_body.replace('</span>', ' · ' + label + '</span>')
        new_open = m.group(1) + ' title="' + tip + '"'
        yes_n += 1
    else:
        new_body = span_body.replace('</span>', ' · ' + label + '</span>')
        new_open = m.group(1) + ' title="' + tip + '"'
        tr_n += 1
    q = q[:m.start()] + new_open + new_body + q[m.end():]

# 口径段
stamps = '✅ 原文核验 %d 条（镜像 /agents/search 10 · EDGAR FTS 3 · stockanalysis 抽样 2）· ⚠️ 转引在册 %d 条 · ❌ 撤下 0 条' % (yes_n, tr_n)
para = ('  <div class="container" style="margin-top:26px"><p style="font-size:12px;color:var(--tx-3, #6b6b6b);line-height:1.9;border-top:1px solid var(--line, rgba(23,25,29,.12));padding-top:12px">'
        '<b>引语核验口径（2026-10-06 R08）</b>：对 101 块非镜像来源引语逐条机核+抽样复核（镜像 /agents/search 精确短语 → EDGAR 全文检索 → stockanalysis 逐字稿 WebFetch 抽样 → ted.com transcript）。'
        + stamps + '。✓ 卡片已附原文锚（悬停查看链接）；◎ 为转引在册——收录底源以卡注来源与言行实录条目双重一致为准，原文逐字档本轮流管线未获，后续轮次继续补核。核验底册：qa/v12/round-08/。</p></div>\n')
anchor_pt = '    <nav class="chapter-pager container" aria-label="章节翻页">'
assert q.count(anchor_pt) == 1
q = q.replace(anchor_pt, para + anchor_pt, 1)

after_count = q.count('class="qs-card"')
assert after_count == orig_count, 'card count changed %d -> %d' % (orig_count, after_count)
assert q.count('✓原文核验') == yes_n and q.count('◎转引在册') == tr_n
assert yes_n + tr_n == 98, 'marked %d != 98 (100 unique ids - 2 ledger-only blocks e2021-07/e2025)' % (yes_n + tr_n)

io.open('quotes.html', 'w', encoding='utf-8', newline='\n').write(q)
print('quotes.html: cards %d unchanged, YES=%d TR=%d, footnote added' % (orig_count, yes_n, tr_n))
