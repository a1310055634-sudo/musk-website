// V9-20 R17: CDP 定位截图（支持 CSS 选择器）——滚动到图形区后截当前视口。
// 用法: node tools/v9r17-shot.js <page> <selector> <w> <h> <outfile> [port]
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = Number(process.argv[7] || 9361);
const [,, pageArg, sel, w, h, out] = process.argv;
if (!pageArg || !sel || !w || !h || !out) { console.error('args: <page> <selector> <w> <h> <outfile> [port]'); process.exit(2); }

function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => {
    let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d))); });
  req.on('timeout', () => req.destroy(new Error('timeout'))); req.on('error', rej); }); }

async function main() {
  const profile = process.env.TEMP + '/v9r17-shot-' + Date.now() + '-' + Math.random().toString(36).slice(2, 7);
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    `--window-size=${w},${h}`, '--no-first-run', 'about:blank'], { stdio: 'ignore' });
  let targets;
  for (let i = 0; i < 60; i++) {
    await new Promise(r => setTimeout(r, 500));
    try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
  }
  if (!targets || !targets.length) throw new Error('CDP 无响应');
  const ws = targets.find(t => t.type === 'page');
  const client = new WebSocket(ws.webSocketDebuggerUrl);
  let id = 0; const pend = new Map();
  client.addEventListener('message', m => { const msg = JSON.parse(m.data);
    if (msg.id && pend.has(msg.id)) { const p = pend.get(msg.id); pend.delete(msg.id);
      msg.error ? p.rej(new Error(JSON.stringify(msg.error))) : p.res(msg.result); } });
  await new Promise(r => client.addEventListener('open', r, { once: true }));
  const send = (method, params) => new Promise((res, rej) => { const mid = ++id;
    pend.set(mid, { res, rej }); client.send(JSON.stringify({ id: mid, method, params })); });
  await send('Page.enable');
  await send('Emulation.setDeviceMetricsOverride',
    { width: Number(w), height: Number(h), deviceScaleFactor: 1, mobile: Number(w) < 500 });
  await send('Page.navigate', { url: `http://127.0.0.1:8766/${pageArg}` });
  await new Promise(r => setTimeout(r, 2000));
  const r = await send('Runtime.evaluate', { expression:
    `(()=>{const el=document.querySelector(${JSON.stringify(sel)});
      if(!el) return 'MISS';
      el.scrollIntoView({block:'center'}); return 'OK';})()`, returnByValue: true });
  if (r.result.value !== 'OK') throw new Error('selector MISS: ' + sel);
  await new Promise(r2 => setTimeout(r2, 900));
  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(out, Buffer.from(shot.data, 'base64'));
  console.log(out, fs.statSync(out).size + 'B');
  client.close(); chrome.kill(); process.exit(0);
}
main().catch(e => { console.error('SHOT ERROR', e.message); process.exit(1); });
