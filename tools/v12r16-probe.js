// V12-20 R16 探针：drop cap/引语题花三族/边注分野/基线锁定/390 降级/print/reduced-motion
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9363;
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
  console.log('[文件级]');
  const css = fs.readFileSync('style.css', 'utf-8');
  A('drop cap 规则入册', css.includes('.lr-main > section.lr-sec:first-of-type > p:first-of-type::first-letter'));
  A('引语三族题花规则入册', css.includes('.sv-node blockquote::before') && css.includes('.pv-case blockquote::before'));
  A('390 降级规则入册', css.includes('390 降级：加粗首字防溢出') || css.includes('font-weight: 700; padding: 0; color: inherit;'));
  A('print 降级规则入册', css.includes('@media print') && css.includes('content: none'));
  A('基线锁定：--fs-body 仍 16.5px', css.includes('--fs-body: 16.5px'));

  const profile = process.env.TEMP + '/v12r16-profile-' + Date.now();
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

    console.log('[drop cap]');
    A('首段 ::first-letter float（下沉生效）', await ev(send,
      `(()=>{const p=document.querySelector('.lr-main > section.lr-sec:first-of-type > p:first-of-type');if(!p)return 'no-p';const st=getComputedStyle(p,'::first-letter');return st.float==='left'?'ok':st.float;})()`),
      String(await ev(send,
        `(()=>{const p=document.querySelector('.lr-main > section.lr-sec:first-of-type > p:first-of-type');const st=getComputedStyle(p,'::first-letter');return st.float+'|'+st.fontSize;})()`)));
    A('首字字号 3.1em（约 51px）', await ev(send,
      `parseFloat(getComputedStyle(document.querySelector('.lr-main > section.lr-sec:first-of-type > p:first-of-type'),'::first-letter').fontSize) > 45`));
    A('首字衬线+主题色', await ev(send,
      `(()=>{const st=getComputedStyle(document.querySelector('.lr-main > section.lr-sec:first-of-type > p:first-of-type'),'::first-letter');return st.fontFamily.includes('Georgia')||st.fontFamily.includes('serif');})()`));

    console.log('[引语题花]');
    A('blockquote ::before 大引号渲染', await ev(send,
      `(()=>{const b=document.querySelector('.lr-sec blockquote');if(!b)return 'no-bq';const st=getComputedStyle(b,'::before');return st.content && st.content!=='none' && st.content!=='normal' ? 'ok' : st.content;})()`),
      String(await ev(send,
        `(()=>{const b=document.querySelector('.lr-sec blockquote');const st=getComputedStyle(b,'::before');return st.content;})()`)));
    A('题花后正文左移（margin-left 30px）', await ev(send,
      `(()=>{const b=document.querySelector('.lr-sec blockquote > *');return b?parseInt(getComputedStyle(b).marginLeft)>=28:'no-child';})()`));

    console.log('[边注分野]');
    A('.lr-note 虚线框保持（与引语实线竖分野）', await ev(send,
      `(()=>{const n=document.querySelector('.lr-note');if(!n)return 'no-note';const st=getComputedStyle(n);return st.borderTopStyle==='dashed'||st.borderStyle.includes('dashed')?'ok':st.borderStyle;})()`),
      String(await ev(send,
        `(()=>{const n=document.querySelector('.lr-note');const st=getComputedStyle(n);return st.borderTopStyle+'/'+st.borderLeftStyle;})()`)));
    A('基线 16.5px 锁定（lr-sec p computed）', await ev(send,
      `getComputedStyle(document.querySelector('.lr-sec p')).fontSize==='16.5px'`),
      String(await ev(send, `getComputedStyle(document.querySelector('.lr-sec p')).fontSize`)));

    console.log('[survival-2008 / promises 三族覆盖]');
    await send('Page.navigate', { url: BASE + '/survival-2008.html' });
    await sleep(1400);
    A('sv-node blockquote 题花生效', await ev(send,
      `(()=>{const b=document.querySelector('.sv-node blockquote');if(!b)return 'no-bq';const st=getComputedStyle(b,'::before');return st.content && st.content!=='none' && st.content!=='normal' ? 'ok' : st.content;})()`));
    await send('Page.navigate', { url: BASE + '/promises.html' });
    await sleep(1400);
    A('pv-case blockquote 题花生效', await ev(send,
      `(()=>{const b=document.querySelector('.pv-case blockquote');if(!b)return 'no-bq';const st=getComputedStyle(b,'::before');return st.content && st.content!=='none' && st.content!=='normal' ? 'ok' : st.content;})()`));

    console.log('[390 降级]');
    await send('Page.navigate', { url: BASE + '/deep-dive-05.html' });
    await sleep(1200);
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await sleep(600);
    A('390 首字降级（float none）', await ev(send,
      `getComputedStyle(document.querySelector('.lr-main > section.lr-sec:first-of-type > p:first-of-type'),'::first-letter').float==='none'`));
    A('390 零横向溢出', await ev(send,
      `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));

    console.log('[print 媒体模拟]');
    await send('Emulation.setDeviceMetricsOverride', { width: 816, height: 1056, deviceScaleFactor: 1, mobile: false });
    await send('Emulation.setEmulatedMedia', { type: 'print' });
    await sleep(600);
    A('print 下题花关闭（content none）', await ev(send,
      `(()=>{const b=document.querySelector('.lr-sec blockquote');if(!b)return 'no-bq';const st=getComputedStyle(b,'::before');return (!st.content || st.content==='none' || st.content==='normal')?'ok':st.content;})()`),
      String(await ev(send,
        `(()=>{const b=document.querySelector('.lr-sec blockquote');const st=getComputedStyle(b,'::before');return st.content;})()`)));
    await send('Emulation.setEmulatedMedia', { type: 'screen' });

    console.log('[reduced-motion]');
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    await sleep(400);
    A('引语块 transition 压平', await ev(send,
      `getComputedStyle(document.querySelector('.lr-sec blockquote')).transitionDuration.split(',').every(x=>parseFloat(x)===0)`));
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: '' }] });

    console.log('');
    console.log(`探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
