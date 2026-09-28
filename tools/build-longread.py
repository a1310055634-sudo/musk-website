# -*- coding: utf-8 -*-
"""V7-19 R5 长文阅读模板生成器：把 deep-dive-01..05.html 迁移到共享 .lr-* 模板。

每页改造为：深色纪实页头（大图 + 元信息行：阅读时长/小节/字数/更新）
→ 目录栏（桌面 sticky / 手机盒装，app.js 滚动定位）
→ 正文（16.5px · 阅读宽度 --read-width）+ 统一引语/数据框/编者注/来源组件。
内容段落逐字保留，仅换结构外壳与类名；旧锚点无外部引用（已核查），新章节 id 为 {stem}-s{n}。

用法：python tools/build-longread.py        （幂等：含 V7-R5-LONGREAD 标记的页自动跳过）
"""
import html
import math
import re
import io
import os
import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

VERSION = io.open('VERSION', encoding='utf-8').read().strip()
TODAY = datetime.date.today().isoformat()

# 每页页头大图配置（全部为 ASSETS.md 已溯源素材，署名随 figcaption 落页）
PAGES = {
    'deep-dive-01.html': dict(
        img='assets/tesla-factory.jpg', w=960, h=638, pos='50% 62%',
        alt='弗里蒙特工厂总装线上的 Model S 车身',
        cap='资本的落点：弗里蒙特工厂总装线上的 Model S 车身（2011）——退出换来的本金，最终变成物理世界的资产。',
        cap_en='Where capital lands: a Model S body on the Fremont assembly line (2011). Photo: Maurizio Pesce / CC BY 2.0, via Wikimedia Commons'),
    'deep-dive-02.html': dict(
        img='assets/portrait-hero.jpg', w=960, h=640, pos='50% 30%',
        alt='马斯克肖像（2018，Royal Society）',
        cap='用人的判断本身就是资产。肖像摄于 2018 年 7 月 Royal Society 活动。',
        cap_en='Judgment of people is itself an asset. Portrait taken at the Royal Society, July 2018. Photo: Debbie Rowe / CC BY-SA 3.0, via Wikimedia Commons'),
    'deep-dive-03.html': dict(
        img='assets/starship-catch.jpg', w=1200, h=1345, pos='50% 45%',
        alt='Starship 第五飞助推器被发射塔机械臂接住',
        cap='2024 年 10 月 13 日，星舰第五飞助推器被塔臂接住——在此之前，是一份很长的爆炸清单。',
        cap_en='Oct 13, 2024: the Super Heavy booster caught by the launch tower — after a long list of explosions. Photo: Steve Jurvetson / CC BY 2.0, via Wikimedia Commons'),
    'deep-dive-04.html': dict(
        img='assets/falcon-heavy.jpg', w=960, h=1440, pos='50% 38%',
        alt='猎鹰重型演示飞行两侧助推器同步着陆',
        cap='2018 年 2 月 6 日，猎鹰重型两侧助推器同步着陆；同年 8 月，同一家公司卷入 funding secured 监管风暴。',
        cap_en='Feb 6, 2018: Falcon Heavy side boosters land in sync; that August, funding secured triggered the SEC storm. Photo: SpaceX / CC0, via Wikimedia Commons'),
    'deep-dive-05.html': dict(
        img='assets/x-hq.jpg', w=1200, h=800, pos='50% 30%',
        alt='2022 年 11 月旧金山 Twitter 总部标牌',
        cap='2022 年 11 月的 Twitter 总部标牌——两年半后，这家公司被 xAI 反向吸收。',
        cap_en='The Twitter HQ sign, November 2022 — two and a half years later the company was absorbed by xAI. Photo: osunpokeh / CC BY-SA 4.0, via Wikimedia Commons'),
}

MARKER = '<!-- V7-R5-LONGREAD -->'
CLASS_MAP = {
    'dd-sec': 'lr-sec', 'dd-zh': 'lr-quote-zh', 'dd-note': 'lr-note',
    'dd-table-wrap': 'lr-data-wrap', 'dd-table': 'lr-data', 'dd-data': 'lr-data-box',
    'dd-lead': 'lr-lead', 'dd-kicker': 'lr-kick', 'dd-foot': 'lr-foot',
}


def rename_classes(s):
    def sub_attr(m):
        toks = [CLASS_MAP.get(t, t) for t in m.group(1).split()]
        return 'class="%s"' % ' '.join(toks)
    return re.sub(r'class="([^"]*)"', sub_attr, s)


def attr_safe(s):
    return s.replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;')


def reading_stats(html_text):
    txt = html.unescape(re.sub(r'<[^>]+>', ' ', html_text))
    cjk = len(re.findall(r'[\u4e00-\u9fff]', txt))
    words = len(re.findall(r'[A-Za-z]+', txt))
    minutes = max(1, math.ceil(cjk / 300 + words / 200))
    return minutes, cjk


