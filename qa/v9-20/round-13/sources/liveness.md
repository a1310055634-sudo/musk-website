# R13 核活留档 · 社区与档案资源（2026-10-01）

核活路径三路法：浏览器 UA curl（直连）→ WebFetch（服务端）→ 服务端读取器。
本机路径说明：curl 时 `%{remote_ip}` 对 en.wikipedia.org 显示 127.0.0.1（本机代理/hosts 接管），
**内容为真**（title/正文/2.68MB 实量核对），故 R10「wikipedia DNS 污染不可达」判断本轮推翻。

## 直连实测（浏览器 UA curl, 2026-10-01）

| URL | code | 备注 |
|---|---|---|
| https://en.wikipedia.org/wiki/Elon_Musk | 200 | 2,680,618 B，title「Elon Musk - Wikipedia」，正文 525 处命中 |
| https://en.wikipedia.org/wiki/SpaceX | 200 | 1,533,580 B，title「SpaceX - Wikipedia」 |
| https://en.wikipedia.org/wiki/Tesla,_Inc. | 200 | |
| https://en.wikipedia.org/wiki/Neuralink | 200 | |
| https://en.wikipedia.org/wiki/The_Boring_Company | 200 | |
| https://en.wikipedia.org/wiki/Acquisition_of_Twitter_by_Elon_Musk | 200 | 1,683,619 B |
| https://en.wikipedia.org/wiki/List_of_SpaceX_launches | 200 | 51,547 B（列表页） |
| https://en.wikipedia.org/wiki/Starship | 200 | 151,653 B |
| https://en.wikipedia.org/wiki/Starlink | 200 | 1,966,776 B |
| https://en.wikipedia.org/wiki/Grok_(chatbot) | 200 | 1,057,599 B |
| https://en.wikipedia.org/wiki/Tesla_Model_3 | 200 | 1,208,799 B |
| https://en.wikipedia.org/wiki/Twitter | 200 | → 重定向 X (social network)，2,085,630 B |
| https://simple.wikipedia.org/wiki/Elon_Musk | 200 | 297,795 B（简版） |
| https://en.wikipedia.org/wiki/List_of_SpaceX_launch_vehicles | 404 | 弃（旧标题，已并入 List of SpaceX launches） |

## 媒体/档案/社区站实测

| URL | code | 判定 |
|---|---|---|
| https://www.teslarati.com/ | 200 | 收（Tesla 爱好者新闻站） |
| https://electrek.co/ | 200 | 收（EV 新闻与 Tesla 追踪） |
| https://arstechnica.com/ | 200 | 收（科技媒体，太空频道） |
| https://arstechnica.com/space/ | 200 | 收（太空条线） |
| https://www.nasaspaceflight.com/ | 200 | 收（独立航天新闻+论坛） |
| https://everydayastronaut.com/ | 200 | 收（EA，星舰巡礼原始出处） |
| https://www.space.com/ | 200 | 收（太空新闻） |
| https://www.theverge.com/elon-musk | 200 | 收（专题 hub） |
| https://techcrunch.com/tag/elon-musk/ | 200 | 收（tag 页） |
| https://www.cnbc.com/elon-musk/ | 200 | 收 |
| https://www.bbc.com/news/topics/c302m85q5ljt | 200 | 收（BBC 专题） |
| https://spaceflightnow.com/ | 403 | 弃（curl UA 被拦，未过服务端复验） |
| https://apnews.com/hub/elon-musk | 403 | 弃（同） |
| https://www.reuters.com/... | 401 | 弃（同） |
| https://www.businessinsider.com/elon-musk | 000 | 留档（连接失败） |
| https://www.science.org/ | 403 | 弃 |
| https://www.sec.gov/edgar/search/ | 403 | 弃（需合规 UA；SEC 主库已在册 sec-edgar-tesla） |
| https://www.nytimes.com/topic/person/elon-musk | 403 | 弃 |
| https://web.archive.org/ | 000 | 留档（Wayback 本机不可达，WebFetch 亦失败） |
| https://www.space.com/elon-musk | 404 | 弃（改收 space.com 主站） |

