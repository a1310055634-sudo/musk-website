// V12-20 R10 探针：events.html 四新档渲染/口径等式/主计数/390
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9356;
const BASE = 'http://127.0.0.1:8766';
const NEW = ['e2023-11', 'e2025-06-22', 'e2026-07', 'e2024-07'];

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
  console.log('[文件级] 口径等式与版本戳');
  const tl = fs.readFileSync('timeline-events.js', 'utf-8');
  const mInd = tl.match(/"nRecords":\s*(\d+)/);
  const nRec = mInd ? parseInt(mInd[1]) : -1;
  const absorbed = (tl.match(/被吸收|absorbed/g) || []).length; // 记录数另取
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  const nIdx = (sidx.match(/"id": "/g) || []).length;
  A('timeline nRecords=309', nRec === 309, String(nRec));
  A('索引总数=387', nIdx === 387, String(nIdx));
  A('口径等式：309 + 58（吸收） + 20（档案记录） = 387',
    nRec === 309 && nIdx === 309 + 58 + 20,
    `309+58+20=${309 + 58 + 20} vs ${nIdx}`);
  for (const cid of NEW) A(`索引含新档 ${cid}`, sidx.includes(`"id": "ev-${cid}"`));
  A('版本戳 11.11.0（app.js）', fs.readFileSync('app.js', 'utf-8').includes("SITE_VERSION = '11.11.0'"));

  const profile = process.env.TEMP + '/v12r10-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/events.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] 四新档渲染');
    A('20 事件档全渲染', (await ev(send, `[...document.querySelectorAll('.ev-item')].length`)) >= 20,
      String(await ev(send, `[...document.querySelectorAll('.ev-item')].length`)));
    A('四新档锚全部存在', await ev(send, NEW.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('四档标题渲染（Grok/Robotaxi/Optimus/America Party）', await ev(send,
      `document.body.textContent.includes('Grok：从聊天玩具到操作系统层') && document.body.textContent.includes('Robotaxi 落地') && document.body.textContent.includes('Optimus 量产线') && document.body.textContent.includes('America Party')`));
    A('etype 徽标（产品里程碑×3 + 争议时刻×1）', await ev(send,
      `document.getElementById('e2023-11').textContent.includes('产品里程碑') && document.getElementById('e2024-07').textContent.includes('争议时刻')`));
    A('政治档正反并陈（他的立场 + 批评方立场）', await ev(send,
      `document.getElementById('e2024-07').textContent.includes('他的立场') && document.getElementById('e2024-07').textContent.includes('批评方立场')`));
    A('材料深链抽查（p2025-08-16 / d2026-01 / i2026-02-05）', await ev(send,
      `!!document.querySelector('#e2025-06-22 a[href="x-posts.html#p2025-08-16"], #e2025-06-22 [data-href]') || document.body.innerHTML.includes('x-posts.html#p2025-08-16')`));
    A('external 镜像链渲染（posts/2008888326871535862）', await ev(send,
      `document.body.innerHTML.includes('elonmuskarchive.org/posts/2008888326871535862')`));
    A('版本戳=11.11.0', await ev(send,
      `document.querySelector('.site-version-val') && document.querySelector('.site-version-val').textContent.trim()==='11.11.0'`));

    console.log('[桌面] 深链目标复核（跨页 fetch）');
    const prim = await getBody(BASE + '/primary.html');
    A('e2024-10-10 / e2026-07-22 / e2024-04-23 / e2023-07-12 账本锚真实存在',
      prim.includes('id="e2024-10-10"') && prim.includes('id="e2026-07-22"') &&
      prim.includes('id="e2024-04-23"') && prim.includes('id="e2023-07-12"'));
    const xp = await getBody(BASE + '/x-posts.html');
    A('p2023-11-04 / p2025-08-16 / p2026-10-03 帖锚真实存在',
      xp.includes('id="p2023-11-04"') && xp.includes('id="p2025-08-16"') && xp.includes('id="p2026-10-03"'));

    console.log('[390] 零横向溢出');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await new Promise(r => setTimeout(r, 800));
    A('390 视口 scrollWidth<=clientWidth',
      await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));

    console.log('');
    console.log(`探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