def build(fname, cfg):
    src = io.open(fname, encoding='utf-8').read()
    if MARKER in src:
        print('  · %s 已应用模板，跳过' % fname)
        return False

    # 1) 去掉页内旧样式块（样式已并入 style.css 共享层）
    src, n_st = re.subn(r'<style>.*?</style>\s*', '', src, count=1, flags=re.S)
    assert n_st == 1, fname + ': 未找到内联样式块'

    # 2) 切出报头之后的正文容器（script 开标签计入 tail，避免 app.js 丢失）
    m = re.search(r'<div class="dd-page">(.*?)</div>\s*(<script src="app\.js">)', src, re.S)
    assert m, fname + ': 未找到 dd-page 容器'
    content = m.group(1)
    head_part = src[:m.start()]
    tail_part = m.group(2) + src[m.end():]

    # 3) 拆解旧结构：返回链接弃用（页头内重建）、题头、章节、来源脚注
    content = re.sub(r'<a class="dd-back"[^>]*>.*?</a>\s*', '', content, flags=re.S)
    mk = re.search(r'<div class="dd-kicker">(.*?)</div>', content, re.S)
    mh1 = re.search(r'(<h1[^>]*>.*?</h1>)', content, re.S)
    mld = re.search(r'(<p class="dd-lead"[^>]*>.*?</p>)', content, re.S)
    mft = re.search(r'(<p class="dd-foot"[^>]*>.*?</p>)', content, re.S)
    assert mk and mh1 and mld and mft, fname + ': 题头结构不全'
    kicker = mk.group(1)
    h1_tag = rename_classes(mh1.group(1))
    lead_tag = rename_classes(mld.group(1))
    foot_tag = rename_classes(mft.group(1))

    secs_raw = re.findall(r'<section class="dd-sec">.*?</section>', content, re.S)
    assert len(secs_raw) >= 4, fname + ': 章节数异常'

    # 4) 章节迁移：h3→h2（带 id）、类名映射、目录条目
    stem = fname[:-5]
    toc_items, secs_out = [], []
    for i, sec in enumerate(secs_raw, 1):
        sid = '%s-s%d' % (stem, i)
        h3 = re.search(r'<h3([^>]*)>(.*?)</h3>', sec, re.S)
        assert h3, fname + ': 章节 %d 缺 h3' % i
        attrs, inner = h3.group(1), h3.group(2)
        men = re.search(r'data-en="([^"]*)"', attrs)
        toc_en = attr_safe(html.unescape(men.group(1))) if men else ''
        toc_zh = re.sub(r'<[^>]+>', '', inner).strip()
        toc_items.append((sid, toc_zh, toc_en))
        sec = sec.replace(h3.group(0), '<h2%s id="%s">%s</h2>' % (attrs, sid, inner), 1)
        secs_out.append(rename_classes(sec))

    # 5) 元信息：按实际内容计算阅读时长与字数
    minutes, cjk = reading_stats(''.join(secs_out))
    cjk_disp = format(int(round(cjk, -2)), ',')

    meta = (
        '<div class="lr-meta">\n'
        '        <span class="lr-m"><span class="lr-m-k" data-en="Reading time">阅读时长</span>'
        '<b data-en="≈ %d min">约 %d 分钟</b></span>\n'
        '        <span class="lr-m"><span class="lr-m-k" data-en="Sections">小节</span>'
        '<b data-en="%d sections">%d 个</b></span>\n'
        '        <span class="lr-m"><span class="lr-m-k" data-en="Length">字数</span>'
        '<b data-en="≈ %s chars">约 %s 字</b></span>\n'
        '        <span class="lr-m"><span class="lr-m-k" data-en="Updated">更新</span>'
        '<b>v%s · %s</b></span>\n'
        '      </div>' % (minutes, minutes, len(secs_out), len(secs_out), cjk_disp, cjk_disp, VERSION, TODAY)
    )

    hero = (
        '%s\n'
        '<div class="progress"></div>\n'
        '<header class="lr-hero">\n'
        '  <div class="container lr-hero-inner">\n'
        '    <a class="lr-back" href="index.html" data-en="← Back to site">← 返回网站主页</a>\n'
        '    <div class="lr-kick">%s</div>\n'
        '    %s\n'
        '    %s\n'
        '    %s\n'
        '  </div>\n'
        '  <figure class="lr-hero-fig">\n'
        '    <img src="%s" width="%d" height="%d" alt="%s" loading="eager" fetchpriority="high" style="object-position:%s">\n'
        '    <figcaption data-en="%s">%s</figcaption>\n'
        '  </figure>\n'
        '</header>' % (
            MARKER, kicker, h1_tag, lead_tag, meta,
            cfg['img'], cfg['w'], cfg['h'], attr_safe(cfg['alt']), cfg['pos'],
            attr_safe(cfg['cap_en']), cfg['cap'])
    )

    toc = (
        '<aside class="lr-toc" aria-label="本篇目录">\n'
        '      <div class="lr-toc-h">目录 · CONTENTS</div>\n' +
        ''.join('    <a href="#%s" data-en="%s">%s</a>\n' % (sid, en, zh)
                for sid, zh, en in toc_items) +
        '    </aside>'
    )

    body = (
        '%s\n'
        '<div class="lr-layout">\n'
        '  <main class="lr-main">\n'
        '%s\n'
        '  %s\n'
        '  </main>\n'
        '  %s\n'
        '</div>' % (hero, '\n\n'.join(secs_out), foot_tag, toc)
    )

    out = head_part + body + tail_part
    # 6) og:image 指向本篇页头大图
    out = out.replace('/assets/portrait.jpg', '/%s' % cfg['img'], 1)
    io.open(fname, 'w', encoding='utf-8', newline='\n').write(out)
    print('  · %s → %d 节 / 约 %d 分钟 / %s 字' % (fname, len(secs_out), minutes, cjk_disp))
    return True


def main():
    changed = 0
    for fname, cfg in PAGES.items():
        if build(fname, cfg):
            changed += 1
    print('完成：%d/%d 页迁移' % (changed, len(PAGES)))


if __name__ == '__main__':
    main()
