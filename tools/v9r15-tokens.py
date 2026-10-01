# -*- coding: utf-8 -*-
"""V9-20 R15 设计系统升级：重写 style.css 的 :root 令牌层，并把正文中的硬编码值收敛为令牌。

原则：
  1) :root 之外的替换一律**值等价**（令牌值 == 原字面值），零视觉回归——唯二例外：
     a) 三处「浅底小字对比度不达标」的修正（#8a857c 3.22 / #9a948b 2.64 → #6A665D 5.02）。
     b) 纯白 #fff 表面（chip/card/node）→ 暖白 --paper-0（#fffdf8），统一暖纸体系。
  2) 公司色标 --co-* 语义与值一律不动。
  3) @media print 块内保持 #fff/#000/#999/#555 印刷原样（本脚本显式保护该区块）。
每个替换打印命中数；关键替换命中数与预期不符则报错退出（防措辞漂移导致静默失效）。
"""
import io
import re
import sys

P = 'style.css'
src = io.open(P, encoding='utf-8').read()
orig_len = len(src)

# ---------------------------------------------------------------- 1) 新 :root 块
NEW_ROOT = r''':root {
  /* ============================================================
     V9-R15 设计系统令牌层
     三层结构：
       ① 刻度令牌（--hue-* / --paper-* / --coal-* / --tx* / --accent-* / --rule-* / --r-* / --shadow-*）
          —— 唯一原值来源；
       ② 语义令牌（--ty-* / --paper / --ink / --muted / --accent …）—— 组件唯一消费入口；
       ③ 焦点令牌（--focus-*）—— 全站 :focus-visible 统一出口。
     规则：组件只消费 ②③；①仅被 ②③ 与单一用途工具类引用。
     对比度：注释内为 WCAG 2.1 对比度比（tools/v9r15-contrast.py 实测，2026-10-01）。
     ============================================================ */

  /* ---- ① 色相刻度（全站五色主张；事件类型与资源徽标共用） ---- */
  --hue-olive:    #4a6b3a;   /* 正面：创业起步 / 维护中 */
  --hue-ochre:    #8a5a00;   /* 警示：争议时刻 / 停更 */
  --hue-graphite: #55524c;   /* 中性：产品里程碑 / 存档 */
  --hue-navy:     #1f3a5f;   /* 资本：交易与运作 */
  --hue-red:      #C84032;   /* 主张：豪赌与强调 */

  /* ---- ① 表面刻度：暖白（浅底，亮→暗） ---- */
  --paper-0:   #fffdf8;   /* 抬升面：卡片/浮层/图节点底 */
  --paper-50:  #F7F4EC;
  --paper-100: #F3F0E8;   /* 阅读底 */
  --paper-150: #EBE7DC;   /* 卡片面 */
  --paper-200: #E2DDD1;   /* 凹陷面/分隔带 */
  /* ---- ① 表面刻度：近黑（深底，亮→暗） ---- */
  --coal-soft: #1B1F24;
  --coal-0:    #17191d;
  --coal-100:  #101316;   /* 封面/重点图底 */
  --coal-200:  #0A0C0E;

  /* ---- ① 文字刻度：浅底（深→浅；对 --paper / 卡片 --card） ---- */
  --tx-1: #17191d;   /* 15.45 / 13.42 正文 */
  --tx-2: #5b5850;   /*  6.24 /  5.75 次级 */
  --tx-3: #6A665D;   /*  5.02 /  4.63 三级（R15 新增；替换原 #8a857c、#9a948b 的浅底小字用法） */
  --tx-4: #8a857c;   /*  3.22 浅底装饰/大字；暗底可作小字（coal 5.08 / ink 4.80） */
  /* ---- ① 文字刻度：深底（对 --coal / 页脚 --ink） ---- */
  --txd-1: rgba(243, 240, 232, 0.74); /*  9.27 /  8.88 = 原 --mist */
  --txd-2: #F3F0E8;                   /* 16.37 / 15.45 */
  --txd-3: #d9d4cc;                   /* 12.64 / 11.93 */
  --txd-4: #b3aea3;                   /*  8.43 /  7.96 */
  --txd-5: #a8a399;                   /*  7.42 /  7.01 */
  --txd-6: #8a857c;                   /*  5.08 /  4.80 */

  /* ---- ① 朱红刻度 ---- */
  --accent-deep:   #A63628;                /* 浅底小字 5.80 */
  --accent:        #C84032;                /* 主强调（大字/边框/填充）4.35 */
  --accent-bright: #E4765F;                /* 暗底小字 6.26 */
  --accent-soft:   #d9a7a7;                /* 暗底引注 8.91 */
  --accent-glow:   rgba(200, 64, 50, 0.9); /* 块影 */

  /* ---- ② 事件类型色（etype；语义固定、值随色相刻度；白字于色块 5.24–11.48） ---- */
  --ty-start:     var(--hue-olive);    /* 创业起步·橄榄绿 5.34 */
  --ty-deal:      var(--hue-navy);     /* 资本运作·藏蓝 10.08 */
  --ty-gamble:    var(--hue-red);      /* 豪赌翻身·酒红 4.35 */
  --ty-milestone: var(--hue-graphite); /* 产品里程碑·石墨 6.84 */
  --ty-risk:      var(--hue-ochre);    /* 争议时刻·赭黄 5.20 */
  --ty-ok:        #1c7c40;             /* 校验通过·绿 4.60 */

  /* ---- ② 深底/色块上的文字 ---- */
  --on-hue: #fff;    /* 饱和色块上的文字 */

  /* ---- ① 描边/分隔刻度（浅底由弱到强） ---- */
  --wash:           rgba(23, 25, 29, 0.04);
  --rule-soft:      rgba(23, 25, 29, 0.15);
  --hairline:       rgba(23, 25, 29, 0.18);
  --rule-mid:       rgba(23, 25, 29, 0.25);
  --rule-strong:    rgba(23, 25, 29, 0.30);
  --hairline-paper: rgba(243, 240, 232, 0.25);  /* 深底分隔 */

  /* ---- ① 圆角刻度 ---- */
  --r-1: 2px;       /* 微：角标/图例块 */
  --r-2: 3px;
  --r-3: 4px;       /* 卡/按钮/输入 */
  --r-4: 6px;       /* 面板/图节点 */
  --r-pill: 999px;  /* 芯片/筛选条 */
  --r-circle: 50%;  /* 圆点 */

  /* ---- ① 阴影/块影刻度（纪实块影体系） ---- */
  --shadow-1:   6px 6px 0 rgba(23, 25, 29, 0.08);
  --shadow-2:   8px 8px 0 rgba(23, 25, 29, 0.08);
  --shadow-2b:  8px 8px 0 rgba(23, 25, 29, 0.10);
  --shadow-accent:    12px 12px 0 var(--accent-glow);
  --shadow-accent-lg: 18px 18px 0 var(--accent-glow);
  --ring-paper: 0 0 0 3px var(--paper);

  /* ---- ③ 焦点环（统一出口；全站 :focus-visible 一律消费本组令牌） ---- */
  --focus-w: 3px;               /* 文字/常规控件 */
  --focus-w-tight: 2px;         /* 密集 SVG 节点 */
  --focus-offset: 3px;
  --focus-offset-tight: 2px;
  --focus-color: var(--accent);
  --focus-color-dark: var(--accent-bright);
  --focus-color-invert: var(--paper);

  /* ---- ② 语义别名（组件唯一消费入口；值与本轮之前完全一致） ---- */
  --paper: var(--paper-100);
  --coal: var(--coal-100);
  --ink: var(--tx-1);
  --card: var(--paper-150);
  --muted: var(--tx-2);
  --mist: var(--txd-1);
  --navy: var(--hue-navy);           /* 藏蓝：资本/链接辅色（= --ty-deal） */
  --accent-text: var(--accent-deep); /* 朱红深阶：小号强调文字 */

  /* ---- 公司色标（V7-R7 定稿；全站唯一出处。色标只作辅助，公司一律以名称文字为准） ---- */
  --co-musk: #17191d;       /* 运营者（中心节点） */
  --co-tesla: #C8102E;      /* Tesla */
  --co-spacex: #1f3a5f;     /* SpaceX（同 --navy） */
  --co-x: #43464d;          /* X */
  --co-xai: #5B4A8A;        /* xAI */
  --co-neuralink: #A04E77;  /* Neuralink */
  --co-boring: #7A601A;     /* The Boring Company */
  --co-solarcity: #2E7D4F;  /* SolarCity */
  --co-paypal: #1476A8;     /* X.com / PayPal */
  --co-history: #6B6558;    /* 历史公司通用（Zip2 / OpenAI） */

  /* ---- 字体 ---- */
  --serif: Georgia, "Times New Roman", "STSong", "SimSun", serif;
  --sans: "Segoe UI", "PingFang SC", "Microsoft YaHei", system-ui, sans-serif;

  /* ---- ① 字号阶梯（标题 clamp 体系 + 正文固定阶梯） ---- */
  --fs-hero: clamp(88px, 11vw, 144px);   /* 桌面封面主标题 */
  --fs-hero-m: clamp(42px, 12vw, 64px);  /* 手机封面主标题 */
  --fs-h1: clamp(30px, 4.2vw, 46px);
  --fs-h2: clamp(24px, 3.2vw, 34px);
  --fs-h3: clamp(20px, 2.3vw, 25px);
  --fs-h4: clamp(18px, 1.9vw, 21px);
  --fs-lead: clamp(17px, 1.6vw, 19px);
  --fs-body-lg: 17.5px;
  --fs-body: 16.5px;
  --fs-body-sm: 15px;
  --fs-label: 14px;
  --fs-note: 13.5px;
  --fs-small: 13px;
  --fs-small-2: 12.5px;
  --fs-xs: 12px;
  --fs-micro: 11.5px;
  --fs-nano: 11px;
  --fs-2xs: 10.5px;
  --fs-3xs: 10px;

  /* ---- ① 间距标尺（4/8 基；--space-N 主阶，--space-Nh 半阶） ---- */
  --space-1: 4px;   --space-2: 8px;   --space-3: 12px;  --space-4: 16px;
  --space-5: 24px;  --space-6: 32px;  --space-7: 48px;  --space-8: 64px;
  --space-1h: 6px;  --space-2h: 10px; --space-3h: 14px; --space-4h: 20px;
  --space-5h: 28px; --space-6h: 40px; --space-9: 80px;
  --gap-inline: var(--space-3);   /* 行内元素间隔 */
  --gap-block: var(--space-5);    /* 区块内间隔 */
  --gap-section: var(--space-7);  /* 章节间间隔 */

  /* ---- 栅格 ---- */
  --content-width: 1080px;
  --read-width: 720px;      /* 长文主体阅读宽度（640–760px 区间） */

  /* ---- 动效（控件 150–250ms / 章节 300–500ms） ---- */
  --t-fast: 180ms ease;
  --t-med: 320ms ease;
  --t-slow: 420ms ease;
}'''

