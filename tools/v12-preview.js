// V12 美术方向预览：三套令牌覆盖注入截图（零文件改动——纯 CDP 运行时注入）
// 用法: node tools/v12-preview.js
// 输出: qa/preview-v12/ 下 3 方向 × (index 桌面) 截图 + 当前基线 1 张
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9418;
const BASE = 'http://127.0.0.1:8766';
const OUT = 'qa/preview-v12';

let PASS = 0, FAIL = 0;
function A(n, c, d) { c ? (PASS++, console.log('  ✓ ' + n)) : (FAIL++, console.log('  ✗ ' + n + (d ? ' —— ' + d : ''))); }
function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => { let d=''; r.on('data',c=>d+=c); r.on('end',()=>res(JSON.parse(d))); });
  req.on('timeout',()=>req.destroy(new Error('t'))); req.on('error',rej); }); }

const DIRECTIONS = {
  baseline: { label: '当前基线 v11（暖白纸 × 朱红）', css: '' },
  cool: {
    label: '方向 A · 墨蓝学术（冷白纸 × 钴青强调）',
    css: `:root{
      --accent:#1F5F8B; --accent-deep:#174A6E; --accent-bright:#5FA8D3; --accent-soft:#A9C6DC; --accent-glow:rgba(31,95,139,.9);
      --hue-red:#1F5F8B; --hue-navy:#0F2A44;
      --paper-0:#FBFCFE; --paper-50:#F2F5F9; --paper-100:#EDF1F6; --paper-150:#E3E9F0; --paper-200:#D8E0EA;
    }`,
  },
  warm: {
    label: '方向 B · 复古杂志（奶油纸 × 深棕强调）',
    css: `:root{
      --accent:#8B4513; --accent-deep:#6D3610; --accent-bright:#C97B4A; --accent-soft:#DDBEA0; --accent-glow:rgba(139,69,19,.9);
      --hue-red:#8B4513; --hue-ochre:#A0702A;
      --paper-0:#FFF9F0; --paper-50:#FBF3E4; --paper-100:#F6EBD7; --paper-150:#EEE0C9; --paper-200:#E4D3B8;
      --tx-1:#2B2118; --tx-2:#5C4B3A;
    }`,
  },
  modern: {
    label: '方向 C · 现代高对比（近黑墨 × 信号橙，更大字距）',
    css: `:root{
      --accent:#E8590C; --accent-deep:#C44A08; --accent-bright:#FF8A3D; --accent-soft:#F5C6A5; --accent-glow:rgba(232,89,12,.9);
      --hue-red:#E8590C; --hue-navy:#0B7285; --hue-olive:#2F9E44; --hue-ochre:#E8590C;
      --paper-0:#FFFFFF; --paper-50:#F5F5F5; --paper-100:#EDEDED; --paper-150:#E0E0E0; --paper-200:#D0D0D0;
      --tx-1:#111111; --tx-2:#495057; --coal-100:#0B0B0C;
      --fs-body:17.5px;
    }`,
  },
};

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const profile = process.env.TEMP + '/v12-preview-' + Date.now();
  const chrome = spawn(CHROME, ['--headless=new','--disable-gpu','--remote-debugging-port='+PORT,'--user-data-dir='+profile,'--window-size=1440,900','--no-first-run','about:blank'], { stdio:'ignore' });
  let targets;
  for (let i=0;i<60;i++){ await new Promise(r=>setTimeout(r,500)); try{ targets=await getJSON('/json'); if(targets&&targets.length) break; }catch(e){} }
  if (!targets || !targets.length) throw new Error('CDP 无响应');
  const ws = targets.find(t=>t.type==='page');
  const client = new WebSocket(ws.webSocketDebuggerUrl);
  let id=0; const pend=new Map();
  client.addEventListener('message', m=>{ const msg=JSON.parse(m.data); if(msg.id&&pend.has(msg.id)){ const p=pend.get(msg.id); pend.delete(msg.id); msg.error?p.rej(new Error(JSON.stringify(msg.error))):p.res(msg.result);} });
  await new Promise(r=>client.addEventListener('open',r,{once:true}));
  const send=(method,params)=>new Promise((res,rej)=>{ const mid=++id; pend.set(mid,{res,rej}); client.send(JSON.stringify({id:mid,method,params})); });
  await send('Page.enable'); await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride',{width:1440,height:900,deviceScaleFactor:1,mobile:false});

  for (const [key, dir] of Object.entries(DIRECTIONS)) {
    await send('Page.navigate',{url:BASE+'/index.html'});
    await new Promise(r=>setTimeout(r,2200));
    if (dir.css) {
      await send('Runtime.evaluate',{expression:
        `(()=>{let st=document.getElementById('v12-preview'); if(st) st.remove();
          st=document.createElement('style'); st.id='v12-preview'; st.textContent=${JSON.stringify(dir.css)};
          document.head.appendChild(st); return 'injected';})()`,returnByValue:true});
      await new Promise(r=>setTimeout(r,600));
    }
    await send('Runtime.evaluate',{expression:`window.scrollTo(0,0)`});
    await new Promise(r=>setTimeout(r,400));
    const shot = await send('Page.captureScreenshot',{format:'png'});
    const file = `${OUT}/${key}.png`;
    fs.writeFileSync(file, Buffer.from(shot.data,'base64'));
    console.log(`  · ${dir.label}  →  ${file} (${fs.statSync(file).size}B)`);
  }
  // 附：modern 方向的 390 移动端样张
  await send('Emulation.setDeviceMetricsOverride',{width:390,height:844,deviceScaleFactor:1,mobile:true});
  await send('Page.navigate',{url:BASE+'/index.html'});
  await new Promise(r=>setTimeout(r,2000));
  await send('Runtime.evaluate',{expression:
    `(()=>{let st=document.getElementById('v12-preview'); if(st) st.remove();
      st=document.createElement('style'); st.id='v12-preview'; st.textContent=${JSON.stringify(DIRECTIONS.modern.css)};
      document.head.appendChild(st); return 'injected';})()`,returnByValue:true});
  await new Promise(r=>setTimeout(r,600));
  const shot = await send('Page.captureScreenshot',{format:'png'});
  fs.writeFileSync(`${OUT}/modern-390.png`, Buffer.from(shot.data,'base64'));
  console.log(`  · 方向 C 移动端  →  ${OUT}/modern-390.png`);
  console.log('DONE');
  process.exit(0);
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
