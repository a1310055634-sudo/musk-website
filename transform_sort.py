# -*- coding: utf-8 -*-
"""v4.5.0 帖墙重建：按年份分组 + 修复网格闭合。运行一次后可删除。"""
import io, re

x = io.open('x-posts.html', encoding='utf-8').read()

# 1. 提取 head 与样式块（保留现有 style 定义并追加年份样式）
head = re.search(r'<!DOCTYPE html>.*?</head>', x, re.S).group(0)
style_css = re.search(r'<style>.*?</style>', x, re.S).group(0)

# 2. 提取全部卡片
cards = []
for m in re.finditer(r'    <div class="tweet-card">.*?\n    </div>\n', x, re.S):
    blk = m.group(0)
    d = re.search(r'tweet-date">([^<]*)<', blk)
    cards.append((d.group(1) if d else '9999.99.99', blk))
assert len(cards) == 13, len(cards)

def key(s):
    parts = s.split(' ')[0].split('.')
    y = int(parts[0])
    m = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 0
    return (y, m)
cards.sort(key=lambda c: key(c[0]))

# 3. 按年份分组重建 grid 内容
out = []
seen = []
for date, blk in cards:
    y = date.split(' ')[0].split('.')[0]
    if y not in seen:
        seen.append(y)
        out.append('      <div class="xp-year" aria-hidden="true">%s</div>\n' % y)
    out.append(blk)
grid_body = ''.join(out)

# 4. 重写整页（网格正确闭合）
page = head.replace('</head>', '''  <style>
.xp-year {
  grid-column: 1 / -1;
  font-family: Georgia, "STSong", serif; font-size: 26px; font-weight: 700;
  color: #7c2d2d; letter-spacing: 0.06em;
  border-bottom: 2px solid #7c2d2d; padding-bottom: 6px;
}
@media print { .tweet-card, .xp-year { break-inside: avoid; } .tweet-card { background: #fff; color: #000; border: 1px solid #000; } .tweet-note { color: #555; } }
  </style>
</head>''') + '''
<body>
<div class="xp-page">
  <a class="xp-back" href="index.html">← 返回网站主页 / Back to site</a>
  <header class="xp-head">
    <h1>X 帖史选辑</h1>
    <p class="xp-sub">POSTS THAT MOVED MARKETS — 商业相关的名帖卡片墙，按年份分组。英文原句逐字保留（含他的拼写与标点）；中译为本站所译；「背景 / 后续」为编者注，非其本人表述。</p>
  </header>
    <nav class="ps-nav" aria-label="第一手板块导航">
      <a href="index.html#primary">言行实录</a><a href="documents.html">一手文档馆</a><a href="interviews.html">访谈与表态</a><a href="x-posts.html" aria-current="page">X 帖史选辑</a><a href="money.html">资本解剖</a>
    </nav>
  <div class="xp-grid">
''' + grid_body + '''  </div>

  <p class="xp-foot">本页由马斯克商业志自动化迭代维护 · 帖文措辞与日期经公开报道核实（Reuters、TechCrunch、Washington Post、BBC、CNBC 及 X 原帖）· 中译为本站所译 · 非官方学习型网站 · <a href="money.html" style="color:#7c2d2d">资本解剖 →</a></p>
</div>
</body>
</html>
'''
io.open('x-posts.html', 'w', encoding='utf-8').write(page)
print('rebuilt:', len(cards), 'cards,', len(seen), 'year groups')
