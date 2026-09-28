// R02 诊断：companies.html 390px 溢出元素定位（headless Chrome + CDP）
const { spawn } = require('child_process');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9223;

function getJSON(path) {
  return new Promise((res, rej) => {
    http.get({ host: '127.0.0.1', port: PORT, path }, r => {
      let d = '';
      r.on('data', c => d += c);
      r.on('end', () => res(JSON.parse(d)));
    }).on('error', rej);
  });
}

async function main() {
  const chrome = spawn(CHROME, [
    '--headless=new', '--disable-gpu', '--remote-debugging-port=' + PORT,
    '--window-size=390,844', '--no-first-run', 'about:blank',
  ], { stdio: 'ignore' });
  try {
    let targets;
    for (let i = 0; i < 30; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); break; } catch (e) {}
    }
    const ws = targets.find(t => t.type === 'page');
    const WebSocket = global.WebSocket;
    if (!WebSocket) throw new Error('no global WebSocket');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    let id = 0;
    const pending = new Map();
    const send = (method, params) => new Promise((res, rej) => {
      const mid = ++id;
      pending.set(mid, { res, rej });
      client.send(JSON.stringify({ id: mid, method, params }));
    });
    client.addEventListener('message', m => {
      const msg = JSON.parse(m.data);
      if (msg.id && pending.has(msg.id)) {
        const p = pending.get(msg.id);
        pending.delete(msg.id);
        msg.error ? p.rej(new Error(JSON.stringify(msg.error))) : p.res(msg.result);
      }
    });
    await new Promise(r => client.addEventListener('open', r, { once: true }));
    await send('Page.enable');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: 'http://127.0.0.1:8765/companies.html' });
    await new Promise(r => setTimeout(r, 3000));
    const probe = `(() => {
      const vw = document.documentElement.clientWidth;
      const out = { vw, scrollW: document.documentElement.scrollWidth, offenders: [] };
      document.querySelectorAll('*').forEach(el => {
        const r = el.getBoundingClientRect();
        if (r.width > vw + 1 || r.right > vw + 1) {
          out.offenders.push({
            tag: el.tagName, cls: (el.className||'').toString().slice(0,60),
            w: Math.round(r.width), right: Math.round(r.right),
            text: (el.textContent||'').trim().slice(0,30),
          });
        }
      });
      out.offenders = out.offenders.slice(0, 25);
      return JSON.stringify(out);
    })()`;
    const r = await send('Runtime.evaluate', { expression: probe, returnByValue: true });
    console.log(r.result.value);
    // 真 390px 视口截图（绕开 headless 最小窗宽 500 伪影）
    for (const url of process.argv.slice(2)) {
      await send('Page.navigate', { url: 'http://127.0.0.1:8765/' + url });
      await new Promise(r2 => setTimeout(r2, 2500));
      const shot = await send('Page.captureScreenshot', { format: 'png' });
      require('fs').writeFileSync('m390-' + url.replace(/\.html$/, '') + '.png', Buffer.from(shot.data, 'base64'));
      console.log('shot m390-' + url.replace(/\.html$/, '') + '.png');
    }
  } finally {
    chrome.kill();
  }
}
main().catch(e => { console.error('ERR', e.message); process.exit(1); });
