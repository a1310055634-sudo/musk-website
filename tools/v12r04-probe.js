// V12-20 R04 探针：账本五条早期加密 渲染/时序邻居/Permalink/双语/引语计数不变 + 390
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9349;
const BASE = 'http://127.0.0.1:8766';
const NEW = ['e2002-05', 'e2004', 'e2008-12-23', 'e2009-05-19', 'e2010-05-20'];

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
  for (const cid of NEW) A(`索引含新条 ${cid}`, sidx.includes(`"id": "${cid}"`));
  A('索引言行实录计数=124', (sidx.match(/"t": "言行实录"/g) || []).length === 124,
    String((sidx.match(/"t": "言行实录"/g) || []).length));
  A('424B4 官方陈述句入索引（since May 2002 / since April 2004）',
    sidx.includes('since May 2002') && sidx.includes('since April 2004'));

  const profile = process.env.TEMP + '/v12r04-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/primary.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] 结构与渲染');
    A('账本条目总数=124', (await ev(send, `document.querySelectorAll('.ps-row').length`)) === 124);
    A('五条全部渲染', await ev(send, NEW.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('五条 Permalink 一一对应',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        const a=e.querySelector('a.ps-date'); return a && a.getAttribute('href')==='#${c}';})()`).join('&&')));
    A('五条双语（data-en 存在 + 中文 CJK）',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        const p=e.querySelector('.ps-sec p');
        return p.hasAttribute('data-en') && /[\\u4e00-\\u9fff]/.test(p.textContent);})()`).join('&&')));
    A('新条无引语（ps-quote 全页计数=115 不变）',
      (await ev(send, `document.querySelectorAll('.ps-quote').length`)) === 115);

    console.log('[桌面] 时序邻居与锚文');
    const before = id => `(()=>{let n=document.getElementById('${id}').previousElementSibling;
      while(n && !(n.id||'').startsWith('e')) n=n.previousElementSibling;
      return n ? n.id : 'NONE';})()`;
    A('e2002-05 在 e2002-10-03 前', (await ev(send, before('e2002-10-03'))) === 'e2002-05');
    A('e2004 在 e2006 前', (await ev(send, before('e2006'))) === 'e2004');
    A('e2008-12-23 在 e2008-12-24 前', (await ev(send, before('e2008-12-24'))) === 'e2008-12-23');
    A('e2010-05-20 在 e2010-06-29 前', (await ev(send, before('e2010-06-29'))) === 'e2010-05-20');
    A('CRS-1 条文含 $1.6 billion/12 flights', await ev(send,
      `(()=>{const t=document.getElementById('e2008-12-23').textContent;
        return t.includes('$1.6') || t.includes('16 亿');})()`));
    A('Daimler 条含 Blackstar Investco', await ev(send,
      `document.getElementById('e2009-05-19').textContent.includes('Blackstar Investco')`));
    A('SpaceX 条含 since May 2002 官方陈述（data-en 属性）', await ev(send,
      `(()=>{const e=document.getElementById('e2002-05');
        const en=[...e.querySelectorAll('[data-en]')].map(p=>p.getAttribute('data-en')).join(' ');
        return en.includes('since May 2002');})()`));

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
