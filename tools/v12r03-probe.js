// V12-20 R03 探针：四张早期加密卡 渲染/时序/年份组/互链/双语/390 + 检索命中
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9347;
const BASE = 'http://127.0.0.1:8766';
const NEW = ['p2018-09-18', 'p2018-10-04', 'p2019-07-26', 'p2019-11-23'];

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
  for (const cid of NEW) A(`索引含新帖 ${cid}`, sidx.includes(`"id": "${cid}"`));
  A('索引 X 帖计数=44', (sidx.match(/"t": "X 帖"/g) || []).length === 44,
    String((sidx.match(/"t": "X 帖"/g) || []).length));
  A('三逐字句入索引（Water towers / Shortseller Enrichment / 146k Cybertruck）',
    sidx.includes('Water towers *can* fly') &&
    sidx.includes('Shortseller Enrichment Commission') &&
    sidx.includes('146k Cybertruck orders'));

  const profile = process.env.TEMP + '/v12r03-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/x-posts.html' });
    await new Promise(r => setTimeout(r, 1500));

    console.log('[桌面] 结构与渲染');
    A('卡总数=44', (await ev(send, `document.querySelectorAll('.tweet-card').length`)) === 44);
    A('四张新卡全部渲染', await ev(send, NEW.map(c => `!!document.getElementById('${c}')`).join('&&')));
    A('全卡时序升序',
      await ev(send, `(() => { const ids=[...document.querySelectorAll('.tweet-card')].map(e=>e.id);
        const k=s=>s.slice(1).split('-').map(Number); for(let i=1;i<ids.length;i++){const a=k(ids[i-1]),b=k(ids[i]);
        if(a[0]>b[0]||(a[0]==b[0]&&(a[1]>b[1]||(a[1]==b[1]&&a[2]>b[2]))))return false;} return true; })()`));
    A('Permalink 一一对应（44/44）',
      await ev(send, `[...document.querySelectorAll('.tweet-card')].every(c =>
        c.querySelector('a.tweet-date') && c.querySelector('a.tweet-date').getAttribute('href')==='#'+c.id)`));

    console.log('[桌面] 新卡逐字与双语');
    A('碳纤维段卡逐字（typo 弯引号保留）',
      await ev(send, `document.querySelector('#p2018-09-18 .tweet-text').textContent.includes('made of a new carbon fiber material')`));
    A('SEC 卡两连发逐字（typo 原样：漏 say）',
      await ev(send, `(()=>{const t=document.querySelector('#p2018-10-04 .tweet-text').textContent;
        return t.includes('Just want to that the Shortseller Enrichment Commission') &&
               t.includes('Sorry about the typo. That was unforgivable');})()`));
    A('水塔卡逐字（*can* 星号保留）',
      await ev(send, `document.querySelector('#p2019-07-26 .tweet-text').textContent === 'Starhopper flight successful. Water towers *can* fly haha!!'`));
    A('Cybertruck 卡两连发逐字',
      await ev(send, `(()=>{const t=document.querySelector('#p2019-11-23 .tweet-text').textContent;
        return t.includes('146k Cybertruck orders so far, with 42% choosing dual') &&
               t.includes('With no advertising & no paid endorsement');})()`));
    A('四新卡双语（EN 原文 + 中文 CJK）',
      await ev(send, NEW.map(c => `(()=>{const c=document.getElementById('${c}');
        const en=c.querySelector('.tweet-text').textContent, zh=c.querySelector('.tweet-zh').textContent;
        return /[A-Za-z]/.test(en) && /[\\u4e00-\\u9fff]/.test(zh);})()`).join('&&')));

    console.log('[桌面] 年份分组与互链');
    const yrFor = id => `(()=>{let n=document.getElementById('${id}').previousElementSibling;
      while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
      return n ? n.textContent.trim() : 'NONE';})()`;
    A('p2018-09-18 / p2018-10-04 归 2018 组',
      (await ev(send, yrFor('p2018-09-18'))) === '2018' && (await ev(send, yrFor('p2018-10-04'))) === '2018');
    A('p2019-07-26 / p2019-11-23 归 2019 组',
      (await ev(send, yrFor('p2019-07-26'))) === '2019' && (await ev(send, yrFor('p2019-11-23'))) === '2019');
    A('2019 组卡序完整（7 张含三新卡）',
      JSON.stringify(await ev(send, `(()=>{let n=document.getElementById('p2019-03-14').previousElementSibling;
        while(n && !n.classList.contains('xp-year')) n=n.previousElementSibling;
        const ids=[]; n=n.nextElementSibling;
        while(n && !n.classList.contains('xp-year')){ if(n.classList.contains('tweet-card')) ids.push(n.id); n=n.nextElementSibling;}
        return ids;})()`)) === JSON.stringify(['p2019-03-14', 'p2019-05-25', 'p2019-07-26', 'p2019-11-21', 'p2019-11-23']));
    A('互链：funding secured / Starhopper→05-25 / 大锤→11-23',
      await ev(send, `!!document.querySelector('#p2018-10-04 a[href="#p2018-08-07"]') &&
        !!document.querySelector('#p2019-07-26 a[href="#p2019-05-25"]') &&
        !!document.querySelector('#p2019-11-23 a[href="#p2019-11-21"]') &&
        !!document.querySelector('#p2018-09-18 a[href="#p2019-07-26"]')`));

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
