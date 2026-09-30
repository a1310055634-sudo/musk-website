// V9-20 R04 探针：interviews.html 四张新卡渲染/六件套/Permalink/双语/互链/无溢出 + 检索命中
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9335;  // 9227 被 aDrive.exe 占用；9333/9334 为 R02/R03 用过（防残留）
const BASE = 'http://127.0.0.1:8766';
const NEW_CARDS = ['i2016-06-01', 'i2020-03-09', 'i2021-07-30', 'i2024-09-08'];

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
  A('索引访谈计数=37',
    (sidx.match(/"t": "访谈与表态"/g) || []).length === 37,
    String((sidx.match(/"t": "访谈与表态"/g) || []).length));
  A('索引总数=262', (sidx.match(/"id": "/g) || []).length === 262,
    String((sidx.match(/"id": "/g) || []).length));
  A('四卡逐字句入索引',
    sidx.includes('one in billions chance') &&
    sidx.includes('any impact whatsoever in astronomical discoveries') &&
    sidx.includes('factory is underrated') &&
    sidx.includes('DMV at scale'));
  A('四卡 bg 字段（ctx 背景句）全部补全',
    NEW_CARDS.every(c => {
      const m = sidx.match(new RegExp('\\{[^{}]*"id": "' + c + '"[^{}]*\\}'));
      return !!m && !/"bg": ""/.test(m[0]);
    }));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r04-profile-' + Date.now();
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
    A('带 id 卡总数=37', (await ev(send, `document.querySelectorAll('.iv-item[id]').length`)) === 37);
    A('四张新卡全部渲染',
      await ev(send, NEW_CARDS.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('每卡六件套（h2/iv-meta/ctx/blockquote/iv-zh/after 各 1）',
      await ev(send, `[...document.querySelectorAll('.iv-item[id]')].every(c =>
        c.querySelector('h2') && c.querySelector('.iv-meta') && c.querySelector('.ctx') &&
        c.querySelectorAll('blockquote').length===1 && c.querySelectorAll('.iv-zh').length===1 &&
        c.querySelectorAll('.after').length===1)`));
    A('Permalink 一一对应（37/37）',
      await ev(send, `[...document.querySelectorAll('.iv-item[id]')].every(c =>
        c.querySelector('a.iv-badge') && c.querySelector('a.iv-badge').getAttribute('href')==='#'+c.id)`));

    console.log('[桌面] 新卡逐字（源=镜像官方转写）');
    A('Code 2016 卡逐字',
      await ev(send, `document.querySelector('#i2016-06-01 blockquote').textContent.includes('a one in billions chance that this is base reality')`));
    A('Satellite 2020 卡逐字',
      await ev(send, `(()=>{const t=document.querySelector('#i2020-03-09 blockquote').textContent;
        return t.includes('any impact whatsoever in astronomical discoveries. Zero.') &&
               t.includes('a fully and rapidly reusable rocket');})()`));
    A('EA Starbase 卡逐字（含五步算法句）',
      await ev(send, `(()=>{const c=document.getElementById('i2021-07-30');
        const q=c.querySelector('blockquote').textContent, a=c.querySelector('.after').textContent;
        return q.includes('a factory is underrated and design is overrated') &&
               q.includes('optimize the thing that should not exist') &&
               a.includes('make your requirements less dumb') && a.includes('the final step is automate');})()`));
    A('All-In 2024 卡逐字',
      await ev(send, `document.querySelector('#i2024-09-08 blockquote').textContent.trim() === '“The government is the DMV at scale.”'`));
    A('新卡双语（h2 data-en + 中文 CJK 正文）',
      await ev(send, NEW_CARDS.map(c => `(()=>{const c=document.getElementById('${c}');
        const en=c.querySelector('h2').getAttribute('data-en')||'', zh=c.querySelector('.iv-zh').textContent;
        return en.length>10 && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));

    console.log('[桌面] 互链与锚完整性');
    A('Code 2016 卡互链页内 i2016-09-27',
      await ev(send, `!!document.querySelector('#i2016-06-01 a[href="#i2016-09-27"]')`));
    A('Satellite 卡互链页内 i2020-05-30',
      await ev(send, `!!document.querySelector('#i2020-03-09 a[href="#i2020-05-30"]')`));
    A('EA 卡互链账本 e2002-10-03 真实存在',
      await ev(send, `!!document.querySelector('#i2021-07-30 a[href="primary.html#e2002-10-03"]')`) &&
      (await getBody(BASE + '/primary.html')).includes('id="e2002-10-03"'));
    A('All-In 卡互链页内 i2024-11-04',
      await ev(send, `!!document.querySelector('#i2024-09-08 a[href="#i2024-11-04"]')`));
    A('全页 #i… 锚零缺失',
      await ev(send, `[...document.querySelectorAll('a[href^="#i"]')].every(a =>
        !!document.getElementById(a.getAttribute('href').slice(1)))`));
    A('批次注释 R04 在档',
      (await getBody(BASE + '/interviews.html')).includes('R04 批次'));

    // ---- 检索命中 ----
    await send('Page.navigate', { url: BASE + '/search.html?q=DMV' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[检索] search.html?q=DMV / q=simulation');
    A('DMV 检索命中≥1', (await ev(send, `document.querySelectorAll('#sr-results .sr-item').length`)) >= 1);
    A('命中含 i2024-09-08',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('i2024-09-08'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=billions' });
    await new Promise(r => setTimeout(r, 1200));
    A('billions 命中含 i2016-06-01',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('i2016-06-01'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=blackmail' });
    await new Promise(r => setTimeout(r, 1200));
    A('存量回归：blackmail 命中不回退（i2023-11-29）',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('i2023-11-29'))`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/interviews.html' });
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
