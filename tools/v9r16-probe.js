// V9-20 R16 探针 · 首页视觉迭代验收
// 覆盖：三入口结构/特大瓦片几何/封面照与图版角标/FEATURE 行分层/焦点可达/EN 不破版/三视口零溢出/版本
// 纪律：断言基于实测计算值或文件级事实；模板字符串内不用 \d 转义。
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9364;   // 前轮 9361-9363 已用，防残留孤儿实例
const BASE = 'http://127.0.0.1:8766';

let PASS = 0, FAIL = 0;
const FAILED = [];
function A(name, cond, detail) {
  if (cond) { PASS++; console.log('  \u2713 ' + name); }
  else { FAIL++; FAILED.push(name); console.log('  \u2717 ' + name + (detail ? ' \u2014\u2014 ' + detail : '')); }
}
function getJSON(p) {
  return new Promise((res, rej) => {
    const req = http.get({ host: '127.0.0.1', port: PORT, path: p, timeout: 3000 }, r => {
      let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
    });
    req.on('timeout', () => { req.destroy(new Error('timeout')); });
    req.on('error', rej);
  });
}
async function attach(client) {
  let id = 0; const pending = new Map();
  client.addEventListener('message', m => {
    const msg = JSON.parse(m.data);
    if (msg.id && pending.has(msg.id)) {
      const p = pending.get(msg.id); pending.delete(msg.id);
      msg.error ? p.rej(new Error(JSON.stringify(msg.error))) : p.res(msg.result);
    }
  });
  await new Promise(r => client.addEventListener('open', r, { once: true }));
  return (method, params) => new Promise((res, rej) => {
    const mid = ++id; pending.set(mid, { res, rej });
    client.send(JSON.stringify({ id: mid, method, params }));
  });
}

