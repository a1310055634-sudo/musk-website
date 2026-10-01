# -*- coding: utf-8 -*-
"""V9-20 R11 官方与标准类资源核活脚本。

策略（沿用 R10 结论）：浏览器 UA curl 串行实测 → 记录 http_code 与最终 URL。
403/000 项交 WebFetch/web_reader 复核（不同网络栈），仍失败则留档不收录。
"""
import json
import time
import urllib.request
import urllib.error
import ssl

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")

TARGETS = [
    # R10 留档重验（反爬 403 / 连接 000）
    "https://www.tesla.com/blog/all-our-patent-are-belong-you",
    "https://www.spacex.com/vehicles/starship/",
    "https://www.spacex.com/vehicles/falcon-9/",
    "https://developer.tesla.com/",
    "https://neuralink.com/patient-registry/",
    # R10 未测，R11 任务书指定
    "https://openai.com/blog/introducing-openai/",
    # NACS 标准类候选
    "https://www.tesla.com/nacs",
    "https://www.sae.org/standards/content/j3400_202511/",
    # 官方站点扩展候选
    "https://www.x.ai/",
    "https://www.boringcompany.com/",
    "https://www.spacex.com/updates/",
    "https://www.tesla.com/impact",
    # Tesla 车主文档
    "https://www.tesla.com/owners",
    "https://www.tesla.com/ownersmanuals",
]

ctx = ssl.create_default_context()


def probe(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    })
    try:
        with urllib.request.urlopen(req, timeout=25, context=ctx) as resp:
            return resp.getcode(), resp.geturl()
    except urllib.error.HTTPError as e:
        return e.code, url
    except Exception as e:
        return 0, f"{type(e).__name__}: {e}"[:120]


results = []
for u in TARGETS:
    code, final = probe(u)
    results.append({"url": u, "http": code, "final": final})
    print(f"{code:>3}  {u}  ->  {final}")
    time.sleep(1.5)

with open(__file__.replace("v9r11-liveness.py", "liveness-r11.json"), "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=1)
print("\nsaved liveness-r11.json")
