# R14 外链抽样核活留档（2026-10-01，质量节点②要求 ≥10 条）

抽样规则：四分类各取（官方/开源/社区/工具），覆盖 R10–R13 各轮条目，浏览器 UA curl -L 直连；
SEC 依 R10 记载须用含联系邮箱的合规 UA（浏览器 UA 403）。

| # | 分类 | URL | code | 备注 |
|---|---|---|---|---|
| 1 | official | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001318605&type=10-K... | **200** | 合规 UA `MuskIncBot/1.0 (research; contact…)`；浏览器 UA 403（R10 已记） |
| 2 | official | https://www.spacex.com/vehicles/starship/ | 200 | R11 入册 |
| 3 | opensource | https://github.com/teslamate-org/teslamate | 200 | R10 入册 |
| 4 | opensource | https://github.com/xai-org/grok-1 | 200 | R10 入册（301 迁移已跟） |
| 5 | community | https://en.wikipedia.org/wiki/SpaceX | 200 | R13 入册（污染判定证伪） |
| 6 | community | https://old.reddit.com/r/spacex/wiki/index | 200 | R12 入册（服务端读取器路径） |
| 7 | community | https://waitbutwhy.com/2017/04/neuralink.html | 200 | R10 入册 |
| 8 | tools | https://www.flightclub.io/ | 200 | R10 入册 |
| 9 | tools | https://thespacedevs.com/llapi | 200 | R10 入册（Launch Library 2） |
| 10 | tools | https://www.tessie.com/ | 200 | R12 入册 |

**结果：10/10 可达（100%）**——抽样的四分类各 2~3 条全部 HTTP 200（SEC 一条按合规 UA 口径）。
补充实测（非抽样、R13 新增项回落验证）：github.com/xai-org/grok-1 200 / starlink.sx 200 /
nextspaceflight.com 200 / planet4589.org/space 200。

> 说明：本项为「抽查外链当前可达性」，非逐条重核全部 36 条（各条已在自身轮次于卡内注明核活日期与响应码，
> 见 resources.html 的「核活」字段行）。地区性屏蔽与反爬策略可能造成差异，页面已声明。
