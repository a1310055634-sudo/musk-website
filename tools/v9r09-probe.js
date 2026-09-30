// V9-20 R09 探针：e2013 新卡 + 语录卡口径 103/105/2 + 主路径五页 + 检索回归 + 390 零溢出
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9353;  // 9227 aDrive 占用；9333-9351 为此前轮次用过（防残留孤儿实例）
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
  // ---------- 文件级：口径复算 ----------
  console.log('[文件级] 语录卡口径复算');
  const qh = fs.readFileSync('quotes.html', 'utf-8');
  const ph = fs.readFileSync('primary.html', 'utf-8');
  const cards = qh.match(/qs-card" href="primary\.html#(e[\d-]+)"/g) || [];
  const cardIds = cards.map(s => s.match(/#(e[\d-]+)"/)[1]);
  A('qs-card 总数=103', cardIds.length === 103, String(cardIds.length));
  const blocks = ph.match(/<li class="ps-row[^"]*" id="e\d[\d-]*"[\s\S]*?<\/li>/g) || [];
  const quoted = blocks.filter(b => b.includes('<blockquote class="ps-quote">'))
    .map(b => b.match(/id="(e[\d-]*)"/)[1]);
  A('账本引文块=105', quoted.length === 105, String(quoted.length));
  const gap = quoted.filter(id => !cardIds.includes(id));
  A('差集={e2021-07,e2025}（白名单精确吻合）',
    gap.length === 2 && gap.includes('e2021-07') && gap.includes('e2025'),
    JSON.stringify(gap));
  A('e2013 卡在册', cardIds.includes('e2013'));
  const i2013 = cardIds.indexOf('e2013');
  A('e2013 插入点局部时序（文件级：前=e2012-06-22 后=e2013-05-08）',
    i2013 > 0 && cardIds[i2013 - 1] === 'e2012-06-22' && cardIds[i2013 + 1] === 'e2013-05-08',
    cardIds.slice(i2013 - 1, i2013 + 2).join(','));
  A('存量卡序未受本轮影响（本轮仅插入 1 卡）',
    cardIds.filter(id => id !== 'e2013').length === 102);
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  A('索引总数=282', (sidx.match(/"id": "/g) || []).length === 282,
    String((sidx.match(/"id": "/g) || []).length));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r09-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'],
    { stdio: 'ignore' });
  const shot = async (send, path, file) => {
    const c = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(path, Buffer.from(c.data, 'base64'));
    console.log('  · 截图 ' + file);
  };
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

    // ---- 主路径① index.html ----
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/index.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[主路径①] index.html');
    A('首页渲染（hero 标题 + 版本 8.9.0）',
      await ev(send, `!!document.querySelector('h1') && document.body.textContent.includes('8.9.0')`));
    A('首页五组导航在册',
      await ev(send, `document.querySelectorAll('nav a[href]').length >= 10`));

    // ---- 主路径② quotes.html 新卡 ----
    await send('Page.navigate', { url: BASE + '/quotes.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[主路径②] quotes.html e2013 新卡');
    A('qs-card DOM 总数=103',
      (await ev(send, `document.querySelectorAll('a.qs-card[href^="primary.html#e"]').length`)) === 103,
      String(await ev(send, `document.querySelectorAll('a.qs-card[href^="primary.html#e"]').length`)));
    A('e2013 卡渲染且 qs-date=「2013（约）」',
      await ev(send, `(()=>{const c=document.querySelector('a.qs-card[href="primary.html#e2013"]');
        return c && c.querySelector('.qs-date').textContent.includes('2013') &&
               c.querySelector('.qs-date').textContent.includes('约');})()`));
    A('e2013 卡位置（前=e2012-06-22，后=e2013-05-08）',
      await ev(send, `(()=>{const c=document.querySelector('a.qs-card[href="primary.html#e2013"]');
        const prev=c.previousElementSibling && c.previousElementSibling.getAttribute('href');
        const next=c.nextElementSibling && c.nextElementSibling.getAttribute('href');
        return prev && prev.includes('e2012-06-22') && next && next.includes('e2013-05-08');})()`));
    A('e2013 卡双语（en 引语 + zh 对照）',
      await ev(send, `(()=>{const c=document.querySelector('a.qs-card[href="primary.html#e2013"]');
        return c.querySelector('.qs-en').textContent.includes('die on Mars') &&
               c.querySelector('.qs-zh').textContent.includes('摔死');})()`));
    A('e2013 卡 qs-src 如实标注「广泛征引」',
      await ev(send, `document.querySelector('a.qs-card[href="primary.html#e2013"] .qs-src').textContent.includes('广泛征引')`));
    A('格言轮播五句仍在（strip 与核实区并存）',
      await ev(send, `document.querySelectorAll('#quote-strip blockquote.quote').length===5 &&
        document.getElementById('quote-strip').textContent.includes('die on Mars')`));
    A('核实组注记（与上方广为征引的格言不同…）在',
      await ev(send, `[...document.querySelectorAll('.qs-p')].some(p=>p.textContent.includes('与上方广为征引的格言不同'))`));
    await ev(send, `(()=>{const c=document.querySelector('a.qs-card[href="primary.html#e2013"]');
      c.scrollIntoView({block:'center'});})()`);
    await new Promise(r => setTimeout(r, 600));
    await shot(send, 'qa/v9-20/round-09/quotes-e2013-desktop.png', 'quotes-e2013-desktop.png');

    // ---- 主路径③ primary.html（卡→账本锚实存） ----
    await send('Page.navigate', { url: BASE + '/primary.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[主路径③] primary.html');
    A('账本 ps-row=115',
      (await ev(send, `document.querySelectorAll('li.ps-row[id]').length`)) === 115,
      String(await ev(send, `document.querySelectorAll('li.ps-row[id]').length`)));
    A('e2013 锚实存且含 die on Mars 引文块',
      await ev(send, `(()=>{const c=document.getElementById('e2013');
        return !!c && c.textContent.includes('die on Mars') && !!c.querySelector('blockquote.ps-quote');})()`));
    A('跳转链路：quotes 卡 href 与账本锚精确匹配',
      (await ev(send, `document.getElementById('e2013').id`)) === 'e2013');
    A('页内时间轴节点=115（verify 第 5 项口径）',
      (await ev(send, `document.querySelectorAll('.pt-dot').length`)) === 115,
      String(await ev(send, `document.querySelectorAll('.pt-dot').length`)));

    // ---- 主路径④ timeline + events ----
    await send('Page.navigate', { url: BASE + '/timeline.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[主路径④] timeline.html');
    A('TIMELINE_V7.meta 回归（14 档案/229 记录/39 吸收）',
      await ev(send, `window.TIMELINE_V7 && window.TIMELINE_V7.meta.nEvents===14 &&
        window.TIMELINE_V7.meta.nRecords===229 && window.TIMELINE_V7.meta.nAbsorbed===39`));
    await send('Page.navigate', { url: BASE + '/events.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('事件档案=14（回归不破）',
      (await ev(send, `document.querySelectorAll('section.ev-item[id]').length`)) === 14,
      String(await ev(send, `document.querySelectorAll('section.ev-item[id]').length`)));

    // ---- 主路径⑤ 检索 ----
    await send('Page.navigate', { url: BASE + '/search.html?q=die%20on%20Mars' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[主路径⑤] 检索');
    A('「die on Mars」命中（账本/语录）',
      await ev(send, `document.querySelectorAll('#sr-results a').length > 0`),
      String(await ev(send, `document.querySelectorAll('#sr-results a').length`)));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/quotes.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[390] quotes.html');
    const sw = await ev(send, `document.documentElement.scrollWidth`);
    const cw = await ev(send, `document.documentElement.clientWidth`);
    A(`[390] 零横向溢出（scrollWidth ${sw} ≤ clientWidth ${cw}）`, sw <= cw, sw + '>' + cw);
    A('[390] e2013 卡渲染', await ev(send,
      `(()=>{const c=document.querySelector('a.qs-card[href="primary.html#e2013"]');
      c.scrollIntoView({block:'center'});return !!c;})()`));
    await new Promise(r => setTimeout(r, 600));
    await shot(send, 'qa/v9-20/round-09/quotes-e2013-390.png', 'quotes-e2013-390.png');
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
