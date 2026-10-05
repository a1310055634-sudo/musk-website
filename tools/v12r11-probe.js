// V12-20 R11 探针：deep-dive-06 新页渲染/双语/导航高亮/互链/390 + chronicle 计数
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9357;
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
function getBody(url) {
  return new Promise((res, rej) => {
    http.get(url, r => { let d = ''; r.on('data', c => d += c); r.on('end', () => res(d)); }).on('error', rej);
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

async function main() {
  console.log('[文件级]');
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  A('索引编年史=64', (sidx.match(/"t": "编年史"/g) || []).length === 64, String((sidx.match(/"t": "编年史"/g) || []).length));
  A('索引深读长文=5（dd06 五章）', (sidx.match(/"t": "深读长文"/g) || []).length === 5);
  A('索引总数=403', (sidx.match(/"id": "/g) || []).length === 403, String((sidx.match(/"id": "/g) || []).length));
  const chron = fs.readFileSync('chronicle.html', 'utf-8');
  A('chronicle cy-year=64', (chron.match(/class="cy-year"/g) || []).length === 64);
  A('新页版本 span 存在', fs.readFileSync('deep-dive-06.html', 'utf-8').includes('site-version-val'));

  const profile = process.env.TEMP + '/v12r11-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/deep-dive-06.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[新页渲染]');
    A('标题=xAI 三年志', await ev(send, `document.querySelector('h1') && document.querySelector('h1').textContent.includes('xAI 三年志')`));
    A('五个 section 全渲染', (await ev(send, `document.querySelectorAll('section.lr-sec').length`)) === 5,
      String(await ev(send, `document.querySelectorAll('section.lr-sec').length`)));
    A('双语（data-en 英文 + 中文正文并存）', await ev(send,
      `document.querySelectorAll('[data-en]').length > 20 && /[\\u4e00-\\u9fff]/.test(document.body.textContent)`));
    A('TOC 五项 + 锚点可达', await ev(send,
      `document.querySelectorAll('.lr-toc a').length === 5 && !!document.getElementById('deep-dive-06-s5')`));
    A('版本戳=11.12.0', await ev(send,
      `document.querySelector('.site-version-val').textContent.trim()==='11.12.0'`));
    A('导航项含 deep-dive-06 且 aria-current 高亮', await ev(send,
      `[...document.querySelectorAll('a[href="deep-dive-06.html"]')].some(a=>a.getAttribute('aria-current')==='page')`));
    A('互链在 DOM（primary/x-posts/documents/events ≥3 类）', await ev(send,
      `['primary.html#e2023-07-12','x-posts.html#p2023-11-04','documents.html#d2026-01','events.html#e2023-11','x-posts.html#p2026-09-14'].filter(h=>!!document.querySelector('a[href="'+h+'"]')).length >= 3`));

    console.log('[互链跨页 fetch 验证]');
    const prim = await getBody(BASE + '/primary.html');
    A('primary 锚 e2023-07-12 / e2025-03-28 / e2026-02-10 存在',
      prim.includes('id="e2023-07-12"') && prim.includes('id="e2025-03-28"') && prim.includes('id="e2026-02-10"'));
    const xp = await getBody(BASE + '/x-posts.html');
    A('x-posts 锚 p2023-11-04 / p2026-09-14 存在', xp.includes('id="p2023-11-04"') && xp.includes('id="p2026-09-14"'));
    const docs = await getBody(BASE + '/documents.html');
    A('documents 锚 d2026-01 存在', docs.includes('id="d2026-01"'));
    const evs = await getBody(BASE + '/events.html');
    A('events 锚 e2023-11 存在', evs.includes('id="e2023-11"'));

    console.log('[chronicle 页]');
    await send('Page.navigate', { url: BASE + '/chronicle.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('cy-ev 渲染=64', (await ev(send, `document.querySelectorAll('.cy-ev').length`)) === 64,
      String(await ev(send, `document.querySelectorAll('.cy-ev').length`)));
    A('新条目渲染（c2026-06-12 SpaceX IPO / c2025-06-22 Robotaxi）', await ev(send,
      `!!document.getElementById('c2026-06-12') && !!document.getElementById('c2025-06-22')`));

    console.log('[390] 零横向溢出（新页+chronicle）');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await new Promise(r => setTimeout(r, 800));
    A('390 chronicle scrollWidth<=clientWidth',
      await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));
    await send('Page.navigate', { url: BASE + '/deep-dive-06.html' });
    await new Promise(r => setTimeout(r, 1200));
    A('390 deep-dive-06 scrollWidth<=clientWidth',
      await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));

    console.log('');
    console.log(`探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
