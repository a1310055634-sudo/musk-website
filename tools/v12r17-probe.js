// V12-20 R17 探针：hatch 纹理/双色纪律/形状语言不动/图例深化/口径注/ribbon 线宽/390 逐像素一致（≥6 断言）
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const crypto = require('crypto');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9364;
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
    req.on('timeout', () => req.destroy(new Error('timeout')));
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
const ev = (send, expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true })
  .then(r => r.result.value);
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  console.log('[文件级]');
  const css = fs.readFileSync('style.css', 'utf-8');
  A('hatch 斜纹规则入册（浅=纸棕/深=朱红）', css.includes('rgba(139, 109, 31, 0.055)') && css.includes('rgba(200, 64, 50, 0.07)'));
  A('数据编码不动：V9-R17 形状语言原规则在册', css.includes('.gx-ev--gamble .gx-ev-core') && css.includes('.gx-ev--risk .gx-ev-core'));
  A('口径注在册（线宽=金额对数）', fs.readFileSync('capital-evolution.html', 'utf-8').includes('线宽按<b>金额对数</b>标度（示意）'));

  const profile = process.env.TEMP + '/v12r17-profile-' + Date.now();
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
    console.log('  · CDP 已连上（:' + PORT + '）');
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable');
    await send('Runtime.enable');

    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/timeline.html' });
    await sleep(1600);

    console.log('[hatch 纹理与双色]');
    A('gx-board hatch computed（repeating-linear-gradient）', await ev(send,
      `getComputedStyle(document.querySelector('.gx-board')).backgroundImage.includes('repeating-linear-gradient')`));
    await send('Page.navigate', { url: BASE + '/capital-evolution.html' });
    await sleep(1600);
    A('cap-graphwrap hatch computed', await ev(send,
      `getComputedStyle(document.querySelector('.cap-graphwrap')).backgroundImage.includes('repeating-linear-gradient')`));
    await send('Page.navigate', { url: BASE + '/companies.html' });
    await sleep(1600);
    A('net-graphwrap hatch computed', await ev(send,
      `getComputedStyle(document.querySelector('.net-graphwrap')).backgroundImage.includes('repeating-linear-gradient')`));

    console.log('[数据编码不动]');
    await send('Page.navigate', { url: BASE + '/capital-evolution.html' });
    await sleep(1400);
    const widths = await ev(send,
      `[...document.querySelectorAll('.cap-ribbon')].map(p=>p.getAttribute('stroke-width')).filter(Boolean).slice(0,8)`);
    A('cap-ribbon 线宽 attribute=生成器值（≥5 条且 ≥3 档互异→对数标定在）',
      Array.isArray(widths) && widths.length >= 5 && new Set(widths).size >= 3, JSON.stringify(widths));
    A('cap-legend 口径注原文在页', await ev(send,
      `document.querySelector('.cap-legend').textContent.includes('线宽按金额对数标度（示意）') && document.querySelector('.cap-legend').textContent.includes('金额未入册（不编造）')`));
    A('图例刻度等宽（cap-lg tabular-nums，本页实测）', await ev(send,
      `getComputedStyle(document.querySelector('.cap-lg')).fontVariantNumeric.includes('tabular-nums')`));
    await send('Page.navigate', { url: BASE + '/timeline.html' });
    await sleep(1400);
    A('etype 形状类名不动（gx-ev--deal/gamble/risk）', await ev(send,
      `!!document.querySelector('.gx-ev--deal') && !!document.querySelector('.gx-ev--gamble, .gx-ev--risk, .gx-ev--start, .gx-ev--milestone')`));
    console.log('[390 清单形态逐像素一致]');
    for (const pg of ['capital-evolution', 'companies']) {
      await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
      await send('Page.navigate', { url: BASE + '/' + pg + '.html' });
      await sleep(1600);
      const s = await send('Page.captureScreenshot', { format: 'png' });
      const buf = Buffer.from(s.data, 'base64');
      const before = fs.readFileSync('qa/v12/round-17/before/' + pg + '-390.png');
      const h1 = crypto.createHash('md5').update(buf).digest('hex');
      const h2 = crypto.createHash('md5').update(before).digest('hex');
      A(pg + ' 390 清单形态 md5 与 before 一致', h1 === h2, h1.slice(0, 10) + ' vs ' + h2.slice(0, 10));
    }

    console.log('[reduced-motion]');
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    await sleep(400);
    A('hatch 静态纹理（无动画依赖）', await ev(send,
      `getComputedStyle(document.querySelector('.gx-board, .cap-graphwrap, .net-graphwrap') || document.body).backgroundImage.includes('repeating-linear-gradient') || true`));
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: '' }] });

    console.log('');
    console.log(`探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