m = re.search(r':root \{.*?\n\}', src, re.S)
if not m:
    sys.exit('FATAL: :root block not found')
root_span = (m.start(), m.end())
src = src[:m.start()] + NEW_ROOT + src[m.end():]
ntok = len(re.findall(r'\n  --[a-z0-9-]+:', NEW_ROOT))
print(f'OK  :root 块重写（{root_span[1]-root_span[0]} -> {len(NEW_ROOT)} 字符，令牌 {ntok} 项）')

body_head = root_span[0] + len(NEW_ROOT)
head, body = src[:body_head], src[body_head:]

# --------------------------------------------- 保护 @media print 块（印刷形态不动）
def protect_print_blocks(text):
    """返回 (可编辑文本, 受保护片段列表)。@media print 块整体替换为占位符。"""
    out, parts, i = [], [], 0
    while True:
        j = text.find('@media print', i)
        if j == -1:
            out.append(text[i:])
            break
        # 找该 @media 的块结束（配平花括号）
        k = text.find('{', j)
        depth, n = 0, k
        while n < len(text):
            if text[n] == '{':
                depth += 1
            elif text[n] == '}':
                depth -= 1
                if depth == 0:
                    break
            n += 1
        out.append(text[i:j])
        parts.append(text[j:n + 1])
        out.append('\x00PRINT%d\x00' % (len(parts) - 1))
        i = n + 1
    return ''.join(out), parts


