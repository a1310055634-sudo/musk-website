# -*- coding: utf-8 -*-
"""R02 素材加工：替换/新产 assets 图片，全部保留加工记录输出。
用法: python tools/prep-assets.py
来源与许可见 ASSETS.md（由本轮一并建立）。"""
import os
from PIL import Image

REVIEW = os.path.join(os.environ.get("TEMP", "/tmp"), "v7r2-review")
ASSETS = "assets"

def load(name):
    return Image.open(os.path.join(REVIEW, name + ".jpg")).convert("RGB")

def save(im, name, max_w=None, quality=82):
    if max_w and im.width > max_w:
        h = round(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    out = os.path.join(ASSETS, name)
    im.save(out, "JPEG", quality=quality, optimize=True, progressive=True)
    kb = os.path.getsize(out) // 1024
    print(f"OK  {name:26s} {im.width}x{im.height}  {kb}KB")
    return im

# 1) falcon-heavy.jpg 替换：Falcon Heavy 演示飞行双助推器同步着陆（SpaceX · CC0）
#    保持 960x1440（2:3）与旧文件一致，indepth.html 尺寸声明零扰动
src = load("falcon-liftoff")
assert src.width * 3 == src.height * 2, src.size  # 2:3 竖幅
save(src.resize((960, 1440), Image.LANCZOS), "falcon-heavy.jpg", quality=82)

# 2) starship-catch.jpg：IFT-5 助推器塔捕（Jurvetson · CC BY 2.0）
save(load("starship-catch"), "starship-catch.jpg", max_w=1200, quality=80)

# 3) x-hq.jpg：旧金山 Twitter/X 总部（osunpokeh · CC BY-SA 4.0）3:2 上部裁切保住 @twitter 标牌
src = load("x-hq-2022")
assert src.width == src.height, src.size  # 原图正方形
crop_h = round(src.width * 2 / 3)
save(src.crop((0, 0, src.width, crop_h)), "x-hq.jpg", max_w=1200, quality=80)

# 4) cybertruck.jpg：Cybertruck 展车（N2e · CC0）3:2 中心偏左对准车头
src = load("cybertruck-denver")
assert src.width * 9 == src.height * 16, src.size  # 16:9
crop_w = round(src.height * 3 / 2)
x0 = round(src.width * 0.037)  # 原图 4032 中偏移 150 的等比位置
save(src.crop((x0, 0, x0 + crop_w, src.height)), "cybertruck.jpg", max_w=1200, quality=80)

# 5) R03 封面备用裁切（来自已溯源 portrait.jpg 主图）
src = Image.open(os.path.join(ASSETS, "portrait.jpg")).convert("RGB")
assert src.size == (960, 1272), src.size
save(src.crop((0, 60, 960, 700)), "portrait-hero.jpg", quality=85)       # 3:2 横版
save(src.crop((0, 36, 960, 1236)), "portrait-hero-mobile.jpg", quality=85)  # 4:5 竖版

print("done")
