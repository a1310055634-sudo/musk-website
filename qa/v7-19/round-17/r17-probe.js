// V7-19 R17 探针：EN 切换回归 + 跨页语言保持 + EN 不破版（可复跑）
const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9253;
const BASE = 'http://127.0.0.1:8766';
const OUT = 'D:/vibe coding/musk-website/qa/v7-19/round-17';

let PASS = 0, FAIL = 0;
const failures = [];
function ok(name, cond, extra) {
  if (cond) { PASS++; console.log('  ok  ' + name); }
  else { FAIL++; failures.push(name + (extra ? ' | ' + extra : '')); console.log('  FAIL ' + name + (extra ? ' | ' + extra : '')); }
}
function getJSON(path) {
  return new Promise((res, rej) => {
    http.get({ host: '127.0.0.1', port: PORT, path }, r => {
      let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
    }).on('error', rej);
  });
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function main() {
  fs.mkdirSync(OUT, { recursive: true });
  const chrome = spawn(CHROME, [
    '--headless=new', '--disable-gpu', '--remote-debugging-port=' + PORT,
    '--window-size=1440,900', '--hide-scrollbars', '--no-first-run', 'about:blank',
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
    async function nav(url) {
      await send('Page.navigate', { url });
      await sleep(800);
    }
    async function toEN() {
      await evalJS(`(() => { var b = document.getElementById('lang-toggle'); if (b && b.textContent === 'EN') b.click(); return 1; })()`);
      await sleep(200);
    }
    async function toZH() {
      await evalJS(`(() => { var b = document.getElementById('lang-toggle'); if (b && b.textContent === '中文') b.click(); return 1; })()`);
      await sleep(200);
    }

    // ============ 1. EN 下关键交互不失效 ============
    console.log('— EN 交互回归 —');
    await nav(BASE + '/search.html');
    await toEN();
    let r = await evalJS(`(() => {
      const input = document.getElementById('sr-input');
      input.value = '圣诞夜';
      input.dispatchEvent(new Event('input'));
      return { count: document.getElementById('sr-count').textContent, items: document.querySelectorAll('.sr-item').length };
    })()`);
    ok('EN 检索：命中行英文格式', /hits/.test(r.count) && r.items >= 1, r.count);
    r = await evalJS(`(() => {
      const input = document.getElementById('sr-input');
      input.value = 'zzz无';
      input.dispatchEvent(new Event('input'));
      return document.getElementById('sr-count').textContent;
    })()`);
    ok('EN 空结果+清除按钮英文', /Clear filters/.test(r), r.slice(0, 60));
    await nav(BASE + '/timeline.html');
    await toEN();
    r = await evalJS(`(() => {
      var opt = document.querySelector('#gx-year option');
      return { firstOpt: opt ? opt.textContent : null };
    })()`);
    ok('EN 时间轴：年份选项英文（刷新路径）', r.firstOpt && /All years|by month/.test(r.firstOpt), JSON.stringify(r));
    await nav(BASE + '/events.html');
    await toEN();
    r = await evalJS(`(() => {
      var ev = document.getElementById('e2008-08-02');
      return { h2: ev.querySelector('.ev-title').getAttribute('data-en').slice(0, 30), mat: !!ev.querySelector('.ev-materials a[data-en]') };
    })()`);
    ok('EN 事件档案：标题英文 · 材料链接英文标签', /Falcon/.test(r.h2) && r.mat, JSON.stringify(r));

    // ============ 2. 跨页语言保持 ============
    console.log('— 跨页语言保持 —');
    await nav(BASE + '/index.html');
    await toEN();
    const trail = ['survival-2008.html', 'events.html', 'primary.html', 'search.html', 'index.html'];
    let allEN = true;
    for (const pg of trail) {
      await nav(BASE + '/' + pg);
      const lang = await evalJS(`document.documentElement.getAttribute('lang')`);
      const btn = await evalJS(`(document.getElementById('lang-toggle')||{}).textContent`);
      if (lang !== 'en' || btn !== '中文') { allEN = false; console.log('   broke at', pg, lang, btn); }
    }
    ok('EN 状态跨 5 页跳转保持（含返回首页）', allEN);
    await toZH();
    r = await evalJS(`document.documentElement.getAttribute('lang')`);
    ok('切回中文恢复 zh-CN', r === 'zh-CN', r);

    // ============ 3. EN 长文本不破版 ============
    console.log('— EN 不破版 —');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    for (const pg of ['controversy.html', 'reading.html', 'promises.html']) {
      await nav(BASE + '/' + pg);
      await toEN();
      r = await evalJS(`(() => {
        var doc = document.documentElement;
        return { over: doc.scrollWidth - doc.clientWidth };
      })()`);
      ok(`[390 EN] ${pg} 英文长段不横向溢出`, r.over <= 1, 'over=' + r.over);
      await toZH();
    }
    await send('Emulation.clearDeviceMetricsOverride');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await nav(BASE + '/controversy.html');
    await toEN();
    await shot('r17-en-controversy.png');
    await send('Emulation.clearDeviceMetricsOverride');
    async function shot(name) {
      const p = await send('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(OUT + '/' + name, Buffer.from(p.data, 'base64'));
      console.log('shot', name);
    }

    // ============ 4. 切回中文完整性（缓存机制） ============
    await nav(BASE + '/controversy.html');
    await toEN();
    await toZH();
    r = await evalJS(`(() => {
      var p = document.querySelector('#sec-pedo p.ct-t');
      return { zh: p.textContent.includes('睡谷救援'), en: !p.textContent.includes('Background.') };
    })()`);
    ok('切回中文：原文完整恢复（缓存往返）', r.zh && r.en, JSON.stringify(r));

    console.log('\\n== R17 PROBE: ' + PASS + ' pass / ' + FAIL + ' fail ==');
    if (failures.length) { console.log('FAILURES:'); failures.forEach(f => console.log('  - ' + f)); }
  } finally {
    chrome.kill();
  }
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