body, print_parts = protect_print_blocks(body)
print(f'    保护 @media print 块 {len(print_parts)} 个')


def sub(old, new, expect=None, label=''):
    global body
    n = body.count(old)
    if n:
        body = body.replace(old, new)
    tag = label or old[:52]
    if expect is not None and n != expect:
        print(f'  !! {tag}  命中 {n}（期望 {expect}）')
        sys.exit('FATAL: replacement count mismatch')
    print(f'  {n:3d}x  {tag}')
    return n


print('[A] 事件类型色 -> --ty-*（语义令牌）')
sub('.tl-btn.t-start.is-active { background: #4a6b3a; border-color: #4a6b3a; }',
    '.tl-btn.t-start.is-active { background: var(--ty-start); border-color: var(--ty-start); }', 1, 't-start btn')
sub('.t-start     { color: #4a6b3a; }', '.t-start     { color: var(--ty-start); }', 1, 't-start tag')
sub('.gx-ev--start .gx-ev-core { background: #4a6b3a; }',
    '.gx-ev--start .gx-ev-core { background: var(--ty-start); }', 1, 'gx-ev start')
sub('.ev-etype--start { background: #4a6b3a; }',
    '.ev-etype--start { background: var(--ty-start); }', 1, 'ev-etype start')
sub('.tl-btn.t-risk.is-active { background: #8a5a00; border-color: #8a5a00; }',
    '.tl-btn.t-risk.is-active { background: var(--ty-risk); border-color: var(--ty-risk); }', 1, 't-risk btn')
