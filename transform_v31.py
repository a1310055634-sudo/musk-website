# -*- coding: utf-8 -*-
"""v3.1.0 一次性结构转换：单页 → 章节.TabPage 架构。运行一次后本文件可删除。"""
import io, re

h = io.open('index.html', encoding='utf-8').read()
a = io.open('app.js', encoding='utf-8').read()

# ---------- 0. 版本 ----------
assert h.count('3.0.0') == 1 and a.count("'3.0.0'") == 1
h = h.replace('3.0.0', '3.1.0')
a = a.replace("'3.0.0'", "'3.1.0'")

# ---------- 1. 全站锚点 → 页面文件 ----------
FILE_MAP = {
    'profile': 'profile.html', 'timeline': 'timeline.html', 'companies': 'companies.html',
    'indepth': 'indepth.html', 'stories': 'stories.html', 'persona': 'persona.html',
    'playbook': 'playbook.html', 'numbers': 'numbers.html', 'grok': 'grok.html',
    'quotes': 'quotes.html', 'primary': 'primary.html', 'cover': 'index.html',
}
for sid, f in FILE_MAP.items():
    h = h.replace('href="#%s"' % sid, 'href="%s"' % f)

# ---------- 2. 提取部件 ----------
body_top = re.search(r'  <div class="progress"[^>]*></div>\n  <a class="skip-link"[^>]*>[^<]*</a>\n', h).group(0)
mast = re.search(r'  <!-- =+ 报头 =+ -->\n  <header class="masthead">.*?</header>\n', h, re.S).group(0)
foot = re.search(r'  <!-- =+ 页脚 =+ -->\n  <footer class="site-footer">.*?</footer>\n\n  <script src="app.js"></script>', h, re.S).group(0)

# ---------- 3. 提取 sections ----------
ORDER = ['cover', 'profile', 'timeline', 'companies', 'indepth', 'stories',
         'persona', 'playbook', 'numbers', 'grok', 'quotes', 'primary']
secs = {}
for sid in ORDER:
    start = h.index('    <section id="%s"' % sid)
    end = h.index('    </section>\n', start) + len('    </section>\n')
    secs[sid] = h[start:end]

# ---------- 4. 章节页模板 ----------
def make_page(title, desc, body_main, prev_name, prev_file, next_name, next_file):
    head = re.search(r'<!DOCTYPE html>.*?</head>', h, re.S).group(0)
    head = re.sub(r'<title>[^<]*</title>', '<title>%s</title>' % title, head)
    head = re.sub(r'<meta name="description" content="[^"]*" />',
                  '<meta name="description" content="%s" />' % desc, head)
    pager = ''
    if prev_file or next_file:
        L = ('<a class="pg" href="%s"><small data-en="Previous">上一章</small><b>%s</b></a>' % (prev_file, prev_name)) if prev_file else '<span></span>'
        R = ('<a class="pg" href="%s"><small data-en="Next">下一章</small><b>%s</b></a>' % (next_file, next_name)) if next_file else '<span></span>'
        pager = '\n    <nav class="chapter-pager container" aria-label="章节翻页">%s%s%s</nav>' % (L, '<span class="pg-gap"></span>', R)
    return (head + '\n<body>\n' + body_top + '\n' + mast
            + '\n  <main id="main">\n' + body_main + pager + '\n  </main>\n\n'
            + foot + '\n\n  <script src="app.js"></script>\n</body>\n</html>\n')

CHAPTERS = [
    ('profile',  '01 速览 · 马斯克商业志 MUSK, INC.', '用生意人的方式认识马斯克：商业叙事与快速档案。'),
    ('timeline', '02 商业时间线 · 马斯克商业志 MUSK, INC.', '24 条言行深读与商业里程碑，按年份与分类检索。'),
    ('companies', '03 公司版图 · 马斯克商业志 MUSK, INC.', '六家公司卡片与早期交易记录表。'),
    ('indepth',  '04 公司深度 · 马斯克商业志 MUSK, INC.', 'Tesla、SpaceX、𝕏、xAI 四份公司深度档案。'),
    ('stories',  '05 经典商战 · 马斯克商业志 MUSK, INC.', '2008 至暗时刻、收购推特、生产地狱、SEC 事件四篇商战故事。'),
    ('persona',  '06 商业人格 · 马斯克商业志 MUSK, INC.', '六张行为证据卡：用行为写成的性格。'),
    ('playbook', '07 可复用的方法 · 马斯克商业志 MUSK, INC.', '六步打法：原则、案例与适用边界。'),
    ('numbers',  '08 数据一览 · 马斯克商业志 MUSK, INC.', '三张 SVG 图表：交易、市值与财富里程碑。'),
    ('grok',     '09 xAI·Grok · 马斯克商业志 MUSK, INC.', '用 AI 公司反向收购社交平台。'),
    ('quotes',   '10 语录 · 马斯克商业志 MUSK, INC.', '四句反复出现在他交易里的话（自动轮播）。'),
    ('primary',  '11 第一手 · 马斯克商业志 MUSK, INC.', '言行实录账本 + 文档馆 / 访谈表态 / 帖史选辑三页入口。'),
]

