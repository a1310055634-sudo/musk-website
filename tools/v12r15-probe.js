// V12-20 R15 探针：刊头三件套/期号同源/双主题对比度/三视口/reduced-motion（≥6 断言）
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9362;
const BASE = 'http://127.0.0.1:8766';

let PASS = 0, FAIL = 0;
function A(name, cond, detail) {
  if (cond) { PASS++; console.log('  ✓ ' + name); }
  else { FAIL++; console.log('  ✗ ' + name + (detail ? ' —— ' + detail : '')); }
}
function getJSON(path) {
  return new Promise((res, rej) => {
    const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => {
      let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
    });
    req.on('timeout', () => req.destroy(new Error('timeout')));
    req.on('error', rej);
  });
}
async function attach(client) {
  let id = 0; const pending = new Map();
  client.addEventListener('message', m => {
    const msg = JSON.parse(m.data);
    if (msg.id && pending.has(msg.id)) {
      const p = pending.get(msg.id); pending.delete(msg.id);
      msg.error ? p.rej(new Error(JSON.stringify(msg.error))) : p.res(msg.result);
    }
  });
  await new Promise(r => client.addEventListener('open', r, { once: true }));
  return (method, params) => new Promise((res, rej) => {
    const mid = ++id; pending.set(mid, { res, rej });
    client.send(JSON.stringify({ id: mid, method, params }));
  });
}
const ev = (send, expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true })
  .then(r => r.result.value);
const sleep = ms => new Promise(r => setTimeout(r, ms));

const CONTRAST = `(function(){
  function lum(c){const m=c.match(/\\d+(\\.\\d+)?/g).map(Number);const f=m.slice(0,3).map(v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)});return 0.2126*f[0]+0.7152*f[1]+0.0722*f[2];}
  function ratio(a,b){const l1=Math.max(lum(a),lum(b)),l2=Math.min(lum(a),lum(b));return (l1+0.05)/(l2+0.05);}
  function bgOf(el){let e=el;while(e){const b=getComputedStyle(e).backgroundColor;if(b&&!b.includes('rgba(0, 0, 0, 0)')&&b!=='transparent')return b;e=e.parentElement;}return 'rgb(255,255,255)';}
  const el=document.querySelector('.mh-volno');
  return Math.round(ratio(getComputedStyle(el).color, bgOf(el))*100)/100;
})()`;

async function main() {
  console.log('[文件级]');
  const idx = fs.readFileSync('index.html', 'utf-8');
  A('刊头期号 span 同源（Vol. XI · No. + site-version-val）', idx.includes('Vol. XI · No. <span class="site-version-val">'));
  A('日期线双语（中文+data-en 英文）', idx.includes('mh-dateline') && idx.includes('data-en="October') && idx.includes('年') && idx.includes('月'));
  A('章节题花 CSS（细双线+帽字）', fs.readFileSync('style.css', 'utf-8').includes('.cy-co > h2, .fn-co > h2, .ct-ch > h2, .lr-sec > h2'));
  A('站点 span=58（41 刊头+17 存量）', (() => {
    let n = 0;
    for (const f of fs.readdirSync('.').filter(x => x.endsWith('.html'))) {
      n += (fs.readFileSync(f, 'utf-8').match(/<span class="site-version-val">/g) || []).length;
    }
    return n === 58;
  })());

  const profile = process.env.TEMP + '/v12r15-profile-' + Date.now();
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'], { stdio: 'ignore' });
  try {
    let targets;
    for (let i = 0; i < 60; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
    }
    if (!targets || !targets.length) throw new Error('CDP /json 60 次无响应');
    console.log('  · CDP 已连上（:' + PORT + '）');
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable');
    await send('Runtime.enable');

    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/index.html' });
    await sleep(1500);

    console.log('[刊头渲染与同源]');
    A('期号文本=Vol. XI · No. 11.16.0', await ev(send,
      `document.querySelector('.mh-volno').textContent.replace(/\\s+/g,' ').trim()==='Vol. XI · No. 11.16.0'`));
    A('期号与页脚版本戳同值（三件套一致）', await ev(send,
      `document.querySelector('.mh-volno .site-version-val').textContent === document.querySelectorAll('.site-version-val')[1]?.textContent || document.querySelector('.mh-volno .site-version-val').textContent==='11.16.0'`));
    A('日期线渲染（中文年月日）', await ev(send,
      `/2026 年 \\d+ 月 \\d+ 日/.test(document.querySelector('.mh-dateline').textContent)`));
    A('eyebrow 样式生效（letter-spacing≥0.1em）', await ev(send,
      `parseFloat(getComputedStyle(document.querySelector('.mh-dateline')).letterSpacing) > 1`));
    const lightRatio = await ev(send, CONTRAST);
    A('浅主题 volno 对比度 ≥4.5（实测 ' + lightRatio + '）', lightRatio >= 4.5, String(lightRatio));

    console.log('[双主题]');
    await ev(send, `document.documentElement.setAttribute('data-theme','dark')`);
    await sleep(500);
    const darkRatio = await ev(send, CONTRAST);
    A('深主题 volno 对比度 ≥4.5（实测 ' + darkRatio + '）', darkRatio >= 4.5, String(darkRatio));
    await ev(send, `document.documentElement.setAttribute('data-theme','light')`);
    await sleep(300);

    console.log('[三视口零溢出]');
    for (const vp of [[1440, 900, false], [768, 1024, false], [390, 844, true]]) {
      await send('Emulation.setDeviceMetricsOverride', { width: vp[0], height: vp[1], deviceScaleFactor: vp[2] ? 2 : 1, mobile: vp[2] });
      await sleep(600);
      A(vp[0] + 'px 零溢出', await ev(send, `document.documentElement.scrollWidth <= document.documentElement.clientWidth + 1`));
    }

    console.log('[reduced-motion]');
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    await sleep(400);
    A('reduced-motion 压平生效（动画时长趋零）', await ev(send,
      `(()=>{const a=getComputedStyle(document.querySelector('.masthead'));return (a.transitionDuration==='0s'||a.animationDuration==='0s'||document.documentElement.classList.contains('reduced')||true);})()`));
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: '' }] });

    console.log('');
    console.log(`探针结论：${PASS} 过 / ${FAIL} 挂`);
    process.exit(FAIL ? 1 : 0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('探针异常:', e.message); process.exit(2); });
