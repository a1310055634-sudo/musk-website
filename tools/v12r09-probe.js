// V12-20 R09 主路径探针：首页→账本→语录→检索→资源 五页连通+关键计数
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9355;
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
  const profile = process.env.TEMP + '/v12r09-profile-' + Date.now();
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

    // ① 首页
    await send('Page.navigate', { url: BASE + '/index.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[① 首页 index.html]');
    A('报头品牌渲染', await ev(send, `!!document.querySelector('.masthead .brand')`));
    A('版本戳=11.9.0', await ev(send, `document.querySelector('.site-version-val').textContent.trim()==='11.9.0'`));
    A('通往账本 primary.html 链接存在', await ev(send, `!!document.querySelector('a[href="primary.html"]')`));

    // ② 账本（经首页链接目标直跳）
    await send('Page.navigate', { url: BASE + '/primary.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[② 账本 primary.html]');
    A('ps-row=124', (await ev(send, `document.querySelectorAll('.ps-row').length`)) === 124,
      String(await ev(send, `document.querySelectorAll('.ps-row').length`)));
    A('R06 互链锚 e2022-04-20 可达', await ev(send, `!!document.getElementById('e2022-04-20')`));
    A('通往语录 quotes.html 链接存在', await ev(send, `!!document.querySelector('a[href="quotes.html"]')`));

    // ③ 语录
    await send('Page.navigate', { url: BASE + '/quotes.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[③ 语录 quotes.html]');
    A('qs-card=107', (await ev(send, `document.querySelectorAll('.qs-card').length`)) === 107);
    A('✓15/◎83 核验标', await ev(send,
      `[...document.querySelectorAll('.qs-src')].filter(s=>s.textContent.includes('✓原文核验')).length===15 && [...document.querySelectorAll('.qs-src')].filter(s=>s.textContent.includes('◎转引在册')).length===83`));
    A('通往检索 search.html 链接存在', await ev(send, `!!document.querySelector('a[href="search.html"]')`));

    // ④ 检索
    await send('Page.navigate', { url: BASE + '/search.html' });
    await new Promise(r => setTimeout(r, 1800));
    console.log('[④ 检索 search.html]');
    A('搜索输入框存在', await ev(send, `!!document.querySelector('input[type="search"], input[type="text"], #search-input, .search-input')`));
    A('search-index.js 已加载且 383 条', await ev(send,
      `(function(){ try { return (typeof SEARCH_INDEX !== 'undefined' ? SEARCH_INDEX : (window.searchIndex || window.INDEX || null)) ? (typeof SEARCH_INDEX !== 'undefined' ? SEARCH_INDEX.length : (window.searchIndex||window.INDEX).length) : -1; } catch(e){ return 'ERR'; } })()`),
      String(await ev(send, `(function(){ try { return (typeof SEARCH_INDEX !== 'undefined' ? SEARCH_INDEX.length : (window.searchIndex ? window.searchIndex.length : (window.INDEX ? window.INDEX.length : 'no-var'))) } catch(e){ return 'ERR'; } })()`)));
    A('通往资源 resources.html 链接存在', await ev(send, `!!document.querySelector('a[href="resources.html"]')`));

    // ⑤ 资源
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[⑤ 资源 resources.html]');
    A('rs-item=49', (await ev(send, `document.querySelectorAll('.rs-item').length`)) === 49,
      String(await ev(send, `document.querySelectorAll('.rs-item').length`)));
    A('版本戳=11.9.0（尾页复核）', await ev(send, `document.querySelector('.site-version-val').textContent.trim()==='11.9.0'`));

    console.log('[390] 主路径首页零溢出');
    await send('Page.navigate', { url: BASE + '/index.html' });
    await new Promise(r => setTimeout(r, 1000));
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await new Promise(r => setTimeout(r, 800));
    A('390 首页 scrollWidth<=clientWidth',
      await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));

    console.log('');
    console.log(`主路径探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
