// V7-19 R16 全站多视口扫描：37 页 × 320/390/768（横向溢出/触摸目标/遮挡）可复跑
const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9249;
const BASE = 'http://127.0.0.1:8766';

function getJSON(path) {
  return new Promise((res, rej) => {
    http.get({ host: '127.0.0.1', port: PORT, path }, r => {
      let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
    }).on('error', rej);
  });
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  const chrome = spawn(CHROME, [
    '--headless=new', '--disable-gpu', '--remote-debugging-port=' + PORT,
    '--window-size=1440,900', '--no-first-run', 'about:blank',
  ], { stdio: 'ignore' });
  try {
    let targets;
    for (let i = 0; i < 30; i++) {
      await sleep(500);
      try { targets = await getJSON('/json'); break; } catch (e) {}
    }
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    let id = 0; const pending = new Map();
    const send = (method, params = {}) => new Promise((res, rej) => {
      const mid = ++id; pending.set(mid, { res, rej });
      client.send(JSON.stringify({ id: mid, method, params }));
    });
    client.addEventListener('message', m => {
      const msg = JSON.parse(m.data);
      if (msg.id && pending.has(msg.id)) {
        const p = pending.get(msg.id); pending.delete(msg.id);
        msg.error ? p.rej(new Error(JSON.stringify(msg.error))) : p.res(msg.result);
      }
    });
    await new Promise(r => client.addEventListener('open', r));
    await send('Page.enable');
    await send('Runtime.enable');
    async function evalJS(expr) {
      const r = await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true });
      if (r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails).slice(0, 300));
      return r.result.value;
    }

    const pages = fs.readFileSync('D:/vibe coding/v7r16-work/pages.txt', 'utf-8').trim().split('\n');
    const issues = [];
    let pagesDone = 0;

    for (const width of [320, 390, 768]) {
      await send('Emulation.setDeviceMetricsOverride', { width, height: 844, deviceScaleFactor: 2, mobile: width < 768 });
      for (const pg of pages) {
        await send('Page.navigate', { url: BASE + '/' + pg });
        await sleep(width === 320 ? 500 : 420);
        const r = await evalJS(`(() => {
          var doc = document.documentElement;
          var over = doc.scrollWidth - doc.clientWidth;
          var offenders = [];
          if (over > 1) {
            document.querySelectorAll('body *').forEach(function (el) {
              var r = el.getBoundingClientRect();
              if (r.right > doc.clientWidth + 2 && r.width > 8 && r.height > 4) {
                var tag = el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : '');
                if (offenders.indexOf(tag) < 0 && offenders.length < 5) offenders.push(tag + '@' + Math.round(r.right));
              }
            });
          }
          return { over: over, offenders: offenders };
        })()`);
        if (r.over > 1) issues.push(`[${width}] ${pg} 横向溢出 ${r.over}px ← ${r.offenders.join(' | ')}`);
        pagesDone++;
      }
      console.log(`-- ${width}px done (${pages.length} pages) --`);
    }

    // 390px 触摸目标抽查（按钮类控件）
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    for (const pg of ['index.html', 'survival-2008.html', 'events.html', 'timeline.html', 'primary.html', 'search.html', 'capital-evolution.html']) {
      await send('Page.navigate', { url: BASE + '/' + pg });
      await sleep(600);
      const r = await evalJS(`(() => {
        var small = [];
        document.querySelectorAll('button, .sr-types button, .cap-chip, .gx-chip, .sr-evbtn, .cite-btn, .lang-toggle, .nav-toggle').forEach(function (el) {
          var r = el.getBoundingClientRect();
          if (r.width === 0 || r.height === 0) return;
          var st = getComputedStyle(el);
          if (st.visibility === 'hidden' || st.display === 'none') return;
          if (r.width < 30 || r.height < 22) {
            var tag = el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + String(el.className).split(' ')[0] : '');
            if (small.indexOf(tag) < 0 && small.length < 6) small.push(tag + ' ' + Math.round(r.width) + 'x' + Math.round(r.height));
          }
        });
        return small;
      })()`);
      if (r.length) issues.push(`[390-touch] ${pg} 小目标: ${r.join(' | ')}`);
    }

    console.log('SCAN COMPLETE. pages×viewports = ' + pagesDone);
    if (issues.length) {
      console.log('ISSUES (' + issues.length + '):');
      issues.forEach(x => console.log('  ' + x));
    } else {
      console.log('NO ISSUES FOUND');
    }
    fs.writeFileSync('D:/vibe coding/v7r16-work/scan-result.txt', issues.join('\n') || 'NO ISSUES');
  } finally {
    chrome.kill();
  }
}
main().catch(e => { console.error('SCAN ERROR', e); process.exit(2); });
