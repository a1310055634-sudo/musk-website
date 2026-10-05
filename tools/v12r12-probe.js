// V12-20 R12 探针：deep-dive-07 新页渲染/三段体/互链/导航高亮/390 + 索引计数
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9358;
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
  A('索引深读长文=10（dd06+dd07）', (sidx.match(/"t": "深读长文"/g) || []).length === 10,
    String((sidx.match(/"t": "深读长文"/g) || []).length));
  A('索引总数=408', (sidx.match(/"id": "/g) || []).length === 408, String((sidx.match(/"id": "/g) || []).length));
  A('索引含 dd07 五章锚', ['s1','s2','s3','s4','s5'].every(x => sidx.includes(`"id": "deep-dive-07-${x}"`)));
  A('site-nav 注册 dd07', fs.readFileSync('tools/site-nav.py', 'utf-8').includes('deep-dive-07.html'));

  const profile = process.env.TEMP + '/v12r12-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/deep-dive-07.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[新页渲染]');
    A('标题=Robotaxi 落地考', await ev(send, `document.querySelector('h1').textContent.includes('Robotaxi 落地考')`));
    A('五章全渲染', (await ev(send, `document.querySelectorAll('section.lr-sec').length`)) === 5);
    A('三段体（指控/回应/本站核查）', await ev(send,
      `document.body.textContent.includes('指控') && document.body.textContent.includes('回应') && document.body.textContent.includes('本站核查')`));
    A('Cybercab 逐字引语在页', await ev(send,
      `document.body.textContent.includes('specifically built for unsupervised full self driving')`));
    A('无监督员帖逐字在页', await ev(send,
      `document.body.textContent.includes('no safety monitor in the car')`));
    A('双语', await ev(send,
      `document.querySelectorAll('[data-en]').length > 20 && /[\\u4e00-\\u9fff]/.test(document.body.textContent)`));
    A('版本戳=11.13.0', await ev(send,
      `document.querySelector('.site-version-val').textContent.trim()==='11.13.0'`));
    A('导航 aria-current 高亮', await ev(send,
      `[...document.querySelectorAll('a[href="deep-dive-07.html"]')].some(a=>a.getAttribute('aria-current')==='page')`));
    A('互链在 DOM（≥3 类）', await ev(send,
      `['primary.html#e2024-10-10','x-posts.html#p2026-01-22','events.html#e2025-06-22','promises.html#promises-s3'].filter(h=>!!document.querySelector('a[href="'+h+'"]')).length >= 3`));

    console.log('[互链跨页 fetch]');
    const prim = await getBody(BASE + '/primary.html');
    A('primary 锚 e2024-10-10 / e2026-07-22 存在',
      prim.includes('id="e2024-10-10"') && prim.includes('id="e2026-07-22"'));
    const xp = await getBody(BASE + '/x-posts.html');
    A('x-posts 锚 p2026-01-22 / p2025-08-16 / p2026-10-03 存在',
      xp.includes('id="p2026-01-22"') && xp.includes('id="p2025-08-16"') && xp.includes('id="p2026-10-03"'));
    const evs = await getBody(BASE + '/events.html');
    A('events 锚 e2025-06-22 存在', evs.includes('id="e2025-06-22"'));
    const prom = await getBody(BASE + '/promises.html');
    A('promises 锚 promises-s3 存在', prom.includes('id="promises-s3"'));

    console.log('[390] 零横向溢出');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await new Promise(r => setTimeout(r, 800));
    A('390 scrollWidth<=clientWidth',
      await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));

    console.log('');
    console.log(`探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
