# -*- coding: utf-8 -*-
"""将马斯克商业志全部页面内容编译为离线 EPUB 电子书。

用法：python tools/build-epub.py
（站点根目录执行。纯 Python zipfile 手写 EPUB 结构，零外部依赖。）

产出：musk-inc.epub —— 可在 Apple Books / Calibre / Kobo / 手机阅读器打开。
"""
import io
import os
import re
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# ---------- 章节顺序 ----------
CHAPTERS = [
    ('index.html',      '卷首 · Cover'),
    ('profile.html',    '壹 · 速览'),
    ('timeline.html',   '贰 · 商业时间线'),
    ('companies.html',  '叁 · 公司版图'),
    ('indepth.html',    '肆 · 公司深度'),
    ('stories.html',    '伍 · 经典商战'),
    ('persona.html',    '陆 · 商业人格'),
    ('playbook.html',   '柒 · 可复用的方法'),
    ('numbers.html',    '捌 · 数据一览'),
    ('grok.html',       '玖 · xAI 与 Grok'),
    ('quotes.html',     '拾 · 语录'),
    ('primary.html',    '言行实录'),
    ('documents.html',  '一手文档馆'),
    ('interviews.html', '访谈与表态'),
    ('x-posts.html',    'X 帖史选辑'),
    ('money.html',      '资本解剖'),
    ('capital-evolution.html', '资本演化时间轴'),
    ('ai-strategy.html','AI 战略布局'),
    ('pricing.html',    '定价与需求管理'),
    ('supplychain.html','供应链与工厂哲学'),
    ('chronicle.html',  '四家公司编年史'),
    ('finance.html',    '财务资本全景'),
    ('controversy.html','争议与批评'),
    ('reading.html',    '长卷阅读版'),
]

def strip_html(html):
    """提取 <main> 或 <body> 内容，去标签转纯文本。"""
    m = re.search(r'<main[^>]*>(.*?)</main>', html, re.S)
    if not m:
        m = re.search(r'<body[^>]*>(.*?)</body>', html, re.S)
    text = m.group(1) if m else html
    # 去掉 nav/footer/script/style/progress
    for pat in [r'<nav[^>]*>.*?</nav>', r'<footer[^>]*>.*?</footer>',
                r'<script[^>]*>.*?</script>', r'<style[^>]*>.*?</style>',
                r'<div class="progress"[^>]*></div>',
                r'<div class="rd-toc".*?</aside>',
                r'<table class="rv-table".*?</table>']:
        text = re.sub(pat, '', text, flags=re.S)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

# ---------- 构建 EPUB ----------
BOOK_ID = 'musk-inc-2026'
EPUB_PATH = os.path.join(ROOT, 'musk-inc.epub')

chapters = []
for fname, title in CHAPTERS:
    path = os.path.join(ROOT, fname)
    if not os.path.exists(path):
        continue
    raw = io.open(path, encoding='utf-8').read()
    body = strip_html(raw)
    # 从 title tag 提取标题
    tm = re.search(r'<title>([^·]+)', raw)
    page_title = tm.group(1).strip() if tm else title
    chapters.append((fname, title, page_title, body))

# 写 EPUB
with zipfile.ZipFile(EPUB_PATH, 'w', zipfile.ZIP_DEFLATED) as zf:
    # mimetype 必须第一个且不压缩
    zf.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)

    # container.xml
    zf.writestr('META-INF/container.xml', '''<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>''')

    # content.opf
    manifest = '\n'.join(
        f'<item id="ch{i}" href="ch{i}.xhtml" media-type="application/xhtml+xml"/>'
        for i in range(len(chapters)))
    spine = '\n'.join(
        f'<itemref idref="ch{i}"/>' for i in range(len(chapters)))
    zf.writestr('OEBPS/content.opf', f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="bookid">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>马斯克商业志 MUSK, INC.</dc:title>
    <dc:creator>马斯克商业志自动化迭代</dc:creator>
    <dc:language>zh-CN</dc:language>
    <dc:identifier id="bookid">{BOOK_ID}</dc:identifier>
  </metadata>
  <manifest>
{manifest}
  </manifest>
  <spine>
{spine}
  </spine>
</package>''')

    # 各章 XHTML
    for i, (fname, title, page_title, body) in enumerate(chapters):
        body_escaped = body.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        # 恢复合法的 HTML 实体
        body_escaped = body_escaped.replace('&amp;lt;', '&lt;').replace('&amp;gt;', '&gt;').replace('&amp;amp;', '&amp;')
        zf.writestr(f'OEBPS/ch{i}.xhtml', f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>{title}</title></head>
<body>
<h1>{page_title}</h1>
<pre style="white-space:pre-wrap;font-family:serif;font-size:14px;line-height:1.8">{body_escaped}</pre>
</body>
</html>''')

    # nav.xhtml（目录）
    toc = '\n'.join(
        f'<li><a href="ch{i}.xhtml">{title}</a></li>'
        for i, (fname, title, _, _) in enumerate(chapters))
    zf.writestr('OEBPS/nav.xhtml', f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>目录</title></head>
<body><h1>目录</h1><ol>{toc}</ol></body>
</html>''')

size = os.path.getsize(EPUB_PATH)
print(f'EPUB 生成完成: musk-inc.epub ({size:,} bytes, {len(chapters)} 章)')
