// V10-15 N11 探针：保留池四卡
const { spawn } = require('child_process');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9402;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  const profile = process.env.TEMP + '/v10n11-' + Date.now();
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
  await send('Page.navigate',{url:BASE+'/interviews.html'});
  await new Promise(r=>setTimeout(r,2400));
  const q = e => send('Runtime.evaluate',{expression:e,returnByValue:true}).then(r=>r.result.value);
  A('48 卡在册', (await q(`document.querySelectorAll('.iv-item').length`)) === 48);
  A('四新卡六件套齐',
    await q(`(()=>{for(const id of ['i2013-05-29','i2019-02-19','i2019-06-13','i2021-09-28']){
      const c=document.getElementById(id);
      if(!c) return id+' missing';
      if(!(c.querySelector('h2')&&c.querySelector('.iv-meta')&&c.querySelector('.ctx')&&c.querySelector('blockquote')&&c.querySelector('.iv-zh')&&c.querySelector('.after'))) return id+' structure';}
      return true;})()`));
  A('四句逐字关键词齐',
    await q(`(()=>{const t=id=>document.getElementById(id).querySelector('blockquote').textContent;
      return t('i2013-05-29').includes('Boston to DC') &&
             t('i2019-02-19').includes('with certainty') &&
             t('i2019-06-13').includes('not trying hard enough') &&
             t('i2021-09-28').includes('freaking cool');})()`));
  A('ASR 平面化注明（两卡编者加注）',
    await q(`(()=>{let n=0;
      for(const id of ['i2019-02-19','i2019-06-13','i2021-09-28']){
        if(document.getElementById(id).textContent.includes('编者')) n++;}
      return n>=2;})()`));
  A('2019 FSD 承诺卡含对账注记（承诺未按年兑现如实）',
    await q(`document.getElementById('i2019-02-19').textContent.includes('承诺未按年兑现')`));
  A('互链：e3 卡链到 i2008-08-05（失败即数据弧线）',
    await q(`!!document.querySelector('#i2019-06-13 .after a[href="#i2008-08-05"]')`));
  const seq = await q(`(()=>{const all=[...document.querySelectorAll('.iv-item')];
      const f=id=>all.findIndex(x=>x.id===id);
      return JSON.stringify({m02:f('i2019-02-19'), m07:f('i2017-07-28'), s28:f('i2021-09-28'), y12:f('i2021-12')});})()`);
  console.log('  · seq=' + seq);
  const sd = JSON.parse(seq);
  A('插入邻居关系：02-19 在 07-28 卡前 / 09-28 在 2021-12 卡前（批次式排列口径）',
    sd.m02 < sd.m07 && sd.s28 < sd.y12 && sd.m02 >= 0 && sd.s28 >= 0, seq);
  await send('Page.navigate',{url:BASE+'/search.html?q=freaking'});
  await new Promise(r=>setTimeout(r,1500));
  A('检索 freaking 命中新卡',
    await q(`[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('interviews.html#i2021-09-28'))`));
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await send('Page.navigate',{url:BASE+'/interviews.html'});
  await new Promise(r=>setTimeout(r,1800));
  A('[390] interviews 零横向溢出',
    await q(`document.documentElement.scrollWidth <= document.documentElement.clientWidth`));
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
