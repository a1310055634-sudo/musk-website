# R07 验收记录 — 公司关系总览（v6.12.0）

## 本轮要解决的问题

在公司版图（首页 #map 六瓦 + companies.html 六卡）基础上制作可探索的关系视图：
点击公司看业务定位、相关事件与资料；关系线标明类型与日期；区分已证实关系与
编者关联；控制初始信息量并提供列表替代。同时落地 R4/R6 遗留的全站公司色标体系
（原计划 R7/R8 承接，本轮 R7 完成）。

## 实际完成的改动

- **tools/companies-data.py**（新）：关系数据单一事实来源——11 节点（运营者 + 10 公司）
  × 13 条关系边；每条边带 type/date/precision/双语标签/图上短标签/evidence 分级
  （verified=站内在册证实 12 条 · editorial=编者关联 1 条）/站内来源锚点+说明；
  自带结构自检（重复 ID/端点存在/双语完整/枚举合法/editorial 也必须有在册出处/
  verified 必须带日期/musk 只能作起点），不过拒生成；
  `events_for_company()` 与 events-data.py 交叉引用（别名映射处理「X（原 Twitter）」口径）。
- **tools/build-network.py**（新）：生成器——companies.html 注入/替换
  `<!-- V7-R7-NETWORK:BEGIN/END -->` 区块（section#network：SVG 静态关系图 +
  图例 + 交互详情面板 + 三组文字清单）；自动补挂 companies-data.js；
  同时产出 companies-data.js（window.COMPANIES_V7，file:// 下 script 标签加载，
  供 R8 公司档案 / R9 时间轴 / R10 资本流向复用）；幂等。
- **SVG 关系图**：全静态绘制（无 JS 完整可读）——中心墨色圆（Elon Musk）+ 10 公司
  色标顶条节点卡 + 13 条着色关系线（创立/入主/创意发起=实线，收购=实线+方向箭头，
  编者关联=虚线）；13 个图上短标签手工避让位；线端按节点边界收缩不穿节点。
- **交互（app.js）**：点击/Enter/Space 打开详情面板（业务定位/状态/相关事件深链
  events.html#e*/关系清单含来源链接与证据标注）；再点同节点或 Esc 关闭且焦点归位；
  数据按 documentElement.lang 取双语字段，MutationObserver 监听语言切换重渲染打开态。
- **公司色标体系（:root --co-*，全站唯一出处）**：musk 墨/tesla 红/spacex 藏蓝/x 石墨/
  xai 紫/neuralink 玫紫/boring 暗金/solarcity 绿/paypal 蓝/history 灰褐；
  接入三处——关系图节点顶条与边线、首页六瓦顶条（hover 亦保持公司色）、
  events.html 公司 chip 顶条（build-events.py 渲染时附 ev-chip--{co} 类）。
  色标只作辅助：节点/chip/清单一律以公司名称文字为准（不只靠颜色）。
- **首页接入**：#map 区头新增 .section-more 入口行「查看关系总览——谁创立了什么、
  谁买了谁，逐条带来源 →」（companies.html#network）。
- **清单（列表替代）**：三组——创立·入主·发起（9）/ 收购与合并（3）/ 编者关联（1）；
  每行含色点、双语标签、证据徽标（已证实=绿字实线框 / 编者关联=琥珀字虚线框，
  文字+边型双编码）、来源锚链接；≤760px 隐藏 SVG 与交互面板，清单成为主形态
  （桌面同址可见，非手机专属降级）；打印隐藏交互面板。
- **同步**：VERSION / app.js SITE_VERSION / 13 页静态 span → 6.12.0；EPUB 重建。

## 事实纪律

- 13 条关系全部取自站内在册口径（账本 primary.html、companies.html、profile.html、
  grok.html、money.html、events-data.py），本轮零新增外部事实。
- 关键甄别：2002 SpaceX 创立**故事细节**未入册（见甄别记录）——数据只使用
  「2002 年创立」全站通识口径并在来源说明中显式标注「创立故事细节未入册」；
  SolarCity 用账本 e2006 口径「表兄弟按他的创意创立，他出任董事长」（创意发起，
  不写「共同创立」）；xAI 收购 X 引账本 e2025-03-28（本人推文 permalink 在册）；
  OpenAI—xAI「对手」标 editorial，注明非任何一方官方表述。
