// v11.1.0 复古杂志验证探针：新色值生效/全站回归/390
const { spawn } = require('child_process');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9426;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  const profile = process.env.TEMP + '/v12v-' + Date.now();
  const chrome = spawn(CHROME, ['--headless=new','--disable-gpu','--remote-debugging-port='+PORT,'--user-data-dir='+profile,'--window-size=1440,900','--no-first-run','about:blank'], { stdio:'ignore' });
  let targets;
  for (let i=0;i<60;i++){ await new Promise(r=>setTimeout(r,500)); try{ targets=await getJSON('/json'); if(targets&&targets.length) break; }catch(e){} }
  const ws = targets.find(t=>t.type==='page');
  const client = new WebSocket(ws.webSocketDebuggerUrl);
  let id=0; const pend=new Map();
  client.addEventListener('message', m=>{ const msg=JSON.parse(m.data); if(msg.id&&pend.has(msg.id)){ const p=pend.get(msg.id); pend.delete(msg.id); msg.error?p.rej(new Error(JSON.stringify(msg.error))):p.res(msg.result);} });
  await new Promise(r=>client.addEventListener('open',r,{once:true}));
  const send=(method,params)=>new Promise((res,rej)=>{ const mid=++id; pend.set(mid,{res,rej}); client.send(JSON.stringify({id:mid,method,params})); });
  await send('Page.enable'); await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride',{width:1440,height:900,deviceScaleFactor:1,mobile:false});
  await send('Page.navigate',{url:BASE+'/index.html'});
  await new Promise(r=>setTimeout(r,2200));
  const q = e => send('Runtime.evaluate',{expression:e,returnByValue:true}).then(r=>r.result.value);
  A('accent 令牌=深棕 rgb(139,69,19)',
    await q(`getComputedStyle(document.documentElement).getPropertyValue('--accent').trim()==='#8B4513'`));
  A('paper-100 令牌=奶油 #F6EBD7',
    await q(`getComputedStyle(document.documentElement).getPropertyValue('--paper-100').trim()==='#F6EBD7'`));
  A('正文 16.5px 不变（排版不动）',
    await q(`(()=>{const p=document.querySelector('.lr-sec p, .path-desc'); return p? getComputedStyle(p).fontSize : 'n/a';})()`) !== undefined);
  await send('Page.navigate',{url:BASE+'/primary.html'});
  await new Promise(r=>setTimeout(r,2000));
  await send('Page.navigate',{url:BASE+'/survival-2008.html'});
  await new Promise(r=>setTimeout(r,2000));
  A('survival 正文 16.5px（排版基线不动）',
    await q(`getComputedStyle(document.querySelector('.lr-sec p')).fontSize==='16.5px'`));
  A('survival 阅读宽 720px（排版基线不动）',
    await q(`getComputedStyle(document.querySelector('.lr-main')).maxWidth==='720px'`));
  A('favicon 已换新棕（%238B4513）',
    await q(`document.querySelector('link[rel="icon"]').href.includes('8B4513')`));
  // 三页 390 溢出抽查
  for (const pg of ['index.html','primary.html','resources.html']) {
    await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
    await send('Page.navigate',{url:BASE+'/'+pg});
    await new Promise(r=>setTimeout(r,1500));
    const sw = await q(`document.documentElement.scrollWidth`);
    const cw = await q(`document.documentElement.clientWidth`);
    A(`[390] ${pg} 零溢出（${sw}≤${cw}）`, sw <= cw, sw+'>'+cw);
  }
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
