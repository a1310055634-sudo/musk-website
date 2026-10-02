# -*- coding: utf-8 -*-
"""生成 sitemap.xml（V9-20 R20 纳入生成器全家桶；幂等）。

扫描站点根 *.html（排除 revisions.html——noindex），按字母序产出
https://a1310055634-sudo.github.io/musk-website/{page} 条目，lastmod=运行日。
"""
import glob
import io
import os
import time

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

pages = sorted(f for f in glob.glob('*.html')
               if f not in ('revisions.html', 'preview-v12.html'))  # revisions noindex；preview-v12 为开发工具页
today = time.strftime('%Y-%m-%d')

rows = '\n'.join(
    f'  <url><loc>https://a1310055634-sudo.github.io/musk-website/{p}</loc>'
    f'<lastmod>{today}</lastmod><priority>0.7</priority></url>'
    for p in pages
)
xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{rows}
</urlset>
'''
io.open('sitemap.xml', 'w', encoding='utf-8', newline='\n').write(xml)
print(f'sitemap.xml: {len(pages)} URL（lastmod {today}）')
