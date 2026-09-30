// V9-20 R02 探针：x-posts.html 四张新卡渲染/时序/互链/双语/无溢出 + 检索命中（≥12 断言）
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9333;  // 9227 被 aDrive.exe 占用（连接通但不响应，轮询会挂死）
const BASE = 'http://127.0.0.1:8766';
const NEW_CARDS = ['p2020-04-29', 'p2021-01-26', 'p2021-05-05', 'p2021-11-02'];

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
  const send = (method, params) => new Promise((res, rej) => {
    const mid = ++id; pending.set(mid, { res, rej });
    client.send(JSON.stringify({ id: mid, method, params }));
  });
  return send;
}
const ev = (send, expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true })
  .then(r => r.result.value);

async function main() {
  // ---------- 文件级：search-index.js 内容 ----------
  console.log('[文件级] search-index.js');
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  for (const cid of NEW_CARDS) A(`索引含新帖 ${cid}`, sidx.includes(`"id": "${cid}"`));
  A('索引 X 帖计数=27',
    (sidx.match(/"t": "X 帖"/g) || []).length === 27,
    String((sidx.match(/"t": "X 帖"/g) || []).length));
  A('Hertz 逐字句入索引', sidx.includes('no contract has been signed yet') && sidx.includes('zero effect on our economics'));

  // ---------- 浏览器（每次全新 user-data-dir，防被杀残留 SingletonLock 卡死后续实例） ----------
  const profile = process.env.TEMP + '/v9r02-profile-' + Date.now();
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
    console.log('  · CDP 已连上，targets=' + targets.length);
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable');
    await send('Runtime.enable');

    // ---- 桌面 1440x900 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/x-posts.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] x-posts.html 结构');
    A('卡总数=27', (await ev(send, `document.querySelectorAll('.tweet-card').length`)) === 27);
    A('四张新卡全部渲染',
      await ev(send, NEW_CARDS.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('全卡时序升序',
      await ev(send, `(() => { const ids=[...document.querySelectorAll('.tweet-card')].map(e=>e.id);
        const k=s=>s.slice(1).split('-').map(Number); for(let i=1;i<ids.length;i++){const a=k(ids[i-1]),b=k(ids[i]);
        if(a[0]>b[0]||(a[0]==b[0]&&(a[1]>b[1]||(a[1]==b[1]&&a[2]>b[2]))))return false;} return true; })()`));
    A('每卡恰 1 个 tweet-zh/tweet-text/tweet-note',
      await ev(send, `[...document.querySelectorAll('.tweet-card')].every(c =>
        c.querySelectorAll('.tweet-zh').length===1 && c.querySelectorAll('.tweet-text').length===1 &&
        c.querySelectorAll('.tweet-note').length===1)`));
    A('新卡双语（EN 原文 + 中文 CJK）',
      await ev(send, NEW_CARDS.map(c => `(()=>{const c=document.getElementById('${c}');
        const en=c.querySelector('.tweet-text').textContent, zh=c.querySelector('.tweet-zh').textContent;
        return /[A-Za-z]/.test(en) && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));
    A('Permalink 一一对应（27/27）',
      await ev(send, `[...document.querySelectorAll('.tweet-card')].every(c =>
        c.querySelector('a.tweet-date') && c.querySelector('a.tweet-date').getAttribute('href')==='#'+c.id)`));

    console.log('[桌面] 年份分组修正');
    A('p2020-03-06 前年份条=2020',
      (await ev(send, `(()=>{let n=document.getElementById('p2020-03-06').previousElementSibling;
        while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
        return n ? n.textContent.trim() : 'NONE';})()`)) === '2020');
    A('p2021-01-26 前年份条=2021',
      (await ev(send, `(()=>{let n=document.getElementById('p2021-01-26').previousElementSibling;
        while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
        return n ? n.textContent.trim() : 'NONE';})()`)) === '2021');
    A('2021 组卡序=01-26/03-02/05-05/11-02',
      JSON.stringify(await ev(send, `(()=>{let n=document.getElementById('p2021-01-26').previousElementSibling;
        while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
        const ids=[]; n=n.nextElementSibling;
        while(n && !n.classList.contains('xp-year')){ if(n.classList.contains('tweet-card')) ids.push(n.id); n=n.nextElementSibling;}
        return ids;})()`)) === JSON.stringify(['p2021-01-26','p2021-03-02','p2021-05-05','p2021-11-02']));
    A('p2022-12-18 归 2022 组（存量错位修正）',
      (await ev(send, `(()=>{let n=document.getElementById('p2022-12-18').previousElementSibling;
        while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
        return n ? n.textContent.trim() : 'NONE';})()`)) === '2022');

    console.log('[桌面] Hertz 卡逐字与互链');
    A('Hertz 卡含两句关键逐字',
      await ev(send, `(()=>{const t=document.querySelector('#p2021-11-02 .tweet-text').textContent;
        return t.includes('no contract has been signed yet') && t.includes('zero effect on our economics') &&
               t.includes('same margin as to consumers');})()`));
    A('Hertz 卡互链账本 e2021-10-25',
      await ev(send, `!!document.querySelector('#p2021-11-02 a[href="primary.html#e2021-10-25"]')`));
    A('跨页锚真实存在',
      (await getBody(BASE + '/primary.html')).includes('id="e2021-10-25"'));
    A('卡间互链双向可解析',
      await ev(send, `!!document.querySelector('#p2021-01-26 a[href="#p2021-11-02"]') &&
        !!document.querySelector('#p2021-11-02 a[href="#p2021-01-26"]') &&
        !!document.querySelector('#p2020-04-29 a[href="#p2020-03-06"]')`));

    // ---- 检索命中 ----
    await send('Page.navigate', { url: BASE + '/search.html?q=Gamestonk' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[检索] search.html?q=Gamestonk');
    const hits = await ev(send, `document.querySelectorAll('#sr-results .sr-item').length`);
    A('Gamestonk 检索命中≥1', hits >= 1, 'hits=' + hits);
    A('命中含 p2021-01-26',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('p2021-01-26'))`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/x-posts.html' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[390] x-posts.html 溢出');
    const sw = await ev(send, `document.documentElement.scrollWidth`);
    A('scrollWidth≤390（零横向溢出）', sw <= 390, 'scrollWidth=' + sw);
    A('Hertz 卡 390 可见且无内部溢出',
      await ev(send, `(()=>{const c=document.getElementById('p2021-11-02'); if(!c) return false;
        const r=c.getBoundingClientRect(); return r.width>0 && c.scrollWidth<=c.clientWidth+1;})()`));
    client.close();
  } finally {
    chrome.kill();
  }
  console.log(`\\n探针结论：${PASS} 过 / ${FAIL} 败`);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
