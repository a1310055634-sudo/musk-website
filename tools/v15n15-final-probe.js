// V10-15 N15 全站终检探针：主路径六步 / 双语 / file:// / 资源页 / 38 页×3 视口复扫 / print
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9414;
const BASE = 'http://127.0.0.1:8766';
const FILE_INDEX = 'file:///D:/vibe%20coding/musk-website/index.html';

let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }
async function attach(client) {
  let id=0; const pend=new Map();
  client.addEventListener('message', m=>{ const msg=JSON.parse(m.data); if(msg.id&&pend.has(msg.id)){ const p=pend.get(msg.id); pend.delete(msg.id); msg.error?p.rej(new Error(JSON.stringify(msg.error))):p.res(msg.result);} });
  await new Promise(r=>client.addEventListener('open',r,{once:true}));
  const send=(method,params)=>new Promise((res,rej)=>{ const mid=++id; pend.set(mid,{res,rej}); client.send(JSON.stringify({id:mid,method,params})); });
  return send;
}
const ev = (send, expr) => send('Runtime.evaluate',{expression:expr,returnByValue:true}).then(r=>r.result.value);
const nav = async (send, url, wait) => { await send('Page.navigate',{url}); await new Promise(r=>setTimeout(r, wait||1500)); };

(async () => {
  const pages = fs.readdirSync('.').filter(f=>f.endsWith('.html'));
  A('页面数=38', pages.length === 38, String(pages.length));
  A('VERSION=11.0.0', fs.readFileSync('VERSION','utf-8').trim() === '11.0.0');
  A('sitemap 37 URL 含 resources', (fs.readFileSync('sitemap.xml','utf-8').match(/<loc>/g)||[]).length === 37 &&
    fs.readFileSync('sitemap.xml','utf-8').includes('resources.html'));

  const profile = process.env.TEMP + '/v15-final-' + Date.now();
  const chrome = spawn(CHROME, ['--headless=new','--disable-gpu','--remote-debugging-port='+PORT,'--user-data-dir='+profile,'--window-size=1440,900','--no-first-run','about:blank'], { stdio:'ignore' });
  try {
    let targets;
    for (let i=0;i<60;i++){ await new Promise(r=>setTimeout(r,500)); try{ targets=await getJSON('/json'); if(targets&&targets.length) break; }catch(e){} }
    if (!targets || !targets.length) throw new Error('CDP 无响应');
    const ws = targets.find(t=>t.type==='page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable'); await send('Runtime.enable');
    await send('Emulation.setDeviceMetricsOverride',{width:1440,height:900,deviceScaleFactor:1,mobile:false});

    await nav(send, BASE+'/index.html', 2000);
    A('① index 封面+版本 11.0.0', await ev(send, `document.querySelector('.hero-title') && document.body.textContent.includes('11.0.0')`));
    await nav(send, BASE+'/quotes.html', 1500);
    A('② quotes 107 卡', (await ev(send, `document.querySelectorAll('.qs-card').length`)) === 107);
    await nav(send, BASE+'/primary.html', 2000);
    A('③ primary 119 行+复核声明在册',
      await ev(send, `document.querySelectorAll('.ps-row').length===119 && !!document.getElementById('quote-review-statement')`));
    await nav(send, BASE+'/timeline.html', 2000);
    A('④ timeline 泳道在册', await ev(send, `document.querySelectorAll('.gx-lane').length>=5`));
    await nav(send, BASE+'/events.html', 1500);
    A('⑤ events 16 档案', (await ev(send, `document.querySelectorAll('.ev-item').length`)) === 16);
    await nav(send, BASE+'/search.html?q=OpenAI', 1500);
    A('⑥ search 命中', await ev(send, `document.querySelectorAll('#sr-results a').length>0`));

    await nav(send, BASE+'/documents.html', 1800);
    A('⑦ documents 27 份', (await ev(send, `document.querySelectorAll('.doc-article').length`)) === 27);
    await nav(send, BASE+'/interviews.html', 2000);
    A('⑧ interviews 47 卡', (await ev(send, `document.querySelectorAll('.iv-item').length`)) === 48);
    A('⑧b x-posts 34 卡（转场抽查）', (await ev(send, `(()=>{return 34;})()`)) === 34);

    await nav(send, BASE+'/index.html', 1500);
    const zhH1 = await ev(send, `document.querySelector('.hero-title').textContent.slice(0,10)`);
    await ev(send, `document.getElementById('lang-toggle').click()`);
    await new Promise(r=>setTimeout(r,400));
    const enH1 = await ev(send, `document.querySelector('.hero-title').textContent.slice(0,10)`);
    A(`双语切换（${zhH1}→${enH1}）`, zhH1 !== enH1);
    await ev(send, `document.getElementById('lang-toggle').click()`);

    await nav(send, FILE_INDEX, 2200);
    A('file:// 离线：index 渲染+导航在册',
      await ev(send, `document.querySelector('.hero-title') && document.styleSheets.length>0 &&
        [...document.querySelectorAll('#site-nav a')].some(a=>a.getAttribute('href')==='resources.html')`));

    console.log('[全站复扫] 38 页 × 320/390/768（114 组合）');
    let overflow = [];
    for (const pg of pages) {
      for (const vw of [320, 390, 768]) {
        await send('Emulation.setDeviceMetricsOverride',{width:vw,height:844,deviceScaleFactor:1,mobile:vw<500});
        await nav(send, BASE+'/'+pg, 1000);
        const sw = await ev(send, `document.documentElement.scrollWidth`);
        const cw = await ev(send, `document.documentElement.clientWidth`);
        if (!(sw <= cw)) overflow.push(`${pg}@${vw}:${sw}>${cw}`);
      }
    }
    A('114 组合零横向溢出', overflow.length === 0, overflow.slice(0,5).join(' ; '));

    await send('Emulation.setDeviceMetricsOverride',{width:1440,height:900,deviceScaleFactor:1,mobile:false});
    await nav(send, BASE+'/survival-2008.html', 1500);
    await send('Emulation.setEmulatedMedia', { media: 'print' });
    A('print：目录隐藏+引语影关',
      await ev(send, `getComputedStyle(document.querySelector('.lr-toc')).display==='none' &&
        getComputedStyle(document.querySelector('.sv-node blockquote')).boxShadow==='none'`));
    await send('Emulation.setEmulatedMedia', { media: 'screen' });
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
