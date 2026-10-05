// V12-20 R02 探针：六张断代卡 渲染/时序/年份组2026/互链/双语/390 + 检索命中
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9345;  // 9227 被 aDrive.exe 占用；9333-9341 历史轮用过，本轮 9345
const BASE = 'http://127.0.0.1:8766';
const NEW = ['p2025-08-16', 'p2025-10-29', 'p2026-01-22', 'p2026-07-01', 'p2026-09-14', 'p2026-10-03'];

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
  console.log('[文件级] search-index.js');
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  for (const cid of NEW) A(`索引含新帖 ${cid}`, sidx.includes(`"id": "${cid}"`));
  A('索引 X 帖计数=40', (sidx.match(/"t": "X 帖"/g) || []).length === 40,
    String((sidx.match(/"t": "X 帖"/g) || []).length));
  A('三逐字句入索引（kittens / no safety monitor / 2.5T C++）',
    sidx.includes('grey kittens on grey tarmac') &&
    sidx.includes('no safety monitor in the car') &&
    sidx.includes('2.5T model trained with our new C++ software stack'));

  const profile = process.env.TEMP + '/v12r02-profile-' + Date.now();
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'],
    { stdio: 'ignore' });
  try {
    let targets;
    for (let i = 0; i < 60; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
    }
    if (!targets || !targets.length) throw new Error('CDP /json 60 次无响应');
    console.log('  · CDP 已连上（:' + PORT + '），targets=' + targets.length);
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable');
    await send('Runtime.enable');

    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/x-posts.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] 结构与渲染');
    A('卡总数=40', (await ev(send, `document.querySelectorAll('.tweet-card').length`)) === 40);
    A('六张新卡全部渲染', await ev(send, NEW.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('全卡时序升序（含 2026）',
      await ev(send, `(() => { const ids=[...document.querySelectorAll('.tweet-card')].map(e=>e.id);
        const k=s=>s.slice(1).split('-').map(Number); for(let i=1;i<ids.length;i++){const a=k(ids[i-1]),b=k(ids[i]);
        if(a[0]>b[0]||(a[0]==b[0]&&(a[1]>b[1]||(a[1]==b[1]&&a[2]>b[2]))))return false;} return true; })()`));
    A('每卡恰 1 个 tweet-text/tweet-zh/tweet-note',
      await ev(send, `[...document.querySelectorAll('.tweet-card')].every(c =>
        c.querySelectorAll('.tweet-zh').length===1 && c.querySelectorAll('.tweet-text').length===1 &&
        c.querySelectorAll('.tweet-note').length===1)`));
    A('Permalink 一一对应（40/40）',
      await ev(send, `[...document.querySelectorAll('.tweet-card')].every(c =>
        c.querySelector('a.tweet-date') && c.querySelector('a.tweet-date').getAttribute('href')==='#'+c.id)`));

    console.log('[桌面] 新卡逐字与双语');
    A('无安全员卡逐字',
      await ev(send, `document.querySelector('#p2026-01-22 .tweet-text').textContent.includes('no safety monitor in the car') &&
        document.querySelector('#p2026-01-22 .tweet-text').textContent.includes('100X harder than cars')`));
    A('全区开放卡逐字',
      await ev(send, `document.querySelector('#p2025-10-29 .tweet-text').textContent === 'Tesla Model Y robotaxi service now available in the greater Austin area!'`));
    A('灰猫卡逐字',
      await ev(send, `document.querySelector('#p2026-10-03 .tweet-text').textContent.includes('grey kittens on grey tarmac in the dark')`));
    A('六新卡双语（EN 原文 + 中文 CJK）',
      await ev(send, NEW.map(c => `(()=>{const c=document.getElementById('${c}');
        const en=c.querySelector('.tweet-text').textContent, zh=c.querySelector('.tweet-zh').textContent;
        return /[A-Za-z]/.test(en) && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));

    console.log('[桌面] 年份分组与互链');
    const yrFor = id => `(()=>{let n=document.getElementById('${id}').previousElementSibling;
      while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
      return n ? n.textContent.trim() : 'NONE';})()`;
    A('p2025-08-16 / p2025-10-29 归 2025 组',
      (await ev(send, yrFor('p2025-08-16'))) === '2025' && (await ev(send, yrFor('p2025-10-29'))) === '2025');
    A('p2026-01-22 / p2026-10-03 归 2026 组（新组头）',
      (await ev(send, yrFor('p2026-01-22'))) === '2026' && (await ev(send, yrFor('p2026-10-03'))) === '2026');
    A('2026 组卡序=四卡全清单',
      JSON.stringify(await ev(send, `(()=>{let n=document.getElementById('p2026-01-22').previousElementSibling;
        while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
        const ids=[]; n=n.nextElementSibling;
        while(n){ if(n.classList.contains('tweet-card')) ids.push(n.id); n=n.nextElementSibling;}
        return ids;})()`)) === JSON.stringify(['p2026-01-22', 'p2026-07-01', 'p2026-09-14', 'p2026-10-03']));
    A('互链：promises / 账本e2026-07-22 / grok / 页内p2026-10-03',
      await ev(send, `!!document.querySelector('#p2025-08-16 a[href="promises.html"]') &&
        !!document.querySelector('#p2026-07-01 a[href="primary.html#e2026-07-22"]') &&
        !!document.querySelector('#p2026-09-14 a[href="grok.html"]') &&
        !!document.querySelector('#p2026-01-22 a[href="#p2026-10-03"]')`));
    A('跨页锚 e2026-07-22 / e2025-02-18 真实存在',
      (await getBody(BASE + '/primary.html')).includes('id="e2026-07-22"') &&
      (await getBody(BASE + '/primary.html')).includes('id="e2025-02-18"'));

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
