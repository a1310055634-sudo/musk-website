// V9-20 R15 截图器：设计系统升级 before/after 对比
// 用法: node tools/v9r15-shot.js <outdir>
// 矩阵：4 页 (index / survival-2008 / timeline / capital-evolution) x 2 视口 (1440x900 / 390x844) x 2 语言 (zh / en)
// 全页截图（captureBeyondViewport），强制 prefers-reduced-motion 冻结入场动画，等字体与 SVG 就绪。
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const path = require('path');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = Number(process.env.R15_PORT || 9361);
const BASE = 'http://127.0.0.1:8766';
const OUT = process.argv[2];
if (!OUT) { console.error('usage: node tools/v9r15-shot.js <outdir>'); process.exit(2); }

const PAGES = ['index', 'survival-2008', 'timeline', 'capital-evolution'];
const VIEWPORTS = [['desktop', 1440, 900], ['mobile', 390, 844]];
const LANGS = ['zh', 'en'];
const MAXH = 7000;

function getJSON(p) {
  return new Promise((res, rej) => {
    const req = http.get({ host: '127.0.0.1', port: PORT, path: p, timeout: 3000 }, r => {
      let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
    });
    req.on('timeout', () => req.destroy(new Error('timeout')));
    req.on('error', rej);
  });
}

async function main() {
  fs.mkdirSync(OUT, { recursive: true });
  const profile = (process.env.TEMP || '/tmp') + '/v9r15-shot-' + Date.now();
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', '--hide-scrollbars', 'about:blank'],
    { stdio: 'ignore' });

  let targets;
  for (let i = 0; i < 60; i++) {
    await new Promise(r => setTimeout(r, 500));
    try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
  }
  if (!targets || !targets.length) throw new Error('CDP no response');
  const ws = targets.find(t => t.type === 'page');
  const client = new WebSocket(ws.webSocketDebuggerUrl);
  let id = 0; const pend = new Map();
  client.addEventListener('message', m => {
    const msg = JSON.parse(m.data);
    if (msg.id && pend.has(msg.id)) { const p = pend.get(msg.id); pend.delete(msg.id);
      msg.error ? p.rej(new Error(JSON.stringify(msg.error))) : p.res(msg.result); }
  });
  await new Promise(r => client.addEventListener('open', r, { once: true }));
  const send = (method, params) => new Promise((res, rej) => {
    const mid = ++id; pend.set(mid, { res, rej });
    client.send(JSON.stringify({ id: mid, method, params }));
  });
  const ev = (expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true }).then(r => r.result.value);

  await send('Page.enable');
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });

  let n = 0, fail = 0;
  for (const [vtag, w, h] of VIEWPORTS) {
    for (const lang of LANGS) {
      for (const page of PAGES) {
        // 先在同源下写入语言偏好，再加载目标页
        await send('Page.navigate', { url: BASE + '/index.html' });
        await new Promise(r => setTimeout(r, 350));
        await ev(`try{localStorage.setItem('musk-inc-lang','${lang}')}catch(e){}`);
        await send('Emulation.setDeviceMetricsOverride',
          { width: w, height: h, deviceScaleFactor: 1, mobile: w < 500 });
        await send('Page.navigate', { url: BASE + '/' + page + '.html' });
        await new Promise(r => setTimeout(r, 1600));
        await ev('document.fonts && document.fonts.ready');
        await new Promise(r => setTimeout(r, 300));
        const full = await ev('Math.min(document.documentElement.scrollHeight, ' + MAXH + ')');
        const sh = Number(full) || h;
        await send('Emulation.setDeviceMetricsOverride',
          { width: w, height: sh, deviceScaleFactor: 1, mobile: w < 500 });
        await new Promise(r => setTimeout(r, 500));
        const shot = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: true });
        const file = path.join(OUT, `${page}-${vtag}-${lang}.png`);
        fs.writeFileSync(file, Buffer.from(shot.data, 'base64'));
        const sz = fs.statSync(file).size;
        const ok = sz > 10000;
        if (!ok) fail++;
        console.log((ok ? 'OK  ' : 'FAIL') + ` ${page}-${vtag}-${lang}.png ${sz}B (h=${sh})`);
        n++;
      }
    }
  }
  console.log(`done ${n} shots, ${fail} fail`);
  client.close(); chrome.kill(); process.exit(fail ? 1 : 0);
}
main().catch(e => { console.error('SHOT ERROR', e.message); process.exit(1); });
