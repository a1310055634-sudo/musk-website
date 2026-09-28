# -*- coding: utf-8 -*-
"""V7 R1 色彩令牌归一化：
- 硬编码旧色统一到 :root 令牌（CSS 上下文）或新十六进制值（SVG 属性 / 内嵌脚本 / favicon / theme-color）。
- 幂等：重复运行无二次效果。
用法: python tools/v7r1-normalize-colors.py
"""
import glob, io, re

HTML_FILES = sorted(glob.glob("*.html"))
# timeline.html 内嵌 <script> 含色值（var() 在 JS 无效）→ 全文件走直换
SCRIPT_HEX_FILES = {"timeline.html"}
SVG_HEX_FILES = {"money.html", "numbers.html", "stories.html", "capital-evolution.html"}

# (旧, 新, 说明)
COMMON = [
    ("fill='%237c2d2d'", "fill='%23C84032'", "favicon 底色"),
    ("fill='%23faf9f6'", "fill='%23F3F0E8'", "favicon 字色"),
    ('content="#faf9f6"', 'content="#F3F0E8"', "theme-color"),
    ("rgba(124, 45, 45,", "rgba(200, 64, 50,", "accent-alpha"),
    ("rgba(124,45,45,", "rgba(200,64,50,", "accent-alpha-tight"),
    ("rgba(250, 249, 246,", "rgba(243, 240, 232,", "paper-alpha"),
    ("rgba(250,249,246,", "rgba(243,240,232,", "paper-alpha-tight"),
    ("rgba(26, 26, 26,", "rgba(23, 25, 29,", "ink-alpha"),
    ("rgba(26,26,26,", "rgba(23,25,29,", "ink-alpha-tight"),
]
SVG_DIRECT = [
    ('fill="#7c2d2d"', 'fill="#C84032"'),
    ('stroke="#7c2d2d"', 'stroke="#C84032"'),
]
CSS_VARS = [
    ("#7c2d2d", "var(--accent)"),
    ("#faf9f6", "var(--paper)"),
    ("#1a1a1a", "var(--ink)"),
    ("#5c574e", "var(--muted)"),
]
HEX_DIRECT = [
    ("#7c2d2d", "#C84032"),
    ("#1a1a1a", "#17191d"),
    ("#faf9f6", "#F3F0E8"),
    ("#5c574e", "#5b5850"),
]

def process(path, is_css, use_hex):
    raw = io.open(path, encoding="utf-8", newline="").read()
    n = 0
    for old, new, _ in COMMON:
        c = raw.count(old); n += c; raw = raw.replace(old, new)
    if use_hex:
        for old, new in SVG_DIRECT:
            c = raw.count(old); n += c; raw = raw.replace(old, new)
        for old, new in HEX_DIRECT:
            c = raw.count(old); n += c; raw = raw.replace(old, new)
    else:
        for old, new in SVG_DIRECT:
            c = raw.count(old); n += c; raw = raw.replace(old, new)
        if is_css or not use_hex:
            for old, new in CSS_VARS:
                c = raw.count(old); n += c; raw = raw.replace(old, new)
    if n:
        io.open(path, "w", encoding="utf-8", newline="").write(raw)
    return n

total = 0
for f in HTML_FILES:
    k = process(f, is_css=False, use_hex=f in SCRIPT_HEX_FILES)
    if k: print(f"{f}: {k} 处")
    total += k
k = process("style.css", is_css=True, use_hex=False)
print(f"style.css: {k} 处"); total += k
k = process("app.js", is_css=False, use_hex=True)
print(f"app.js: {k} 处"); total += k
print(f"TOTAL {total} 处替换")
