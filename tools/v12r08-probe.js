// V12-20 R08 探针：quotes.html 核验标/口径段/卡数恒定/390
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9354;
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
    req.on('timeout', () => req.destroy(new Error('timeout')));
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
  return (method, params) => new Promise((res, rej) => {
    const mid = ++id; pending.set(mid, { res, rej });
    client.send(JSON.stringify({ id: mid, method, params }));
  });
}
const ev = (send, expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true })
  .then(r => r.result.value);

async function main() {
  console.log('[文件级] TSV 与版本戳');
  const tsv = fs.readFileSync('qa/v12/round-01/quotes-worklog.tsv', 'utf-8').trim().split('\n');
  A('TSV 数据行 101（+1 header = 102）', tsv.length === 102, String(tsv.length));
  A('TSV verdict 全非空', tsv.slice(1).every(l => { const p = l.split('\t'); return p[3] && p[3].trim(); }));
  const yesRows = tsv.slice(1).filter(l => l.split('\t')[3].indexOf('✅') === 0).length;
  const trRows = tsv.slice(1).filter(l => l.split('\t')[3].indexOf('⚠️') === 0).length;
  A('TSV 三态分布 ✅15/⚠️86（含 e2023-11-30 双行）/❌0', yesRows === 15 && trRows === 86, '✅' + yesRows + '/⚠️' + trRows);
  A('✅ 行 anchor_url 全非空', tsv.slice(1).every(l => {
    const p = l.split('\t'); return p[3].indexOf('✅') !== 0 || (p[4] && p[4].trim());
  }));
  A('版本戳 11.9.0（app.js）', fs.readFileSync('app.js', 'utf-8').includes("SITE_VERSION = '11.9.0'"));

  const profile = process.env.TEMP + '/v12r08-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/quotes.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] 卡与核验标');
    A('qs-card 总数=107（恒定）', (await ev(send, `document.querySelectorAll('.qs-card').length`)) === 107,
      String(await ev(send, `document.querySelectorAll('.qs-card').length`)));
    A('✓原文核验标=15', (await ev(send, `[...document.querySelectorAll('.qs-src')].filter(s=>s.textContent.includes('✓原文核验')).length`)) === 15,
      String(await ev(send, `[...document.querySelectorAll('.qs-src')].filter(s=>s.textContent.includes('✓原文核验')).length`)));
    A('◎转引在册标=83', (await ev(send, `[...document.querySelectorAll('.qs-src')].filter(s=>s.textContent.includes('◎转引在册')).length`)) === 83,
      String(await ev(send, `[...document.querySelectorAll('.qs-src')].filter(s=>s.textContent.includes('◎转引在册')).length`)));
    A('✓ 卡 title 悬停含原文锚', await ev(send,
      `[...document.querySelectorAll('.qs-src[title]')].filter(s=>s.title.indexOf('R08 2026-10-06 原文锚:')===0 && s.title.includes('http')).length === 15`));
    A('✓ 抽样锚示例（e2016-05-04 → stockanalysis 23974）', await ev(send,
      `[...document.querySelectorAll('.qs-card')].find(c=>c.getAttribute('href')==='#e2016-05-04' || c.getAttribute('href').endsWith('#e2016-05-04')).querySelector('.qs-src').title.includes('stockanalysis.com/stocks/tsla/transcripts/23974-q1-2016')`));
    A('口径段上屏（引语核验口径 2026-10-06 R08）', await ev(send,
      `[...document.querySelectorAll('p')].some(p=>p.textContent.includes('引语核验口径（2026-10-06 R08）') && p.textContent.includes('✅ 原文核验 15 条') && p.textContent.includes('❌ 撤下 0 条'))`));
    A('口径段含底册路径', await ev(send,
      `[...document.querySelectorAll('p')].some(p=>p.textContent.includes('qa/v12/round-08/'))`));
    A('390 视口 scrollWidth<=clientWidth（桌面先测 1440）',
      await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));

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
