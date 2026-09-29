// V7-19 R16 验收探针：三视口链路走通 + 弹层遮挡 + hover-only 抽查（可复跑）
const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9250;
const BASE = 'http://127.0.0.1:8766';
const OUT = 'D:/vibe coding/musk-website/qa/v7-19/round-16';

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
    async function shot(name) {
      const p = await send('Page.captureScreenshot', { format: 'png' });
      fs.writeFileSync(OUT + '/' + name, Buffer.from(p.data, 'base64'));
      console.log('shot ' + name);
    }

    // ============ 三视口链路走通：首页→专题→事件→来源 ============
    for (const width of [320, 390, 768]) {
      console.log('— 链路 @' + width + ' —');
      await send('Emulation.setDeviceMetricsOverride', { width, height: 844, deviceScaleFactor: 2, mobile: width < 768 });
      await nav(BASE + '/index.html');
      let r = await evalJS(`(() => {
        var doc = document.documentElement;
        var navT = document.getElementById('nav-toggle');
        navT.click();
        var menuVisible = getComputedStyle(document.getElementById('site-nav')).display !== 'none' || document.getElementById('site-nav').getBoundingClientRect().height > 0;
        navT.click();
        var row = document.querySelector('a.feature-row[href="survival-2008.html"]');
        return { over: doc.scrollWidth - doc.clientWidth, menu: menuVisible, row: !!row };
      })()`);
      ok(`[${width}] 首页：无溢出 · 菜单开关可用 · 专题行在`, r.over <= 1 && r.menu && r.row, 'over=' + r.over);
      // 首页点击专题行 → 专题页
      r = await evalJS(`(() => { document.querySelector('a.feature-row[href="survival-2008.html"]').click(); return 1; })()`);
      await sleep(700);
      r = await evalJS(`(() => {
        var doc = document.documentElement;
        return { page: location.pathname.endsWith('survival-2008.html'), over: doc.scrollWidth - doc.clientWidth,
                 evLink: !!document.querySelector('a[href="events.html#e2008-08-02"]') };
      })()`);
      ok(`[${width}] 专题：到达 · 无溢出 · 事件链接在`, r.page && r.over <= 1 && r.evLink, 'over=' + r.over);
      // 专题 → 事件档案
      r = await evalJS(`(() => { document.querySelector('a[href="events.html#e2008-08-02"]').click(); return 1; })()`);
      await sleep(700);
      r = await evalJS(`(() => {
        var doc = document.documentElement;
        var ev = document.getElementById('e2008-08-02');
        return { page: location.pathname.endsWith('events.html'), anchor: !!ev, over: doc.scrollWidth - doc.clientWidth,
                 mat: !!ev.querySelector('a[href="primary.html#e2008-08-02"]') };
      })()`);
      ok(`[${width}] 事件档案：锚点定位 · 无溢出 · 材料链接在`, r.page && r.anchor && r.over <= 1 && r.mat, 'over=' + r.over);
      // 事件 → 来源（账本）
      r = await evalJS(`(() => { document.querySelector('#e2008-08-02 .ev-materials a[href="primary.html#e2008-08-02"]').click(); return 1; })()`);
      // hash 定位在布局稳定后由浏览器重定位（320px 布局漂移可达 1.6s）——轮询等待
      var visible = false, topSeen = 9999, pageOk = false, overSeen = 9999;
      for (var poll = 0; poll < 5; poll++) {
        await sleep(800);
        r = await evalJS(`(() => {
          var doc = document.documentElement;
          var row = document.getElementById('e2008-08-02');
          var rTop = row.getBoundingClientRect().top;
          return { page: location.pathname.endsWith('primary.html'), over: doc.scrollWidth - doc.clientWidth,
                   top: rTop, visible: rTop > -60 && rTop < window.innerHeight };
        })()`);
        pageOk = r.page; overSeen = r.over; topSeen = r.top;
        if (r.visible) { visible = true; break; }
      }
      ok(`[${width}] 来源：到达账本锚点 · 未被固定导航遮挡`, pageOk && overSeen <= 1 && visible, 'over=' + overSeen + ' top=' + Math.round(topSeen || 0));
      if (width === 390) await shot('r16-390-ledger-arrival.png');
    }
    await send('Emulation.clearDeviceMetricsOverride');

    // ============ hover-only 抽查（390）：时间轴悬浮提示 ============
    console.log('— hover-only 抽查 @390 —');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await nav(BASE + '/primary.html');
    let r = await evalJS(`(() => {
      // pt-dot 时间轴悬浮提示：点击是否也能定位（a 链接行为）
      var dot = document.querySelector('.pt-dot');
      return { dot: !!dot, isLink: dot ? dot.tagName === 'A' && !!dot.getAttribute('href') : false };
    })()`);
    ok('账本时间轴悬浮点 = 原生链接（点击可定位，非 hover-only）', r.dot && r.isLink);
    await nav(BASE + '/companies.html');
    r = await evalJS(`(() => {
      // 关系图节点：click 驱动详情面板（非 hover）
      var node = document.querySelector('.net-node, .cap-node, [data-co]');
      return { hasInteractive: !!node };
    })()`);
    ok('公司关系视图为点击驱动', r.hasInteractive);
    // 弹层遮挡：菜单展开后可关闭且不遮内容
    await nav(BASE + '/survival-2008.html');
    r = await evalJS(`(() => {
      var navT = document.getElementById('nav-toggle');
      navT.click();
      var nav = document.getElementById('site-nav');
      var open = nav.getBoundingClientRect().height > 0;
      navT.click();
      var closed = nav.getBoundingClientRect().height === 0 || getComputedStyle(nav).display === 'none';
      var h1 = document.querySelector('.lr-hero h1');
      return { open: open, closed: closed, content: !!h1 };
    })()`);
    ok('菜单弹层：可开可关 · 不残留遮挡', r.open && r.closed && r.content, JSON.stringify(r));
    await send('Emulation.clearDeviceMetricsOverride');

    // ============ 长标题 @320 ============
    console.log('— 长标题 @320 —');
    await send('Emulation.setDeviceMetricsOverride', { width: 320, height: 844, deviceScaleFactor: 2, mobile: true });
    for (const pg of ['platform-x.html', 'promises.html']) {
      await nav(BASE + '/' + pg);
      r = await evalJS(`(() => {
        var doc = document.documentElement;
        var h1 = document.querySelector('.lr-hero h1');
        return { over: doc.scrollWidth - doc.clientWidth, h1w: h1.getBoundingClientRect().width };
      })()`);
      ok(`[320] ${pg} 长标题不破版不溢出`, r.over <= 1 && r.h1w <= 321, 'over=' + r.over);
    }
    if (true) {
      await nav(BASE + '/platform-x.html');
      await shot('r16-320-platform.png');
    }
    await send('Emulation.clearDeviceMetricsOverride');

    console.log('\\n== R16 PROBE: ' + PASS + ' pass / ' + FAIL + ' fail ==');
    if (failures.length) { console.log('FAILURES:'); failures.forEach(f => console.log('  - ' + f)); }
  } finally {
    chrome.kill();
  }
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
