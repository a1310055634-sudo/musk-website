// V9-20 R05 探针：interviews.html 五张新卡渲染/六件套/Permalink/双语/互链/无溢出 + 检索命中
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9336;  // 9227 aDrive 占用；9333-9335 为 R02-R04 用过（防残留）
const BASE = 'http://127.0.0.1:8766';
const NEW_CARDS = ['i2013-02-27', 'i2014-09-25', 'i2018-08-15', 'i2021-12-28-2', 'i2023-11-10-2'];

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
  for (const cid of NEW_CARDS) A(`索引含新卡 ${cid}`, sidx.includes(`"id": "${cid}"`));
  A('索引访谈计数=42',
    (sidx.match(/"t": "访谈与表态"/g) || []).length === 42,
    String((sidx.match(/"t": "访谈与表态"/g) || []).length));
  A('索引总数=267', (sidx.match(/"id": "/g) || []).length === 267,
    String((sidx.match(/"id": "/g) || []).length));
  A('五卡逐字句入索引',
    sidx.includes('life insurance for life') &&
    sidx.includes('Free speech only matters') &&
    sidx.includes('a rapidly and fully reusable rocket') &&
    sidx.includes('direct democracy') &&
    sidx.includes('pay full retail price for my own cars'));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r05-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/interviews.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] 结构与渲染');
    A('带 id 卡总数=42', (await ev(send, `document.querySelectorAll('.iv-item[id]').length`)) === 42);
    A('五张新卡全部渲染',
      await ev(send, NEW_CARDS.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('每卡六件套（h2/iv-meta/ctx/blockquote/iv-zh/after 各 1）',
      await ev(send, `[...document.querySelectorAll('.iv-item[id]')].every(c =>
        c.querySelector('h2') && c.querySelector('.iv-meta') && c.querySelector('.ctx') &&
        c.querySelectorAll('blockquote').length===1 && c.querySelectorAll('.iv-zh').length===1 &&
        c.querySelectorAll('.after').length===1)`));
    A('Permalink 一一对应（42/42）',
      await ev(send, `[...document.querySelectorAll('.iv-item[id]')].every(c =>
        c.querySelector('a.iv-badge') && c.querySelector('a.iv-badge').getAttribute('href')==='#'+c.id)`));

    console.log('[桌面] 五卡逐字（源=镜像官方转写/官方逐字稿）');
    A('TED 2013 卡逐字',
      await ev(send, `(()=>{const t=document.querySelector('#i2013-02-27 blockquote').textContent;
        return t.includes('a rapidly and fully reusable rocket') &&
               t.includes('a billion dollars per flight');})()`));
    A('Code 2014 卡逐字',
      await ev(send, `(()=>{const t=document.querySelector('#i2014-09-25 blockquote').textContent;
        return t.includes('direct democracy') && t.includes('sunset provision');})()`));
    A('MKBHD 2018 卡逐字',
      await ev(send, `(()=>{const t=document.querySelector('#i2018-08-15 blockquote').textContent;
        return t.includes('word of mouth') && t.includes('pay full retail price for my own cars');})()`));
    A('Lex #252 卡逐字（life insurance + I love humanity）',
      await ev(send, `(()=>{const t=document.querySelector('#i2021-12-28-2 blockquote').textContent;
        return t.includes('life insurance for life') && t.includes('I love humanity');})()`));
    A('Lex #400 卡逐字（free speech + worst thing on Earth today）',
      await ev(send, `(()=>{const t=document.querySelector('#i2023-11-10-2 blockquote').textContent;
        return t.includes("Free speech only matters if people you don't like") &&
               t.includes('worst thing that happened on Earth today');})()`));
    A('五卡双语（h2 data-en + 中文 CJK 正文）',
      await ev(send, NEW_CARDS.map(c => `(()=>{const c=document.getElementById('${c}');
        const en=c.querySelector('h2').getAttribute('data-en')||'', zh=c.querySelector('.iv-zh').textContent;
        return en.length>10 && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));

    console.log('[桌面] 互链与锚完整性');
    A('TED 卡互链页内 i2024-10-13 与 i2018-08-15',
      await ev(send, `!!document.querySelector('#i2013-02-27 a[href="#i2024-10-13"]') &&
        !!document.querySelector('#i2013-02-27 a[href="#i2018-08-15"]')`));
    A('Code 2014 卡互链 x-posts.html#p2025-07-05 真实存在',
      await ev(send, `!!document.querySelector('#i2014-09-25 a[href="x-posts.html#p2025-07-05"]')`) &&
      (await getBody(BASE + '/x-posts.html')).includes('id="p2025-07-05"'));
    A('MKBHD 卡互链 promises.html#promises-s4 真实存在 + 页内 i2017-07-28',
      await ev(send, `!!document.querySelector('#i2018-08-15 a[href="promises.html#promises-s4"]') &&
        !!document.querySelector('#i2018-08-15 a[href="#i2017-07-28"]')`) &&
      (await getBody(BASE + '/promises.html')).includes('id="promises-s4"'));
    A('Lex #400 卡互链 platform-x.html + 页内 i2022-11-16',
      await ev(send, `!!document.querySelector('#i2023-11-10-2 a[href="platform-x.html"]') &&
        !!document.querySelector('#i2023-11-10-2 a[href="#i2022-11-16"]')`) &&
      (await getBody(BASE + '/platform-x.html')).length > 1000);
    A('全页 #i… 锚零缺失',
      await ev(send, `[...document.querySelectorAll('a[href^="#i"]')].every(a =>
        !!document.getElementById(a.getAttribute('href').slice(1)))`));
    A('批次注释 R05 在档',
      (await getBody(BASE + '/interviews.html')).includes('R05 批次'));

    // ---- 检索命中 ----
    await send('Page.navigate', { url: BASE + '/search.html?q=censorship' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[检索] q=censorship / q=insurance / 回归 q=DMV');
    A('censorship 命中含 i2023-11-10-2',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('i2023-11-10-2'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=insurance' });
    await new Promise(r => setTimeout(r, 1200));
    A('insurance 命中含 i2021-12-28-2',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('i2021-12-28-2'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=DMV' });
    await new Promise(r => setTimeout(r, 1200));
    A('存量回归：DMV 命中不回退（i2024-09-08）',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('i2024-09-08'))`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/interviews.html' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[390] 溢出');
    const sw = await ev(send, `document.documentElement.scrollWidth`);
    A('scrollWidth≤390（零横向溢出）', sw <= 390, 'scrollWidth=' + sw);
    A('五张新卡 390 可见且无内部溢出',
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
