// V10-15 N05 探针：i2008-08-05 新卡渲染/双语/互链/检索
const { spawn } = require('child_process');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9388;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  const profile = process.env.TEMP + '/v10n05-' + Date.now();
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
  await new Promise(r=>setTimeout(r,2200));
  const q = e => send('Runtime.evaluate',{expression:e,returnByValue:true}).then(r=>r.result.value);
  A('新卡渲染（44 iv-item 中含 i2008-08-05）', (await q(`document.querySelectorAll('.iv-item').length`)) === 44);
  A('六件套齐（h2/meta/ctx/blockquote/iv-zh/after）',
    await q(`(()=>{const c=document.getElementById('i2008-08-05');
      return !!(c.querySelector('h2') && c.querySelector('.iv-meta') && c.querySelector('.ctx') &&
                c.querySelector('blockquote') && c.querySelector('.iv-zh') && c.querySelector('.after'));})()`));
  A('逐字主句在卡内（fuck that / hell-bent）',
    await q(`(()=>{const c=document.getElementById('i2008-08-05');
      const t=c.querySelector('blockquote').textContent;
      return t.includes('fuck that') && t.includes('hell-bent');})()`));
  A('双语：h2 EN 切换（data-en 生效）',
    await q(`(()=>{const h=document.querySelector('#i2008-08-05 h2');
      const zh=h.textContent;
      document.getElementById('lang-toggle').click();
      const en=h.textContent;
      document.getElementById('lang-toggle').click();
      return zh!==en && en.includes('Optimism');})()`));
  A('互链双通（→i2008-09-28 页内锚存在；survival-2008 链接）',
    await q(`(()=>{const a=document.querySelector('#i2008-08-05 .after a[href="#i2008-09-28"]');
      const b=document.querySelector('#i2008-08-05 .after a[href="survival-2008.html"]');
      return !!a && !!b && !!document.getElementById('i2008-09-28');})()`));
  A('时间序：08-05 卡位于 09-28 卡之前',
    await q(`(()=>{const all=[...document.querySelectorAll('.iv-item')];
      return all.findIndex(x=>x.id==='i2008-08-05') < all.findIndex(x=>x.id==='i2008-09-28');})()`));
  await send('Page.navigate',{url:BASE+'/search.html?q=hell-bent'});
  await new Promise(r=>setTimeout(r,1500));
  A('检索 hell-bent 命中新卡',
    await q(`[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('interviews.html#i2008-08-05'))`));
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await send('Page.navigate',{url:BASE+'/interviews.html'});
  await new Promise(r=>setTimeout(r,1800));
  const sw = await q(`document.documentElement.scrollWidth <= document.documentElement.clientWidth`);
  A('[390] interviews.html 零横向溢出（真 390 模拟）', sw);
  const shot = await send('Page.captureScreenshot', { format: 'png' });
  require('fs').writeFileSync('qa/v10-15/round-05/i2008-08-05-390.png', Buffer.from(shot.data,'base64'));
  console.log('  · 截图 i2008-08-05-390.png');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
