// V12-20 R05 探针：四场 2026 访谈 渲染/Permalink/双语/逐字/互链/390
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9351;
const BASE = 'http://127.0.0.1:8766';
const NEW = ['i2026-01-06', 'i2026-01-22', 'i2026-02-05', 'i2026-07-23'];

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
  for (const cid of NEW) A(`索引含新场 ${cid}`, sidx.includes(`"id": "${cid}"`));
  A('索引访谈计数=51', (sidx.match(/"t": "访谈与表态"/g) || []).length === 51,
    String((sidx.match(/"t": "访谈与表态"/g) || []).length));
  A('四场逐字句入索引',
    sidx.includes('Grok keeps updating') &&
    sidx.includes('largest flying machine ever made') &&
    sidx.includes('digital and physical intelligence'));

  const profile = process.env.TEMP + '/v12r05-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/interviews.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] 结构与渲染');
    A('iv-item 总数=52（51 带 id + 1 legacy 无 id）',
      (await ev(send, `document.querySelectorAll('article.iv-item').length`)) === 52);
    A('带 id 条目=51', (await ev(send, `[...document.querySelectorAll('article.iv-item')].filter(e=>e.id).length`)) === 51);
    A('四场全部渲染', await ev(send, NEW.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('四场六件套齐全（h2/iv-meta/ctx/blockquote/iv-zh/after）',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        return e.querySelector('h2') && e.querySelector('.iv-meta') && e.querySelector('.ctx') &&
               e.querySelector('blockquote') && e.querySelector('.iv-zh') && e.querySelector('.after');})()`).join('&&')));
    A('Permalink 一一对应',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        const a=e.querySelector('a.iv-badge[href]'); return a && a.getAttribute('href')==='#${c}';})()`).join('&&')));

    console.log('[桌面] 逐字与双语');
    A('Moonshots 场逐字（Grok keeps updating）', await ev(send,
      `document.querySelector('#i2026-01-06 blockquote').textContent.includes('Grok keeps updating')`));
    A('Davos 场逐字（largest flying machine）', await ev(send,
      `document.querySelector('#i2026-01-22 blockquote').textContent.includes('largest flying machine ever made')`));
    A('Dwarkesh 场逐字（AI5/Optimus）', await ev(send,
      `document.querySelector('#i2026-02-05 blockquote').textContent.includes('AI5 chip is going into our Optimus robot')`));
    A('Economist 场逐字（digital and physical intelligence）', await ev(send,
      `document.querySelector('#i2026-07-23 blockquote').textContent.includes('digital and physical intelligence')`));
    A('四场双语（EN 引文 + 中文 CJK 对照）',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        const en=e.querySelector('blockquote').textContent, zh=e.querySelector('.iv-zh').textContent;
        return /[A-Za-z]/.test(en) && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));

    console.log('[桌面] 互链');
    A('跨页互链真实存在（grok/x-posts/ai-strategy/deep-dive-05）',
      (await getBody(BASE + '/x-posts.html')).includes('id="p2026-09-14"') &&
      (await getBody(BASE + '/grok.html')).length > 1000 &&
      (await getBody(BASE + '/ai-strategy.html')).length > 1000 &&
      (await getBody(BASE + '/deep-dive-05.html')).includes('Deep Dive'));

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
