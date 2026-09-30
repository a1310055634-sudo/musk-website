# R10 种子资源核活留档（2026-10-01，生成机实测）

## 已入库 10 条（curl http_code 或 WebFetch / GitHub API 实测）

| id | URL | 核活结果 | 附加实测 |
|---|---|---|---|
| sec-edgar-tesla | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001318605&type=10-K&dateb=&owner=include&count=40 | HTTP 200（浏览器 UA 403 → **SEC 合规 UA（含联系邮箱）200**） | 政府公开数据 |
| tesla-vehicle-command | https://github.com/teslamotors/vehicle-command | HTTP 200 | api.github.com：705★ / pushed 2026-09-25 / Apache-2.0 / 未存档 |
| teslamate | https://github.com/teslamate-org/teslamate | HTTP 200 | api.github.com：9,061★ / pushed 2026-09-30 / AGPL-3.0 / 未存档 |
| grok-1 | https://github.com/xai-org/grok-1 | HTTP 200（**原 xai-org/grok 已 301 迁移至 grok-1**，API repositories/773286980 跟随后建档） | api.github.com：52,239★ / pushed 2024-08-30 / Apache-2.0 / 未存档 |
| elonmuskarchive | https://elonmuskarchive.org/ | HTTP 200 | 本站第一手采料镜像（R02-R07 管线在用） |
| wbw-neuralink | https://waitbutwhy.com/2017/04/neuralink.html | HTTP 200 | — |
| flight-club | https://www.flightclub.io/ | HTTP 200 | WebFetch 确认在站（JS 渲染页，标题 Flight Club；功能描述按公知口径保守表述） |
| next-spaceflight | https://nextspaceflight.com/ | HTTP 200 | WebFetch 确认内容（Crew-13/Transporter 18 在列=数据新鲜） |
| launch-library-2 | https://thespacedevs.com/llapi | HTTP 200 | — |
| starlink-sx | https://starlink.sx/ | HTTP 200 | WebFetch 确认内容（Mike Puchol，非官方注明） |

## 本机不可核活（未入库，EXPANSION.md 留档待重验）

| 候选 | URL | 现象 | 判读 |
|---|---|---|---|
| Tesla 专利开放博文 | tesla.com/blog/all-our-patent-are-belong-you | curl 403 + WebFetch 403 | 反爬，非死链；R11 换路径重验 |
| SpaceX Starship 页 | spacex.com/vehicles/starship/ | curl 000 + WebFetch 403 | 反爬/连接失败；R11 重验 |
| Neuralink Patient Registry | neuralink.com/patient-registry/ | curl 000 | 本机连接失败；R11 重验 |
| Tesla 开发者文档 | developer.tesla.com/ | curl 403 | 反爬；R11 重验 |
| Wikipedia Elon Musk | en.wikipedia.org/wiki/Elon_Musk | curl 000（DNS 解析至 31.13.88.26=污染地址） | 本机 DNS 污染不可达；R13 换镜像/离线快照路径 |
| tesla-api.io | tesla-api.io/ | curl 000 + WebFetch ENOTFOUND | **域名可能已失效**（DNS 不解析）；R12 重验，若确认死链按纪律标「存档」 |
| OpenAI 早期博客 | openai.com/... | 未测（同域预期反爬） | R11 一并重验 |

环境备注：web_reader MCP 当时限流（429）不可用；核活路径=浏览器 UA curl → 失败则 WebFetch → GitHub 走 api.github.com。
