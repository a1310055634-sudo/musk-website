# -*- coding: utf-8 -*-
"""R02 页面接入：companies 卡配图 / indepth 图注修正 / index 封面来源行 / style.css 卡图样式。
每文件：读全文 → 精确替换（断言计数）→ 立即写盘。"""
import io

def edit(path, reps):
    with io.open(path, encoding="utf-8", newline="") as f:
        s = f.read()
    for old, new, cnt in reps:
        n = s.count(old)
        assert n == cnt, f"{path}: expect {cnt} got {n} for: {old[:60]!r}"
        s = s.replace(old, new)
    with io.open(path, "w", encoding="utf-8", newline="") as f:
        f.write(s)
    print(f"OK  {path}  ({len(reps)} edits)")

# ---------- companies.html：三张公司卡配纪实图 ----------
FIG_TESLA = '''<article class="company-card reveal">
          <figure class="card-photo">
            <img src="assets/cybertruck.jpg" alt="Tesla Cybertruck 展车前脸（2023）" width="1080" height="720" loading="lazy" decoding="async" />
            <figcaption>图：N2e · CC0 · Wikimedia Commons</figcaption>
          </figure>
          <h3>Tesla</h3>'''
OLD_TESLA = '''<article class="company-card reveal">
          <h3>Tesla</h3>'''

FIG_SPACEX = '''<article class="company-card reveal">
          <figure class="card-photo">
            <img src="assets/starship-catch.jpg" alt="Starship 超重型助推器被发射塔机械臂接住（2024 年 10 月第五飞）" width="1200" height="1345" loading="lazy" decoding="async" />
            <figcaption>图：Steve Jurvetson · CC BY 2.0 · Wikimedia Commons</figcaption>
          </figure>
          <h3>SpaceX</h3>'''
OLD_SPACEX = '''<article class="company-card reveal">
          <h3>SpaceX</h3>'''

FIG_X = '''<article class="company-card reveal">
          <figure class="card-photo">
            <img src="assets/x-hq.jpg" alt="旧金山市场街 Twitter 总部，2022 年 11 月收购完成时仍挂 @twitter 标牌" width="1200" height="800" loading="lazy" decoding="async" />
            <figcaption>图：osunpokeh · CC BY-SA 4.0 · Wikimedia Commons</figcaption>
          </figure>
          <h3>𝕏</h3>'''
OLD_X = '''<article class="company-card reveal">
          <h3>𝕏</h3>'''

edit("companies.html", [
    (OLD_TESLA, FIG_TESLA, 1),
    (OLD_SPACEX, FIG_SPACEX, 1),
    (OLD_X, FIG_X, 1),
])

# ---------- indepth.html：alt 修正 + 图注许可补全 + Falcon 取景下移 ----------
edit("indepth.html", [
    ('alt="Tesla 弗里蒙特工厂外景"',
     'alt="Tesla 弗里蒙特工厂总装线上的 Model S 车身（2011）"', 1),
    ('<figcaption data-en="Tesla\'s Fremont factory · Wikimedia Commons">Tesla 弗里蒙特工厂 · 图源 Wikimedia Commons</figcaption>',
     '<figcaption data-en="Tesla Fremont assembly line (2011) · Photo: Maurizio Pesce · CC BY 2.0 via Wikimedia Commons">Tesla 弗里蒙特工厂总装线 · 图：Maurizio Pesce · CC BY 2.0 via Wikimedia Commons</figcaption>', 1),
    ('alt="Falcon Heavy 演示飞行从肯尼迪航天中心 39A 发射台升空" loading="lazy" decoding="async" width="960" height="1440"',
     'alt="Falcon Heavy 两侧助推器在佛罗里达着陆场同步降落（2018）" loading="lazy" decoding="async" width="960" height="1440" style="object-position: 50% 100%"', 1),
    ('<figcaption data-en="Falcon Heavy demo flight liftoff from LC-39A (2018) · SpaceX via Wikimedia Commons">Falcon Heavy 首飞升空，肯尼迪航天中心 39A（2018）· SpaceX via Wikimedia Commons</figcaption>',
     '<figcaption data-en="Falcon Heavy demo flight: twin side-booster landing (2018) · Photo: SpaceX · CC0 via Wikimedia Commons">Falcon Heavy 演示飞行：两侧助推器同步着陆（2018）· 图：SpaceX · CC0 via Wikimedia Commons</figcaption>', 1),
])

# ---------- index.html：封面肖像来源行 + 首屏加载优先级 ----------
edit("index.html", [
    ('<img src="assets/portrait.jpg" alt="埃隆·马斯克肖像（Wikimedia Commons）" width="360" height="477" decoding="async" />',
     '<img src="assets/portrait.jpg" alt="埃隆·马斯克肖像（Wikimedia Commons）" width="360" height="477" fetchpriority="high" decoding="async" />\n            <figcaption data-en="Photo: Debbie Rowe · CC BY-SA 3.0 via Wikimedia Commons">照片：Debbie Rowe · CC BY-SA 3.0 via Wikimedia Commons</figcaption>', 1),
])

# ---------- style.css：全局防拉伸 + 公司卡图样式 + 打印灰度 ----------
edit("style.css", [
    ("img { max-width: 100%; display: block; }",
     "img { max-width: 100%; height: auto; display: block; }", 1),
    (".company-desc { font-size: 14px; color: var(--muted); }",
     """.company-desc { font-size: 14px; color: var(--muted); }
/* 公司卡纪实配图（V7 R02） */
.company-card .card-photo { margin: 0 0 14px; }
.company-card .card-photo img {
  width: 100%; aspect-ratio: 3 / 2; object-fit: cover; display: block;
  border: 1px solid var(--ink); background: #fff; padding: 4px; box-sizing: border-box;
}
.company-card .card-photo figcaption { font-size: 11px; color: var(--muted); margin-top: 6px; letter-spacing: 0.05em; }""", 1),
    ("  .feature-photo img { filter: grayscale(20%); }",
     "  .feature-photo img, .company-card .card-photo img { filter: grayscale(20%); }", 1),
])

# ---------- README.md：素材清单位置 ----------
edit("README.md", [
    ("assets/            图片", "assets/            图片（来源与许可见 ASSETS.md）", 1),
])

print("ALL DONE")
