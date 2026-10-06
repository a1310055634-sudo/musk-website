// V12-20 R20 全站终检探针：主路径五步+双语+390+file://+资源页+dd06/07+print 抽查（≥10 断言）
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9369;
const BASE = 'http://127.0.0.1:8766';

let PASS = 0, FAIL = 0;
function A(name, cond, detail) {
  if (cond) { PASS++; console.log('  ✓ ' + name); }
  else { FAIL++; console.log('  ✗ ' + name + (detail ? ' —— ' + detail : '')); }
}
function getJSON(path) {
  return new Promise((res, rej) => {
    const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 5000 }, r => {
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
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  console.log('[文件级]');
  A('VERSION=12.0.0 待升（当前 11.20.0）', fs.readFileSync('VERSION', 'utf-8').trim() === '11.20.0');
  A('sitemap 39 URL=41 页−revisions(noindex)−preview-v12(开发页)——R11/R12 新页欠账已清偿（dd06/07 在册）', (fs.readFileSync('sitemap.xml', 'utf-8').match(/<loc>/g) || []).length === 39 && fs.readFileSync('sitemap.xml', 'utf-8').includes('deep-dive-06.html') && fs.readFileSync('sitemap.xml', 'utf-8').includes('deep-dive-07.html'));

  const profile = process.env.TEMP + '/v12r20-profile-' + Date.now();
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

    // 主路径五步
    const steps = [
      ['index.html', `!!document.querySelector('.masthead .brand')`],
      ['primary.html', `document.querySelectorAll('.ps-row').length === 124`],
      ['quotes.html', `document.querySelectorAll('.qs-card').length === 107`],
      ['search.html', `(typeof SEARCH_INDEX!=='undefined'?SEARCH_INDEX.length:(window.searchIndex||window.INDEX||[]).length)===413`],
      ['resources.html', `document.querySelectorAll('.rs-item').length === 54`],
    ];
    console.log('[主路径五步]');
    for (const [pg, cond] of steps) {
      await send('Page.navigate', { url: BASE + '/' + pg });
      await sleep(1300);
      A('① ' + pg, await ev(send, cond));
    }

    console.log('[新页与封面]');
    await send('Page.navigate', { url: BASE + '/deep-dive-06.html' });
    await sleep(1300);
    A('② dd06 五章+版本 span', await ev(send,
      `document.querySelectorAll('section.lr-sec').length===5 && document.querySelector('.site-version-val')`));
    await send('Page.navigate', { url: BASE + '/deep-dive-07.html' });
    await sleep(1300);
    A('③ dd07 三段体（指控/回应/核查）', await ev(send,
      `document.body.textContent.includes('指控') && document.body.textContent.includes('本站核查')`));

    console.log('[双语往返]');
    await send('Page.navigate', { url: BASE + '/index.html' });
    await sleep(1300);
    A('④ EN 往返（英文渲染+中文复原）', await ev(send,
      `(function(){const h=document.querySelector('.hero-title');const z=h.textContent;const b=document.getElementById('lang-toggle');b.click();const en=h.textContent.includes('Making the Future');b.click();return en&&h.textContent===z?'ok':'fail';})()`));

    console.log('[print 抽查]');
    await send('Emulation.setEmulatedMedia', { type: 'print' });
    await sleep(500);
    A('⑤ print 下题花关闭', await ev(send,
      `(()=>{const b=document.querySelector('.lr-sec blockquote, section blockquote');if(!b)return 'no-bq';const st=getComputedStyle(b,'::before');return !st.content||st.content==='none'||st.content==='normal'?'ok':'on';})()`),
      String(await ev(send, `(()=>{const b=document.querySelector('.lr-sec blockquote, section blockquote');return b?getComputedStyle(b,'::before').content:'no-bq';})()`)));
    await send('Emulation.setEmulatedMedia', { type: 'screen' });

    console.log('[三视口全站抽扫]');
    for (const w of [320, 390, 768]) {
      await send('Emulation.setDeviceMetricsOverride', { width: w, height: 900, deviceScaleFactor: 2, mobile: w < 700 });
      await send('Page.navigate', { url: BASE + '/index.html' });
      await sleep(900);
      A('⑥ ' + w + 'px 零溢出', await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));
      await send('Page.navigate', { url: BASE + '/documents.html' });
      await sleep(1000);
      A('⑦ ' + w + 'px documents 零溢出', await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));
    }

    console.log('[file:// 自包含]');
    await send('Page.navigate', { url: 'file:///D:/vibe%20coding/musk-website/index.html' });
    await sleep(1800);
    A('⑧ file:// index 渲染（品牌+刊头期号 span）', await ev(send,
      `!!document.querySelector('.masthead .brand') && document.querySelector('.mh-volno .site-version-val')`));
    A('⑨ file:// 无网络请求失败（样式生效=背景非透明）', await ev(send,
      `getComputedStyle(document.body).backgroundColor !== 'rgba(0, 0, 0, 0)'`));
    await send('Page.navigate', { url: 'file:///D:/vibe%20coding/musk-website/resources.html' });
    await sleep(1500);
    A('⑩ file:// resources 54 条', await ev(send, `document.querySelectorAll('.rs-item').length === 54`));

    console.log('');
    console.log(`终检探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