sub('.t-risk      { color: #8a5a00; }', '.t-risk      { color: var(--ty-risk); }', 1, 't-risk tag')
sub('.gx-ev--risk .gx-ev-core { background: #8a5a00; }',
    '.gx-ev--risk .gx-ev-core { background: var(--ty-risk); }', 1, 'gx-ev risk')
sub('.ev-etype--risk { background: #8a5a00; }',
    '.ev-etype--risk { background: var(--ty-risk); }', 1, 'ev-etype risk')
sub('.tl-btn.t-milestone.is-active { background: #55524c; border-color: #55524c; }',
    '.tl-btn.t-milestone.is-active { background: var(--ty-milestone); border-color: var(--ty-milestone); }', 1, 't-milestone btn')
sub('.t-milestone { color: #55524c; }', '.t-milestone { color: var(--ty-milestone); }', 1, 't-milestone tag')
sub('.gx-ev--milestone .gx-ev-core { background: #55524c; }',
    '.gx-ev--milestone .gx-ev-core { background: var(--ty-milestone); }', 1, 'gx-ev milestone')
sub('.ev-etype--milestone { background: #55524c; }',
    '.ev-etype--milestone { background: var(--ty-milestone); }', 1, 'ev-etype milestone')

print('[B] 资源徽标色 -> --hue-*（色相刻度，与事件类型同源）')
sub('.rs-badge--opensource { background: #4a6b3a; }',
    '.rs-badge--opensource { background: var(--hue-olive); }', 1, 'rs opensource')
sub('.rs-act--on { background: #4a6b3a; }',
    '.rs-act--on { background: var(--hue-olive); }', 1, 'rs on')
sub('.rs-badge--community { background: #8a5a00; }',
    '.rs-badge--community { background: var(--hue-ochre); }', 1, 'rs community')
sub('.rs-act--stale { background: #8a5a00; }',
    '.rs-act--stale { background: var(--hue-ochre); }', 1, 'rs stale')
sub('.rs-badge--tools { background: #55524c; }',
    '.rs-badge--tools { background: var(--hue-graphite); }', 1, 'rs tools')
sub('.rs-act--arch { background: #55524c; }',
    '.rs-act--arch { background: var(--hue-graphite); }', 1, 'rs arch')

