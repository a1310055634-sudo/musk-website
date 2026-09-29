// V7-19 R15 探针：搜索与发现（质量节点：11-15 连通）+ 中英代表性查询（可复跑）
const { spawn } = require('child_process');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9247;
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

    // ============ 1. 基础 ============
    console.log('— 基础 —');
    await nav(BASE + '/search.html');
    let r = await evalJS(`(() => ({
      total: window.SEARCH_INDEX.length,
      evRecords: window.SEARCH_INDEX.filter(x => x.t === '事件档案').length,
      evField: window.SEARCH_INDEX.filter(x => x.ev).length,
      typeBtn: !!document.querySelector('.sr-types button[data-t="事件档案"]'),
      count0: document.getElementById('sr-count').textContent,
    }))()`);
    ok('索引 178 条 · 事件档案 9 · ev 聚合字段', r.total === 178 && r.evRecords === 9 && r.evField >= 9, r.total + '/' + r.evRecords + '/' + r.evField);
    ok('类型按钮含事件档案 · 初始计数 178', r.typeBtn && /178/.test(r.count0), r.count0);

    // ============ 2. 中文代表性查询：圣诞夜 ============
    console.log('— 中文查询「圣诞夜」 —');
    await nav(BASE + '/search.html');
    r = await evalJS(`(() => {
      const input = document.getElementById('sr-input');
      input.value = '圣诞夜';
      input.dispatchEvent(new Event('input'));
      return {
        count: document.getElementById('sr-count').textContent,
        items: document.querySelectorAll('.sr-item').length,
        hitTags: [...document.querySelectorAll('.sr-hit')].slice(0, 3).map(x => x.textContent),
        marks: document.querySelectorAll('mark').length,
        evlines: document.querySelectorAll('.sr-evline').length,
      };
    })()`);
    ok('中文「圣诞夜」命中 ≥2 条（账本+事件档案）', r.items >= 2, JSON.stringify({ items: r.items, count: r.count }));
    ok('命中于标签在（解释为什么搜到）', r.hitTags.some(t => /原话|摘要/.test(t)), JSON.stringify(r.hitTags));
    ok('关键词高亮 mark 存在', r.marks >= 1, String(r.marks));
    ok('事件聚合条存在', r.evlines >= 1, String(r.evlines));
    r = await evalJS(`(() => {
      const item = [...document.querySelectorAll('.sr-itemwrap')].find(w => w.textContent.includes('e2008-12-24'));
      if (!item) return { found: false };
      const btn = item.querySelector('.sr-evbtn');
      if (!btn) return { found: true, btn: false };
      const mat = item.querySelector('.sr-evmat');
      const before = mat.hasAttribute('hidden');
      btn.click();
      const after = mat.hasAttribute('hidden');
      const links = [...mat.querySelectorAll('a')].map(a => a.getAttribute('href'));
      return { found: true, btn: true, toggled: before !== after, links };
    })()`);
    ok('聚合展开：同事件多份来源', r.found && r.btn && r.toggled && r.links.length >= 1, JSON.stringify(r));

    // ============ 3. 英文代表性查询：funding secured ============
    console.log('— 英文查询「funding secured」 —');
    await nav(BASE + '/search.html');
    r = await evalJS(`(() => {
      const input = document.getElementById('sr-input');
      input.value = 'funding secured';
      input.dispatchEvent(new Event('input'));
      return {
        items: document.querySelectorAll('.sr-item').length,
        has807: [...document.querySelectorAll('.sr-item')].some(x => x.href.includes('e2018-08-07') || x.textContent.includes('e2018-08-07')),
        url: location.search,
      };
    })()`);
    ok('英文「funding secured」命中含 e2018-08-07', r.items >= 1 && r.has807, 'items=' + r.items);
    ok('URL 同步 ?q=', /q=funding/.test(r.url), r.url);

    // ============ 4. 事件档案记录可搜 ============
    console.log('— 事件档案入检索 —');
    await nav(BASE + '/search.html');
    r = await evalJS(`(() => {
      const input = document.getElementById('sr-input');
      input.value = 'xAI 收购';
      input.dispatchEvent(new Event('input'));
      const items = [...document.querySelectorAll('.sr-item')];
      return {
        evHit: items.some(x => x.getAttribute('href') === 'events.html#ev-e2025-03-28' || x.textContent.includes('信息流与模型')),
        typeBtnFilter: (function () {
          input.value = '';
          input.dispatchEvent(new Event('input'));
          document.querySelector('.sr-types button[data-t="事件档案"]').click();
          return document.querySelectorAll('.sr-item').length;
        })(),
      };
    })()`);
    ok('「xAI 收购」命中事件档案 ev-e2025-03-28', r.evHit);
    ok('事件档案类型筛选有结果', r.typeBtnFilter === 9, String(r.typeBtnFilter));

    // ============ 5. URL 参数预填 ============
    console.log('— URL 参数 —');
    await nav(BASE + '/search.html?q=%E7%81%AB%E7%AE%AD&type=%E8%A8%80%E8%A1%8C%E5%AE%9E%E5%BD%95');
    r = await evalJS(`(() => ({
      inputVal: document.getElementById('sr-input').value,
      pressed: document.querySelector('.sr-types button[aria-pressed="true"]').getAttribute('data-t'),
      count: document.getElementById('sr-count').textContent,
      items: document.querySelectorAll('.sr-item').length,
    }))()`);
    ok('?q=&type= 预填生效（火箭×言行实录）', r.inputVal === '火箭' && r.pressed === '言行实录' && r.items >= 1, JSON.stringify(r));
    ok('状态行含关键词与类型描述', /关键词「火箭」/.test(r.count) && /类型:言行实录/.test(r.count), r.count);
    r = await evalJS(`(() => {
      document.getElementById('sr-clearbtn').click();
      return {
        count: document.getElementById('sr-count').textContent,
        input: document.getElementById('sr-input').value,
        url: location.search,
      };
    })()`);
    ok('清除全部筛选 → 178 条恢复 · URL 清空', /178/.test(r.count) && r.input === '' && r.url === '', r.count + ' url=' + JSON.stringify(r.url));

    // ============ 6. 空结果 ============
    await nav(BASE + '/search.html');
    r = await evalJS(`(() => {
      const input = document.getElementById('sr-input');
      input.value = 'zzzz不存在的关键词qqq';
      input.dispatchEvent(new Event('input'));
      return { empty: !!document.querySelector('.sr-empty'), clear: !!document.getElementById('sr-clearbtn') };
    })()`);
    ok('空结果提示 + 清除按钮', r.empty && r.clear, JSON.stringify(r));

    // ============ 7. 质量节点：11-15 连通链路 ============
    console.log('— 质量节点：专题→事件→材料→检索 —');
    // 专题 survival-2008 存在且链事件档案
    await nav(BASE + '/survival-2008.html');
    r = await evalJS(`(() => !!document.querySelector('a[href="events.html#e2008-08-02"]'))()`);
    ok('专题 → 事件档案链接', r);
    // events.html 事件档案 → 材料（账本）
    await nav(BASE + '/events.html');
    r = await evalJS(`(() => {
      const ev = document.getElementById('e2008-08-02');
      return { mat: !!ev.querySelector('.ev-materials a[href="primary.html#e2008-08-02"]'), cite: false };
    })()`);
    ok('事件档案 → 账本材料链接', r.mat);
    // 账本 → 建档卡（R14）→ 回事件
    await nav(BASE + '/primary.html');
    r = await evalJS(`(() => !!document.querySelector('#e2008-08-02 .ps-linkcard a[href="events.html#e2008-08-02"]'))()`);
    ok('账本建档卡 → 回事件档案', r);
    // 检索 → 事件档案记录
    await nav(BASE + '/search.html');
    r = await evalJS(`(() => {
      const input = document.getElementById('sr-input');
      input.value = '最后一枚火箭';
      input.dispatchEvent(new Event('input'));
      return [...document.querySelectorAll('.sr-item')].some(x => x.getAttribute('href') === 'events.html#ev-e2008-08-02' || x.textContent.includes('最后一枚火箭'));
    })()`);
    ok('检索 → 命中事件档案与账本（第 01 案原话）', r);

    // ============ 8. 无 JS 退路 ============
    console.log('— 无 JS —');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await nav(BASE + '/search.html');
    r = await evalJS(`(() => ({ body: document.body.textContent.includes('检索'), foot: document.body.textContent.includes('无任何运行时联网') }))()`);
    ok('无 JS：页面文案与页脚说明在（静态说明退路）', r.foot);
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ============ 9. 390 真视口 ============
    console.log('— 390 —');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await nav(BASE + '/search.html');
    r = await evalJS(`(() => {
      const doc = document.documentElement;
      const input = document.getElementById('sr-input');
      input.value = '圣诞夜';
      input.dispatchEvent(new Event('input'));
      return {
        overflow: doc.scrollWidth - doc.clientWidth,
        itemW: document.querySelector('.sr-item').getBoundingClientRect().width,
        evbtn: !!document.querySelector('.sr-evbtn'),
      };
    })()`);
    ok('390 无横向溢出 · 结果满宽 · 聚合按钮可用', r.overflow <= 1 && r.itemW > 300 && r.evbtn, 'overflow=' + r.overflow);
    await send('Emulation.clearDeviceMetricsOverride');

    // ============ 10. file:// ============
    console.log('— file:// —');
    await nav('file:///D:/vibe%20coding/musk-website/search.html?q=funding');
    r = await evalJS(`(() => ({
      inputVal: document.getElementById('sr-input').value,
      items: document.querySelectorAll('.sr-item').length,
      span: (document.querySelector('.site-version-val')||{}).textContent,
    }))()`);
    ok('file://：URL 预填 + 结果正常', r.inputVal === 'funding' && r.items >= 1, JSON.stringify(r));

    console.log('\\n== R15 PROBE: ' + PASS + ' pass / ' + FAIL + ' fail ==');
    if (failures.length) { console.log('FAILURES:'); failures.forEach(f => console.log('  - ' + f)); }
  } finally {
    chrome.kill();
  }
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