## Reddit 社区档案（JS 空壳，本轮不收）

| URL | curl | 判定 |
|---|---|---|
| https://www.reddit.com/r/teslamotors/wiki/index | 200 | **假活**：8,422 B JS 空壳，title 仅「Reddit」，正文 0 |
| https://old.reddit.com/r/teslamotors/wiki/index | 200 | 同上，WebFetch 复验亦为空壳（仅欢迎语） |
| https://www.reddit.com/r/SpaceXLounge/wiki/index | 200 | 同上 8,423 B 空壳 |
| https://www.reddit.com/r/teslamotors/wiki/index.json | 403 | JSON API 被拦 |
| https://www.reddit.com/r/SpaceXLounge/wiki/index.json | 403 | 同上 |

→ 结论：Reddit 本轮**直连返回 200 但内容为空壳、JSON API 403**，无法确认 wiki 正文在线，
按纪律 B「宁缺毋滥」**本轮不收**（R12 曾收 r/SpaceX wiki，其核活路径为服务端读取器 200 且内容到手；
本轮服务端读取器对 teslamotors/SpaceXLounge 返回同为空壳，不满足「内容到手」门槛）。
留档 EXPANSION，重验条件=服务端读取器能取得 wiki 正文或 Reddit 放开 JSON API。

## 工具与数据类实测

| URL | code | 备注 |
|---|---|---|
| https://planet4589.org/space/ | 200 | Jonathan McDowell 太空档案（独立学者，权威数据源） |
| https://www.spacelaunchschedule.com/ | 200 | 发射日程 |
| https://nextspaceflight.com/launches/ | 200 | 已在册（nextspaceflight） |
| https://www.spacexstats.xyz/ | 000 | 留档（疑似下线） |

## Tesla 生态开源实测（api.github.com 串行）

| repo | stars | pushed | archived | license | 判定 |
|---|---|---|---|---|---|
| tdorssers/TeslaPy | 417 | 2026-07 | False | MIT | 收（Python Owner API 客户端，活跃） |
| mseminatore/TeslaJS | 423 | 2024-09 | False | MIT | 收（NodeJS 非官方库） |
| vloschiavo/powerwall2 | 290 | 2024-10 | False | Apache-2.0 | 收（Powerwall 2 本地网关 API 文档） |
| adriankumpf/tesla_auth | 648 | 2026-09 | False | MIT | 候选留档（token 生成工具，与 TeslaPy 功能重叠，本轮不收） |
| jsgoecke/tesla | 327 | 2024-12 | False | MIT | 候选留档 |
| jonasman/TeslaSwift | 255 | 2026-06 | False | MIT | 候选留档 |
| rt-bishop/Look4Sat | 1501 | 2026-09 | False | GPL-3.0 | 排除（通用卫星追踪，非马斯克系） |
| KULeuven-COSIC/Starlink-FI | 1044 | 2022-11 | False | None | 排除（学术攻防研究） |
| sgayou/subaru-starlink-research | 599 | 2020-09 | False | MIT | 排除（斯巴鲁车载同名） |
| danopstech/starlink | 370 | 2022-09 | False | GPL-3.0 | 候选留档（星链监测系统） |

## 文档站实测

| URL | code | 备注 |
|---|---|---|
| https://www.teslaapi.io/ | 200 | 收（社区 API 文档站，与 tesla-api.io 并列） |
| https://tesla-api.timdorr.com/ | 200 | 收（timdorr 文档站，仓库已收故收其文档落地） |
| https://teslaownersonline.com/ | 202 | 收（车主社区，202 非 2xx 标准 200——按实记，内容可读） |
| https://forum.nasaspaceflight.com/ | 403 | 弃（论坛需登录/被拦） |
| https://www.teslamotorsclub.com/ | 000 | 留档（连接失败，改用 teslaownersonline） |