print('[C] 兜底色相 / 校验绿')
sub('#1c7c40', 'var(--ty-ok)', 2, 'ty-ok')
sub('.ev-etype { font-size: 10.5px; letter-spacing: .1em; font-weight: 700; color: #fff; background: #55524c;',
    '.ev-etype { font-size: 10.5px; letter-spacing: .1em; font-weight: 700; color: var(--on-hue); background: var(--hue-graphite);', 1, 'ev-etype base')
sub('.rs-badge, .rs-act { display: inline-block; font-size: 10.5px; letter-spacing: .08em; font-weight: 700; padding: 2px 9px; border-radius: 999px; color: #fff; background: #55524c;',
    '.rs-badge, .rs-act { display: inline-block; font-size: 10.5px; letter-spacing: .08em; font-weight: 700; padding: 2px 9px; border-radius: 999px; color: var(--on-hue); background: var(--hue-graphite);', 1, 'rs badge base')

print('[D] 朱红派生值')
sub('#d9a7a7', 'var(--accent-soft)', 2)
sub('box-shadow: 12px 12px 0 rgba(200, 64, 50, 0.9)', 'box-shadow: var(--shadow-accent)', 1)
sub('box-shadow: 18px 18px 0 rgba(200, 64, 50, 0.9)', 'box-shadow: var(--shadow-accent-lg)', 1)

print('[E] 浅底小字对比度修正（#8a857c 3.22 / #9a948b 2.64 -> --tx-3 5.02）')
sub('.pt-year { position: absolute; top: 58px; font-size: 10px; color: #8a857c;',
    '.pt-year { position: absolute; top: 58px; font-size: 10px; color: var(--tx-3);', 1, 'pt-year')
sub('.gx-axis span { position: absolute; transform: translateX(-50%); font-size: 10px; color: #8a857c; }',
    '.gx-axis span { position: absolute; transform: translateX(-50%); font-size: 10px; color: var(--tx-3); }', 1, 'gx-axis span')
sub('.gxl-q { display: block; color: #8a857c;',
    '.gxl-q { display: block; color: var(--tx-3);', 1, 'gxl-q')
sub('.gx-empty { font-size: 12px; color: #9a948b;',
    '.gx-empty { font-size: 12px; color: var(--tx-3);', 1, 'gx-empty')
sub('.cap-detail-empty { font-size: 12.5px; color: #9a948b;',
    '.cap-detail-empty { font-size: 12.5px; color: var(--tx-3);', 1, 'cap-detail-empty')

print('[F] 深底文字与剩余中性值')
sub('color: #d8d4cb', 'color: var(--txd-3)')
sub('color: #d9d4cc', 'color: var(--txd-3)')
sub('color: #b3aea3', 'color: var(--txd-4)')
sub('color: #a8a399', 'color: var(--txd-5)')
sub('#8a857c', 'var(--tx-4)')
sub('#9a948b', 'var(--tx-4)')

print('[G] 表面与色块文字')
sub('fill: #fffdf8', 'fill: var(--paper-0)', 1)
sub('background: #fffdf8', 'background: var(--paper-0)', 1)
sub('fill: #fff;', 'fill: var(--paper-0);', 4)
sub('background: #fff;', 'background: var(--paper-0);')
sub('color: #fff;', 'color: var(--on-hue);')
sub('color: #fff }', 'color: var(--on-hue) }')
sub('color: #1f3a5f;', 'color: var(--navy);', 1)

print('[H] 分隔/描边')
sub('rgba(23, 25, 29, 0.25)', 'var(--rule-mid)')
sub('rgba(23,25,29,.25)', 'var(--rule-mid)')
sub('rgba(23,25,29,.15)', 'var(--rule-soft)')
sub('rgba(23,25,29,.04)', 'var(--wash)')
sub('rgba(243, 240, 232, 0.25)', 'var(--hairline-paper)')

print('[I] 圆角')
sub('border-radius: 999px', 'border-radius: var(--r-pill)')
sub('border-radius: 50%', 'border-radius: var(--r-circle)')
sub('border-radius: 6px', 'border-radius: var(--r-4)')
sub('border-radius: 4px', 'border-radius: var(--r-3)')
sub('border-radius: 3px', 'border-radius: var(--r-2)')
sub('border-radius: 2px', 'border-radius: var(--r-1)')

