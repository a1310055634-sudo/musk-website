// V9-20 R17 探针：三图工业风精修——形状语言/刻度/等宽标注/图例统一/点阵网格 + 数据编码不动 + 三视口零溢出 + 390 清单形态
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9365;  // 9227 aDrive 占用；9333-9364 为此前轮次用过
const BASE = 'http://127.0.0.1:8766';

let PASS = 0, FAIL = 0;
function A(name, cond, detail) {
  if (cond) { PASS++; console.log('  ✓ ' + name); }
  else { FAIL++; console.log('  ✗ ' + name + (detail ? ' —— ' + detail : '')); }
}

function getJSON(path) {
  return new Promise((res, rej) => {
    const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => {
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
  const send = (method, params) => new Promise((res, rej) => {
    const mid = ++id; pending.set(mid, { res, rej });
    client.send(JSON.stringify({ id: mid, method, params }));
  });
  return send;
}
const ev = (send, expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true })
  .then(r => r.result.value);

async function main() {
  let capLegendFont = '';
  // ---------- 文件级 ----------
  console.log('[文件级] R17 段与数据编码保全');
  const css = fs.readFileSync('style.css', 'utf-8');
  const seg = css.slice(css.indexOf('V9-R17 数据图形工业风'));
  A('--font-num 令牌入字体层', css.includes('--font-num: "Cascadia Mono", Consolas'));
  A('R17 段无新增 transition/animation 声明（reduced-motion 免复核前提）',
    !/transition\s*:/.test(seg) && !/animation\s*:/.test(seg),
    '段内出现 transition:/animation: 声明');
  A('数据编码保全：R17 段不触碰 ribbon/edge 线宽与色',
    !/\.cap-ribbon|\.net-edge|marker/.test(seg.slice(0, seg.indexOf('打印'))));
  const cap = fs.readFileSync('capital-evolution.html', 'utf-8');
  A('「示意」口径注原文保留（capital-evolution）',
    cap.includes('示意）——精确数字一律以标注与详情为准'));
  A('reduce 块仍在（既有 gx 过渡豁免）',
    css.includes('@media (prefers-reduced-motion: reduce)') && css.includes('.gx-fchip, a.gx-dot, button.gx-ev { transition: none; }'));

  // ---------- 浏览器 ----------
  const profile = process.env.TEMP + '/v9r17-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'], { stdio: 'ignore' });
  try {
    let targets;
    for (let i = 0; i < 60; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
    }
    if (!targets || !targets.length) throw new Error('CDP /json 60 次无响应');
    console.log('  · CDP 已连上，targets=' + targets.length);
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable');
    await send('Runtime.enable');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });

    // ---- timeline gx-* ----
    await send('Page.navigate', { url: BASE + '/timeline.html' });
    await new Promise(r => setTimeout(r, 2200));
    console.log('[gx] timeline.html（桌面 1440）');
    A('泳道在册（结构未动）', (await ev(send, `document.querySelectorAll('.gx-lane').length`)) >= 5,
      String(await ev(send, `document.querySelectorAll('.gx-lane').length`)));
    A('年轴等宽字体（--font-num 生效）',
      await ev(send, `getComputedStyle(document.querySelector('.gx-axis span')).fontFamily.includes('Consolas')`));
    A('年轴刻度线（::after 6px）',
      await ev(send, `getComputedStyle(document.querySelector('.gx-axis span'),'::after').height === '6px'`),
      String(await ev(send, `getComputedStyle(document.querySelector('.gx-axis span'),'::after').height`)));
    A('形状语言·deal=方（border-radius 1.5px）',
      await ev(send, `getComputedStyle(document.querySelector('.gx-ev--deal .gx-ev-core')).borderRadius === '1.5px'`));
    A('形状语言·gamble=菱（45° 旋转）',
      await ev(send, `getComputedStyle(document.querySelector('.gx-ev--gamble .gx-ev-core')).transform.includes('0.707')`));
    A('形状语言·risk=三角（clip-path polygon）',
      await ev(send, `getComputedStyle(document.querySelector('.gx-ev--risk .gx-ev-core')).clipPath.includes('polygon')`));
    A('类型芯片形状图例（::before 补色点：deal 方 / gamble 菱 / risk 三角 / 色为 etype 令牌）',
      await ev(send, `(()=>{const g=(sel,pseudo)=>getComputedStyle(document.querySelector(sel), pseudo);
        const d=g('.gx-tchip--deal','::before'), gm=g('.gx-tchip--gamble','::before'), r=g('.gx-tchip--risk','::before');
        return d.content !== 'none' && d.borderRadius === '1.5px' &&
               gm.transform.includes('0.707') && r.clipPath.includes('polygon') &&
               d.backgroundColor !== 'rgba(0, 0, 0, 0)';})()`));
    A('色标未动：gamble 核心仍为朱红系（形状不换色）',
      await ev(send, `(()=>{const c=getComputedStyle(document.querySelector('.gx-ev--gamble .gx-ev-core')).backgroundColor;
        return c === 'rgb(200, 64, 50)';})()`));

    // ---- capital cap-* ----
    await send('Page.navigate', { url: BASE + '/capital-evolution.html' });
    await new Promise(r => setTimeout(r, 2200));
    console.log('[cap] capital-evolution.html（桌面 1440）');
    A('18 条流向线全在（数据编码不动）',
      (await ev(send, `document.querySelectorAll('.cap-flow').length`)) === 18,
      String(await ev(send, `document.querySelectorAll('.cap-flow').length`)));
    A('首条 ribbon 线宽 = 生成器属性值（CSS 未覆盖数据编码）',
      await ev(send, `(()=>{const r=document.querySelector('.cap-ribbon');
        return Math.abs(parseFloat(getComputedStyle(r).strokeWidth) - parseFloat(r.getAttribute('stroke-width'))) < 0.01;})()`));
    A('图底点阵网格（radial-gradient 生效）',
      await ev(send, `getComputedStyle(document.querySelector('.cap-graph')).backgroundImage.includes('radial-gradient')`));
    A('标注层改技术字体 + 数字等宽（sans + tabular-nums）',
      await ev(send, `(()=>{const s=getComputedStyle(document.querySelector('.cap-elabel'));
        return s.fontFamily.includes('Segoe UI') && s.fontVariantNumeric.includes('tabular-nums');})()`));
    capLegendFont = await ev(send, `getComputedStyle(document.querySelector('.cap-legend')).fontSize`);

    // ---- companies net-* ----
    await send('Page.navigate', { url: BASE + '/companies.html' });
    await new Promise(r => setTimeout(r, 2200));
    console.log('[net] companies.html（桌面 1440）');
    A('节点在册（结构未动）', (await ev(send, `document.querySelectorAll('.net-node').length`)) >= 7,
      String(await ev(send, `document.querySelectorAll('.net-node').length`)));
    A('图底点阵网格（与 cap 同规格）',
      await ev(send, `getComputedStyle(document.querySelector('.net-graph')).backgroundImage.includes('radial-gradient')`));
    A('标注层数字等宽（tabular-nums）',
      await ev(send, `getComputedStyle(document.querySelector('.net-elabel')).fontVariantNumeric.includes('tabular-nums')`));
    A('图例虚线同构造（repeating-linear-gradient）',
      await ev(send, `getComputedStyle(document.querySelector('.net-lg-dash')).backgroundImage.includes('repeating-linear-gradient')`));
    A('图例统一：cap 与 net 同字号（跨页取值比较，均 --fs-small-2）',
      (await ev(send, `getComputedStyle(document.querySelector('.net-legend')).fontSize`)) === capLegendFont &&
      capLegendFont !== '', 'cap=' + capLegendFont);

    // ---- 三视口零溢出（美术轮纪律 C：320/390/768） ----
    console.log('[溢出] 三页 × 三视口复扫');
    for (const pg of ['timeline.html', 'capital-evolution.html', 'companies.html']) {
      for (const vw of [320, 390, 768]) {
        await send('Emulation.setDeviceMetricsOverride', { width: vw, height: 844, deviceScaleFactor: 1, mobile: vw < 500 });
        await send('Page.navigate', { url: BASE + '/' + pg });
        await new Promise(r => setTimeout(r, 1600));
        const sw = await ev(send, `document.documentElement.scrollWidth`);
        const cw = await ev(send, `document.documentElement.clientWidth`);
        A(`[${pg} @${vw}] 零横向溢出（${sw} ≤ ${cw}）`, sw <= cw, sw + '>' + cw);
      }
    }

    // ---- 390 清单形态（timeline 视图切换） ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/timeline.html' });
    await new Promise(r => setTimeout(r, 2000));
    console.log('[390 清单形态] timeline.html');
    await ev(send, `document.getElementById('gx-view-list').click()`);
    A('点「清单」：mode-list 生效，泳道图隐藏、清单可见',
      await ev(send, `(()=>{const sec=document.querySelector('.gx-sec');
        const boardHidden=getComputedStyle(sec.querySelector('.gx-wrap')).display==='none';
        const listShown=getComputedStyle(sec.querySelector('ol.gx-list')).display!=='none';
        return sec.classList.contains('mode-list') && boardHidden && listShown;})()`));
    const sw2 = await ev(send, `document.documentElement.scrollWidth`);
    const cw2 = await ev(send, `document.documentElement.clientWidth`);
    A(`[390 清单态] 零横向溢出（${sw2} ≤ ${cw2}）`, sw2 <= cw2, sw2 + '>' + cw2);
    await ev(send, `document.getElementById('gx-view-board').click()`);
    A('切回泳道：mode-list 移除（回归正常）',
      await ev(send, `!document.querySelector('.gx-sec').classList.contains('mode-list')`));
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
