// V9-20 R07 探针：primary.html 六条新账本条目 + quotes.html 六张新卡 + 检索命中 + 390 零溢出
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9341;  // 9227 aDrive 占用；9333-9339 为此前轮次用过（防残留）
const BASE = 'http://127.0.0.1:8766';
const NEW = ['e2015-12-02', 'e2018-09-17', 'e2019-04-22', 'e2022-09-30', 'e2022-11-30', 'e2024-03-18'];

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
  for (const id of NEW) A(`索引含新条目 ${id}`, sidx.includes(`"id": "${id}"`));
  A('索引言行实录计数=115',
    (sidx.match(/"t": "言行实录"/g) || []).length === 115,
    String((sidx.match(/"t": "言行实录"/g) || []).length));
  A('索引总数=277', (sidx.match(/"id": "/g) || []).length === 277,
    String((sidx.match(/"id": "/g) || []).length));
  A('六条逐字句入索引',
    sidx.includes('dumbest experiment in history ever') &&
    sidx.includes('walk in the park here') &&
    sidx.includes("LIDAR is a fool's errand") &&
    sidx.includes('just a person in a robot suit') &&
    sidx.includes('most of our paperwork to the FDA') &&
    sidx.includes('we will indeed occupy Mars'));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r07-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2,8);
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

    // ---- 桌面 1440x900：primary.html ----
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/primary.html' });
    // 冷启动加固：等 ps-row 数稳定到 115（最多 15s）
    for (let i = 0; i < 30; i++) {
      const n = await ev(send, `document.querySelectorAll('li.ps-row[id]').length`);
      if (n === 115) break;
      await new Promise(r => setTimeout(r, 500));
    }
    console.log('[桌面] 结构与渲染');
    A('账本条目总数=115', (await ev(send, `document.querySelectorAll('li.ps-row[id]').length`)) === 115);
    A('六条新条目全部渲染',
      await ev(send, NEW.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('新条四段五件套（ps-head/ps-sec×4/ps-quote/ps-zh/permalink）',
      await ev(send, NEW.map(c => `(()=>{const c=document.getElementById('${c}');
        return c.classList.contains('ps-row') && c.querySelectorAll('.ps-sec').length===4 &&
               c.querySelector('.ps-head .ps-src') &&
               c.querySelector('blockquote.ps-quote') && c.querySelector('p.ps-zh') &&
               c.querySelector('a.ps-date[href="#${c}"]');})()`).join('&&')));
    A('新条双语（4 个 data-en 标签 + 中文正文）',
      await ev(send, NEW.map(c => `(()=>{const c=document.getElementById('${c}');
        const tags=[...c.querySelectorAll('[data-en]')].length;
        const zh=c.textContent;
        return tags>=7 && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));
    A('Permalink 一一对应（115/115）',
      await ev(send, `[...document.querySelectorAll('li.ps-row[id]')].every(c =>
        !!c.querySelector('a.ps-date[href="#'+c.id+'"]'))`));

    console.log('[桌面] 六条逐字（源=镜像 /video/{id} 全场逐字转写）');
    A('COP21 逐字', await ev(send, `document.querySelector('#e2015-12-02 blockquote').textContent.includes('dumbest experiment in history ever')`));
    A('BFR 逐字', await ev(send, `document.querySelector('#e2018-09-17 blockquote').textContent.includes("It's dangerous. To be clear, this is dangerous.")`));
    A('Autonomy Day 逐字', await ev(send, `document.querySelector('#e2019-04-22 blockquote').textContent.includes("LIDAR is a fool's errand") && document.querySelector('#e2019-04-22 blockquote').textContent.includes('doomed')`));
    A('AI Day 2022 逐字', await ev(send, `document.querySelector('#e2022-09-30 blockquote').textContent.includes('just a person in a robot suit')`));
    A('Neuralink 逐字', await ev(send, `document.querySelector('#e2022-11-30 blockquote').textContent.includes('most of our paperwork to the FDA')`));
    A('Starbase 逐字', await ev(send, `document.querySelector('#e2024-03-18 blockquote').textContent.includes('we will indeed occupy Mars')`));
    A('e2024-03-18 双日期口径注（镜像归档锚+IFT-3）',
      await ev(send, `(()=>{const t=document.getElementById('e2024-03-18').textContent;
        return t.includes('2024-03-18') && t.includes('2024-03-14');})()`));
    A('ASR 口径注明（Yusaku/Usage 类）',
      await ev(send, `(()=>{const t=document.getElementById('e2022-11-30').textContent;
        return t.includes('镜像转写') || t.includes('听写');})()`));

    console.log('[桌面] 互链与锚完整性');
    A('全页 #e… 锚零缺失',
      await ev(send, `[...document.querySelectorAll('a[href^="#e"]')].every(a =>
        !!document.getElementById(a.getAttribute('href').slice(1)))`));
    A('COP21 互链 e2015-04-30 页内存在',
      await ev(send, `!!document.querySelector('#e2015-12-02 a[href="primary.html#e2015-04-30"]')`));
    A('BFR 互链 e2017-09-29/e2019-09-28 存在',
      await ev(send, `!!document.querySelector('#e2018-09-17 a[href="primary.html#e2017-09-29"]') &&
        !!document.querySelector('#e2018-09-17 a[href="primary.html#e2019-09-28"]')`));
    A('AI Day 2022 互链 e2021-08 存在',
      await ev(send, `!!document.querySelector('#e2022-09-30 a[href="primary.html#e2021-08"]')`));
    A('Neuralink 互链 e2020-08-28/e2021-04-09/e2024-01-29 存在',
      await ev(send, `!!document.querySelector('#e2022-11-30 a[href="primary.html#e2020-08-28"]') &&
        !!document.querySelector('#e2022-11-30 a[href="primary.html#e2021-04-09"]') &&
        !!document.querySelector('#e2022-11-30 a[href="primary.html#e2024-01-29"]')`));
    A('Starbase 互链 e2024-10-13 页内 + x-posts.html#p2024-10-13 跨页真实',
      await ev(send, `!!document.querySelector('#e2024-03-18 a[href="primary.html#e2024-10-13"]')`) &&
      (await getBody(BASE + '/x-posts.html')).includes('id="p2024-10-13"'));
    A('Autonomy Day 互链 promises.html 页面存在',
      await ev(send, `!!document.querySelector('#e2019-04-22 a[href="promises.html"]')`) &&
      (await getBody(BASE + '/promises.html')).length > 5000);

    // ---- quotes.html ----
    await send('Page.navigate', { url: BASE + '/quotes.html' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[桌面] quotes.html');
    A('语录卡总数=102', (await ev(send, `document.querySelectorAll('a.qs-card').length`)) === 102);
    A('六张新卡渲染且链向正确条目',
      await ev(send, NEW.map(c => `!!document.querySelector('a.qs-card[href="primary.html#${c}"]')`).join('&&')));
    A('新卡结构（qs-date/qs-en/qs-zh/qs-src）',
      await ev(send, NEW.map(c => `(()=>{const c=document.querySelector('a.qs-card[href="primary.html#${c}"]');
        return c.querySelector('.qs-date') && c.querySelector('.qs-en') &&
               c.querySelector('.qs-zh') && c.querySelector('.qs-src');})()`).join('&&')));
    A('六张新卡英文引语逐字',
      await ev(send, NEW.map(c => `(()=>{const c=document.querySelector('a.qs-card[href="primary.html#${c}"] .qs-en');
        const t=c.textContent; return t.length>10;})()`).join('&&')));

    // ---- index.html 计数 ----
    await send('Page.navigate', { url: BASE + '/index.html' });
    await new Promise(r => setTimeout(r, 1200));
    A('index 计数 115（中文）',
      await ev(send, `document.body.textContent.includes('115 条言行账本')`));
    A('index 计数 115（data-en 属性）',
      await ev(send, `!!document.querySelector('[data-en*="All 115 ledger entries"]')`));

    // ---- 检索 ----
    console.log('[检索] 新条命中 + 存量回归');
    await send('Page.navigate', { url: BASE + '/search.html?q=dumbest%20experiment' });
    await new Promise(r => setTimeout(r, 1200));
    A('dumbest experiment 命中 e2015-12-02',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('e2015-12-02'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=robot%20suit' });
    await new Promise(r => setTimeout(r, 1200));
    A('robot suit 命中 e2022-09-30',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('e2022-09-30'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=LIDAR' });
    await new Promise(r => setTimeout(r, 1200));
    A('LIDAR 命中 e2019-04-22',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('e2019-04-22'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=funding%20secured' });
    await new Promise(r => setTimeout(r, 1200));
    A('存量回归：funding secured 不回退',
      await ev(send, `document.querySelectorAll('#sr-results .sr-item').length > 0`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/primary.html' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[390] primary.html');
    let sw = await ev(send, `document.documentElement.scrollWidth`);
    A('scrollWidth≤390（零横向溢出）', sw <= 390, 'scrollWidth=' + sw);
    A('六条新条 390 可见且无内部溢出',
      await ev(send, NEW.map(c => `(()=>{const x=document.getElementById('${c}'); if(!x) return false;
        const r=x.getBoundingClientRect(); return r.width>0 && x.scrollWidth<=x.clientWidth+1;})()`).join('&&')));
    await send('Page.navigate', { url: BASE + '/quotes.html' });
    await new Promise(r => setTimeout(r, 1200));
    sw = await ev(send, `document.documentElement.scrollWidth`);
    A('quotes 390 零溢出', sw <= 390, 'scrollWidth=' + sw);

    client.close();
  } finally {
    chrome.kill();
  }
  console.log('\n探针结论：' + PASS + ' 过 / ' + FAIL + ' 败');
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
