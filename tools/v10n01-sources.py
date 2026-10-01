# -*- coding: utf-8 -*-
"""V10-15 N01：全站源存活复测。

扫六页（primary/documents/interviews/x-posts/quotes/events）全部外链
（正则抓 https?:// 全形态：href/data-*/JS 字符串/cite.js 单元），按域分类；
串行限速复测（浏览器 UA；GitHub 网页直连即可 200）；已知本机受限域预分类，
不冒充死链。产出存活/死链/受限/漂移四栏报告落盘 qa/v10-15/round-01/。

用法：python tools/v10n01-sources.py scan|check
  scan  只提取分类不请求（干跑）
  check 全量复测（串行 ~0.8s/条）
"""
import io
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
import ssl
from collections import Counter

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# N01 实测口径修正（scan 干跑发现）：六页来源标注为 .ps-src 文字徽章形态、
# 无明文外链（引语锚存于账本文字与 qa 溯源，引语逐字核验归 N02 transcript diff）。
# 故本脚本复测对象 = 全站 38 页全部外链（真实外链集合：resources 36 卡 + 零星互链）。
import glob as _glob
PAGES = sorted(f for f in _glob.glob('*.html'))
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36')
# 本机已知受限域（历史轮实测：403 反爬/连接重置/TLS 中断）——单列不冒充死链
RESTRICTED = (
    ('tesla.com', 'Akamai 反爬 403（R11 三路实测）'),
    ('spacex.com', 'Akamai 反爬 403（R11 三路实测）'),
    ('reddit.com', '反爬 000（R12 实测，须服务端读取器）'),
    ('openai.com', 'Akamai 反爬 403（R11/N01 实测）'),
    ('web.archive.org', '本机 TLS 中断（R04 实测）'),
)
URL_RX = re.compile(r'https?://[^\s"\'<>)\]]+', re.I)


def norm(u):
    u = u.rstrip('.,;:）】')
    u = re.sub(r'&amp;', '&', u)
    return u


def collect():
    urls = {}
    for pg in PAGES:
        s = io.open(pg, encoding='utf-8').read()
        for m in URL_RX.finditer(s):
            u = norm(m.group(0))
            if 'a1310055634-sudo.github.io' in u:
                continue
            urls.setdefault(u, []).append(pg)
    return urls


def classify(u):
    host = re.match(r'https?://([^/]+)', u).group(1).lower()
    for dom, why in RESTRICTED:
        if host == dom or host.endswith('.' + dom):
            return f'restricted:{why}'
    if 'sec.gov' in host:
        return 'edgar'
    if 'elonmuskarchive.org' in host:
        return 'mirror'
    if 'youtube.com' in host or 'youtu.be' in host:
        return 'youtube'
    if 'github.com' in host:
        return 'github'
    return 'web'


def scan():
    urls = collect()
    by_domain = Counter()
    by_host = Counter()
    for u in urls:
        by_host[re.match(r'https?://([^/]+)', u).group(1)] += 1
        by_domain[classify(u).split(':')[0]] += 1
    print(f'唯一外链 {len(urls)} 条')
    print('按类别:', dict(by_domain))
    print('Top hosts:')
    for h, c in by_host.most_common(15):
        print(f'  {h}: {c}')
    with io.open('qa/v10-15/round-01/sources-inventory.tsv', 'w', encoding='utf-8', newline='\n') as f:
        f.write('url\tcategory\tpages\n')
        for u in sorted(urls):
            f.write(f'{u}\t{classify(u)}\t{",".join(sorted(set(urls[u])))}\n')
    print('inventory saved')


def check():
    urls = collect()
    ctx = ssl.create_default_context()
    results = []
    n = 0
    for u in sorted(urls):
        n += 1
        cat = classify(u)
        if cat.startswith('restricted:'):
            results.append({'url': u, 'cat': cat, 'http': None, 'verdict': 'restricted'})
            continue
        code = 0
        try:
            req = urllib.request.Request(u, headers={
                'User-Agent': UA + ' (musk-website verification; contact: reader@example.org)',
                'Accept': 'text/html,*/*;q=0.8'})
            with urllib.request.urlopen(req, timeout=14, context=ctx) as r:
                code = r.getcode()
                r.read(2048)
        except urllib.error.HTTPError as e:
            code = e.code
        except Exception as e:
            code = 0
        verdict = 'alive' if 200 <= code < 400 else ('dead' if code else 'unreachable')
        results.append({'url': u, 'cat': cat, 'http': code, 'verdict': verdict})
        if n % 25 == 0:
            print(f'  ...{n}/{len(urls)}')
        time.sleep(0.8)

    alive = [r for r in results if r['verdict'] == 'alive']
    dead = [r for r in results if r['verdict'] == 'dead']
    unreach = [r for r in results if r['verdict'] == 'unreachable']
    restr = [r for r in results if r['verdict'] == 'restricted']
    print(f'\n总计 {len(results)}：存活 {len(alive)} / HTTP错误 {len(dead)} / 连接失败 {len(unreach)} / 本机受限 {len(restr)}')
    print('\n-- HTTP 错误（须逐条处置） --')
    for r in dead:
        print(f"  {r['http']} {r['cat']:<8} {r['url'][:100]}")
    print('-- 连接失败 --')
    for r in unreach:
        print(f"  --- {r['cat']:<8} {r['url'][:100]}")
    with io.open('qa/v10-15/round-01/sources-check.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=1)
    with io.open('qa/v10-15/round-01/sources-report.tsv', 'w', encoding='utf-8', newline='\n') as f:
        f.write('url\tcategory\thttp\tverdict\n')
        for r in results:
            f.write(f"{r['url']}\t{r['cat']}\t{r['http']}\t{r['verdict']}\n")
    print('report saved')


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'scan'
    scan() if mode == 'scan' else check()
