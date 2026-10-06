# -*- coding: utf-8 -*-
"""R15 patch I：site-nav.py 刊头三件套（期号/日期线/eyebrow）。失败不落盘。"""
import io

p = 'tools/site-nav.py'
s = io.open(p, encoding='utf-8').read()

assert s.count('import io') == 1
s = s.replace('import io', 'import io\nfrom datetime import datetime, timezone, timedelta', 1)

OLD_FN = '''def build_masthead(current):
    """current: 文件名（如 'grok.html'），用于标注 aria-current。"""
    blocks = []
    for g in NAV_GROUPS:
        rows = []
        for href, zh, en in g["items"]:
            cur = ' aria-current="page"' if href == current else ""
            rows.append(ITEM_TMPL.format(href=href, cur=cur, en=en, zh=zh))
        blocks.append(GROUP_TMPL.format(gz=g["zh"], gen=g["en"], items="\\n".join(rows)))
    return MASTHEAD_TMPL.format(groups="\\n".join(blocks))'''

NEW_FN = '''ROMAN = {10: "X", 11: "XI", 12: "XII"}


def build_masthead(current):
    """current: 文件名（如 'grok.html'），用于标注 aria-current。"""
    blocks = []
    for g in NAV_GROUPS:
        rows = []
        for href, zh, en in g["items"]:
            cur = ' aria-current="page"' if href == current else ""
            rows.append(ITEM_TMPL.format(href=href, cur=cur, en=en, zh=zh))
        blocks.append(GROUP_TMPL.format(gz=g["zh"], gen=g["en"], items="\\n".join(rows)))
    # R15 刊头：期号（Vol.=主版本罗马数字/No.=VERSION，与页脚版本戳同源）+ 日期线（构建日北京时间）
    _root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ver = io.open(os.path.join(_root, "VERSION"), encoding="utf-8").read().strip()
    major = int(ver.split(".")[0])
    vol = ROMAN.get(major, "V" + "I" * major if major < 4 else str(major))
    now = datetime.now(timezone(timedelta(hours=8)))
    dateline_zh = "{y} 年 {m} 月 {d} 日".format(y=now.year, m=now.month, d=now.day)
    dateline_en = now.strftime("%B %d, %Y")
    return MASTHEAD_TMPL.format(
        groups="\\n".join(blocks),
        volno="Vol. " + vol + " · No. " + ver,
        dateline_zh=dateline_zh, dateline_en=dateline_en)'''

assert s.count(OLD_FN) == 1, 'fn anchor missing'
s = s.replace(OLD_FN, NEW_FN)

OLD_T = '      <span class="masthead-issue" data-en="Business Profile · No. 001">商业人物志 · 创刊号</span>'
NEW_T = '''      <div class="masthead-eyebrow">
        <span class="mh-dateline" data-en="{dateline_en}">{dateline_zh}</span>
        <span class="mh-sep" aria-hidden="true">—</span>
        <span class="masthead-issue" data-en="Business Profile · No. 001">商业人物志 · 创刊号</span>
        <span class="mh-sep" aria-hidden="true">—</span>
        <span class="mh-volno" title="版本三件套同源（VERSION / app.js / 页脚 span）">{volno}</span>
      </div>'''
assert s.count(OLD_T) == 1, 'tmpl anchor missing'
s = s.replace(OLD_T, NEW_T)

io.open(p, 'w', encoding='utf-8', newline='\n').write(s)
print('site-nav.py patched')