- 金额沿用站内口径：440 亿（2022 交割）/ 约 26 亿（2016 收购）/ xAI 800 亿·X 330 亿
  （2025 全股票），不混用估值与收入。
- xai 详情面板无相关事件深链：R6 事件档案为六个代表性事件（未含 e2025-03-28），
  本轮不为此扩口径；该关系证据锚点直接指向账本条目。

## 检查了哪些页面和交互

tools/verify.py 9 项、node --check app.js、CDP 真视口探针（r07-probe.js，
仓库外 D:/vibe coding/v7r7-work/）43 断言 + 6 张补拍截图：

- **A 结构（14）**：#network 存在；SVG 11 节点/13 边/13 短标签；图例 4 项；
  清单三组 13 行；证据徽标 12 实+1 编者；companies-data.js 挂载且
  window.COMPANIES_V7=11 公司 13 关系；musk 中心圆；节点全部 tabindex=0；
  详情空态文案可见（无 JS 也有内容）；SVG role=group。
- **B 交互（5）**：点 Tesla 开详情（blurb+4 个事件深链+2 条关系+节点高亮）；
  再点同节点关闭；点 xAI 详情含「编者关联」标注（3 条关系）。
- **C 键盘（2）**：Enter 打开 SpaceX；Esc 关闭且焦点保留在节点。
- **D 双语（6）**：EN 标题/图例/边短标签（All-stock 2025）/导语/清单组题全量切换；
  打开态详情面板随语言切换重渲染为英文（RELATIONSHIPS (3)）。
- **E 首页（2）**：入口行 href=companies.html#network；六瓦顶条 6 色互异。
- **F events 回归（2）**：chip 全部带色标类；版本 6.12.0。
- **G 无 JS（3）**：SVG 11 节点在；清单 13 行完整；空态提示可见。
- **H 390 真视口（4）**：SVG 隐藏；清单 13 行为主形态；详情面板隐藏；零横向溢出。
- **I file://（4）**：SVG 渲染；数据加载；--co-tesla=#C8102E 变量生效；
  PayPal 详情交互可用。
- **J 版本（1）**：companies 页脚 6.12.0。

## 测试结果及发现的问题

- 首轮探针 41/43：抓到两个真 bug——详情面板 `evidenceLabel`/`statusLabel` 为双语
  对象被直接字符串化成 [object Object] → 改为按语言取字段（netT）；复测 43/43。
- D6 首轮失败为探针场景设计错误（C 组 Esc 已关闭面板），debug 复现证明
  MutationObserver 重渲染正常 → 修正探针场景后通过。
- 截图伪影两处（非站点缺陷）：CSS scroll-behavior:smooth 使 scrollIntoView 截图
  停在页顶 → 补拍用 scrollTo({behavior:'instant'})（R6 同类经验）；懒加载图在
  视口外不取图 → 补拍脚本 eager 化。

## 视觉复核（人工）

- companies-network-desktop.png / -bottom.png：11 节点 13 边全渲染，三组短标签
  避让无重叠，公司色顶条与边线着色正确，收购箭头方向正确（Tesla→SolarCity、
  xAI→X），OpenAI—xAI 虚线，图例四项完整。
- companies-network-detail-tesla.png：Tesla 选中红框高亮 + 详情面板。
- companies-network-en.png：EN 全量（标题/导语/边标签/导航/报头）不破版。
- companies-network-390.png：清单形态排版正常、徽标与来源链接完整、零溢出。
- index-map.png：入口行 + 六瓦色标与关系图一致。
- events-chips.png：四色 chip 顶条生效，事件页无回归。
- companies-network-file.png：file:// 与 http 渲染一致。

## 是否完成本轮

完成。R7 验收通过：关系图有实际可读的信息（11×13 全标注）；每条事实关系有来源
支持（12 条 verified 逐条带站内锚点）；键盘和手机能完成主要操作（Tab/Enter/Esc
+ 390 清单形态）；图形、文字和公司色标一致（--co-* 三处接入）。

## 下一次

R8 公司档案体系（v6.13.0）：可复用公司档案模板，优先覆盖 Tesla、SpaceX、X、xAI；
汇总业务介绍、里程碑、财务口径、风险、来源与相关文章；消费 companies-data.js 与
EVENTS_V7；其余公司给清楚简介和资料入口；历史与现状表述带截止日期。
