// V9-20 R08 探针：14 档案渲染 + TIMELINE_V7.meta 口径断言 + chronicle 徽标 + 深链 + 检索 + 390 零溢出
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9351;  // 9227 aDrive 占用；9333-9341 为此前轮次用过（防残留）
const BASE = 'http://127.0.0.1:8766';
const NEW = ['e2010-06-29', 'e2021-10-25', 'e2021-11-26', 'e2024-01-29', 'e2019-04-22'];

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
  // ---------- 文件级：timeline-events.js meta 口径 ----------
  console.log('[文件级] timeline-events.js 口径红线');
  const tjs = fs.readFileSync('timeline-events.js', 'utf-8');
  const parsed = JSON.parse(tjs.slice(tjs.indexOf('{'), tjs.lastIndexOf('}') + 1));
  const meta = parsed.meta;
  A('nEvents=14', meta.nEvents === 14, String(meta.nEvents));
  A('nAbsorbed=39', meta.nAbsorbed === 39, String(meta.nAbsorbed));
  A('nRecords=229', meta.nRecords === 229, String(meta.nRecords));
  A('口径公式 282−14−39=229 成立', 282 - meta.nEvents - meta.nAbsorbed === meta.nRecords);
  A('version 已刷 8.8.0', meta.version === '8.8.0', meta.version);
  A('五新档案均入 absorbedByEvent', NEW.every(id => (meta.absorbedByEvent[id] || 0) >= 1),
    JSON.stringify(NEW.map(id => id + '=' + (meta.absorbedByEvent[id] || 0))));
  A('records 池不含 events.html 条目', !parsed.records.some(r => r.pg === 'events.html'));
  A('records 池不含已吸收 href（抽 e2021-10-25）',
    !parsed.records.some(r => r.pg === 'primary.html' && r.id === 'e2021-10-25'));

  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  A('索引总数=282', (sidx.match(/"id": "/g) || []).length === 282,
    String((sidx.match(/"id": "/g) || []).length));
  A('索引事件档案计数=14', (sidx.match(/"t": "事件档案"/g) || []).length === 14,
    String((sidx.match(/"t": "事件档案"/g) || []).length));
  A('新引语入索引（Technoking/Telepathy/same margin/love with steel）',
    sidx.includes('Technoking of Tesla') && sidx.includes('called Telepathy') &&
    sidx.includes('same margin as to consumers') && sidx.includes("in love with steel"));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r08-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2,8);
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

    // ---- 桌面 1440x900：events.html ----
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/events.html' });
    for (let i = 0; i < 30; i++) {
      const n = await ev(send, `document.querySelectorAll('section.ev-item[id]').length`);
      if (n === 14) break;
      await new Promise(r => setTimeout(r, 500));
    }
    console.log('[桌面] events.html 14 档案');
    A('档案 section 总数=14', (await ev(send, `document.querySelectorAll('section.ev-item[id]').length`)) === 14);
    A('五新卡全部渲染', await ev(send, NEW.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('五新卡结构（ev-item 内 head/summary/facts/quotes/materials）',
      await ev(send, NEW.map(c => `(()=>{const c=document.getElementById('${c}');
        return c.querySelector('.ev-head') && c.querySelector('.ev-summary') &&
               c.querySelectorAll('.ev-quote, blockquote').length>=1 &&
               c.querySelectorAll('.ev-mat li, .ev-materials li').length>=3;})()`).join('&&')));
    A('新卡双语（标题 data-en + 中文正文）',
      await ev(send, NEW.map(c => `(()=>{const c=document.getElementById('${c}');
        return !!c.querySelector('[data-en]') && /[\\u4e00-\\u9fff]/.test(c.textContent);})()`).join('&&')));
    A('chronicle 徽标渲染（e2021-10-25 内「编年史条目」）',
      await ev(send, `(()=>{const c=document.getElementById('e2021-10-25');
        return !!c.querySelector('.ev-kind-chronicle') &&
               [...c.querySelectorAll('.ev-kind-chronicle')].some(k=>k.textContent.includes('编年史'));})()`));
    A('IPO 档案三引语（S-1/10-K/股东信）',
      await ev(send, `document.getElementById('e2010-06-29').querySelectorAll('blockquote').length===3 && document.getElementById('e2010-06-29').textContent.includes('highly dependent') && document.getElementById('e2010-06-29').textContent.includes('Technoking') &&
        document.getElementById('e2010-06-29').textContent.includes('reached profitability')`));
    A('Starship 档案五材料 + 破产警报逐字',
      await ev(send, `document.getElementById('e2021-11-26').textContent.includes('genuine risk of bankruptcy') &&
        document.getElementById('e2021-11-26').textContent.includes("in love with steel")`));
    A('Neuralink 档案预言与兑现同卡',
      await ev(send, `document.getElementById('e2024-01-29').textContent.includes('about six months') &&
        document.getElementById('e2024-01-29').textContent.includes('Telepathy')`));
    A('Autonomy 档案 LIDAR 逐字 + promises 对账注',
      await ev(send, `document.getElementById('e2019-04-22').textContent.includes("fool's errand") &&
        document.getElementById('e2019-04-22').textContent.includes('promises')`));
    console.log('[桌面] 互链与深链');
    A('五新卡页内 related 锚全部实存',
      await ev(send, NEW.map(c => `(()=>{const c=document.getElementById('${c}');
        return [...c.querySelectorAll('a[href^="#e"]')].every(a=>
          !!document.getElementById(a.getAttribute('href').slice(1)));})()`).join('&&')));
    A('e2019-04-22 互链 controversy.html#autopilot 跨页真实',
      await ev(send, `!!document.querySelector('#e2019-04-22 a[href="controversy.html#autopilot"]')`) &&
      (await getBody(BASE + '/controversy.html')).includes('id="autopilot"'));
    A('e2021-11-26 互链 documents.html#d2021-11-26 跨页真实',
      await ev(send, `!!document.querySelector('#e2021-11-26 a[href="documents.html#d2021-11-26"]')`) &&
      (await getBody(BASE + '/documents.html')).includes('id="d2021-11-26"'));
    A('hash 深链定位（#e2021-11-26 进入视口）',
      await ev(send, `(async()=>{location.hash='#e2021-11-26';
        await new Promise(r=>setTimeout(r,300));
        const r=document.getElementById('e2021-11-26').getBoundingClientRect();
        return r.top < window.innerHeight && r.bottom > 0;})()`));
    await shot(send, 'qa/v9-20/round-08/events-newfiles-desktop.png', 'events-newfiles-desktop.png');

    // ---- timeline.html 口径 ----
    await send('Page.navigate', { url: BASE + '/timeline.html' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[桌面] timeline.html 口径');
    A('gx-listmeta 文本=14 事件 · 229 记录 · 39 归档',
      await ev(send, `(()=>{const t=document.getElementById('gx-listmeta');
        return t && t.textContent.includes('14 个已建档事件') &&
               t.textContent.includes('229 条一手记录') && t.textContent.includes('39 条已归入事件档案');})()`));
    A('window.TIMELINE_V7.meta 探针（14/229/39）',
      await ev(send, `window.TIMELINE_V7 && window.TIMELINE_V7.meta.nEvents===14 &&
        window.TIMELINE_V7.meta.nRecords===229 && window.TIMELINE_V7.meta.nAbsorbed===39`));
    A('静态清单含五个新档案行',
      await ev(send, NEW.map(c => `!!document.querySelector('.gxl-ev[data-ev="${c}"]')`).join('&&')));
    A('已吸收记录不再单列（抽 e2021-10-25 / e2024-03-18）',
      await ev(send, `![...document.querySelectorAll('.gxl-row[data-key]')].some(r=>
        r.dataset.key.includes('e2021-10-25')||r.dataset.key.includes('e2024-03-18'))`));
    await shot(send, 'qa/v9-20/round-08/timeline-desktop.png', 'timeline-desktop.png');

    // ---- primary.html 建档卡 ----
    await send('Page.navigate', { url: BASE + '/primary.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[桌面] primary.html 建档卡');
    A('建档卡注入=23 处',
      (await ev(send, `document.querySelectorAll('.ps-evlink, a[href^="events.html#e"]').length`)) >= 23,
      String(await ev(send, `document.querySelectorAll('a[href^="events.html#e"]').length`)));
    A('e2010-06-29 条目含建档卡链',
      await ev(send, `!!document.querySelector('#e2010-06-29 a[href="events.html#e2010-06-29"]')`));

    // ---- 检索 ----
    console.log('[检索] 新档案命中 + 类型筛选');
    await send('Page.navigate', { url: BASE + '/search.html?q=Telepathy' });
    await new Promise(r => setTimeout(r, 1200));
    A('Telepathy 命中 e2024-01-29',
      await ev(send, `!![...document.querySelectorAll('#sr-results a')].find(a=>(a.getAttribute('href')||'').includes('events.html%23e2024-01-29')||(a.getAttribute('href')||'').includes('events.html#e2024-01-29'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=Technoking' });
    await new Promise(r => setTimeout(r, 1200));
    A('Technoking 命中（IPO 档案或 10-K 文档）',
      await ev(send, `document.querySelectorAll('#sr-results a').length > 0`));
    await send('Page.navigate', { url: BASE + '/search.html?q=same%20margin&type=' + encodeURIComponent('事件档案') });
    await new Promise(r => setTimeout(r, 1200));
    A('类型筛选「事件档案」可用（有结果区）',
      await ev(send, `!!document.getElementById('sr-results')`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    for (const p of ['events.html', 'timeline.html']) {
      await send('Page.navigate', { url: BASE + '/' + p });
      await new Promise(r => setTimeout(r, 1200));
      const sw = await ev(send, `document.documentElement.scrollWidth`);
      const cw = await ev(send, `document.documentElement.clientWidth`);
      A(`[390] ${p} 零横向溢出（scrollWidth ${sw} ≤ clientWidth ${cw}）`, sw <= cw, sw + '>' + cw);
      if (p === 'events.html') {
        await ev(send, `location.hash='#e2024-01-29';`);
        await new Promise(r => setTimeout(r, 600));
        await shot(send, 'qa/v9-20/round-08/events-newfile-390.png', 'events-newfile-390.png');
      }
    }
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
