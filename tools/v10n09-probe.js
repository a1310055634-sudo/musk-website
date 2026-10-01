// V10-15 N09 探针：四封冲刺信渲染/逐字/时序/口径/检索/390
const { spawn } = require('child_process');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9396;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  const profile = process.env.TEMP + '/v10n09-' + Date.now();
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
  await send('Page.navigate',{url:BASE+'/documents.html'});
  await new Promise(r=>setTimeout(r,2200));
  const q = e => send('Runtime.evaluate',{expression:e,returnByValue:true}).then(r=>r.result.value);
  A('27 卡在册', (await q(`document.querySelectorAll('.doc-article').length`)) === 27);
  A('四封信逐字关键词齐',
    await q(`(()=>{const t=id=>document.getElementById(id).textContent;
      return t('d2018-06-17').includes('quite extensive and damaging sabotage') &&
             t('d2020-09-20').includes('record quarter for deliveries') &&
             t('d2020-12-01').includes('soufflé under a sledgehammer') &&
             t('d2022-05-31').includes('minimum of 40 hours in the office');})()`));
  A('四卡均注明「媒体获得」口径',
    await q(`(()=>{for(const id of ['d2018-06-17','d2020-09-20','d2020-12-01','d2022-05-31']){
      if(!document.getElementById(id).textContent.includes('媒体获得')) return id; }
      return true;})()`));
  A('时序：sabotage<08-07 卡；rq<soufflé<11-26 卡；rto<07-26 卡',
    await q(`(()=>{const all=[...document.querySelectorAll('.doc-article')];
      const f=id=>all.findIndex(x=>x.id===id);
      return f('d2018-06-17')<f('d2018-08-07') && f('d2020-09-20')<f('d2020-12-01') &&
             f('d2020-12-01')<f('d2021-11-26') && f('d2022-05-31')<f('d2022-07-26');})()`));
  await send('Page.navigate',{url:BASE+'/search.html?q=profitability%20is%20very%20low'});
  await new Promise(r=>setTimeout(r,1500));
  A('检索命中新文档卡（第一 blockquote 入索引——R06 已知架构口径）',
    await q(`[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('documents.html#d2020-12-01'))`));
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await send('Page.navigate',{url:BASE+'/documents.html'});
  await new Promise(r=>setTimeout(r,1800));
  A('[390] documents 零横向溢出',
    await q(`document.documentElement.scrollWidth <= document.documentElement.clientWidth`));
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
