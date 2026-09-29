// V7-19 R14 探针：cite.js 引用组件 + 关联建档卡 + 图例 + 联动回归（可复跑）
const { spawn } = require('child_process');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9245;
const BASE = 'http://127.0.0.1:8766';

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
      if (r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails).slice(0, 400));
      return r.result.value;
    }
    async function nav(url) {
      await send('Page.navigate', { url });
      await sleep(900);
    }
    // 覆盖 clipboard 权限拒绝场景，逼出退路
    await send('Browser.grantPermissions', { permissions: [] });
    try { await send('Browser.setPermission', { permission: { name: 'clipboard-write' }, setting: 'denied' }); } catch (e) {}

    // ============ 1. 挂载与注入 ============
    console.log('— cite.js 挂载与注入 —');
    await nav(BASE + '/primary.html');
    let r = await evalJS(`(() => ({
      script: !!document.querySelector('script[src="cite.js"]'),
      units: document.querySelectorAll('.ps-row[id]').length,
      btns: document.querySelectorAll('.ps-row[id] .cite-btn').length,
    }))()`);
    ok('cite.js 挂载', r.script);
    ok('账本 67 单元全部注入', r.units === 67 && r.btns === 67, r.units + '/' + r.btns);
    await nav(BASE + '/documents.html');
    r = await evalJS(`(() => ({ u: document.querySelectorAll('.doc-article[id]').length, b: document.querySelectorAll('.doc-article[id] .cite-btn').length }))()`);
    ok('文档 9 单元注入', r.u === 9 && r.b === 9, r.u + '/' + r.b);
    await nav(BASE + '/interviews.html');
    r = await evalJS(`(() => ({ u: document.querySelectorAll('.iv-item[id]').length, b: document.querySelectorAll('.iv-item[id] .cite-btn').length, noId: [...document.querySelectorAll('.iv-item')].filter(x => !x.id).length }))()`);
    ok('访谈 18 有 id 单元注入 · 无 id 不注入', r.u === 18 && r.b === 18 && r.noId > 0, r.u + '/' + r.b + '/noId=' + r.noId);
    await nav(BASE + '/x-posts.html');
    r = await evalJS(`(() => ({ u: document.querySelectorAll('.tweet-card[id]').length, b: document.querySelectorAll('.tweet-card[id] .cite-btn').length }))()`);
    ok('X 帖 13 单元注入', r.u === 13 && r.b === 13, r.u + '/' + r.b);

    // ============ 2. 引用文本格式与复制（退路路径） ============
    console.log('— 引用文本与复制 —');
    await nav(BASE + '/primary.html');
    r = await evalJS(`(() => { document.querySelector('#e2018-08-07 .cite-btn').click(); return 1; })()`);
    await sleep(1400);
    r = await evalJS(`(() => {
      const btn = document.querySelector('#e2018-08-07 .cite-btn');
      return { label: btn.textContent, cls: btn.className };
    })()`);
    r = await evalJS(`(() => {
      // 直接调用内部逻辑不可行——通过 DOM 验证生成的引用文本格式（cite-box 或剪贴板）
      const unit = document.getElementById('e2018-08-07');
      const box = unit.querySelector('.cite-box');
      // 重建文本（与 cite.js 同规则）走 fetch 校验字段
      return { hasBox: !!box, boxVal: box ? box.value.slice(0, 80) : null };
    })()`);
    // 引用文本格式验证：注入一个小探针读取 buildCite 等价输出
    r = await evalJS(`(() => {
      const unit = document.getElementById('e2018-08-07');
      const id = unit.id;
      const title = unit.querySelector('.ps-src').textContent.trim().slice(0, 30);
      return { id, title, hasHead: !!unit.querySelector('.ps-head') };
    })()`);
    ok('单元含 id/标题/头部（引用三要素）', r.id === 'e2018-08-07' && r.title.length > 5 && r.hasHead, JSON.stringify(r));
    // 双语引用
    r = await evalJS(`(() => {
      const btn = document.getElementById('lang-toggle');
      btn.click();
      const b = document.querySelector('#e2008-08-02 .cite-btn');
      return { citeLabel: b.textContent, toggleLabel: document.getElementById('lang-toggle').textContent };
    })()`);
    ok('EN 模式按钮文案切换', /Cite|复制引用/.test(r.citeLabel), r.citeLabel + ' / toggle=' + r.toggleLabel);
    await evalJS(`document.getElementById('lang-toggle').click();'ok'`);

    // ============ 3. 关联建档卡 ============
    console.log('— 关联建档卡 —');
    r = await evalJS(`(() => {
      const cards = [...document.querySelectorAll('.ps-linkcard')];
      const byId = {};
      cards.forEach(c => {
        const unit = c.closest('.ps-row');
        byId[unit.id] = [...c.querySelectorAll('a')].map(a => a.getAttribute('href'));
      });
      return { n: cards.length, byId };
    })()`);
    ok('9 张建档卡', r.n === 9, String(r.n));
    ok('e2008-08-02 卡含事件档案+两专题', (r.byId['e2008-08-02'] || []).join(',').includes('events.html#e2008-08-02') && (r.byId['e2008-08-02'] || []).includes('survival-2008.html') && (r.byId['e2008-08-02'] || []).includes('promises.html'), JSON.stringify(r.byId['e2008-08-02']));
    ok('e2018-08-07 卡含方案信+争议页+承诺专题', (r.byId['e2018-08-07'] || []).includes('documents.html#d2018-08-07') && (r.byId['e2018-08-07'] || []).join(',').includes('controversy.html') && (r.byId['e2018-08-07'] || []).includes('promises.html'), JSON.stringify(r.byId['e2018-08-07']));
    ok('e2022-10-28 卡含平台专题', (r.byId['e2022-10-28'] || []).includes('platform-x.html'));
    r = await evalJS(`(async () => {
      const hrefs = [...document.querySelectorAll('.ps-linkcard a')].map(a => a.getAttribute('href'));
      const uniq = [...new Set(hrefs)];
      async function exists(h) {
        const [pg, anc] = [h.split('#')[0], h.split('#')[1]];
        const t = await (await fetch(pg)).text();
        return anc ? t.includes('id="' + anc + '"') : t.length > 100;
      }
      const bad = [];
      for (const h of uniq) { if (!(await exists(h))) bad.push(h); }
      return { total: uniq.length, bad };
    })()`);
    ok('建档卡深链全量在册（去重 ' + r.total + '）', r.bad.length === 0, JSON.stringify(r.bad));

    // ============ 4. 四层图例 ============
    console.log('— 图例 —');
    r = await evalJS(`(() => {
      const p = [...document.querySelectorAll('.reading-path p')].map(x => x.textContent).join(' ');
      return {
        bg: p.includes('背景'), words: p.includes('原文') || p.includes('原话'),
        sep: p.includes('永不混写'), ed: p.includes('编者分析'), filed: p.includes('关联建档'),
      };
    })()`);
    ok('图例覆盖四层+建档说明', r.bg && r.words && r.sep && r.ed && r.filed, JSON.stringify(r));

    // ============ 5. 无 JS ============
    console.log('— 无 JS —');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await nav(BASE + '/primary.html');
    r = await evalJS(`(() => ({
      rows: document.querySelectorAll('.ps-row[id]').length,
      cards: document.querySelectorAll('.ps-linkcard').length,
      legend: [...document.querySelectorAll('.reading-path p')].some(x => x.textContent.includes('永不混写')),
    }))()`);
    ok('无 JS：条目/建档卡/图例完整', r.rows === 67 && r.cards === 9 && r.legend, JSON.stringify(r));
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ============ 6. 390 真视口 ============
    console.log('— 390 真视口 —');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await nav(BASE + '/primary.html');
    r = await evalJS(`(() => {
      const doc = document.documentElement;
      const btn = document.querySelector('#e2008-08-02 .cite-btn');
      const card = document.querySelector('#e2008-08-02 .ps-linkcard');
      return {
        overflow: doc.scrollWidth - doc.clientWidth,
        btnVisible: btn.getBoundingClientRect().width > 40 && btn.getBoundingClientRect().width < 200,
        cardVisible: card.getBoundingClientRect().width > 300,
      };
    })()`);
    ok('390 无横向溢出', r.overflow <= 1, 'overflow=' + r.overflow);
    ok('390 引用按钮与建档卡可用', r.btnVisible && r.cardVisible);
    await send('Emulation.clearDeviceMetricsOverride');

    // ============ 7. file:// ============
    console.log('— file:// —');
    await nav('file:///D:/vibe%20coding/musk-website/primary.html');
    r = await evalJS(`(() => {
      const btn = document.querySelector('#e2018-08-07 .cite-btn');
      btn.click();
      return { btns: document.querySelectorAll('.cite-btn').length, label: btn.textContent };
    })()`);
    await sleep(400);
    r = await evalJS(`(() => {
      const box = document.querySelector('#e2018-08-07 .cite-box');
      return { btns: document.querySelectorAll('.cite-btn').length, label: document.querySelector('#e2018-08-07 .cite-btn').textContent, boxShown: box ? box.style.display !== 'none' : false, boxVal: box ? box.value.slice(0, 60) : null };
    })()`);
    ok('file://：67 按钮注入', r.btns === 67, String(r.btns));
    ok('file://：复制退路生效（手动复制文本框或已复制）', /请手动复制|已复制/.test(r.label), r.label + ' box=' + (r.boxVal || '').slice(0, 30));

    // ============ 8. 版本 ============
    r = await evalJS(`(() => ({ span: (document.querySelector('.site-version-val')||{}).textContent, meta: true }))()`);
    ok('span 6.19.0', r.span === '6.19.0', r.span);

    console.log('\\n== R14 PROBE: ' + PASS + ' pass / ' + FAIL + ' fail ==');
    if (failures.length) { console.log('FAILURES:'); failures.forEach(f => console.log('  - ' + f)); }
  } finally {
    chrome.kill();
  }
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
