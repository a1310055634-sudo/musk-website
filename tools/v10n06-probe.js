// V10-15 N06 探针：d2016-10-12 recusal 卡
const { spawn } = require('child_process');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9390;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  const profile = process.env.TEMP + '/v10n06-' + Date.now();
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
  await new Promise(r=>setTimeout(r,2000));
  const q = e => send('Runtime.evaluate',{expression:e,returnByValue:true}).then(r=>r.result.value);
  A('文档 19 卡（d2016-10-12 在册）', (await q(`document.querySelectorAll('.doc-article').length`)) === 19);
  A('recusal 三段摘录逐字在卡内',
    await q(`(()=>{const c=document.getElementById('d2016-10-12');
      const t=c.textContent;
      return t.includes('should recuse themselves from any vote by the Tesla Board') &&
             t.includes('recused themselves and left the meeting') &&
             t.includes('absent, having recused themselves');})()`));
  A('双语：第一段 zh-line 与 EN 对照在',
    await q(`(()=>{const c=document.getElementById('d2016-10-12');
      return c.querySelectorAll('blockquote').length===3 && c.querySelectorAll('.zh-line').length===3;})()`));
  A('meta 三徽标（EDGAR 备案/日期/备案号 CIK）',
    await q(`(()=>{const c=document.getElementById('d2016-10-12');
      return c.querySelectorAll('.doc-badge').length===3 && c.textContent.includes('0001193125-16-736379');})()`));
  A('时间序：10-12 卡在 2018-08-07 卡前',
    await q(`(()=>{const all=[...document.querySelectorAll('.doc-article')];
      return all.findIndex(x=>x.id==='d2016-10-12') < all.findIndex(x=>x.id==='d2018-08-07');})()`));
  await send('Page.navigate',{url:BASE+'/search.html?q=recuse'});
  await new Promise(r=>setTimeout(r,1500));
  A('检索 recuse 命中新文档卡',
    await q(`[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('documents.html#d2016-10-12'))`));
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await send('Page.navigate',{url:BASE+'/documents.html'});
  await new Promise(r=>setTimeout(r,1800));
  A('[390] documents 零横向溢出',
    await q(`document.documentElement.scrollWidth <= document.documentElement.clientWidth`));
  const el = await q(`(()=>{document.getElementById('d2016-10-12').scrollIntoView({block:'center'});
    return document.documentElement.scrollWidth <= document.documentElement.clientWidth;})()`);
  A('[390] 新卡区零溢出', el);
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
