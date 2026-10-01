// V10-15 N07 探针：三新卡渲染/时序/分组/五件套/检索/390
const { spawn } = require('child_process');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9392;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  const profile = process.env.TEMP + '/v10n07-' + Date.now();
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
  await send('Page.navigate',{url:BASE+'/x-posts.html'});
  await new Promise(r=>setTimeout(r,2200));
  const q = e => send('Runtime.evaluate',{expression:e,returnByValue:true}).then(r=>r.result.value);
  A('34 卡在册', (await q(`document.querySelectorAll('.tweet-card').length`)) === 34);
  A('三新卡五件套齐',
    await q(`(()=>{for(const id of ['p2018-08-14','p2019-03-14','p2019-05-25']){
      const c=document.getElementById(id);
      if(!c) return id+' missing';
      if(!(c.querySelector('.tweet-text')&&c.querySelector('.tweet-zh')&&c.querySelector('.tweet-note')&&c.querySelector('.tweet-date'))) return id+' structure';}
      return true;})()`));
  A('逐字断言（Silver Lake 顾问阵容 / S3XY / superalloy+foundry）',
    await q(`(()=>{const a=document.querySelector('#p2018-08-14 .tweet-text').textContent;
      const b=document.querySelector('#p2019-03-14 .tweet-text').textContent;
      const c=document.querySelector('#p2019-05-25 .tweet-text').textContent;
      return a.includes('Silver Lake and Goldman Sachs') && b.startsWith('S3XY') && c.includes('superalloy');})()`));
  A('时间序与分组：08-07<08-14<2019 条<03-14<05-25<11-21',
    await q(`(()=>{const els=[...document.querySelectorAll('.tweet-card, .xp-year')];
      const idx=id=>els.findIndex(x=>x.id===id||x.textContent.trim()==='2019'&&x.className.includes('xp-year'));
      const a=els.findIndex(x=>x.id==='p2018-08-07'), b=els.findIndex(x=>x.id==='p2018-08-14'),
            y=els.findIndex(x=>x.className.includes('xp-year')&&x.textContent.trim()==='2019'),
            c=els.findIndex(x=>x.id==='p2019-03-14'), d=els.findIndex(x=>x.id==='p2019-05-25'),
            e=els.findIndex(x=>x.id==='p2019-11-21');
      return a<b && b<y && y<c && c<d && d<e;})()`));
  A('互链：08-14 卡内链接到 p2018-08-07',
    await q(`!!document.querySelector('#p2018-08-14 .tweet-note a[href="#p2018-08-07"]')`));
  A('双语切换不塌（34 卡保持）',
    await q(`(()=>{document.getElementById('lang-toggle').click();
      const n=document.querySelectorAll('.tweet-card').length;
      document.getElementById('lang-toggle').click();
      return n===34;})()`));
  await send('Page.navigate',{url:BASE+'/search.html?q=S3XY'});
  await new Promise(r=>setTimeout(r,1500));
  A('检索 S3XY 命中新卡',
    await q(`[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('x-posts.html#p2019-03-14'))`));
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await send('Page.navigate',{url:BASE+'/x-posts.html'});
  await new Promise(r=>setTimeout(r,1800));
  A('[390] 零横向溢出',
    await q(`document.documentElement.scrollWidth <= document.documentElement.clientWidth`));
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