async function main() {
  // ================= 文件级 =================
  console.log('[文件级] R16 结构改动');
  const html = fs.readFileSync('index.html', 'utf-8');
  const css = fs.readFileSync('style.css', 'utf-8');

  A('index.html 特大瓦片 2 处（Tesla / SpaceX）',
    (html.match(/firm-tile--xl/g) || []).length === 2, String((html.match(/firm-tile--xl/g) || []).length));
  A('三入口：act-no / act-arr / act-txt 各 3 处',
    (html.match(/class="act-no"/g) || []).length === 3 &&
    (html.match(/class="act-arr"/g) || []).length === 3 &&
    (html.match(/class="act-txt"/g) || []).length === 3,
    'no=' + (html.match(/class="act-no"/g) || []).length + ' arr=' + (html.match(/class="act-arr"/g) || []).length + ' txt=' + (html.match(/class="act-txt"/g) || []).length);
  A('三入口语言切换安全：data-en 全部落在 .act-txt 叶子上（a.act 自身无 data-en）',
    !/class="act[ "] [^>]*data-en/.test(html) && (html.match(/class="act-txt" data-en=/g) || []).length === 3);
  A('封面照角标 cover-tag 1 处（aria-hidden 装饰）',
    (html.match(/class="cover-tag" aria-hidden="true"/g) || []).length === 1);
  A('图版角标：strip-tag 4 处且均为 <img> 后的 figure 直接子元素',
    (html.match(/<img [^>]*>\s*<span class="strip-tag">/g) || []).length === 4,
    String((html.match(/<img [^>]*>\s*<span class="strip-tag">/g) || []).length));
  A('figcaption 中不再嵌套 strip-tag（说明区纯文字）',
    !/figcaption><span class="strip-tag">/.test(html));

  console.log('[文件级] R16 样式规则');
  A('.firm-tile--xl 跨 2 列 + 大标题 + 宽行距', /firm-tile--xl \{ grid-column: span 2;/.test(css) && /firm-tile--xl h3 \{ font-size: var\(--fs-26\);/.test(css));
  A('.act 入口条规则 + .act-primary 主入口（朱红实底）', /\.act \{/.test(css) && /\.act-primary \{ background: var\(--accent\);/.test(css));
  A('.act:focus-visible 走统一焦点令牌', /\.act:focus-visible \{ outline: var\(--focus-w\) solid var\(--focus-color\);/.test(css));
  A('FEATURE 前三条朱红左标线', /\.feature-row:nth-child\(-n\+3\) \{ border-left: 3px solid var\(--accent\);/.test(css));
  A('.cover-tag 绝对定位角标', /\.cover-tag \{\s*position: absolute;/.test(css));
  A('.strip-tag 绝对定位图版角标（深底浅红字）', /\.hero-strip \.strip-tag \{\s*position: absolute;/.test(css) && /color: var\(--accent-bright\);/.test(css.slice(css.indexOf('.hero-strip .strip-tag'))));
  A('hero-stats 分隔线 2px/55%', /border-top: 2px solid rgba\(243, 240, 232, 0\.55\);/.test(css));
  A('新增微动效的 reduced-motion 全覆盖', /R16 v9\.6\.0：本轮新增微动效/.test(css) && /\.act:hover, \.act:hover \.act-arr, \.hero-strip figure:hover img, \.firm-tile:hover \{ transform: none !important; \}/.test(css));

  console.log('[文件级] 版本与产物');
  const VER = fs.readFileSync('VERSION', 'utf-8').trim();
  A('VERSION = 9.6.0', VER === '9.6.0', VER);
  A('app.js SITE_VERSION = 9.6.0', /SITE_VERSION = '9\.6\.0'/.test(fs.readFileSync('app.js', 'utf-8')));
  const pages = fs.readdirSync('.').filter(f => f.endsWith('.html'));
  const withSpan = pages.filter(f => fs.readFileSync(f, 'utf-8').includes('class="site-version-val">9.6.0<'));
  A('站点版本 span 覆盖 15 页', withSpan.length === 15, String(withSpan.length));

  // ================= 浏览器 =================
  const profile = (process.env.TEMP || '/tmp') + '/v9r16-probe-' + Date.now();
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'], { stdio: 'ignore' });
  let targets;
  for (let i = 0; i < 60; i++) {
    await new Promise(r => setTimeout(r, 500));
    try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
  }
  if (!targets || !targets.length) throw new Error('CDP 无响应');
  const ws = targets.find(t => t.type === 'page');
  const client = new WebSocket(ws.webSocketDebuggerUrl);
  const send = await attach(client);
  const ev = (expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true }).then(r => r.result.value);

  await send('Page.enable');
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });

  const goto = async (page, w, h) => {
    await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: w < 500 });
    await send('Page.navigate', { url: BASE + '/' + page });
    await new Promise(r => setTimeout(r, 1400));
  };
  const setLang = async (lang) => {
    await send('Page.navigate', { url: BASE + '/index.html' });
    await new Promise(r => setTimeout(r, 350));
    await ev(`try{localStorage.setItem('musk-inc-lang','${lang}')}catch(e){}`);
  };

  console.log('[浏览器] 特大瓦片几何（index @1440）');
  await setLang('zh');
  await goto('index.html', 1440, 900);
  const geo = await ev(`(function(){
    var xls = document.querySelectorAll('.firm-tile--xl');
    var std = document.querySelector('.firm-grid a:not(.firm-tile--xl)');
    var xlH3 = xls[0] && xls[0].querySelector('h3');
    var stdH3 = std && std.querySelector('h3');
    var r1 = xls[0] && xls[0].getBoundingClientRect();
    var r2 = xls[1] && xls[1].getBoundingClientRect();
    var rs = std && std.getBoundingClientRect();
    return {
      xlW: xls[0] ? xls[0].offsetWidth : 0, stdW: std ? std.offsetWidth : 0,
      xlH3: xlH3 ? getComputedStyle(xlH3).fontSize : '', stdH3: stdH3 ? getComputedStyle(stdH3).fontSize : '',
      sameRow: (r1 && r2) ? (Math.abs(r1.top - r2.top) < 5) : false,
      xlRight: r1 ? Math.round(r1.right) : 0, xl2Left: r2 ? Math.round(r2.left) : 0
    };
  })()`);
  A('特大瓦片宽 ≈ 标准瓦片 2 倍（实测 ' + geo.xlW + ' vs ' + geo.stdW + '）',
    geo.xlW > geo.stdW * 1.9, JSON.stringify(geo));
  A('特大瓦片标题字号 26px > 标准 20px', geo.xlH3 === '26px' && geo.stdH3 === '20px', geo.xlH3 + ' / ' + geo.stdH3);
  A('Tesla 与 SpaceX 同行并排（上行两大）', geo.sameRow && geo.xlRight <= geo.xl2Left + 1, JSON.stringify({ right: geo.xlRight, left2: geo.xl2Left }));

  console.log('[浏览器] 三入口与封面元素计算样式');
  const actInfo = await ev(`(function(){
    var acts = document.querySelectorAll('.hero-actions .act');
    var prim = document.querySelector('.hero-actions .act-primary');
    var no = document.querySelector('.hero-actions .act .act-no');
    var cover = document.querySelector('.cover-tag');
    var stag = document.querySelector('.hero-strip .strip-tag');
    var stats = document.querySelector('.deal-lines.hero-stats');
    return {
      n: acts.length,
      primBg: prim ? getComputedStyle(prim).backgroundColor : '',
      primColor: prim ? getComputedStyle(prim).color : '',
      noBorder: no ? getComputedStyle(no).borderRightWidth : '',
      coverPos: cover ? getComputedStyle(cover).position : '',
      coverBg: cover ? getComputedStyle(cover).backgroundColor : '',
      stagPos: stag ? getComputedStyle(stag).position : '',
      statsBt: stats ? getComputedStyle(stats).borderTopWidth : ''
    };
  })()`);
  A('三入口按钮 3 枚', actInfo.n === 3, String(actInfo.n));
  A('主入口朱红实底白字（--on-hue #fff）', actInfo.primBg === 'rgb(200, 64, 50)' && actInfo.primColor === 'rgb(255, 255, 255)', JSON.stringify(actInfo));
  A('入口编号右细分隔线存在', actInfo.noBorder !== '0px', actInfo.noBorder);
  A('封面角标绝对定位 + 朱红底', actInfo.coverPos === 'absolute' && actInfo.coverBg === 'rgb(200, 64, 50)', JSON.stringify(actInfo));
  A('图版角标绝对定位（叠于图片左上）', actInfo.stagPos === 'absolute', actInfo.stagPos);
  A('hero-stats 分隔线 2px', actInfo.statsBt === '2px', actInfo.statsBt);

  console.log('[浏览器] FEATURE 行分层（前三条左标线）');
  const rows = await ev(`(function(){
    var rs = document.querySelectorAll('.feature-row');
    var out = [];
    for (var i = 0; i < rs.length; i++) {
      out.push({ bl: getComputedStyle(rs[i]).borderLeftWidth, bc: getComputedStyle(rs[i]).borderLeftColor, tp: getComputedStyle(rs[i]).transitionProperty });
    }
    return out;
  })()`);
  A('feature-row 共 7 条', rows.length === 7, String(rows.length));
  A('前三条 border-left 3px 朱红（FEATURE 级）',
    rows.slice(0, 3).every(r => r.bl === '3px' && r.bc === 'rgb(200, 64, 50)'), JSON.stringify(rows.slice(0, 3)));
  A('后四条无左标线（DEEP DIVE 级）', rows.slice(3).every(r => r.bl === '0px'), JSON.stringify(rows.slice(3).map(r => r.bl)));
  A('行 hover 背景规则存在（文件级：.feature-row:hover background paper-50）',
    /\.feature-row:hover \{ background: var\(--paper-50\); \}/.test(css));

  console.log('[浏览器] EN 语言切换后结构与首屏不破版');
  await setLang('en');
  await goto('index.html', 1440, 900);
  const enInfo = await ev(`(function(){
    var acts = document.querySelectorAll('.hero-actions .act');
    var txts = document.querySelectorAll('.hero-actions .act-txt');
    var t = document.querySelector('.hero-title');
    var kicker = document.querySelector('.hero-kicker');
    return {
      actN: acts.length, txtN: txts.length,
      first: txts[0] ? txts[0].textContent : '',
      htmlLang: document.documentElement.lang,
      titleW: t ? t.scrollWidth : 0, titleC: t ? t.clientWidth : 0,
      kickerTxt: kicker ? kicker.textContent : ''
    };
  })()`);
  A('EN 下三入口结构保持 3 枚（data-en 叶子替换不破坏 span）', enInfo.actN === 3 && enInfo.txtN === 3, JSON.stringify(enInfo));
  A('EN 主入口文案 = Start Reading', enInfo.first === 'Start Reading', enInfo.first);
  A('EN hero 标题不破版（scrollWidth ≤ clientWidth）', enInfo.titleW <= enInfo.titleC, enInfo.titleW + ' > ' + enInfo.titleC);
  const enOver = await ev(`document.documentElement.scrollWidth - document.documentElement.clientWidth`);
  A('EN @1440 零横向溢出', enOver <= 1, String(enOver) + 'px');

  console.log('[浏览器] 三视口零横向溢出（320 / 390 / 768，中英）');
  for (const [tag, w] of [['320', 320], ['390', 390], ['768', 768]]) {
    let bad = [];
    for (const p of ['index.html', 'survival-2008.html', 'timeline.html', 'capital-evolution.html']) {
      await goto(p, w, 900);
      const over = await ev(`document.documentElement.scrollWidth - document.documentElement.clientWidth`);
      if (over > 1) bad.push(p + ':' + over + 'px');
    }
    A(`四页 ${tag}px 零横向溢出（zh）`, bad.length === 0, bad.join(' '));
  }
  await setLang('en');
  for (const [tag, w] of [['320', 320], ['390', 390], ['768', 768]]) {
    await goto('index.html', w, 900);
    const over = await ev(`document.documentElement.scrollWidth - document.documentElement.clientWidth`);
    A(`index ${tag}px 零横向溢出（en）`, over <= 1, String(over) + 'px');
  }

  console.log('[浏览器] 三入口键盘可达与焦点环（真实 Tab；导航下拉经 :focus-within 展开，需穿越约 43 个导航项）');
  await setLang('zh');
  await goto('index.html', 1440, 900);
  let hitAct = null;
  for (let i = 0; i < 60 && !hitAct; i++) {
    await send('Input.dispatchKeyEvent', { type: 'rawKeyDown', windowsVirtualKeyCode: 9, key: 'Tab', code: 'Tab', nativeVirtualKeyCode: 9 });
    await send('Input.dispatchKeyEvent', { type: 'keyUp', windowsVirtualKeyCode: 9, key: 'Tab', code: 'Tab', nativeVirtualKeyCode: 9 });
    await new Promise(r => setTimeout(r, 120));
    const ae = await ev(`(document.activeElement && document.activeElement.className) || ''`);
    if (String(ae).indexOf('act') !== -1) hitAct = await ev(`(function(){
      var a = document.activeElement; var cs = getComputedStyle(a);
      return { cls: a.className, w: cs.outlineWidth, style: cs.outlineStyle, off: cs.outlineOffset, col: cs.outlineColor, href: a.getAttribute('href') };
    })()`);
  }
  A('60 次 Tab 内聚焦命中三入口之一', !!hitAct, hitAct ? hitAct.cls : '未命中');
  A('入口聚焦焦点环 3px solid（--focus-w 统一）',
    !!hitAct && hitAct.w === '3px' && hitAct.style === 'solid', JSON.stringify(hitAct));

  // 探针截图（首屏证据）
  await goto('index.html', 1440, 900);
  const shotZh = await send('Page.captureScreenshot', { format: 'png' });
  fs.mkdirSync('qa/v9-20/round-16/probe', { recursive: true });
  fs.writeFileSync('qa/v9-20/round-16/probe/probe-index-desktop-zh.png', Buffer.from(shotZh.data, 'base64'));
  await setLang('en');
  await goto('index.html', 1440, 900);
  const shotEn = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync('qa/v9-20/round-16/probe/probe-index-desktop-en.png', Buffer.from(shotEn.data, 'base64'));
  A('探针首屏截图落盘（zh + en）',
    fs.existsSync('qa/v9-20/round-16/probe/probe-index-desktop-zh.png') &&
    fs.existsSync('qa/v9-20/round-16/probe/probe-index-desktop-en.png'));

  console.log(`\n结果：${PASS}/${PASS + FAIL} 通过` + (FAIL ? `，失败 ${FAIL}：${FAILED.join(' | ')}` : ''));
  client.close(); chrome.kill();
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e.message); process.exit(1); });
