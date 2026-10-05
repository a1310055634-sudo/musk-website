# -*- coding: utf-8 -*-
"""R13 采料：候选资源批量核活（curl http 码）+ GitHub API 实测（串行限流）。"""
import io, json, subprocess, time, urllib.request

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36'
SEC_UA = 'MuskArchiveResearch admin@example.com'

CANDIDATES = [
    ('sec-edgar-spacex', 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001181412&type=10-Q&dateb=&owner=include&count=40', SEC_UA),
    ('spacex-ir', 'https://www.spacex.com/investors', UA),
    ('docs-xai', 'https://docs.x.ai/', UA),
    ('xai-model-card', 'https://x.ai/models', UA),
    ('tesla-support', 'https://www.tesla.com/support', UA),
    ('xai-org-github', 'https://github.com/xai-org', UA),
    ('tesla-owners-manual', 'https://www.tesla.com/ownersmanual/modely/en_us/', UA),
]

results = {}
for rid, url, ua in CANDIDATES:
    try:
        r = subprocess.run(['curl', '-sL', '-o', '/dev/null', '-w', '%{http_code}',
                            '--max-time', '25', '-A', ua, url],
                           capture_output=True, text=True, timeout=30)
        code = int(r.stdout.strip() or 0)
    except Exception as e:
        code = 0
    results[rid] = {'url': url, 'http': code}
    print(rid, code)
    time.sleep(1)

# GitHub API（无认证限流：串行+sleep）
GH = ['xai-org/grok-1']
for repo in GH:
    try:
        req = urllib.request.Request('https://api.github.com/repos/' + repo,
                                     headers={'User-Agent': 'MuskArchiveResearch', 'Accept': 'application/vnd.github+json'})
        with urllib.request.urlopen(req, timeout=20) as r:
            d = json.load(r)
        results.setdefault('gh', {})[repo] = {'stars': d.get('stargazers_count'), 'pushed': (d.get('pushed_at') or '')[:7]}
        print('gh', repo, d.get('stargazers_count'), (d.get('pushed_at') or '')[:7])
    except Exception as e:
        print('gh', repo, 'ERR', str(e)[:50])
    time.sleep(2)

io.open('qa/v12/round-13/probe.json', 'w', encoding='utf-8', newline='\n').write(json.dumps(results, ensure_ascii=False, indent=1))
print('saved')