# 写 11 个章节页（cover 除外）
for i, (sid, title, desc) in enumerate(CHAPTERS):
    prev = CHAPTERS[i - 1] if i > 0 else None
    nxt = CHAPTERS[i + 1] if i + 1 < len(CHAPTERS) else None
    prev_arg = ('%s.html' % prev[0], prev[1].split(' · ')[0]) if prev else (None, None)
    nxt_arg = ('%s.html' % nxt[0], nxt[1].split(' · ')[0]) if nxt else (None, None)
    body = '    ' + secs[sid].strip() + '\n'
    io.open('%s.html' % sid, 'w', encoding='utf-8').write(
        make_page(title, desc, body, prev_arg[1], prev_arg[0], nxt_arg[1], nxt_arg[0]))

# ---------- 5. 新 index：封面 + 章节目录 ----------
CARDS = [
    ('profile',  '01', '速览', 'Profile', '用生意人的方式认识他'),
    ('timeline', '02', '商业时间线', 'Timeline', '一部用交易写成的生涯'),
    ('companies', '03', '公司版图', 'Companies', '六家公司，一个运营者'),
    ('indepth', '04', '公司深度', 'In Depth', '四份公司档案，四种下注方式'),
    ('stories', '05', '经典商战', 'War Stories', '至暗时刻，与它的翻盘'),
    ('persona', '06', '商业人格', 'Persona', '用行为写成的性格'),
    ('playbook', '07', '可复用的方法', 'Playbook', '六步打法，附适用边界'),
    ('numbers', '08', '数据一览', 'In Numbers', '把帝国画在坐标纸上'),
    ('grok', '09', 'xAI·Grok', 'xAI & Grok', '用 AI 公司反向收购平台'),
    ('primary', '10', '第一手', 'Primary', '他自己的话，他亲手做的事'),
    ('quotes', '11', '语录', 'Quotes', '四句话，反复出现在他的交易里'),
]
cards = '\n'.join(
    '''        <a class="chapter-card reveal" href="%s.html">
          <span class="ch-num" aria-hidden="true">%s</span>
          <h3 data-en="%s">%s</h3>
          <p data-en="%s">%s</p>
          <span class="ch-go" data-en="Read →">阅读 →</span>
        </a>''' % (f, n, en, zh, en, zhl)
    for f, n, zh, en, zhl in CARDS)

grid = '''    <!-- ============ 章节目录 ============ -->
    <section id="chapters" class="section container">
      <header class="section-head reveal">
        <p class="kicker">CONTENTS</p>
        <h2 data-en="Enter the chapters">进入篇章</h2>
        <p class="section-standfirst" data-en="Eleven chapters. Every fact traceable to the public record.">十一个篇章，每个事实都可溯源。</p>
      </header>
      <div class="chapter-grid">
%s
      </div>
    </section>
''' % cards

new_index = (re.search(r'<!DOCTYPE html>.*?</head>', h, re.S).group(0)
             .replace('<title>马斯克商业志 MUSK, INC. — 埃隆·马斯克的商业故事</title>',
                      '<title>马斯克商业志 MUSK, INC. — 埃隆·马斯克的商业故事（章节版）</title>')
             + '\n<body>\n' + body_top + '\n' + mast
             + '\n  <main id="main">\n' + secs['cover'] + grid + '\n  </main>\n\n'
             + foot + '\n\n  <script src="app.js"></script>\n</body>\n</html>\n')
io.open('index.html', 'w', encoding='utf-8').write(new_index)

print('pages built:', len(CHAPTERS) + 1)
