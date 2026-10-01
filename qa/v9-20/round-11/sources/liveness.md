# V9-20 R11 核活留档 · 三路法全记录（2026-10-01）

方法：①浏览器 UA curl（tools/v9r11-liveness.py，串行 1.5s 间隔）；②失败项 WebFetch 复核；③再失败项服务端读取器（web_reader MCP，当日恢复可用）复核并取得官方 meta/正文。**入库条目的 http 字段记录成功路径的响应码；凡非直连成功者，卡内 note 如实注明核活路径。**

## 候选全表（14 URL）

| URL | curl | WebFetch | 服务端读取器 | 结论 |
|---|---|---|---|---|
| spacex.com/vehicles/starship/ | 403 | 403 | 200（官方 meta 全） | **入册** r-spacex-starship |
| spacex.com/vehicles/falcon-9/ | 403 | — | 200 | **入册** r-spacex-falcon9 |
| spacex.com/updates/ | 403 | — | 200（og:title 在） | **入册** r-spacex-updates |
| developer.tesla.com/ | 403 | 403 | 200（Fleet API 文档正文到手） | **入册** r-tesla-fleet-api |
| neuralink.com/patient-registry/ | 000（WinError 10054 连接重置） | ECONNRESET | 200（Patient Registry 标题+og:image） | **入册** r-neuralink-registry |
| openai.com/blog/introducing-openai/ | 403 | 403 | 200（全文到手：非营利宣言、"co-chairs are Sam Altman and Elon Musk"） | **入册** r-openai-2015 |
| x.ai/ | 000（WinError 10060 超时） | — | 200（xAI 使命+Grok 4 meta） | **入册** r-xai-official |
| boringcompany.com/ | **200 直连** | — | 200（使命句+Prufrock 简介到手） | **入册** r-boringcompany-official |
| tesla.com/blog/all-our-patent-are-belong-you | 403 | 403 | Akamai 拦截页 | 弃收留档（R10 项维持） |
| tesla.com/nacs | 403 | — | Akamai 拦截页 | 弃收留档 |
| tesla.com/impact | 403 | — | Akamai 拦截页 | 弃收留档 |
| tesla.com/ownersmanuals | 403 | — | Akamai 拦截页 | 弃收留档 |
| sae.org/standards/content/j3400_202511/ | **200（构造 URL）** | 200 软页 | JS 壳（无 J3400 内容） | **弃收**：无法确认内容级真实性 |
| connect.sae.org/ | — | 404（猜测路径） | 200（职业培训页，非 J3400 落地） | **弃收**：按「宁缺毋滥」 |

## 判定说明

- **tesla.com 全站三路均拦**：Akamai 边缘拦截（服务端读取器返回的亦为 "Powered and protected by Akamai" 拦截壳），非页面死亡。All Our Patent Are Belong To You 博文等四 URL 重验条件=用户环境实访或代理路径（EXPANSION.md R11 块）。
- **SAE J3400**：WebSearch 确认标准存在（J3400/2_202504 连接器与插座尺寸；J3400/1 适配器安全；SAE 官方公告 2025-05-28），但本机所有读取路径均拿不到 J3400 产品页内容级证据；构造 URL 的 200 不可信（可能为软 200）。宁缺毋滥不入，重验条件在 EXPANSION.md。
- **curl 层原始数据**：liveness-r11.json（本目录）。
