# V10-15 N05 验收记录 · 早期年代 I：访谈库 2003–2012 深挖（v10.5.0）

日期：2026-10-02（定时任务第八次触发，锁 run=V10-15-N05）

## 候选池实测（如实盘点，与预告预期有偏差）

interviews-all.json 161 场中 2013 前场次 **9 场**；逐场试拉 transcript 端点：**仅 1 场有逐字稿**（wired-musk-2008，4,008 字符，Wired.com Carl Hoffman 2008-08-05），其余 8 场 404（latimes-2003/pbs-2007/churchill-2009/kpcs-2009/charlie-rose-2009/npc-2011/60-minutes-2012/foundation-2012）。
**预告修正**：R04/R05 留档的「60-minutes-2012-03-18 官方转写在档可立」经本轮实测不成立（transcript 端点 404）——保留池该成员降级为「待外部逐字源」（CBS 官网/电视播出稿），不影响 N11 其余四场。

## 立条：+1 条（i2008-08-05，访谈 42→43）

- **i2008-08-05**「乐观悲观，滚他妈的；我们会让它发生」——Wired.com 电话专访（三连败后、四飞前 5 周、金融危机最坏周）：主句 "Optimism, pessimism, fuck that; we're going to make it happen. As God is my bloody witness, I'm hell-bent on making it work."（站外广泛征引名句的**原始出处补全**，查重站内 4 页零命中）+ "That was the dumbest thing I've ever said."（「钱只够烧三次」论的当场自嘲修正）+ "Patience is a virtue…It's a tough lesson."；after 注 Founder's Fund 过桥投资确认 + 互链 i2008-09-28（四飞成功）与 survival-2008（144 天专题）。
- 镜像 transcriptSource：Wired.com (Carl Hoffman, Aug 5, 2008)——媒体专访但镜像逐字存档（R04 interview 库同口径）。
- 查重：站内 4 页（primary/quotes/survival/interviews）名句零命中；与 i2008-09-28 成「三败→四飞」弧线互补。

## 留档（8 场，EXPANSION 同步）

latimes-2003 / pbs-2007 / churchill-club-2009 / kpcs-2009 / charlie-rose-2009 / npc-2011 / 60-minutes-2012 / foundation-2012——镜像无逐字稿；重验条件=镜像补档或外部逐字源（CBS/C-SPAN 官网等）。2003–2012 断档改善有限（+1 条 2008），如实入账。

## 验证

| 项 | 结果 |
|---|---|
| 索引 | ✓ 319 条（访谈 42→43，断言同步） |
| verify.py | ✓ 9/9 |
| CDP 探针 tools/v10n05-probe.js（端口 9388） | ✓ **8/8**：渲染/六件套/逐字主句/双语切换/互链双通/时间序/检索命中/真 390 零溢出 |
| 版本三件套 | ✓ 10.4.0→10.5.0 |

## 工程记录

- 集成断言三修：interviews.html iv-item 标签数=入索引数+1（legacy 无 id 条目，R07 已知坑的现役复现）——before/after 断言改为 43/44。
- 探针「假 390」自误修正（未切视口就查溢出）——改真 390 模拟+截图。

## 提交

- 成果提交：`[V10-15 N05]`（本地，不推送）；第二提交：账本回填+revisions+EPUB 重刷。
