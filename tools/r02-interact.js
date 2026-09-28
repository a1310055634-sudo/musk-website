// R02 交互验收：EN 切换 / lazy 与尺寸声明 / 图片自然加载
const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9224;

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
    '--window-size=1440,900', '--no-first-run', 'about:blank',
  ], { stdio: 'ignore' });
  try {
    let targets;
    for (let i = 0; i < 30; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); break; } catch (e) {}
    }
    const page = targets.find(t => t.type === 'page');
    const client = new WebSocket(page.webSocketDebuggerUrl);
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
    const evalJs = async expr => {
      const r = await send('Runtime.evaluate', { expression: expr, returnByValue: true });
      return r.result.value;
    };

    // 1) index: EN 切换后封面署名行
    await send('Page.navigate', { url: 'http://127.0.0.1:8765/index.html' });
    await new Promise(r => setTimeout(r, 2000));
    console.log('index zh caption:', await evalJs(`document.querySelector('.cover-portrait figcaption').textContent.trim()`));
    await evalJs(`document.getElementById('lang-toggle').click()`);
    await new Promise(r => setTimeout(r, 400));
    console.log('index en caption:', await evalJs(`document.querySelector('.cover-portrait figcaption').textContent.trim()`));
    console.log('index cover img fetchpriority:', await evalJs(`document.querySelector('.cover-portrait img').getAttribute('fetchpriority')`));

    // 2) companies: 全部卡片图有 width/height/lazy/figcaption
    await send('Page.navigate', { url: 'http://127.0.0.1:8765/companies.html' });
    await new Promise(r => setTimeout(r, 2000));
    console.log('companies imgs:', await evalJs(`JSON.stringify([...document.querySelectorAll('.company-card img')].map(i => ({
      src: i.getAttribute('src'), w: i.width, h: i.height, lazy: i.loading === 'lazy',
      cap: !!i.closest('figure').querySelector('figcaption'),
      ratio: Math.abs(i.getBoundingClientRect().width / i.getBoundingClientRect().height - 1.5) < 0.02,
    })))`));

    // 3) indepth: falcon 取景位置 + 懒加载滚动后 complete
    await send('Page.navigate', { url: 'http://127.0.0.1:8765/indepth.html' });
    await new Promise(r => setTimeout(r, 2000));
    await evalJs(`document.querySelectorAll('.feature-photo img')[1].scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 1200));
    console.log('indepth falcon:', await evalJs(`(() => { const i = document.querySelectorAll('.feature-photo img')[1];
      return JSON.stringify({ src: i.getAttribute('src'), complete: i.complete, natural: i.naturalWidth + 'x' + i.naturalHeight, pos: i.style.objectPosition }); })()`));
  } finally {
    chrome.kill();
  }
}
main().catch(e => { console.error('ERR', e.message); process.exit(1); });
