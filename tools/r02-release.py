# -*- coding: utf-8 -*-
"""R02 发布流程：CHANGELOG 记账 → sync-changelog → 版本步进（VERSION/app.js/12页span）。"""
import io, re, glob

# ---------- 1) CHANGELOG 记账 ----------
ENTRY = """## v6.7.0 — 2026-09-29 · V7 改版（2/19）：图片与纪实素材体系

**主题包成果（V7-19 第 2 轮 · 图片与纪实素材体系）**
- **全站图片溯源建档**：新建 ASSETS.md 作为素材唯一权威清单（来源页/作者/许可/核实日期/加工方式/用途）；portrait.jpg 经感知哈希比对**逐像素命中** Commons「Elon Musk Royal Society (crop2)」（Debbie Rowe · CC BY-SA 3.0）、tesla-factory.jpg 命中「Tesla Factory, Fremont」（Maurizio Pesce · CC BY 2.0）；falcon-heavy.jpg 两轮检索无法定位原文件——整体替换为 SpaceX 官方 CC0 的「Falcon Heavy 演示飞行双助推器同步着陆（2018）」，画面更有冲击力且来源可查；
- **新增纪实素材 4 张**：Starship 助推器塔捕（Jurvetson · CC BY 2.0，2024-10-13 第五飞，与账本 e2024-10-13 锚点互证）、Twitter/X 总部（osunpokeh · CC BY-SA 4.0，2022-11 收购交割时点）、Cybertruck 量产展车（N2e · CC0）、及上述 Falcon 替换图；全部经目检、裁切（3:2 上部/偏移构图保主体）、压缩与尺寸声明，检索与下载脚本入 tools/（trace-assets/find-assets/get-files/prep-assets）；
- **公司版图卡配图**：companies.html 六卡中 Tesla/SpaceX/X 三家接入纪实配图（带作者·许可署名行），xAI/Neuralink/Boring 暂无可查纪实素材、诚实保持文字卡；新增 `.card-photo` 样式（3:2 object-fit、边框衬纸、署名行、打印灰度）；
- **首页与深读页素材治理**：首页封面肖像补 figcaption 署名行（中英双语）+ fetchpriority=high；indepth.html 图注升级为完整署名并修正 alt 与实拍内容不符处（「工厂外景」实为总装线内景）；全站 `img` 补 `height:auto` 防拉伸；
- **封面备用裁切入库**：portrait-hero.jpg（3:2 横版）与 portrait-hero-mobile.jpg（4:5 竖版）供第 3 轮首页首屏重构取用；
- **加载策略**：三张公司卡图 loading=lazy + decoding=async；首屏肖像 eager+高优先级；真实 390px 视口（CDP 仿真）验证零横向溢出——此前截图「裁字」系 headless Chrome 最小窗宽 500px 伪影，已用 CDP 探针（tools/r02-probe.js）实证排除。

**质量门**
- verify.py 9 项全绿；`node --check app.js` 通过；EN 切换署名行/懒加载滚动加载/21:9 底部取景（object-position）实测正常；断链与锚点零变化。

"""
with io.open("CHANGELOG.md", encoding="utf-8", newline="") as f:
    s = f.read()
marker = "## v6.6.0"
i = s.index(marker)
s = s[:i] + ENTRY + s[i:]
with io.open("CHANGELOG.md", "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("OK CHANGELOG entry inserted")

# ---------- 2) 版本步进 ----------
OLD, NEW = "6.6.0", "6.7.0"

with io.open("VERSION", encoding="utf-8", newline="") as f:
    v = f.read()
assert v.strip() == OLD, v
with io.open("VERSION", "w", encoding="utf-8", newline="") as f:
    f.write(NEW + "\n")
print("OK VERSION", NEW)

with io.open("app.js", encoding="utf-8", newline="") as f:
    a = f.read()
old = "var SITE_VERSION = '%s';" % OLD
assert a.count(old) == 1
a = a.replace(old, "var SITE_VERSION = '%s';" % NEW)
with io.open("app.js", "w", encoding="utf-8", newline="") as f:
    f.write(a)
print("OK app.js SITE_VERSION", NEW)

pat = re.compile(r'(site-version-val">)%s(' % OLD)
n_total = 0
for p in glob.glob("*.html"):
    with io.open(p, encoding="utf-8", newline="") as f:
        h = f.read()
    n = len(pat.findall(h))
    if n:
        h2 = pat.sub(r"\g<1>%s\g<2>" % NEW, h)
        with io.open(p, "w", encoding="utf-8", newline="") as f:
            f.write(h2)
        n_total += n
        print("OK span", p, n)
assert n_total == 12, n_total
print("ALL DONE, spans:", n_total)
