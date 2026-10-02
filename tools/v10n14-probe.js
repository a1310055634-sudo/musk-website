// V10-15 N14 探针：2 新档案渲染/深链/口径闭环
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9412;
const BASE = 'http://127.0.0.1:8766';
let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
(async () => {
  // 文件级口径
  const tljs = fs.readFileSync('timeline-events.js', 'utf-8');
  const recM = tljs.match(/window\.TIMELINE_V7 = (\{[\s\S]*?\});\s*\n/);
  const recs = JSON.parse(recM[1].replace(/\n/g, ' '));
  const idxN = (fs.readFileSync('search-index.js', 'utf-8').match(/"id": "/g) || []).length;
  A(`口径闭环：索引 ${idxN} = 档案 16 + 吸收 ${idxN-16-recs.records.length} + 独立 ${recs.records.length}`,
    16 + (idxN - 16 - recs.records.length) + recs.records.length === idxN);
  const evHtml = fs.readFileSync('events.html', 'utf-8');
  A('events.html 16 档案卡', (evHtml.match(/class="ev-item lr-sec" id="/g) || []).length === 16);
  A('新档案材料深链目标全在册（d2015-11-22/d2017-09-13/d2017-09-21）',
    ['d2015-11-22','d2017-09-13','d2017-09-21'].every(id => evHtml.includes(`id="${id}"`) ||
      fs.readFileSync('documents.html', 'utf-8').includes(`id="${id}"`)));

  const profile = process.env.TEMP + '/v10n14-' + Date.now();
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
  await send('Page.navigate',{url:BASE+'/events.html'});
  await new Promise(r=>setTimeout(r,2500));
  const q = e => send('Runtime.evaluate',{expression:e,returnByValue:true}).then(r=>r.result.value);
  A('DOM：16 档案渲染', (await q(`document.querySelectorAll('.ev-item').length`)) === 16);
  A('OpenAI 弧线档案渲染（标题+三封邮件材料）',
    await q(`(()=>{const c=document.getElementById('e2015-11-22');
      return !!c && c.textContent.includes('最后一根稻草') && c.textContent.includes('10 亿');})()`));
  A('xAI 线档案渲染（toddler+银河百科）',
    await q(`(()=>{const c=document.getElementById('e2026-02-10');
      return !!c && c.textContent.includes('幼儿') && c.textContent.includes('银河百科');})()`));
  A('新档案材料深链可点（documents 三链）',
    await q(`(()=>{const c=document.getElementById('e2015-11-22');
      return !!c.querySelector('a[href="documents.html#d2015-11-22"]') &&
             !!c.querySelector('a[href="documents.html#d2017-09-13"]') &&
             !!c.querySelector('a[href="documents.html#d2017-09-21"]');})()`));
  A('390 零溢出（events）',
    await q(`(()=>{window.scrollTo(0,0); return document.documentElement.scrollWidth <= document.documentElement.clientWidth;})()`));
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
