// V9-20 R06 探针：documents.html 四张新卡渲染/结构五件套/Permalink 18/双语/互链/无溢出 + 检索命中
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9339;  // 9227 aDrive 占用；9333-9338 为此前轮次用过（防残留）
const BASE = 'http://127.0.0.1:8766';
const NEW_CARDS = ['d2010-01-29', 'd2010-05-04', 'd2021-11-26', 'd2022-02-07'];

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
  for (const cid of NEW_CARDS) A(`索引含新文档 ${cid}`, sidx.includes(`"id": "${cid}"`));
  A('索引一手文档计数=18',
    (sidx.match(/"t": "一手文档"/g) || []).length === 18,
    String((sidx.match(/"t": "一手文档"/g) || []).length));
  A('索引总数=271', (sidx.match(/"id": "/g) || []).length === 271,
    String((sidx.match(/"id": "/g) || []).length));
  A('四卡逐字句入索引',
    sidx.includes('intentionally departed from the traditional automotive industry model') &&
    sidx.includes('There is a creeping tendency to use made up acronyms') &&
    sidx.includes('the Raptor production crisis is much worse') &&
    sidx.includes('Technoking of Tesla and our Chief Executive Officer'));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r06-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/documents.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] 结构与渲染');
    A('带 id 文档总数=18', (await ev(send, `document.querySelectorAll('.doc-article[id]').length`)) === 18);
    A('四份新文档全部渲染',
      await ev(send, NEW_CARDS.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('新卡五件套（h2/doc-meta/zh-line/note 各≥1）',
      await ev(send, NEW_CARDS.map(c => `(()=>{const c=document.getElementById('${c}');
        return c && c.querySelector('h2') && c.querySelector('.doc-meta') &&
               c.querySelectorAll('.zh-line').length>=1 && c.querySelectorAll('.note').length>=1;})()`).join('&&')));
    A('新卡至少两个 blockquote（多段摘录）',
      await ev(send, NEW_CARDS.map(c => `document.querySelectorAll('#${c} blockquote').length>=2`).join('&&')));
    A('Permalink 一一对应（18/18）',
      await ev(send, `[...document.querySelectorAll('.doc-article[id]')].every(c => {
        const badges=[...c.querySelectorAll('a.doc-badge')];
        return badges.some(b=>b.getAttribute('href')==='#'+c.id); })`));

    console.log('[桌面] 四卡逐字（源=EDGAR 原文/镜像 email 底本+二源转载）');
    A('S-1 卡逐字（总纲+关键人+赤字）',
      await ev(send, `(()=>{const b=[...document.querySelectorAll('#d2010-01-29 blockquote')].map(x=>x.textContent).join('\\n');
        return b.includes('intentionally departed from the traditional automotive industry model') &&
               b.includes('highly dependent on the services of Elon Musk, our Chief Executive Officer, Product Architect and Chairman') &&
               b.includes('accumulated deficit of $236.4 million');})()`));
    A('Acronyms 卡逐字（禁令+词表+Tripod）',
      await ev(send, `(()=>{const b=[...document.querySelectorAll('#d2010-05-04 blockquote')].map(x=>x.textContent).join('\\n');
        return b.includes('Excessive use of made up acronyms is a significant impediment to communication') &&
               b.includes('it should not enter the SpaceX glossary') &&
               b.includes("the bloody acronym version actually takes longer to say than the name");})()`));
    A('Raptor 卡逐字（crisis+bankruptcy+flight rate）',
      await ev(send, `(()=>{const b=[...document.querySelectorAll('#d2021-11-26 blockquote')].map(x=>x.textContent).join('\\n');
        return b.includes('There is no way to sugarcoat this') &&
               b.includes('a genuine risk of bankruptcy') &&
               b.includes('at least once every two weeks next year');})()`));
    A('10-K 卡逐字（Technoking+无固定期限）',
      await ev(send, `(()=>{const b=[...document.querySelectorAll('#d2022-02-07 blockquote')].map(x=>x.textContent).join('\\n');
        return b.includes('Technoking of Tesla and our Chief Executive Officer') &&
               b.includes('None of our key employees is bound by an employment agreement for any specific term');})()`));
    A('doc-path 口径升级（十八份/eighteen documents）',
      await ev(send, `(()=>{const p=document.querySelector('.doc-path p');
        return /十八份/.test(p.textContent) && /eighteen documents/.test(p.getAttribute('data-en')||'');})()`));
    A('四卡双语（zh-line 中文 + badge/标题英文原文）',
      await ev(send, NEW_CARDS.map(c => `(()=>{const c=document.getElementById('${c}');
        const zh=[...c.querySelectorAll('.zh-line')].map(x=>x.textContent).join('');
        return /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));

    console.log('[桌面] 互链与锚完整性');
    A('全页 #d… 锚零缺失',
      await ev(send, `[...document.querySelectorAll('a[href^="#d"]')].every(a =>
        !!document.getElementById(a.getAttribute('href').slice(1)))`));
    A('全页 #e…/跨页锚零缺失',
      await ev(send, `[...document.querySelectorAll('a[href^="#e"]')].every(a =>
        !!document.getElementById(a.getAttribute('href').slice(1)))`));
    A('S-1 卡互链 primary.html#e2010-06-29 真实存在',
      await ev(send, `!!document.querySelector('#d2010-01-29 a[href="primary.html#e2010-06-29"]')`) &&
      (await getBody(BASE + '/primary.html')).includes('id="e2010-06-29"'));
    A('Raptor 卡互链 primary.html#e2019-09-28 与 x-posts.html#p2024-10-13 真实存在',
      await ev(send, `!!document.querySelector('#d2021-11-26 a[href="primary.html#e2019-09-28"]') &&
        !!document.querySelector('#d2021-11-26 a[href="x-posts.html#p2024-10-13"]')`) &&
      (await getBody(BASE + '/primary.html')).includes('id="e2019-09-28"') &&
      (await getBody(BASE + '/x-posts.html')).includes('id="p2024-10-13"'));
    A('Acronyms 卡互链 interviews.html#i2021-07-30 真实存在',
      await ev(send, `!!document.querySelector('#d2010-05-04 a[href="interviews.html#i2021-07-30"]')`) &&
      (await getBody(BASE + '/interviews.html')).includes('id="i2021-07-30"'));
    A('10-K 卡互链 d2024-04-29/d2022-10-27 页内存在',
      await ev(send, `!!document.querySelector('#d2022-02-07 a[href="#d2024-04-29"]') &&
        !!document.querySelector('#d2022-02-07 a[href="#d2022-10-27"]')`));
    A('reading.html 计数同步（十八份）',
      (await getBody(BASE + '/reading.html')).includes('十八份一手文档'));

    // ---- 检索命中 ----
    console.log('[检索] q=Technoking / q=acronyms / 回归 q=funding secured');
    await send('Page.navigate', { url: BASE + '/search.html?q=Technoking' });
    await new Promise(r => setTimeout(r, 1200));
    A('Technoking 命中含 d2022-02-07',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('d2022-02-07'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=acronyms' });
    await new Promise(r => setTimeout(r, 1200));
    A('acronyms 命中含 d2010-05-04',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('d2010-05-04'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=Raptor' });
    await new Promise(r => setTimeout(r, 1200));
    A('Raptor 命中含 d2021-11-26',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('d2021-11-26'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=wild%20swings' });
    await new Promise(r => setTimeout(r, 1200));
    A('存量回归：wild swings 命中不回退（d2018-08-07）',
      await ev(send, `!![...document.querySelectorAll('#sr-results .sr-item')].find(a=>(a.getAttribute('href')||'').includes('d2018-08-07'))`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/documents.html' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[390] 溢出');
    const sw = await ev(send, `document.documentElement.scrollWidth`);
    A('scrollWidth≤390（零横向溢出）', sw <= 390, 'scrollWidth=' + sw);
    A('四份新文档 390 可见且无内部溢出',
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
