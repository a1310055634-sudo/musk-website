// V9-20 R05: CDP 定位截图（可配 base，用于 before worktree 端口）
// 用法: node tools/v9r05-shot.js <page[#anchor]> <w> <h> <outfile> [port] [base]
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = Number(process.argv[6] || 9342);
const BASE = process.argv[7] || 'http://127.0.0.1:8766';
const [,, pageArg, w, h, out] = process.argv;
if (!pageArg || !w || !h || !out) { console.error('args: <page[#anchor]> <w> <h> <outfile> [port] [base]'); process.exit(2); }

function getJSON(path) { return new Promise((res, rej) => {
  const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => {
    let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d))); });
  req.on('timeout', () => req.destroy(new Error('timeout'))); req.on('error', rej); }); }

async function main() {
  const profile = process.env.TEMP + '/v9r05-shot-' + Date.now();
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
  await send('Page.navigate', { url: `${BASE}/${pageArg}` });
  await new Promise(r => setTimeout(r, 1800));
  const anchor = pageArg.includes('#') ? pageArg.split('#')[1] : null;
  if (anchor) {
    await send('Runtime.evaluate', { expression:
      `document.getElementById('${anchor}').scrollIntoView({block:'start'});` +
      `window.scrollBy(0,-20); 'scrolled'` });
    await new Promise(r => setTimeout(r, 900));
  }
  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.writeFileSync(out, Buffer.from(shot.data, 'base64'));
  console.log(out, fs.statSync(out).size + 'B');
  client.close(); chrome.kill(); process.exit(0);
}
main().catch(e => { console.error('SHOT ERROR', e.message); process.exit(1); });
