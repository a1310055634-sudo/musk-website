// V12-20 R02 QA 截图：x-posts.html 新卡区（桌面 1440 + 390），滚到 2026 组入画
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9350;
const BASE = 'http://127.0.0.1:8766';
const OUT = 'qa/v12/round-04';

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

async function main() {
  fs.mkdirSync(OUT, { recursive: true });
  const profile = process.env.TEMP + '/v12r04shot-' + Date.now();
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'], { stdio: 'ignore' });
  try {
    let targets;
    for (let i = 0; i < 60; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
    }
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable');

    // 桌面：滚到 2026 年份条居中
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/x-posts.html#p2008-12-23' });
    await new Promise(r => setTimeout(r, 1800));
    await send('Runtime.evaluate', { expression: `document.getElementById('p2008-12-23').scrollIntoView({block:'center'})` });
    await new Promise(r => setTimeout(r, 400));
    const shot1 = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(OUT + '/desktop-2008crs.png', Buffer.from(shot1.data, 'base64'));
    console.log('saved desktop-2008crs.png');

    // 390：同一位置
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await new Promise(r => setTimeout(r, 800));
    await send('Runtime.evaluate', { expression: `document.getElementById('p2008-12-23').scrollIntoView({block:'start'})` });
    await new Promise(r => setTimeout(r, 400));
    const shot2 = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(OUT + '/mobile-390-2008crs.png', Buffer.from(shot2.data, 'base64'));
    console.log('saved mobile-390-2008crs.png');
    process.exit(0);
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
}
main().catch(e => { console.error('shot 异常:', e.message); process.exit(2); });
