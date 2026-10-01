// V10-15 N03：双语卡 EN/ZH 对齐探针（quotes+primary）+ 声明上站断言
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9385;
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
  const profile = process.env.TEMP + '/v10n03-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'], { stdio: 'ignore' });
  try {
    let targets;
    for (let i = 0; i < 60; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
    }
    if (!targets || !targets.length) throw new Error('CDP 无响应');
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable');
    await send('Runtime.enable');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });

    // ---- quotes.html 双语对齐（全卡遍历）----
    console.log('[双语] quotes.html 103 卡 EN/ZH 对齐');
    await send('Page.navigate', { url: BASE + '/quotes.html' });
    await new Promise(r => setTimeout(r, 1800));
    const q = await ev(send, `(()=>{
      const cards=[...document.querySelectorAll('.qs-card')];
      let both=0, enOnly=0;
      for(const c of cards){
        const en=c.querySelector('.qs-en'), zh=c.querySelector('.qs-zh');
        if(en&&zh&&en.textContent.trim().length>10&&zh.textContent.trim().length>10) both++;
        else if(en&&!zh) enOnly++;
      }
      return JSON.stringify({cards:cards.length, both, enOnly});})()`);
    const qd = JSON.parse(q);
    A(`quotes ${qd.cards} 卡中 ${qd.both} 卡 EN/ZH 双语齐备（enOnly=${qd.enOnly}）`,
      qd.cards === 103 && qd.both >= 100, q);
    A('EN 切换：quotes 卡区仍渲染（app.js 整卡替换不塌）',
      await ev(send, `(()=>{document.getElementById('lang-toggle').click();
        const n=document.querySelectorAll('.qs-card').length;
        document.getElementById('lang-toggle').click();
        return n===103;})()`));

    // ---- primary.html 双语对齐（抽样 20 行）----
    console.log('[双语] primary.html 账本行抽样');
    await send('Page.navigate', { url: BASE + '/primary.html' });
    await new Promise(r => setTimeout(r, 1800));
    const p = await ev(send, `(()=>{
      const rows=[...document.querySelectorAll('.ps-row')].filter((_,i)=>i%5===0).slice(0,20);
      let ok=0, noQuote=0;
      for(const r of rows){
        const quote=r.querySelector('.ps-quote'), zh=r.querySelector('.ps-zh');
        if(quote){ if(zh&&zh.textContent.trim().length>10) ok++; }
        else noQuote++;
      }
      return JSON.stringify({sampled:rows.length, ok, noQuote});})()`);
    const pd = JSON.parse(p);
    A(`primary 抽样 ${pd.sampled} 行：含引文块者 ${pd.ok} 行 100% 配译文；无引语行 ${pd.noQuote}（SolarCity 两案无本人逐字引语，如实设计）`, pd.ok + pd.noQuote === pd.sampled && pd.ok >= 15, p);

    // ---- 声明上站断言 ----
    console.log('[声明] 引语复核声明');
    A('primary.html：复核声明在册（双语+覆盖口径）',
      await ev(send, `(()=>{const el=document.getElementById('quote-review-statement');
        return !!el && el.getAttribute('data-en').length > 60;})()`));
    await send('Page.navigate', { url: BASE + '/quotes.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('quotes.html：复核声明在册',
      await ev(send, `!!document.getElementById('quote-review-statement')`));
    A('声明 EN 切换生效',
      await ev(send, `(()=>{const el=document.getElementById('quote-review-statement');
        const zh=el.textContent.trim();
        document.getElementById('lang-toggle').click();
        const en=el.textContent.trim();
        document.getElementById('lang-toggle').click();
        return zh!==en && en.length>40;})()`));
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
