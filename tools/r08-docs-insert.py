# -*- coding: utf-8 -*-
"""V8 R08: CHANGELOG v7.8.0 entry (CRLF prepend) + EXPANSION R08 block (LF prepend)."""
import io

CHANGELOG_ENTRY = """## v7.8.0 — 2026-09-30 · V8 扩充（8/10）：X 帖史扩容 · 十帖入册

**主题包成果（V8 R08 · x-posts.html 13 → 23 张）**
- **十张帖卡入册（逐字全部经 elonmuskarchive.org 镜像详情页直读核验，status ID 经 snowflake 解码对表日期）**：
  **p2020-03-06**「The coronavirus panic is dumb」（CNBC/Reuters 双源）；
  **p2020-05-01**「卖掉几乎所有有形财产」+「Tesla stock price is too high imo」相隔一分钟两连发（互链 i2020-05）；
  **p2022-03-26**「de facto public town square」——收购案公开起点（引用嵌套完整存档，含 3.25 投票原帖）；
  **p2022-04-14**「I made an offer」三个字要约帖（互链 i2022-04-14/d2022-04-25/px-0414）；
  **p2022-05-13**「temporarily on hold」spam 之争引线（互链 d2022-10-27）；
  **p2022-11-01**「lords & peasants…Blue for $8/month」定价宣言；
  **p2022-12-18**「Should I step down…」辞职投票（57.5%/1750 万票，Reuters/BBC/CNBC）；
  **p2023-07-23**「bid adieu to the twitter brand」更名宣言两连发（互链 px-0723）；
  **p2024-04-05**「Tesla Robotaxi unveil on 8/8」一句话预告（互链 e2024-04-23/promises）；
  **p2025-03-28**「@xAI has acquired @X」全股票收购官宣（互链 e2025-03-28）。
- **交叉引用**：platform-x px-0414/px-0723 sv-links 各补帖史直链；多卡互链账本/文档/访谈锚点。
- **检索索引 234 → 244 条**（X 帖 13→23）。
- **甄别记录（宁缺毋滥）**：Hertz 对冲推文（2021-10-26）镜像站无存档且站内记忆措辞存疑，弃收；「I endorse President Trump」（2024-07-13/14）镜像分页未命中原帖，弃收待后续补；web.archive.org 本机 TLS 中断不可用，已删帖核验全部改走 elonmuskarchive.org 镜像（status ID=归档路径，详情页直读=逐字锚）。

**自主优化**
- 工具脚本 tools/r08-snippet.html + tools/r08-integrate.py（10 卡结构断言+时间序分组插入）+ tools/r08-xlinks.py（交叉引用断言）。

**质量门**
- verify.py 9 项全绿；node --check（app.js + cite.js）通过。
"""

EXPANSION_ENTRY = """> **新事实入包（V8 R08 轮 / 2026-09-30 X 帖史镜像直读核验）**：x-posts.html +10 张（13→23）。采料方法：web.archive.org 本机不可用，改用 **elonmuskarchive.org 镜像**（/posts/{statusID} 详情页直读=逐字锚，列表页按年分页 20 帖/页，sort=old 全量回溯；status ID→日期用 snowflake 解码 `(id>>22)+1288834974657` 对表复核）。十条锚点与印证源：
> - **p2020-03-06** status/1236029449042198528（snowflake 2020-03-06 20:42 UTC）：CNBC cnbc.com/2020/03/06/teslas-elon-musk-says-the-coronavirus-panic-is-dumb.html + Reuters idUSKBN20T2WK。
> - **p2020-05-01** status/1256239554148724737（15:10）+ status/1256239815256797184（15:11）两连发：镜像逐字；当日股价大跌与卖房后续媒体广泛报道；五周后 JRE #1470「Mars or a house」自释（站内 i2020-05）。
> - **p2022-03-26** status/1507777261654605828（snowflake 2022-03-26 17:51 UTC——UTC 口径 3.26，美媒 3.25 系 ET 报道口径，条目已注明）：镜像详情页直读验证；3.25 投票帖以引用嵌套完整存档（status/1507596559831101446，snowflake 03-26 05:53 UTC）。
> - **p2022-04-14** status/1514564966564651008（11:23 UTC）「I made an offer」+ 同日 status/1514681422212128770（19:06 UTC）「Will endeavor…」：镜像逐字；要约条款与当日 TED 表态见站内 i2022-04-14 与 d2022-04-25。
> - **p2022-05-13** status/1525049369552048129（09:44 UTC）：镜像逐字；Reuters 当日报道。
> - **p2022-11-01** status/1587498907336118274（snowflake 2022-11-01 21:12 UTC）：镜像详情页直读验证（此前猜测 ID 1587553180897927168 系误记——镜像 404，已纠正）；The Verge 等报道 $8 方案与仿冒风波。
> - **p2022-12-18** status/1604617643973124097（23:20 UTC）：镜像逐字；57.5% 赞成/1750 万票=Reuters（2022-12-19）+BBC（12-20）+CNBC 口径。
> - **p2023-07-23** status/1682964919325724673（04:04 UTC）+ status/1682965462886535168（04:06 UTC）：镜像逐字；更名执行时间线见站内 px-0723。
> - **p2024-04-05** status/1776351450542768368（20:49 UTC）：镜像逐字；R05 已核 Reuters 等当日报道；跳票后续在 e2024-04-23 与 promises 档案。
> - **p2025-03-28** status/1905731750275510312（21:20 UTC）：镜像详情页直读验证（8 处关键词命中）；CNBC/Forbes/AP 多源已在册。
> 甄别记录（宁缺毋滥）：①Hertz 对冲推文（p2021-10-26 候选：「no contract has been signed yet」「zero effect on our economics」——站内 verified-facts 记忆有录）镜像站 r_2021_121/122、u_2021_123/124 四页直读均无此二句，措辞存疑，弃收待补；②「I endorse President Trump and hope he has a rapid recovery」（2024-07-13/14 候选）镜像 v_2024_525-531 七页未命中（分页跨 UTC 或措辞差异），媒体虽广泛报道但无镜像逐字，本轮弃收；③镜像站 2020 年归档仅约 55 页、2025 年约 160 页（远少于 2022 年约 200 页），早期帖覆盖率有限，后续轮次可再回捞。

"""

# --- CHANGELOG (CRLF) ---
s = io.open('CHANGELOG.md', encoding='utf-8', newline='').read()
assert s.count('## v7.7.0') == 1 and '## v7.8.0' not in s, 'changelog state unexpected'
entry = CHANGELOG_ENTRY.replace('\n', '\r\n')
s2 = s.replace('## v7.7.0', entry + '## v7.7.0', 1)
assert s2.count('## v7.8.0') == 1
io.open('CHANGELOG.md', 'w', encoding='utf-8', newline='').write(s2)
print('CHANGELOG.md: v7.8.0 prepended')

# --- EXPANSION (LF) ---
e = io.open('EXPANSION.md', encoding='utf-8', newline='').read()
marker = '> **新事实入包（V8 R07 轮'
assert e.count(marker) == 1 and 'V8 R08 轮' not in e, 'expansion state unexpected'
e2 = e.replace(marker, EXPANSION_ENTRY.rstrip('\n') + '\n\n' + marker, 1)
assert e2.count('V8 R08 轮') == 1
io.open('EXPANSION.md', 'w', encoding='utf-8', newline='').write(e2)
print('EXPANSION.md: R08 block prepended')
