// V10-15 N13 探针：5 新资源卡
const { spawn } = require('child_process');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9410;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  const profile = process.env.TEMP + '/v10n13-' + Date.now();
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
  await send('Page.navigate',{url:BASE+'/resources.html'});
  await new Promise(r=>setTimeout(r,2200));
  const q = e => send('Runtime.evaluate',{expression:e,returnByValue:true}).then(r=>r.result.value);
  A('49 卡在册', (await q(`document.querySelectorAll('.rs-item').length`)) === 49);
  A('五新卡 id 全在册',
    await q(`(()=>{for(const id of ['r-wikidata-elon-musk','r-archive-org-search','r-isaacson-official-page','r-vance-official-page','r-reuters-tesla-topic']){
      if(!document.getElementById(id)) return id; }
      return true;})()`));
  A('书页双卡（Isaacson/Vance）与 DNS 注记',
    await q(`(()=>{const a=document.getElementById('r-isaacson-official-page');
      const b=document.getElementById('r-vance-official-page');
      return a.textContent.includes('DNS') && b.textContent.includes('DNS');})()`));
  A('Wikidata 卡 CC0 许可在',
    await q(`document.getElementById('r-wikidata-elon-musk').textContent.includes('CC0')`));
  A('wikipedia 主条目不重复（R13 已在册仅一张）',
    (await q(`[...document.querySelectorAll('.rs-item')].filter(c=>c.id==='r-wikipedia-elon-musk').length`)) === 1);
  await send('Page.navigate',{url:BASE+'/search.html?q=Q317521'});
  await new Promise(r=>setTimeout(r,1500));
  A('检索 Q317521 命中 Wikidata 卡',
    await q(`[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-wikidata-elon-musk'))`));
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await send('Page.navigate',{url:BASE+'/resources.html'});
  await new Promise(r=>setTimeout(r,1800));
  A('[390] resources 零横向溢出',
    await q(`document.documentElement.scrollWidth <= document.documentElement.clientWidth`));
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
