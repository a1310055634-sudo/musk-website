# -*- coding: utf-8 -*-
"""修正 CHANGELOG：把误插的 ACCEPTANCE 全文替换为规范 v10.5.0 条目。"""
import io

s = io.open('CHANGELOG.md', encoding='utf-8').read()
start = s.find('# V10-15 N05 验收记录')
end = s.find('## v10.4.0')
assert 0 < start < end, (start, end)
entry = '''## v10.5.0 — 2026-10-02 · V10-15 N05/15：早期年代 I——访谈库 2003–2012 深挖（+1 条）

**主题包成果（V10-15 N05 · 第一手信息线开跑）**
- **候选池实测（预告修正）**：镜像 161 场中 2013 前场次 9 场，逐场试拉 transcript——**仅 wired-musk-2008 有逐字稿**（4,008 字符），其余 8 场 404。R04/R05「60-minutes-2012 官方转写在档」判断经实测不成立（端点 404），该保留池成员降级「待外部逐字源」，EXPANSION 已注记。
- **+1 条入册（访谈 42→43，索引 318→319）**：**i2008-08-05**「乐观悲观，滚他妈的；我们会让它发生」——Wired.com 电话专访（Falcon 1 三连败后、四飞前 5 周、金融危机最坏周）：主句 "Optimism, pessimism, fuck that; we're going to make it happen…"（站外广为征引名句的**原始出处补全**，站内四页查重零命中）+ "That was the dumbest thing I've ever said."（「钱只够烧三次」论当场自嘲修正）+ "Patience is a virtue…It's a tough lesson."；互链 i2008-09-28（四飞成功）与 survival-2008（144 天专题）；transcript 存档 qa/v10-15/round-05/sources/。
- 2003–2012 断档改善有限（+1 条 2008），8 场无档留档如实入账（重验条件=镜像补档或外部逐字源）。

**质量门**
- verify.py 9 项全绿（38 页 / 索引 319）；CDP 探针 tools/v10n05-probe.js 8/8（渲染/六件套/逐字主句/双语/互链双通/时间序/检索 hell-bent 命中/真 390 零溢出）；版本三件套 10.4.0→10.5.0（三步法）；EPUB 重跑（224,144 B）。本轮仅本地提交，不推送。

'''
s = s[:start] + entry + s[end:]
io.open('CHANGELOG.md', 'w', encoding='utf-8', newline='').write(s)
print('CHANGELOG fixed')
