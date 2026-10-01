// V10-15 N10 探针：4 新条+AI Day 升级+quotes 卡+检索+390
const { spawn } = require('child_process');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9400;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  const profile = process.env.TEMP + '/v10n10-' + Date.now();
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
  await send('Page.navigate',{url:BASE+'/primary.html'});
  await new Promise(r=>setTimeout(r,2500));
  const q = e => send('Runtime.evaluate',{expression:e,returnByValue:true}).then(r=>r.result.value);
  A('119 账本行', (await q(`document.querySelectorAll('.ps-row').length`)) === 119);
  A('AI Day 2021 升级：官方逐字在册+现场段 data-en 注明 2022 媒体口径（属性级）+中文重申句在',
    await q(`(()=>{const c=document.getElementById('e2021-08');
      const quote=c.querySelector('.ps-quote').textContent;
      const ground=c.querySelector('[data-en*="2022 AI Day"]');
      return quote.includes('semi-sentient robots on wheels') &&
             quote.includes('prototype sometime next year') &&
             !!ground && ground.textContent.includes('重申');})()`));
  A('AI Day 升级：ps-src 注明官方转写+2026-10 复核',
    await q(`document.getElementById('e2021-08').querySelector('.ps-src').textContent.includes('2026-10')`));
  A('四新条逐字齐（股东会 hope/Mars 百万吨/toddler/epic chip）',
    await q(`(()=>{const t=id=>document.getElementById(id).textContent;
      return t('e2024-06-13-2').includes('fully sustainable global economy') &&
             t('e2025-05-29').includes('self sustaining civilization on Mars') &&
             t('e2026-02-10').includes('basically a toddler') &&
             t('e2026-03-21').includes('most epic chip building exercise');})()`));
  A('时序：613<613-2<0529<0210<0321<0722',
    await q(`(()=>{const all=[...document.querySelectorAll('.ps-row')];
      const f=id=>all.findIndex(x=>x.id===id);
      const a=f('e2024-06-13'), b=f('e2024-06-13-2'), c=f('e2025-05-29'), d=f('e2026-02-10'), e=f('e2026-03-21'), g=f('e2026-07-22');
      return a<b && b<c && c<d && d<e && e<g;})()`));
  A('双语：四新条 ps-quote/ps-zh 成对',
    await q(`(()=>{for(const id of ['e2024-06-13-2','e2025-05-29','e2026-02-10','e2026-03-21']){
      const c=document.getElementById(id);
      if(!(c.querySelector('.ps-quote')&&c.querySelector('.ps-zh'))) return id;}
      return true;})()`));
  await send('Page.navigate',{url:BASE+'/quotes.html'});
  await new Promise(r=>setTimeout(r,1800));
  A('quotes 107 卡（四新卡在册）', (await q(`document.querySelectorAll('.qs-card').length`)) === 107);
  A('AI Day 卡文已升级（semi-sentient）',
    await q(`[...document.querySelectorAll('.qs-card')].some(c=>c.querySelector('.qs-en').textContent.includes('semi-sentient robots on wheels'))`));
  await send('Page.navigate',{url:BASE+'/search.html?q=toddler'});
  await new Promise(r=>setTimeout(r,1500));
  A('检索 toddler 命中 xAI 新条',
    await q(`[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('primary.html#e2026-02-10'))`));
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await send('Page.navigate',{url:BASE+'/primary.html'});
  await new Promise(r=>setTimeout(r,2000));
  A('[390] primary 零横向溢出',
    await q(`document.documentElement.scrollWidth <= document.documentElement.clientWidth`));
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
