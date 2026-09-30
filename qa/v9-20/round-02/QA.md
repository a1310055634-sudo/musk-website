# V9-20 R02 验收记录 · X 帖回捞 I（2020–2021）

日期：2026-10-01 ｜ 版本：v8.2.0 ｜ 分支：main（纯本地，不推送）

## 轮次范围与完成情况

- 目标：x-posts.html 23→27± 张；镜像 2020–2021 全量回捞；重验 V8 弃收件（Hertz 对冲）。
- 完成：**+4 卡（23→27）**；Hertz 对冲重验成功入册；两处存量年份分组错位一并修正。

## 采料方法与来源留档

- 管线升级：elonmuskarchive.org **Agent API**（免钥、无限流）
  - 全量清单：`/agents/index?type=posts&year=Y&month=MM&list=1&fields=id,date,title,url&sort=date_asc`
    → **2020 年 3,359 帖 / 2021 年 3,111 帖**（V8 R08「早期覆盖率有限」判断作废）
  - 精确短语检索：`/agents/search?q="…"&type=posts`
  - 逐字全文：`/agents/transcript/{id}`
  - 走页脚本：tools/v9r02-walk-posts.py（清单抓取，R03 可复用）
- 四帖证据（transcript JSON + snowflake 解码字段，存 `sources/`）：

| 卡 | status ID | snowflake UTC | 站内口径注 |
|---|---|---|---|
| p2020-04-29 FREE AMERICA NOW | 1255380013488189440 | 2020-04-29 06:14:53 | 美西 4.28 深夜 |
| p2021-01-26 Gamestonk!! | 1354174279894642703 | 2021-01-26 21:08:02 | 美股当日收盘后 |
| p2021-05-05 Starship landing nominal! | 1390073153347592192 | 2021-05-05 22:37:20 | — |
| p2021-11-02 Hertz 对冲 | 1455351085170823169 | 2021-11-02 01:48:32 | 美国时间 11.01 晚（账本「11.01 对冲」即此帖） |

- Hertz 重验：镜像精确短语「no contract has been signed yet」「zero effect on our economics」双命中同一帖 x-1455351085170823169，四段全文含第三句「only sell cars to Hertz for the same margin as to consumers」（首次入册）。

## 甄别与弃收（EXPANSION.md 同步）

- 弃收：Bitcoin 暂停购车帖（2021-05-12, status/1392602041025867777）——镜像三短语 0 命中（同日「Tesla & Bitcoin」短帖在库、非同一帖）；重验条件=镜像补录或 SEC/官方文锚。
- 留档：Trump 背书帖（2024-07-13/14）→ R03 深水区用 Agent API 重打。
- 未立卡：「卖房系列后续」以 p2020-05-01 既有卡注弧线为准（JRE #1470 自释 + 2021 无房确认）。

## 结构与存量修复

- 四卡严格克隆 tweet-card 五件套（tweet-top/tweet-text/tweet-zh/tweet-note，类名零新增）。
- 存量错位修正两处：①「2020」年份条错标「2021」→ 改正并补 2021 条；②「2023」条压住 p2022-12-18 → 归位到 p2023-07-23 前。
- R02 自身一处返工：集成脚本锚选在 p2022-03-26 卡标签（其前即 2022 条），致 05-05/11-02 误入 2022 组——v9r02-fixgroup.py 归位并加「逐卡年份一致」静态断言。

## 验证证据

- **verify.py 9/9 全绿**（37 页 / 索引 254 = 109+14+33+**27**+5+53+4+9 / 版本 8.2.0 一致）。
- **CDP 探针 24/24 全过**（tools/v9r02-probe.js）：索引含 4 新帖、X 帖计数 27、Hertz 逐字句入索引；27 卡渲染/时序升序/五件套唯一性/Permalink 一一对应；新卡双语（EN+CJK）；年份条 2020/2021 正确 + 2021 组卡序 + p2022-12-18 归 2022；Hertz 三句逐字在卡 + 跨页锚 primary.html#e2021-10-25 真实存在 + 卡间互链双向解析；search.html?q=Gamestonk 命中含 p2021-01-26；390 视口 scrollWidth≤390 零溢出。
- node --check：app.js / cite.js 通过。
- 生成器链：build-search-index（断言 23→27 同步）/ build-ledger-timeline（109 节点幂等）/ sync-changelog（191 条）/ build-epub（203,255 B / 24 章）。
- 截图：before/（首屏双视口）+ after/（首屏双视口与 before 逐字节一致——首屏无改动即无回归；另有定位截图 freeam 桌面 149KB / hertz 桌面 78KB / gamestonk 手机 56KB，CDP scrollIntoView 拍摄，tools/v9r02-shot.js 可复用）。

## 过程记录（探针环境坑，供后续轮参考）

- 本机 **9227 端口被 aDrive.exe 占用**（连接通但不响应，CDP 轮询挂死）——探针端口改 9333+；getJSON 加 3s 超时。
- 被 timeout 杀掉的 node 会遗留孤儿 headless Chrome（占端口+内存缓存旧页面），探针需用全新 user-data-dir + 端口避让；清理脚本 _tmp 段有留档（只杀带 remote-debugging-port=93xx 的 headless 实例）。
- headless `--screenshot` 不认锚点滚动，定位截图须走 CDP scrollIntoView + captureScreenshot。

## 结论

验收通过。成果提交 + 账本回填提交（含 build-revisions/EPUB 重刷）各一，纯本地不推送。下一轮：R03 X 帖回捞 II（2022–2025 深水区，目标 27→31±，含 Trump 背书帖 Agent API 重验）。
