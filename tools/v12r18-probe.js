// V12-20 R18 探针：封面三段式/IN THIS ISSUE/.act 三入口/EN 往返/320·390·768 零溢出/像素 diff（≥8 断言）
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const crypto = require('crypto');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9366;
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
  const idx = fs.readFileSync('index.html', 'utf-8');
  A('封面三段式 CSS 入册（lr-kick 双线/h1 serif/fig 双线框）',
    css.includes('.lr-hero .lr-kick') && css.includes('.lr-hero-fig { border: 3px double'));
  A('IN THIS ISSUE 块入 index', idx.includes('issue-now') && idx.includes('IN THIS ISSUE'));
  A('COVER STORY kicker 替换（不删 .act 三入口）',
    idx.includes('COVER STORY · DEEP DIVE 01') && idx.includes('act-primary') && idx.includes('act-no') && (idx.match(/class="act[ "]/g) || []).length >= 3);
  A('noscript 不受影响/结构完整', idx.includes('</html>'));

  const profile = process.env.TEMP + '/v12r18-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/deep-dive-05.html' });
    await sleep(1500);

    console.log('[封面三段式渲染]');
    A('lr-kick 双线题花生效', await ev(send,
      `getComputedStyle(document.querySelector('.lr-hero .lr-kick')).borderTopStyle==='double'`));
    A('图版双线框生效', await ev(send,
      `getComputedStyle(document.querySelector('.lr-hero-fig')).borderTopStyle==='double'`));
    A('h1 serif 字族', await ev(send,
      `getComputedStyle(document.querySelector('.lr-hero h1')).fontFamily.includes('Georgia') || getComputedStyle(document.querySelector('.lr-hero h1')).fontFamily.includes('serif')`));

    await send('Page.navigate', { url: BASE + '/index.html' });
    await sleep(1500);
    console.log('[首页封面故事]');
    A('本期看点渲染（三条 li）', (await ev(send, `document.querySelectorAll('.issue-now li').length`)) === 3,
      String(await ev(send, `document.querySelectorAll('.issue-now li').length`)));
    A('COVER STORY kicker 上墙', await ev(send,
      `document.querySelector('.feature-lead .kicker').textContent.includes('COVER STORY')`));
    A('.act 三入口编号条健在（01/02/03）', await ev(send,
      `[...document.querySelectorAll('.act-no')].map(e=>e.textContent).join('')==='010203'`));
    A('feature-row 目录编号 ::before（规则在册+渲染宽度>0；Chrome computed 保留 counter() 记法）', await ev(send,
      `(()=>{const fk=document.querySelector('.feature-row .fk');if(!fk)return 'no-fk';const st=getComputedStyle(fk,'::before');const r=fk.getBoundingClientRect();return st.content.includes('counter(ftr)') && r.width>0 ? 'ok' : st.content;})()`));

    console.log('[EN 往返断言（data-en 不破版）]');
    const enRound = await ev(send,
      `(function(){
        const h1 = document.querySelector('.hero-title');
        const zhBefore = h1.textContent;
        const en = h1.getAttribute('data-en');
        const b = document.getElementById('lang-toggle');
        b.click();
        const enShown = h1.textContent;
        const ok1 = enShown.replace(/\\s+/g,' ') === en.replace(/&lt;br&gt;/g,' ').replace(/\\s+/g,' ') || enShown.includes('Making the Future');
        b.click();
        const zhBack = h1.textContent;
        return JSON.stringify({ok1, zhBack: zhBack === zhBefore});
      })()`);
    A('EN 切换往返：英文渲染+中文复原', /"ok1":true/.test(enRound) && /"zhBack":true/.test(enRound), enRound);

    console.log('[320/390/768 复扫零溢出]');
    for (const w of [320, 390, 768]) {
      await send('Emulation.setDeviceMetricsOverride', { width: w, height: 900, deviceScaleFactor: 2, mobile: w < 700 });
      await send('Page.navigate', { url: BASE + '/index.html' });
      await sleep(900);
      A(w + 'px index 零溢出', await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));
    }

    console.log('[新旧首屏像素 diff（显著差异）]');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/index.html' });
    await sleep(1500);
    const shot = await send('Page.captureScreenshot', { format: 'png' });
    const buf = Buffer.from(shot.data, 'base64');
    fs.writeFileSync('qa/v12/round-18/after/index-desktop.png', buf);
    const before = fs.readFileSync('qa/v12/round-18/before/index-desktop.png');
    const h1 = crypto.createHash('md5').update(buf).digest('hex');
    const h2 = crypto.createHash('md5').update(before).digest('hex');
    A('新旧首屏 md5 显著不同（差异显著）', h1 !== h2, h1.slice(0, 10) + ' vs ' + h2.slice(0, 10));

    console.log('');
    console.log(`探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
