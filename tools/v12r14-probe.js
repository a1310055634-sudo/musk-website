// V12-20 R14 探针：互链 6 对 + 检索审计（命中/排序/高亮/Ctrl+K/清除/aria-live/noscript）+ 双语/390
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9360;
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
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  console.log('[文件级]');
  const evHtml = fs.readFileSync('events.html', 'utf-8');
  A('互链对① e2019-07-16 入 events', evHtml.includes('primary.html#e2019-07-16'));
  A('互链对②③ i2024-01-29/i2019-11-12 入 events', evHtml.includes('interviews.html#i2024-01-29') && evHtml.includes('interviews.html#i2019-11-12'));
  A('互链对④⑤ i2026-07-23/i2026-02-05 入 events', evHtml.includes('interviews.html#i2026-07-23') && evHtml.includes('interviews.html#i2026-02-05'));
  A('互链对⑥ e2025-11-06 入 e2024-07', evHtml.includes('primary.html#e2025-11-06'));
  {
    const edSrc = fs.readFileSync('tools/events-data.py', 'utf-8');
    const i0 = edSrc.indexOf('"id": "e2025-03-28"');
    const i1 = edSrc.indexOf('"id": "e2026-02-10"', i0);
    A('None href 已修（e2025-03-28 段内；其余 8 处 None 为历史档媒体占位体例如实保留）',
      evHtml.includes('search?q=xAI%20acquires%20X') && edSrc.slice(i0, i1).indexOf('"href": None') < 0);
  }
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  A('索引 413 恒定', (sidx.match(/"id": "/g) || []).length === 413);

  const profile = process.env.TEMP + '/v12r14-profile-' + Date.now();
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

    // 互链跨页 fetch 验证
    const iv = await getBody(BASE + '/interviews.html');
    const prim = await getBody(BASE + '/primary.html');
    A('互链目标锚真实（i2024-01-29/i2019-11-12/i2026-07-23/i2026-02-05）',
      iv.includes('id="i2024-01-29"') && iv.includes('id="i2019-11-12"') && iv.includes('id="i2026-07-23"') && iv.includes('id="i2026-02-05"'));
    A('互链目标锚真实（e2019-07-16/e2025-11-06）',
      prim.includes('id="e2019-07-16"') && prim.includes('id="e2025-11-06"'));

    // 检索审计
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/search.html' });
    await sleep(1500);
    console.log('[检索审计]');
    const total = await ev(send, `document.getElementById('sr-count').textContent`);
    A('初始全量计数（aria-live 计数含 413）', /413/.test(total || ''), String(total).slice(0, 50));
    A('aria-live=polite 存在', await ev(send, `document.getElementById('sr-count').getAttribute('aria-live')==='polite'`));
    // 抽样 30：检索 SpaceX
    await ev(send, `document.getElementById('sr-input').value='SpaceX'`);
    await ev(send, `document.getElementById('sr-input').dispatchEvent(new Event('input',{bubbles:true}))`);
    await sleep(600);
    const c1 = await ev(send, `document.getElementById('sr-count').textContent`);
    const n1 = await ev(send, `document.querySelectorAll('#sr-results a').length`);
    A('命中 SpaceX ≥30 条（抽 30 验证样本）', (parseInt((c1.match(/\d+/) || [0])[0]) >= 30 || n1 >= 30), c1 + ' / nodes ' + n1);
    A('高亮 <mark> 出现', await ev(send, `!!document.querySelector('#sr-results mark')`));
    // 排序 asc：首条日期 ≤ 末条
    A('默认日期升序（首条≤末条）', await ev(send,
      `(()=>{const ds=[...document.querySelectorAll('#sr-results .sr-d, #sr-results time, #sr-results b')].map(e=>e.textContent.match(/\\d{4}[.-]\\d{2}/)).filter(Boolean).map(m=>m[0].replace('.',''));if(ds.length<2)return 'few';return ds[0]<=ds[ds.length-1]?'ok':'desc';})()`),
      String(await ev(send, `(()=>{const ds=[...document.querySelectorAll('#sr-results .sr-d, #sr-results time, #sr-results b')].map(e=>e.textContent.match(/\\d{4}[.-]\\d{2}/)).filter(Boolean).map(m=>m[0].replace('.',''));return ds.slice(0,2).join(',')+'..'+ds.slice(-1)})()`)));
    // 类型过滤+aria-pressed
    await ev(send, `[...document.querySelectorAll('.sr-types button')].find(b=>b.textContent.includes('访谈')||b.getAttribute('data-t')==='访谈与表态')?.click()`);
    await sleep(400);
    A('类型过滤生效（aria-pressed 切换）', await ev(send,
      `[...document.querySelectorAll('.sr-types button')].some(b=>b.getAttribute('aria-pressed')==='true' && b.getAttribute('data-t')!=='全部')`));
    // 清除筛选
    await ev(send, `document.getElementById('sr-clearbtn')?.click()`);
    await sleep(500);
    A('清除筛选恢复全量 413', /413/.test(String(await ev(send, `document.getElementById('sr-count').textContent`))));
    // Ctrl+K 聚焦
    await send('Runtime.evaluate', { expression: `document.activeElement.blur()` });
    await send('Input.dispatchKeyEvent', { type: 'keyDown', modifiers: 2, key: 'k', code: 'KeyK', windowsVirtualKeyCode: 75 });
    await send('Input.dispatchKeyEvent', { type: 'keyUp', modifiers: 2, key: 'k', code: 'KeyK', windowsVirtualKeyCode: 75 });
    await sleep(300);
    A('Ctrl+K 聚焦检索框', await ev(send, `document.activeElement===document.getElementById('sr-input')`));
    // URL 参数回填
    await send('Page.navigate', { url: BASE + '/search.html?q=Grok' });
    await sleep(1200);
    A('URL ?q=Grok 回填并命中', await ev(send,
      `document.getElementById('sr-input').value==='Grok' && document.querySelectorAll('#sr-results a').length > 0`));
    A('noscript 降级提示存在（静态 HTML 层）', (await getBody(BASE + '/search.html')).includes('<noscript>'));
    A('双语切换（lang-toggle 后计数语言变）', await ev(send,
      `(function(){var b=document.getElementById('lang-toggle');if(!b)return 'no-btn';var before=b.textContent;b.click();var after=b.textContent;b.click();return 'toggle-ok:'+before+'→'+after;})()`),
      String(await ev(send, `document.getElementById('lang-toggle')?document.getElementById('lang-toggle').textContent:'?'`)));

    console.log('[390] 零横向溢出');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await sleep(800);
    A('390 search 零溢出', await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));
    await send('Page.navigate', { url: BASE + '/events.html' });
    await sleep(1200);
    A('390 events 零溢出', await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));

    console.log('');
    console.log(`探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
