// V12-20 R06 探针：四条 email 双源新文档 渲染/Permalink/双语/逐字/互链/390
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9352;
const BASE = 'http://127.0.0.1:8766';
const NEW = ['d2022-04-20', 'd2022-11-09', 'd2023-01', 'd2023-02'];

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
  A('索引一手文档计数=31', (sidx.match(/"t": "一手文档"/g) || []).length === 31,
    String((sidx.match(/"t": "一手文档"/g) || []).length));
  A('索引总条数=377', (sidx.match(/"id": "/g) || []).length === 377,
    String((sidx.match(/"id": "/g) || []).length));
  A('版本戳 11.7.0（app.js）', fs.readFileSync('app.js', 'utf-8').includes("SITE_VERSION = '11.7.0'"));

  const profile = process.env.TEMP + '/v12r06-profile-' + Date.now();
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
    A('doc-article 总数=31', (await ev(send, `document.querySelectorAll('article.doc-article').length`)) === 31,
      String(await ev(send, `document.querySelectorAll('article.doc-article').length`)));
    A('四条全部渲染', await ev(send, NEW.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('四条五件套齐全（h2/doc-meta/blockquote/zh-line 或 note）',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        return e.querySelector('h2') && e.querySelector('.doc-meta') &&
               e.querySelector('blockquote') && e.querySelector('.zh-line') &&
               e.querySelector('.note');})()`).join('&&')));
    A('Permalink 一一对应',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        const a=e.querySelector('a.doc-badge[href]'); return a && a.getAttribute('href')==='#${c}';})()`).join('&&')));
    A('页面定制 doc-foot 存在（本页历史上无站点页脚版本戳，以 doc-foot 为页尾结构）',
      await ev(send, `!!document.querySelector('.doc-foot')`));

    console.log('[桌面] 逐字与口径');
    A('Ellison 四行短信逐字（A billion … or whatever you recommend）', await ev(send,
      `document.querySelector('#d2022-04-20').textContent.includes('A billion') && document.querySelector('#d2022-04-20').textContent.includes('or whatever you recommend')`));
    A('首封全员信逐字（no longer allowed / 40 hours per week）', await ev(send,
      `document.querySelector('#d2022-11-09').textContent.includes('Remote work is no longer allowed') && document.querySelector('#d2022-11-09').textContent.includes('40 hours per week')`));
    A('bait and switch 逐字 + 庭审追述口径标注', await ev(send,
      `document.querySelector('#d2023-01').textContent.includes('This is a bait and switch') && document.querySelector('#d2023-01').textContent.includes('庭审宣誓作证的当场追述')`));
    A('my-hero 逐字（my hero / civilization）+ 解封口径', await ev(send,
      `document.querySelector('#d2023-02').textContent.includes('my hero') && document.querySelector('#d2023-02').textContent.includes('The fate of civilization is at stake')`));
    A('四条双语（EN 引文 + 中文 CJK 对照）',
      await ev(send, NEW.map(c => `(()=>{const e=document.getElementById('${c}');
        const en=e.querySelector('blockquote').textContent;
        const zh=[...e.querySelectorAll('.zh-line')].map(x=>x.textContent).join('');
        return /[A-Za-z]/.test(en) && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));
    A('四条口径戳=2026-10-06 核验',
      await ev(send, NEW.map(c => `document.getElementById('${c}').textContent.includes('2026-10-06 核验')`).join('&&')));

    console.log('[桌面] 时序与互链');
    A('2022-04 段时序正确（04-11 → 04-20 → 04-25）', await ev(send,
      `(()=>{const ids=[...document.querySelectorAll('article.doc-article')].map(e=>e.id);
        return ids.indexOf('d2022-04-11') < ids.indexOf('d2022-04-20') && ids.indexOf('d2022-04-20') < ids.indexOf('d2022-04-25');})()`));
    A('2022-11 段时序正确（10-27 → 11-09 → 11-16）', await ev(send,
      `(()=>{const ids=[...document.querySelectorAll('article.doc-article')].map(e=>e.id);
        return ids.indexOf('d2022-10-27') < ids.indexOf('d2022-11-09') && ids.indexOf('d2022-11-09') < ids.indexOf('d2022-11-16');})()`));
    A('2023 段时序正确（11-16 → 2023-01 → 2023-02 → 2023-04-05）', await ev(send,
      `(()=>{const ids=[...document.querySelectorAll('article.doc-article')].map(e=>e.id);
        return ids.indexOf('d2022-11-16') < ids.indexOf('d2023-01') && ids.indexOf('d2023-01') < ids.indexOf('d2023-02') && ids.indexOf('d2023-02') < ids.indexOf('d2023-04-05');})()`));
    const prim = await getBody(BASE + '/primary.html');
    A('互链目标 e2022-04-20 真实存在（primary.html）', prim.includes('id="e2022-04-20"'));
    A('d2023-01 → d2023-02 站内互链', await ev(send,
      `!!document.querySelector('#d2023-01 a[href="#d2023-02"]')`));

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
