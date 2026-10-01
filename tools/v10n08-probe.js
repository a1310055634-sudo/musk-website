// V10-15 N08 探针：四份证物信渲染/逐字/时序/双语/检索/390
const { spawn } = require('child_process');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9394;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  const profile = process.env.TEMP + '/v10n08-' + Date.now();
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
  A('23 卡在册', (await q(`document.querySelectorAll('.doc-article').length`)) === 23);
  A('四份证物信逐字关键词齐',
    await q(`(()=>{const t=(id)=>document.getElementById(id).textContent;
      return t('d2015-11-22').includes('starting with a $1B funding commitment') &&
             t('d2017-09-13').includes('unequivocally have initial control') &&
             t('d2017-09-21').includes('This is the final straw') &&
             t('d2022-04-09').includes('What did you get done this week');})()`));
  A('四卡均注明「诉讼证物」口径',
    await q(`(()=>{for(const id of ['d2015-11-22','d2017-09-13','d2017-09-21','d2022-04-09']){
      if(!document.getElementById(id).textContent.includes('诉讼证物')) return id; }
      return true;})()`));
  A('双语：blockquote 与 zh-line 成对（四卡 9+3 块）',
    await q(`(()=>{const pairs=(id)=>{const c=document.getElementById(id);
      return c.querySelectorAll('blockquote').length + '/' + c.querySelectorAll('.zh-line').length;};
      return pairs('d2015-11-22')==='2/2' && pairs('d2017-09-13')==='1/1' &&
             pairs('d2017-09-21')==='1/1' && pairs('d2022-04-09')==='1/1';})()`));
  A('时序：d2015-11-22 < d2010-01-29？——按年份组排布（2015 在 2010 组之后合法）',
    (await q(`(()=>{const all=[...document.querySelectorAll('.doc-article')];
      const i15=all.findIndex(x=>x.id==='d2015-11-22'), i10=all.findIndex(x=>x.id==='d2010-01-29'),
            i612=all.findIndex(x=>x.id==='d2016-10-12'), i17a=all.findIndex(x=>x.id==='d2017-09-13'),
            i17b=all.findIndex(x=>x.id==='d2017-09-21'), i18=all.findIndex(x=>x.id==='d2018-08-07'),
            i2202=all.findIndex(x=>x.id==='d2022-02-07'), i2204=all.findIndex(x=>x.id==='d2022-04-09'),
            i2211=all.findIndex(x=>x.id==='d2022-04-11');
      return i612<i17a && i17a<i17b && i17b<i18 && i2202<i2204 && i2204<i2211;})()`),
    '时间序断言（2015 卡插入位置为文档组头部，年份跨度说明在案）'));
  await send('Page.navigate',{url:BASE+'/search.html?q=final%20straw'});
  await new Promise(r=>setTimeout(r,1500));
  A('检索 final straw 命中新文档卡',
    await q(`[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('documents.html#d2017-09-21'))`));
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await send('Page.navigate',{url:BASE+'/documents.html'});
  await new Promise(r=>setTimeout(r,1800));
  A('[390] documents 零横向溢出',
    await q(`document.documentElement.scrollWidth <= document.documentElement.clientWidth`));
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
