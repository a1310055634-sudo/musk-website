// V12-20 R07 探针：六条新文档（email 2 + EDGAR 4）渲染/逐字/时序/互链/390
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9353;
const BASE = 'http://127.0.0.1:8766';
const NEW = ['d2018-08-12', 'd2022-03-26', 'd2025-09-17', 'd2026-01-29', 'd2026-06-12', 'd2026-06-22'];

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
  console.log('[文件级] search-index.js 与版本戳');
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  for (const cid of NEW) A(`索引含新条 ${cid}`, sidx.includes(`"id": "${cid}"`));
  A('索引一手文档计数=37', (sidx.match(/"t": "一手文档"/g) || []).length === 37,
    String((sidx.match(/"t": "一手文档"/g) || []).length));
  A('索引总条数=383', (sidx.match(/"id": "/g) || []).length === 383,
    String((sidx.match(/"id": "/g) || []).length));
  A('版本戳 11.8.0（app.js）', fs.readFileSync('app.js', 'utf-8').includes("SITE_VERSION = '11.8.0'"));

  const profile = process.env.TEMP + '/v12r07-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/documents.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] 结构与渲染');
    A('doc-article 总数=37', (await ev(send, `document.querySelectorAll('article.doc-article').length`)) === 37,
      String(await ev(send, `document.querySelectorAll('article.doc-article').length`)));
    A('六条全部渲染', await ev(send, NEW.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('六条五件套齐全（h2/doc-meta/blockquote/zh-line/note）',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        return e.querySelector('h2') && e.querySelector('.doc-meta') &&
               e.querySelector('blockquote') && e.querySelector('.zh-line') &&
               e.querySelector('.note');})()`).join('&&')));
    A('Permalink 一一对应',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        const a=e.querySelector('a.doc-badge[href]'); return a && a.getAttribute('href')==='#${c}';})()`).join('&&')));

    console.log('[桌面] 逐字与口径');
    A('PIF 短信逐字（throwing me under the bus / takes two to tango）', await ev(send,
      `document.querySelector('#d2018-08-12').textContent.includes('throwing me under the bus') && document.querySelector('#d2018-08-12').textContent.includes('takes two to tango')`));
    A('Dorsey 短信逐字（new platform is needed / open source protocol）', await ev(send,
      `document.querySelector('#d2022-03-26').textContent.includes('a new platform is needed') && document.querySelector('#d2022-03-26').textContent.includes('open source protocol')`));
    A('万亿薪酬包逐字（$2 trillion / $8.5 trillion）', await ev(send,
      `document.querySelector('#d2025-09-17').textContent.includes('$2 trillion') && document.querySelector('#d2025-09-17').textContent.includes('$8.5 trillion')`));
    A('10-K FY2025 逐字（Technoking / artificial intelligence）', await ev(send,
      `document.querySelector('#d2026-01-29').textContent.includes('Technoking of Tesla') && document.querySelector('#d2026-01-29').textContent.includes('bringing artificial intelligence')`));
    A('424B4 逐字（555,555,555 / $135.00 / SPCX）', await ev(send,
      `document.querySelector('#d2026-06-12').textContent.includes('555,555,555') && document.querySelector('#d2026-06-12').textContent.includes('135.00') && document.querySelector('#d2026-06-12').textContent.includes('SPCX')`));
    A('notes 8-K 逐字（5.350% / 6.650% Senior Notes due 2056）', await ev(send,
      `document.querySelector('#d2026-06-22').textContent.includes('5.350% Senior Notes due 2031') && document.querySelector('#d2026-06-22').textContent.includes('6.650% Senior Notes due 2056')`));
    A('六条双语（EN 引文 + 中文 CJK 对照）',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        const en=[...e.querySelectorAll('blockquote')].map(x=>x.textContent).join('');
        const zh=[...e.querySelectorAll('.zh-line')].map(x=>x.textContent).join('');
        return /[A-Za-z]/.test(en) && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));
    A('六条口径戳=2026-10-06 核验',
      await ev(send, NEW.map(c => `document.getElementById('${c}').textContent.includes('2026-10-06 核验')`).join('&&')));

    console.log('[桌面] 时序与互链');
    const ORDER = ['d2018-08-07', 'd2018-08-12', 'd2018-08-14', 'd2022-02-07', 'd2022-03-26', 'd2022-04-09',
      'd2025-09-01', 'd2025-09-17', 'd2026-01', 'd2026-01-29', 'd2026-06-12', 'd2026-06-22'];
    A('六条全部按全页时序归位（12 邻居链）', await ev(send,
      `(()=>{const ids=[...document.querySelectorAll('article.doc-article')].map(e=>e.id);
        for (let i = 0; i < ${JSON.stringify(ORDER)}.length - 1; i++) {
          const a = ids.indexOf(${JSON.stringify(ORDER)}[i]), b = ids.indexOf(${JSON.stringify(ORDER)}[i+1]);
          if (a < 0 || b < 0 || a >= b) return 'fail@' + ${JSON.stringify(ORDER)}[i];
        } return true;})()`),
      String(await ev(send, `(()=>{const ids=[...document.querySelectorAll('article.doc-article')].map(e=>e.id);
        const O=${JSON.stringify(ORDER)}; for (let i=0;i<O.length-1;i++){const a=ids.indexOf(O[i]),b=ids.indexOf(O[i+1]); if(a<0||b<0||a>=b) return 'fail@'+O[i];} return true;})()`)));
    const prim = await getBody(BASE + '/primary.html');
    A('互链目标 e2018-08-07 / e2022-03-26 / e2025-11-06 真实存在（primary.html）',
      prim.includes('id="e2018-08-07"') && prim.includes('id="e2022-03-26"') && prim.includes('id="e2025-11-06"'));
    A('d2026-06-12 → d2026-06-22 站内互链', await ev(send,
      `!!document.querySelector('#d2026-06-12 a[href="#d2026-06-22"]')`));

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
