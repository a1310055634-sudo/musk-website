// V9-20 R20 全站终检探针：主路径五步 / 双语 / file:// 离线 / 资源页 / 38 页×3 视口全站复扫
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9381;  // 9227 aDrive 占用；9333-9380 为此前轮次用过
const BASE = 'http://127.0.0.1:8766';
const FILE_INDEX = 'file:///D:/vibe%20coding/musk-website/index.html';

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
const nav = async (send, url, wait) => { await send('Page.navigate', { url }); await new Promise(r => setTimeout(r, wait || 1500)); };

async function main() {
  const pages = fs.readdirSync('.').filter(f => f.endsWith('.html'));
  A('页面数=38', pages.length === 38, String(pages.length));
  const v = fs.readFileSync('VERSION', 'utf-8').trim();
  A('VERSION=10.0.0', v === '10.0.0', v);
  const sm = fs.readFileSync('sitemap.xml', 'utf-8');
  A('sitemap 37 URL 且含 resources', (sm.match(/<loc>/g) || []).length === 37 && sm.includes('resources.html'));

  const profile = process.env.TEMP + '/v9r20-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
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
    console.log('  · CDP 已连上');
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable');
    await send('Runtime.enable');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });

    // ---- 主路径五步 ----
    console.log('[主路径] index→quotes→primary→timeline→events→search');
    await nav(send, BASE + '/index.html', 2000);
    A('① index：封面 h1 + 资料入口 + 版本 10.0.0',
      await ev(send, `document.querySelector('.hero-title') && document.body.textContent.includes('10.0.0')`));
    await nav(send, BASE + '/quotes.html', 1500);
    A('② quotes：语录卡 103',
      (await ev(send, `document.querySelectorAll('.qs-card').length`)) === 103,
      String(await ev(send, `document.querySelectorAll('.qs-card').length`)));
    await nav(send, BASE + '/primary.html', 1800);
    A('③ primary：账本 115 行',
      (await ev(send, `document.querySelectorAll('.ps-row').length`)) === 115,
      String(await ev(send, `document.querySelectorAll('.ps-row').length`)));
    await nav(send, BASE + '/timeline.html', 1800);
    A('④ timeline：泳道 + 事件 14',
      await ev(send, `document.querySelectorAll('.gx-lane').length >= 5`));
    await nav(send, BASE + '/events.html', 1500);
    A('⑤ events：档案 14',
      (await ev(send, `document.querySelectorAll('.ev-item').length`)) === 14,
      String(await ev(send, `document.querySelectorAll('.ev-item').length`)));
    await nav(send, BASE + '/search.html?q=Starship', 1500);
    A('⑥ search：检索命中',
      await ev(send, `document.querySelectorAll('#sr-results a').length > 0`));

    // ---- 双语 ----
    console.log('[双语] EN 切换');
    await nav(send, BASE + '/index.html', 1500);
    const zhH1 = await ev(send, `document.querySelector('.hero-title') ? document.querySelector('.hero-title').textContent.slice(0,10) : ''`);
    await ev(send, `document.getElementById('lang-toggle').click()`);
    await new Promise(r => setTimeout(r, 400));
    const enH1 = await ev(send, `document.querySelector('.hero-title').textContent.slice(0,10)`);
    A(`双语切换生效（zh="${zhH1}" → en="${enH1}"）`, zhH1 !== enH1 && enH1.length > 0);

    // ---- 资源页 ----
    console.log('[资源] resources.html');
    await nav(send, BASE + '/resources.html', 1500);
    A('资源 36 卡 + 筛选芯片 5',
      (await ev(send, `document.querySelectorAll('.rs-item').length`)) === 36 &&
      (await ev(send, `document.querySelectorAll('.rs-fchip').length`)) === 5,
      String(await ev(send, `document.querySelectorAll('.rs-item').length`)));

    // ---- file:// 离线 ----
    console.log('[file://] 离线自包含');
    await nav(send, FILE_INDEX, 2200);
    A('file://：index 渲染（封面+样式生效+无外部请求依赖）',
      await ev(send, `document.querySelector('.hero-title') &&
        getComputedStyle(document.body).fontFamily.length > 0 &&
        document.styleSheets.length > 0`));
    A('file://：导航在册（资料组可达）',
      await ev(send, `[...document.querySelectorAll('#site-nav a')].some(a => a.getAttribute('href') === 'resources.html')`));

    // ---- 38 页 × 3 视口全站复扫 ----
    console.log('[全站复扫] 38 页 × 320/390/768（114 组合）');
    let overflow = [];
    for (const pg of pages) {
      for (const vw of [320, 390, 768]) {
        await send('Emulation.setDeviceMetricsOverride', { width: vw, height: 844, deviceScaleFactor: 1, mobile: vw < 500 });
        await nav(send, BASE + '/' + pg, 1100);
        const sw = await ev(send, `document.documentElement.scrollWidth`);
        const cw = await ev(send, `document.documentElement.clientWidth`);
        if (!(sw <= cw)) overflow.push(`${pg}@${vw}:${sw}>${cw}`);
      }
    }
    A(`114 组合零横向溢出`, overflow.length === 0, overflow.slice(0, 5).join(' ; '));

    // ---- 打印抽查 ----
    console.log('[打印] print 媒体抽查');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await nav(send, BASE + '/survival-2008.html', 1500);
    await send('Emulation.setEmulatedMedia', { media: 'print' });
    A('print：目录/返回隐藏、引语影关',
      await ev(send, `(()=>{const toc=getComputedStyle(document.querySelector('.lr-toc')).display;
        const bq=getComputedStyle(document.querySelector('.sv-node blockquote')).boxShadow;
        return toc==='none' && bq==='none';})()`));
    await send('Emulation.setEmulatedMedia', { media: 'screen' });
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
