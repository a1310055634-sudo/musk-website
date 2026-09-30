// V9-20 R03 探针：x-posts.html 四张新卡渲染/时序/年份组/互链/双语/无溢出 + 检索命中
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9334;  // 9227 被 aDrive.exe 占用；9333 为 R02 用过（防残留），R03 用 9334
const BASE = 'http://127.0.0.1:8766';
const NEW_CARDS = ['p2023-11-30', 'p2024-01-30', 'p2024-07-13', 'p2025-07-05'];

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
  // ---------- 文件级：search-index.js ----------
  console.log('[文件级] search-index.js');
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  for (const cid of NEW_CARDS) A(`索引含新帖 ${cid}`, sidx.includes(`"id": "${cid}"`));
  A('索引 X 帖计数=31',
    (sidx.match(/"t": "X 帖"/g) || []).length === 31,
    String((sidx.match(/"t": "X 帖"/g) || []).length));
  A('四帖逐字句入索引',
    sidx.includes('Never incorporate your company') &&
    sidx.includes('fully endorse President Trump') &&
    sidx.includes('America Party is formed') &&
    sidx.includes('First Cybertruck deliveries'));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r03-profile-' + Date.now();
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

    console.log('[桌面] 结构与渲染');
    A('卡总数=31', (await ev(send, `document.querySelectorAll('.tweet-card').length`)) === 31);
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
    A('Permalink 一一对应（31/31）',
      await ev(send, `[...document.querySelectorAll('.tweet-card')].every(c =>
        c.querySelector('a.tweet-date') && c.querySelector('a.tweet-date').getAttribute('href')==='#'+c.id)`));

    console.log('[桌面] 新卡逐字（源=镜像 transcript）');
    A('Cybertruck 卡逐字',
      await ev(send, `document.querySelector('#p2023-11-30 .tweet-text').textContent.includes('First Cybertruck deliveries in 2 hours!')`));
    A('Delaware 卡逐字',
      await ev(send, `document.querySelector('#p2024-01-30 .tweet-text').textContent.includes('Never incorporate your company in the state of Delaware')`));
    A('Trump 卡逐字',
      await ev(send, `document.querySelector('#p2024-07-13 .tweet-text').textContent === 'I fully endorse President Trump and hope for his rapid recovery'`));
    A('America Party 卡三段全文逐字',
      await ev(send, `(()=>{const t=document.querySelector('#p2025-07-05 .tweet-text').textContent;
        return t.includes('By a factor of 2 to 1, you want a new political party and you shall have it!') &&
               t.includes('we live in a one-party system, not a democracy') &&
               t.includes('Today, the America Party is formed to give you back your freedom');})()`));
    A('新卡双语（EN 原文 + 中文 CJK）',
      await ev(send, NEW_CARDS.map(c => `(()=>{const c=document.getElementById('${c}');
        const en=c.querySelector('.tweet-text').textContent, zh=c.querySelector('.tweet-zh').textContent;
        return /[A-Za-z]/.test(en) && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));

    console.log('[桌面] 年份分组');
    const yrFor = id => `(()=>{let n=document.getElementById('${id}').previousElementSibling;
      while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
      return n ? n.textContent.trim() : 'NONE';})()`;
    A('p2023-11-30 归 2023 组', (await ev(send, yrFor('p2023-11-30'))) === '2023');
    A('p2024-01-30 归 2024 组', (await ev(send, yrFor('p2024-01-30'))) === '2024');
    A('p2024-07-13 归 2024 组', (await ev(send, yrFor('p2024-07-13'))) === '2024');
    A('p2025-07-05 归 2025 组', (await ev(send, yrFor('p2025-07-05'))) === '2025');
    A('2024 组卡序完整（8 张含两新卡）',
      JSON.stringify(await ev(send, `(()=>{let n=document.getElementById('p2024-01-29').previousElementSibling;
        while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
        const ids=[]; n=n.nextElementSibling;
        while(n && !n.classList.contains('xp-year')){ if(n.classList.contains('tweet-card')) ids.push(n.id); n=n.nextElementSibling;}
        return ids;})()`)) === JSON.stringify(['p2024-01-29','p2024-01-30','p2024-03-11','p2024-04-05','p2024-07-13','p2024-10-13']));

    console.log('[桌面] 互链');
    A('Trump 卡→America Party 卡互链',
      await ev(send, `!!document.querySelector('#p2024-07-13 a[href="#p2025-07-05"]') &&
        !!document.querySelector('#p2025-07-05 a[href="#p2024-07-13"]')`));
    A('跨页锚 e2023-11-30 / e2024-06-13 真实存在',
      (await getBody(BASE + '/primary.html')).includes('id="e2023-11-30"') &&
      (await getBody(BASE + '/primary.html')).includes('id="e2024-06-13"'));
    A('Delaware 卡互链账本 e2024-06-13',
      await ev(send, `!!document.querySelector('#p2024-01-30 a[href="primary.html#e2024-06-13"]')`));
    A('Cybertruck 卡互链账本 e2023-11-30',
      await ev(send, `!!document.querySelector('#p2023-11-30 a[href="primary.html#e2023-11-30"]')`));
    A('Trump 卡互链 platform-x.html',
      await ev(send, `!!document.querySelector('#p2024-07-13 a[href="platform-x.html"]')`));
    A('帖墙小结含政治维度（EN 属性同步）',
      await ev(send, `(()=>{const p=document.querySelector('.chapter-summary p');
        return p.getAttribute('data-en').includes('political weapon') && p.textContent.includes('政治武器');})()`));

    // ---- 检索命中 ----
    await send('Page.navigate', { url: BASE + '/search.html?q=endorse' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[检索] search.html?q=endorse');
    const hits = await ev(send, `document.querySelectorAll('#sr-results .sr-item').length`);
    A('endorse 检索命中≥1', hits >= 1, 'hits=' + hits);
    A('命中含 p2024-07-13',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('p2024-07-13'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=Gamestonk' });
    await new Promise(r => setTimeout(r, 1200));
    A('存量回归：Gamestonk 命中不回退',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('p2021-01-26'))`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/x-posts.html' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[390] 溢出');
    const sw = await ev(send, `document.documentElement.scrollWidth`);
    A('scrollWidth≤390（零横向溢出）', sw <= 390, 'scrollWidth=' + sw);
    A('四张新卡 390 可见且无内部溢出',
      await ev(send, NEW_CARDS.map(c => `(()=>{const x=document.getElementById('${c}'); if(!x) return false;
        const r=x.getBoundingClientRect(); return r.width>0 && x.scrollWidth<=x.clientWidth+1;})()`).join('&&')));
    client.close();
  } finally {
    chrome.kill();
  }
  console.log('\n探针结论：' + PASS + ' 过 / ' + FAIL + ' 败');
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
