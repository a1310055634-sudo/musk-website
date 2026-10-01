# V9-20 R12 核活留档（2026-10-01）

方法：GitHub 仓库走 api.github.com（无认证、串行 2s 间隔）；普通站点浏览器 UA curl → 失败则服务端读取器（web_reader MCP）复核。**卡内 note 如实注明核活路径。**

## 核活全表（6 入库 + 3 甄别排除）

| URL | 本机 curl | GitHub API / 服务端读取器 | 结论 |
|---|---|---|---|
| github.com/timdorr/tesla-api | —（走 API） | 200：2,065★ · pushed 2026-03 · MIT · 未存档 | **入册**（维护中） |
| github.com/r-spacex/SpaceX-API | —（走 API） | 200：10,912★ · pushed 2024-08 · Apache-2.0 · **archived=true** | **入册**（存档） |
| github.com/sparky8512/starlink-grpc-tools | —（走 API） | 200：710★ · pushed 2026-09 · Unlicense | **入册**（维护中） |
| tesla-api.io | DNS ENOTFOUND（nslookup 本地 resolver NXDOMAIN） | **服务端读取器 200**：站点在线，自注 "As of January 2024, this site is no longer being maintained" | **入册**（停更）——**R10 死链判断证伪** |
| old.reddit.com/r/spacex/wiki/index | 000（Reddit 反爬） | 服务端读取器 200：r/SpaceX Wiki Index 内容到手 | **入册**（community） |
| www.tessie.com/ | **200 直连** | 服务端读取器内容确认（商业遥测服务） | **入册**（tools） |
| rt-bishop/Look4Sat | GitHub 搜索候选 | 1,501★，通用卫星追踪 Android 应用 | 甄别排除：与马斯克系弱相关 |
| sgayou/subaru-starlink-research | GitHub 搜索候选 | 599★，**斯巴鲁车载 StarLink** 安全研究 | 甄别排除：同名不同司 |
| SmoothWAN/SmoothWAN | GitHub 搜索候选 | 346★，通用组网 | 甄别排除：主题无关 |

## tesla-api.io 死链判定过程（R10 留档项处置）

1. 本机 resolver（gd.cnmobile.net）NXDOMAIN（R10 同结果）；
2. 独立解析尝试 8.8.8.8 / 1.1.1.1 直连 UDP——**全部超时（本机网络环境下独立 DNS 不可行）**；
3. dns.google DoH 直连 curl 超时；
4. **服务端读取器核活 HTTP 200 且站点在线**——站点自注 2024-01 起弃用（"The Tesla API has matured, and Tesla now provides official API documentation"），页面完整可读；
5. 结论：**本地运营商 DNS 污染**（同 en.wikipedia.org 污染至 31.13.88.26 机制），非死链。收录为「停更」，卡内注明判定过程与路径。

## 教训

- GitHub 搜索结果按星数排序会混入同名无关项目（Subaru StarLink）——按星数收录前必须读 description 甄别公司归属。
- 本机 DNS 对 .io 域名的 NXDOMAIN 不可作为死链证据（污染前科：wikipedia/tesla-api.io 两例）——死链判定必须服务端路径交叉确认。