print('[J] 阴影')
sub('box-shadow: 6px 6px 0 rgba(23, 25, 29, 0.08)', 'box-shadow: var(--shadow-1)')
sub('box-shadow: 8px 8px 0 rgba(23, 25, 29, 0.08)', 'box-shadow: var(--shadow-2)')
sub('box-shadow: 8px 8px 0 rgba(23, 25, 29, 0.1)', 'box-shadow: var(--shadow-2b)')
sub('box-shadow: 0 0 0 3px var(--paper)', 'box-shadow: var(--ring-paper)')

print('[K] 焦点环统一')
sub(':focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }',
    ':focus-visible { outline: var(--focus-w) solid var(--focus-color); outline-offset: var(--focus-offset); }', 1, 'base')
sub('  outline-color: var(--paper);', '  outline-color: var(--focus-color-invert);', 1, 'invert')
sub('.section-more a:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }',
    '.section-more a:focus-visible { outline: var(--focus-w-tight) solid var(--focus-color); outline-offset: var(--focus-offset); }', 1, 'section-more')
sub('.net-d-close:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }',
    '.net-d-close:focus-visible { outline: var(--focus-w-tight) solid var(--focus-color); outline-offset: var(--focus-offset-tight); }', 1, 'net-d-close')
sub('.cap-flow:focus-visible, .cap-node:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }',
    '.cap-flow:focus-visible, .cap-node:focus-visible { outline: var(--focus-w-tight) solid var(--focus-color); outline-offset: var(--focus-offset-tight); }', 1, 'cap-flow')
sub('.sv-axis a:focus-visible { outline: 2px solid var(--accent-bright); outline-offset: 2px; }',
    '.sv-axis a:focus-visible { outline: var(--focus-w-tight) solid var(--focus-color-dark); outline-offset: var(--focus-offset-tight); }', 1, 'sv-axis')
sub('.sv-axis a:focus-visible .sv-stage-box, .sv-axis a:focus-visible .sv-own-box { outline: 2px solid var(--accent-bright); }',
    '.sv-axis a:focus-visible .sv-stage-box, .sv-axis a:focus-visible .sv-own-box { outline: var(--focus-w-tight) solid var(--focus-color-dark); }', 1, 'sv-axis inner')

print('[L] 字号阶梯（值等价）')
for px, tok in [('17.5px', '--fs-body-lg'), ('16.5px', '--fs-body'), ('15px', '--fs-body-sm'),
                ('14px', '--fs-label'), ('13.5px', '--fs-note'), ('13px', '--fs-small'),
                ('12.5px', '--fs-small-2'), ('12px', '--fs-xs'), ('11.5px', '--fs-micro'),
                ('11px', '--fs-nano'), ('10.5px', '--fs-2xs'), ('10px', '--fs-3xs')]:
    sub(f'font-size: {px}', f'font-size: var({tok})')

# --------------------------------------------- 还原被保护的 @media print 块
for i, blk in enumerate(print_parts):
    body = body.replace('\x00PRINT%d\x00' % i, blk)

src = head + body
io.open(P, 'w', encoding='utf-8', newline='\n').write(src)
print(f'\n写入 {P}：{orig_len} -> {len(src)} 字符')

print('残留硬编码自检（正文区）：')
for pat, note in [(r'#4a6b3a|#8a5a00|#55524c|#1c7c40', 'etype 类型色'),
                  (r'#d9a7a7|#8a857c|#9a948b|#b3aea3|#a8a399|#d9d4cc|#d8d4cb', '中性/朱红派生'),
                  (r'font-size: \d', '字号'), (r'border-radius: \d', '圆角'),
                  (r'outline: \dpx solid', '焦点环'), (r'\b#fff\b(?!df8)', '纯白（应仅余 print/内联）')]:
    hits = re.findall(pat, body)
    print(f'  {note:14s} 残留 {len(hits):3d}  {sorted(set(hits))[:5]}')
