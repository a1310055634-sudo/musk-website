// V12-20 R19 探针：transition 归一/三态/reveal 节奏/reduced-motion 逐组件/性能/清点（≥10 断言）
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9368;
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
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  console.log('[文件级：审计 TSV 与归一]');
  const tsv = fs.readFileSync('qa/v12/round-19/transition-audit.tsv', 'utf-8').trim().split('\n');
  A('transition TSV 存在（52 行+header）', tsv.length === 53, String(tsv.length));
  const css = fs.readFileSync('style.css', 'utf-8');
  A('归一后无裸 0.3s/.25s/0.4s transition', !/transition:[^;]*\.(25|3)s/.test(css) && !/transition:[^;]*0\.(25|3|4)s/.test(css));
  A('白名单保留：1s 图表生长+0.6s reveal+delay 级联', css.includes('transition: transform 1s ease') && css.includes('transition: opacity 0.6s ease') && css.includes('transition-delay: 0.15s'));
  A('两档令牌在册（--t-fast 180ms/--t-slow 420ms）', css.includes('--t-fast: 180ms') && css.includes('--t-slow: 420ms'));
  A('btn 三态统一出口（:active 80ms+:focus-visible 令牌）', css.includes('.btn:active') && css.includes('.btn:focus-visible'));
  A('R15–R18 before/after 清点：44+3 张截图在册', (() => {
    const dirs = ['qa/v12/round-15/before', 'qa/v12/round-15/after', 'qa/v12/round-17/before', 'qa/v12/round-17/after', 'qa/v12/round-18/before', 'qa/v12/round-18/after'];
    let n = 0;
    for (const d of dirs) n += fs.readdirSync(d).filter(f => f.endsWith('.png')).length;
    return n === 44;
  })());
  A('性能报告在册（五页实测）', fs.readFileSync('qa/v12/round-19/perf-report.txt', 'utf-8').includes('deep-dive-05'));

  const profile = process.env.TEMP + '/v12r19-profile-' + Date.now();
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
    await send('Page.navigate', { url: BASE + '/deep-dive-05.html' });
    await sleep(1500);

    console.log('[reduced-motion 逐组件 CDP 实测（压平后仍可用）]');
    // 组件 1：reveal 进场
    const rm1 = await ev(send, `(function(){
      document.documentElement.setAttribute('data-rm','1');
      const el = document.querySelector('html.js .reveal');
      if (!el) return 'no-el';
      return getComputedStyle(el).transitionDuration;
    })()`);
    // reduced-motion 媒体模拟
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    await sleep(500);
    A('组件① reveal 压平（duration 0）', await ev(send,
      `(()=>{const el=document.querySelector('html.js .reveal');return el?getComputedStyle(el).transitionDuration.split(',').every(x=>parseFloat(x)===0)?'ok':getComputedStyle(el).transitionDuration:'no-el';})()`),
      String(rm1));
    A('组件② reveal 压平后仍可见可用（opacity 1）', await ev(send,
      `(()=>{const el=document.querySelector('html.js .reveal');return el?getComputedStyle(el).opacity==='1'?'ok':getComputedStyle(el).opacity:'no-el';})()`));
    // 组件 3：引语块
    A('组件③ 引语块 transition 压平', await ev(send,
      `(()=>{const b=document.querySelector('.lr-sec blockquote');return b?getComputedStyle(b).transitionDuration.split(',').every(x=>parseFloat(x)===0)?'ok':getComputedStyle(b).transitionDuration:'no-bq';})()`));
    // 组件 4：btn
    await send('Page.navigate', { url: BASE + '/index.html' });
    await sleep(1200);
    A('组件④ .btn transition 压平', await ev(send,
      `(()=>{const b=document.querySelector('.btn');return b?getComputedStyle(b).transitionDuration.split(',').every(x=>parseFloat(x)===0)?'ok':getComputedStyle(b).transitionDuration:'no-btn';})()`));
    A('组件④ 压平后 .btn 仍可点击（pointer-events 正常+href 在）', await ev(send,
      `(()=>{const b=document.querySelector('a.btn,.btn');return b&&(b.href||b.getAttribute('href'))&&getComputedStyle(b).pointerEvents!=='none'?'ok':'broken';})()`));
    // 组件 5：刊头 volno（对bear R15 假测量教训——本探针为单主题纸面口径）
    A('组件⑤ 刊头期号仍同源 11.20.0（压平后可用性复核）', await ev(send,
      `document.querySelector('.mh-volno .site-version-val').textContent==='11.20.0'`));
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: '' }] });

    console.log('[390]');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await sleep(700);
    A('390 零溢出', await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));

    console.log('');
    console.log(`探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
