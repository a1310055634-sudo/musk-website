// V7-19 R10 探针：capital-evolution.html#flow 资本流向 + 三页联动 + 回归（可复跑）
// headless Chrome + CDP（Node 全局 WebSocket 直连）
const { spawn } = require('child_process');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9235;
const BASE = 'http://127.0.0.1:8765';

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
      await sleep(850);
    }
    const staticize = `document.querySelectorAll('.reveal,.reveal-delay').forEach(el=>el.classList.add('is-visible'));'ok'`;

    // ============ 1. 结构 ============
    console.log('— 结构 —');
    await nav(BASE + '/capital-evolution.html');
    let r = await evalJS(`(() => {
      const sec = document.getElementById('flow');
      return {
        sec: !!sec,
        oldGone: !document.getElementById('ce-flow'),
        flows: document.querySelectorAll('.cap-flow').length,
        ribbons: document.querySelectorAll('.cap-ribbon').length,
        hits: document.querySelectorAll('.cap-hit').length,
        nodes: document.querySelectorAll('.cap-node').length,
        srcNodes: document.querySelectorAll('.cap-node').length,
        elabels: document.querySelectorAll('.cap-elabel').length,
        chips: document.querySelectorAll('.cap-chip[data-cap-filter]').length,
        listRows: document.querySelectorAll('.cap-li').length,
        groups: document.querySelectorAll('.cap-group').length,
        legend: !!document.querySelector('.cap-legend'),
        nonflow: !!document.querySelector('.cap-nonflow'),
        data: !!(window.CAPITAL_V7 && window.CAPITAL_V7.flows),
        dataN: window.CAPITAL_V7 ? window.CAPITAL_V7.flows.length : 0,
        metaN: window.CAPITAL_V7 ? window.CAPITAL_V7.meta.flows : 0,
        scriptTag: !!document.querySelector('script[src="capital-data.js"]'),
        markers: document.querySelectorAll('marker[id^="cap-arrow-"]').length,
        noamt: document.querySelectorAll('.cap-flow--noamt').length,
        noamtDash: (document.querySelector('.cap-flow--noamt .cap-ribbon') || {}).getAttribute?.('stroke-dasharray'),
        arrows: document.querySelectorAll('.cap-ribbon[marker-end]').length,
        focusables: document.querySelectorAll('.cap-flow[tabindex="0"], .cap-node[tabindex="0"]').length,
      };
    })()`);
    ok('section#flow 注入', r.sec);
    ok('旧 #ce-flow 装饰图已移除', r.oldGone);
    ok('18 条流向组', r.flows === 18, String(r.flows));
    ok('18 条可见丝带', r.ribbons === 18, String(r.ribbons));
    ok('18 条命中区', r.hits === 18);
    ok('12 个节点', r.nodes === 12, String(r.nodes));
    ok('图上标签 ≥26', r.elabels >= 26, String(r.elabels));
    ok('筛选芯片 6（含全部）', r.chips === 6, String(r.chips));
    ok('清单 18 行 · 5 组', r.listRows === 18 && r.groups === 5, r.listRows + '/' + r.groups);
    ok('图例与不入图声明在', r.legend && r.nonflow);
    ok('CAPITAL_V7 = 18 流向', r.data && r.dataN === 18 && r.metaN === 18, String(r.dataN));
    ok('capital-data.js 已挂载', r.scriptTag);
    ok('5 个组色箭头 marker', r.markers === 5, String(r.markers));
    ok('箭头方向全标注', r.arrows === 18, String(r.arrows));
    ok('金额未入册 = 1 笔（虚线）', r.noamt === 1 && r.noamtDash === '3 3', r.noamt + '/' + r.noamtDash);
    ok('流向/节点全部可键盘聚焦', r.focusables === 30, String(r.focusables));

    // 线宽语义：大额线 > 小额线（44B > 6.5M）
    r = await evalJS(`(() => {
      const w = id => parseFloat(document.querySelector('[data-cap-flow="' + id + '"] .cap-ribbon').getAttribute('stroke-width'));
      return { tw: w('tw-acq'), tf: w('tesla-found'), ipo: w('tesla-ipo'), gf: w('spacex-gf') };
    })()`);
    ok('线宽语义：44B > 10亿 > IPO2.26亿 > 650万',
       r.tw > r.gf && r.gf > r.ipo && r.ipo > r.tf, JSON.stringify(r));

    // 来源锚点在册（含事件/档案）
    r = await evalJS(`(async () => {
      const evs = [...new Set(window.CAPITAL_V7.flows.filter(f=>f.event).map(f=>'events.html#'+f.event))];
      const files = [...new Set(window.CAPITAL_V7.flows.filter(f=>f.file).map(f=>'company-files.html#'+f.file))];
      async function exists(h) {
        const [pg, anc] = [h.split('#')[0], h.split('#')[1]];
        const t = await (await fetch(pg)).text();
        return t.includes('id="' + anc + '"');
      }
      const evBad = []; for (const h of evs) { if (!(await exists(h))) evBad.push(h); }
      const fBad = []; for (const h of files) { if (!(await exists(h))) fBad.push(h); }
      const srcBad = [];
      for (const f of window.CAPITAL_V7.flows) for (const s of f.sources) {
        if (s.href.includes('#')) { if (!(await exists(s.href))) srcBad.push(f.id + '→' + s.href); }
      }
      return { evN: evs.length, evBad, fBad, srcBad };
    })()`);
    ok(`事件深链 ${r.evN} 个全部在册`, r.evBad.length === 0, JSON.stringify(r.evBad));
    ok('档案锚点全部在册', r.fBad.length === 0, JSON.stringify(r.fBad));
    ok('来源锚点全部在册', r.srcBad.length === 0, JSON.stringify(r.srcBad));

    // ============ 2. 交互 ============
    console.log('— 交互 —');
    await evalJS(`document.querySelector('[data-cap-flow="pp-exit"]').dispatchEvent(new MouseEvent('click',{bubbles:true})); 'ok'`);
    r = await evalJS(`(() => {
      const d = document.getElementById('cap-detail');
      return { t: d.textContent, on: !!document.querySelector('[data-cap-flow="pp-exit"].on') };
    })()`);
    ok('点选流向 → 详情打开', r.t.includes('X.com / PayPal → 个人资本') && r.t.includes('税后') && r.t.includes('口径') && r.t.includes('来源'), r.t.slice(0, 60));
    ok('选中丝带高亮', r.on);
    await evalJS(`document.querySelector('[data-cap-flow="pp-exit"]').dispatchEvent(new MouseEvent('click',{bubbles:true})); 'ok'`);
    r = await evalJS(`document.getElementById('cap-detail').textContent.length < 90 && !document.querySelector('.cap-flow.on')`);
    ok('再点同一线 → 关闭（toggle）', r);

    // 节点点击
    await evalJS(`document.querySelector('[data-cap-node="tesla"]').dispatchEvent(new MouseEvent('click',{bubbles:true})); 'ok'`);
    r = await evalJS(`(() => {
      const d = document.getElementById('cap-detail').textContent;
      return { t: d.slice(0, 200), hl: document.querySelectorAll('.cap-flow.hl').length,
               links: [...document.querySelectorAll('#cap-detail a')].map(a => a.getAttribute('href')) };
    })()`);
    ok('节点详情：Tesla 相关流向 4 条', r.t.includes('Tesla') && r.hl === 4, 'hl=' + r.hl);
    ok('节点详情带档案链接', r.links.some(h => h.startsWith('company-files.html#file-tesla')), JSON.stringify(r.links));
    // jump 按钮切换到单笔流向
    await evalJS(`document.querySelector('#cap-detail [data-cap-jump="tesla-doe"]').click(); 'ok'`);
    r = await evalJS(`document.getElementById('cap-detail').textContent`);
    ok('面板内 jump → 单笔流向详情（DOE 贷款）', r.includes('DOE') && r.includes('ATVM') && r.includes('2013.05.22'), r.slice(0, 50));
    // Esc 关闭 + 焦点归还
    r = await evalJS(`(() => {
      const el = document.querySelector('[data-cap-flow="tesla-doe"]');
      el.focus();
      el.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
      return { closed: document.getElementById('cap-detail').textContent.length < 90,
               focusBack: document.activeElement === el };
    })()`);
    ok('Esc 关闭且焦点归还触发元素', r.closed && r.focusBack, JSON.stringify(r));

    // 键盘 Enter 打开
    r = await evalJS(`(() => {
      const el = document.querySelector('[data-cap-flow="xai-e"]');
      el.focus();
      el.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', bubbles: true }));
      const t = document.getElementById('cap-detail').textContent;
      const closed = (el.dispatchEvent(new KeyboardEvent('keydown', { key: 'Enter', bubbles: true })), true);
      return { open: t.includes('200 亿美元') && t.includes('E 轮'), focusable: document.activeElement === el };
    })()`);
    ok('键盘 Enter 打开（xAI E 轮）', r.open);

    // 筛选
    await evalJS(`document.querySelector('.cap-chip[data-cap-filter="gov"]').click(); 'ok'`);
    r = await evalJS(`(() => {
      const dim = document.querySelectorAll('.cap-flow.dim').length;
      const rows = document.querySelectorAll('.cap-li').length - document.querySelectorAll('.cap-li.cap-hidden').length;
      const groups = [...document.querySelectorAll('.cap-group')].filter(g => !g.classList.contains('cap-hidden')).map(g => g.id);
      const nodeDim = document.querySelectorAll('.cap-node.dim').length;
      return { dim, rows, groups, nodeDim, status: document.getElementById('cap-status').textContent,
               pressed: document.querySelector('.cap-chip[data-cap-filter="gov"]').getAttribute('aria-pressed') };
    })()`);
    ok('筛选 政府资金：16 dim / 2 行 / 仅 gov 组', r.dim === 16 && r.rows === 2 && r.groups.join() === 'cap-g-gov', JSON.stringify(r));
    ok('筛选后状态行 aria-live 更新', r.status.includes('2 笔') && r.pressed === 'true', r.status);
    ok('无流向节点置灰', r.nodeDim >= 1, String(r.nodeDim));
    await evalJS(`document.querySelector('[data-cap-clear]').click(); 'ok'`);
    r = await evalJS(`({ dim: document.querySelectorAll('.cap-flow.dim').length,
                         rows: document.querySelectorAll('.cap-li.cap-hidden').length,
                         status: document.getElementById('cap-status').textContent })`);
    ok('清除筛选恢复 18/18', r.dim === 0 && r.rows === 0 && r.status.includes('18'), JSON.stringify(r));

    // 清单行点击开详情（非链接区）
    await evalJS(`document.querySelectorAll('.cap-li[data-cap-flow]')[2].click(); 'ok'`);
    r = await evalJS(`document.getElementById('cap-detail').textContent.length > 100`);
    ok('清单行点击 → 同一详情', r);
    await evalJS(`(document.querySelector('[data-cap-close]')||{}).click?.(); 'ok'`);

    // 双语：打开详情后切 EN 重渲染
    await evalJS(`document.querySelector('[data-cap-flow="xai-x"]').dispatchEvent(new MouseEvent('click',{bubbles:true})); 'ok'`);
    await evalJS(`document.getElementById('lang-toggle').click(); 'ok'`);
    r = await evalJS(`(() => {
      const d = document.getElementById('cap-detail');
      const lab = document.querySelector('[data-cap-flow="xai-x"] .cap-elabel').textContent;
      return { d: d.textContent, lab };
    })()`);
    ok('EN：详情面板切换（merger/口径/来源）',
       r.d.includes('xAI → X') && r.d.includes('Merger price') && r.d.includes('CALIBER') && r.d.includes('Sources'), r.d.slice(0, 80));
    ok('EN：图上标签切换', r.lab.includes('$33B (all-stock)'), r.lab);
    await evalJS(`document.getElementById('lang-toggle').click();
      document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true })); 'ok'`);

    // ============ 3. 双语静态覆盖 ============
    console.log('— 双语 —');
    r = await evalJS(`(() => {
      const miss = [...document.querySelectorAll('#flow [data-en]')].filter(el => !el.getAttribute('data-en')).length;
      const enAria = document.querySelectorAll('#flow [data-en-aria]').length;
      return { miss, enAria, chipsEn: document.querySelector('.cap-chip[data-cap-filter="personal"]').textContent.trim() };
    })()`);
    ok('data-en 全部有英文值', r.miss === 0, String(r.miss));
    ok('SVG 焦点元素带 data-en-aria', r.enAria === 30, String(r.enAria));
    await evalJS(`document.getElementById('lang-toggle').click(); 'ok'`);
    r = await evalJS(`({
      chip: document.querySelector('.cap-chip[data-cap-filter="personal"]').textContent.trim(),
      title: document.querySelector('#flow h2').textContent.trim(),
      nonflow: document.querySelector('.cap-nonflow').textContent.slice(0, 200),
    })`);
    ok('EN：芯片/标题/声明切换', r.chip.startsWith('Founder capital') && /money/i.test(r.title) && /never drawn/i.test(r.nonflow), JSON.stringify(r));
    await evalJS(`document.getElementById('lang-toggle').click(); 'ok'`);

    // ============ 4. 无 JS 完整性 ============
    console.log('— 无 JS —');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await nav(BASE + '/capital-evolution.html');
    r = await evalJS(`(() => {
      const sec = document.getElementById('flow');
      return {
        ribbons: document.querySelectorAll('.cap-ribbon').length,
        labels: document.querySelectorAll('.cap-elabel').length,
        rows: document.querySelectorAll('.cap-li').length,
        rowHasCaliber: !!document.querySelector('.cap-li .cap-li-caliber'),
        rowHasSrc: document.querySelectorAll('.cap-li .cap-li-src a').length,
        emptyHint: !!document.querySelector('.cap-detail-empty'),
        dataAbsent: !window.CAPITAL_V7,
      };
    })()`);
    ok('无 JS：图与清单完整（18 丝带/标签/18 行）', r.ribbons === 18 && r.labels >= 26 && r.rows === 18, JSON.stringify({ rb: r.ribbons, lb: r.labels, rw: r.rows }));
    ok('无 JS：口径与来源在清单行内', r.rowHasCaliber && r.rowHasSrc >= 18, String(r.rowHasSrc));
    ok('无 JS：面板只有占位提示', r.emptyHint && r.dataAbsent);
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ============ 5. 打印 ============
    console.log('— 打印 —');
    await nav(BASE + '/capital-evolution.html');
    await send('Emulation.setEmulatedMedia', { media: 'print' });
    r = await evalJS(`(() => ({
      chips: getComputedStyle(document.querySelector('.cap-controls')).display,
      detail: getComputedStyle(document.getElementById('cap-detail')).display,
      svg: getComputedStyle(document.querySelector('.cap-graph')).display,
      list: getComputedStyle(document.querySelector('.cap-list')).display,
    }))()`);
    ok('打印：控件/面板隐藏，图与清单保留', r.chips === 'none' && r.detail === 'none' && r.svg !== 'none' && r.list !== 'none', JSON.stringify(r));
    await send('Emulation.setEmulatedMedia', { media: 'screen' });

    // ============ 6. 手机 390 真视口 ============
    console.log('— 手机 390 —');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await nav(BASE + '/capital-evolution.html');
    await evalJS(staticize);
    r = await evalJS(`(() => ({
      svg: getComputedStyle(document.querySelector('.cap-graphwrap')).display,
      legend: getComputedStyle(document.querySelector('.cap-legend')).display,
      rows: document.querySelectorAll('.cap-li').length,
      overflowX: document.documentElement.scrollWidth - document.documentElement.clientWidth,
      chips: getComputedStyle(document.querySelector('.cap-controls')).display,
    }))()`);
    ok('390：图与图例隐、清单为主', r.svg === 'none' && r.legend === 'none' && r.rows === 18, JSON.stringify({ svg: r.svg, rows: r.rows }));
    ok('390：零横向溢出', r.overflowX <= 0, String(r.overflowX));
    ok('390：筛选芯片仍可用', r.chips !== 'none');
    await send('Emulation.clearDeviceMetricsOverride');

    // ============ 7. 三页联动（R7-R10 连贯探索质量门） ============
    console.log('— 联动 —');
    await nav(BASE + '/companies.html');
    await evalJS(staticize);
    r = await evalJS(`(() => {
      const node = document.querySelector('[data-net-node="spacex"]');
      node.dispatchEvent(new MouseEvent('click', { bubbles: true }));
      const d = document.getElementById('net-detail');
      const a = [...d.querySelectorAll('a')].find(a => a.getAttribute('href') === 'capital-evolution.html#flow');
      return { panel: !!d.textContent.includes('SpaceX'), capLink: !!a, capText: a ? a.textContent.trim() : '' };
    })()`);
    ok('关系图面板 → 资本流向链接', r.panel && r.capLink, JSON.stringify(r));
    await nav(BASE + '/money.html');
    r = await evalJS(`(() => {
      const a = document.querySelector('a[href="capital-evolution.html#flow"]');
      return { exists: !!a, txt: a ? a.textContent.slice(0, 30) : '' };
    })()`);
    ok('资本解剖 → 资本流向入口', r.exists, r.txt);
    await nav(BASE + '/index.html');
    r = await evalJS(`(() => {
      const a = document.querySelector('#map a[href="capital-evolution.html#flow"]');
      return { exists: !!a };
    })()`);
    ok('首页 #map → 资本流向入口', r.exists);
    // hash 落地
    await nav(BASE + '/capital-evolution.html#flow');
    r = await evalJS(`(() => {
      const rect = document.getElementById('flow').getBoundingClientRect();
      return { inView: rect.top > -400 && rect.top < 400, h1: document.title.includes('资本演化') };
    })()`);
    ok('#flow 深链落地到区', r.inView, JSON.stringify(r));

    // ============ 8. 版本与回归 ============
    console.log('— 版本与回归 —');
    await nav(BASE + '/index.html');
    r = await evalJS(`document.querySelector('.site-version-val').textContent`);
    ok('版本 span = 6.15.0', r === '6.15.0', r);
    await nav(BASE + '/timeline.html');
    r = await evalJS(`({ evNodes: document.querySelectorAll('.gx-ev').length,
                         ver: document.querySelector('.site-version-val').textContent })`);
    ok('时间轴回归：事件节点仍在', r.evNodes >= 7, String(r.evNodes));
    ok('时间轴版本 = 6.15.0', r.ver === '6.15.0', r.ver);
    await nav(BASE + '/events.html');
    r = await evalJS(`({ files: document.querySelectorAll('[id^="e"]').length,
                         ver: document.querySelector('.site-version-val').textContent })`);
    ok('事件档案回归', r.ver === '6.15.0');
    await nav(BASE + '/company-files.html');
    r = await evalJS(`({ files: document.querySelectorAll('[id^="file-"]').length,
                         ver: document.querySelector('.site-version-val').textContent })`);
    ok('公司档案回归（4 档案）', r.files === 4, String(r.files));
    await nav(BASE + '/search.html');
    r = await evalJS(`({ idx: window.SEARCH_INDEX ? window.SEARCH_INDEX.length : 0 })`);
    ok('检索索引 169 不变', r.idx === 169, String(r.idx));

    // ============ 9. file:// 冒烟 ============
    console.log('— file:// —');
    await nav('file:///D:/vibe%20coding/musk-website/capital-evolution.html');
    r = await evalJS(`(() => {
      const f = document.querySelector('[data-cap-flow="spacex-found"]');
      f.dispatchEvent(new MouseEvent('click', { bubbles: true }));
      const d = document.getElementById('cap-detail').textContent;
      return { data: !!(window.CAPITAL_V7 && window.CAPITAL_V7.flows.length === 18),
               detail: d.includes('SpaceX') && d.includes('1 亿美元'),
               ribbons: document.querySelectorAll('.cap-ribbon').length,
               css: getComputedStyle(document.querySelector('.cap-ribbon')).strokeWidth !== '' };
    })()`);
    ok('file://：数据/样式/交互可用', r.data && r.detail && r.ribbons === 18 && r.css, JSON.stringify(r));

    console.log('—');
    console.log(`PASS ${PASS}  FAIL ${FAIL}`);
    if (failures.length) { console.log('FAILURES:'); failures.forEach(f => console.log('  ✗ ' + f)); process.exit(1); }
  } finally {
    chrome.kill();
  }
}
main().catch(e => { console.error('ERR', e); process.exit(1); });
