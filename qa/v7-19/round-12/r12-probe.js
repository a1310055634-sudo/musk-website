// V7-19 R12 探针：platform-x.html 专题 + 联动回归 + 双端/file://（可复跑）
const { spawn } = require('child_process');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9240;
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
      await sleep(850);
    }

    // ============ 1. 结构 ============
    console.log('— 结构 platform-x —');
    await nav(BASE + '/platform-x.html');
    let r = await evalJS(`(() => {
      const secs = [...document.querySelectorAll('.lr-main .lr-sec')];
      return {
        hero: !!document.querySelector('.lr-hero'),
        yearX: (document.querySelector('.sv-year')||{}).textContent,
        stageBoxes: document.querySelectorAll('svg.sv-axis a[href^="#px-stage"]').length,
        ownFig: !!document.querySelector('svg.sv-own'),
        ownEras: document.querySelectorAll('.sv-own-box').length,
        nodes: document.querySelectorAll('.sv-node').length,
        nodeIds: [...document.querySelectorAll('.sv-node')].map(n => n.id),
        quotes: document.querySelectorAll('.sv-node blockquote').length,
        quoteSrc: document.querySelectorAll('.sv-node .lr-quote-src').length,
        linksRows: document.querySelectorAll('.sv-links').length,
        deepLinks: document.querySelectorAll('.sv-links a').length,
        scope: document.querySelectorAll('.sv-scope li').length,
        secs: secs.length,
        tocLinks: document.querySelectorAll('.lr-toc a').length,
        evGroups: document.querySelectorAll('.sv-ev-h').length,
        evItems: document.querySelectorAll('.sv-ev li').length,
        method: document.querySelectorAll('.sv-method li').length,
        calTable: document.querySelectorAll('.lr-data th').length,
        metaVer: ([...document.querySelectorAll('.lr-m b')].map(b => b.textContent).find(t => /v6\\./.test(t)) || ''),
        mastCurrent: (document.querySelector('.mainnav a[aria-current="page"]')||{}).getAttribute?.('href'),
      };
    })()`);
    ok('页头 + 装饰 X + 三阶段图 + 所有权图', r.hero && r.yearX === 'X' && r.stageBoxes === 3 && r.ownFig && r.ownEras === 3, r.yearX + '/' + r.stageBoxes + '/' + r.ownEras);
    ok('正文 11 节点', r.nodes === 11, JSON.stringify(r.nodeIds));
    ok('引语 2 块 · 来源行 2 条', r.quotes === 2 && r.quoteSrc === 2, r.quotes + '/' + r.quoteSrc);
    ok('记录深链行 11 · 链接 23', r.linksRows === 11 && r.deepLinks === 23, r.linksRows + '/' + r.deepLinks);
    ok('分工表 4 行', r.scope === 4, String(r.scope));
    ok('九节 + 目录 9 项', r.secs === 9 && r.tocLinks === 9, r.secs + '/' + r.tocLinks);
    ok('证据清单 4 组 · 条目 19（7+4+5+3）', r.evGroups === 4 && r.evItems === 19, r.evGroups + '/' + r.evItems);
    ok('方法与边界 6 条', r.method === 6, String(r.method));
    ok('状态口径表 3 列', r.calTable >= 3, String(r.calTable));
    ok('版本 meta 6.17.0', r.metaVer.includes('6.17.0'), r.metaVer);
    ok('导航 aria-current 指向本页', r.mastCurrent === 'platform-x.html', String(r.mastCurrent));

    // ============ 2. 深链有效性 ============
    console.log('— 深链有效性 —');
    r = await evalJS(`(async () => {
      const hrefs = [...document.querySelectorAll('.sv-links a'), ...document.querySelectorAll('svg a'), ...document.querySelectorAll('.sv-ev li a'), ...document.querySelectorAll('.sv-scope li a')].map(a => a.getAttribute('href')).filter(h => h && !h.startsWith('#'));
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
    ok('全页深链目标在册（去重 ' + r.total + '）', r.bad.length === 0, JSON.stringify(r.bad));

    // ============ 3. 三阶段方块点击 ============
    console.log('— 交互 —');
    r = await evalJS(`(() => {
      const a = document.querySelector('svg.sv-axis a[href="#px-stage3"]');
      a.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
      return { hash: location.hash, target: !!document.getElementById('px-stage3') };
    })()`);
    await sleep(900);
    let top = await evalJS(`document.getElementById('px-stage3').getBoundingClientRect().top`);
    ok('阶段三方块点击 → 定位', r.hash === '#px-stage3' && r.target && top > -300 && top < 500, r.hash + ' top=' + Math.round(top));

    // ============ 4. 双语 ============
    console.log('— 双语 —');
    r = await evalJS(`(() => {
      const btn = document.getElementById('lang-toggle');
      btn.click();
      const h1 = document.querySelector('.lr-hero h1');
      const tag = document.querySelector('.sv-tag-s3');
      const cap = document.querySelector('.sv-own-fig + .sv-axis-cap, figcaption.sv-axis-cap');
      const out = { h1: h1.textContent.slice(0, 20), tag: tag.textContent, cap: cap.textContent.slice(0, 30) };
      btn.click();
      out.h1zh = document.querySelector('.lr-hero h1').textContent.slice(0, 8);
      return out;
    })()`);
    ok('EN：h1 英文', /^Platform/.test(r.h1), r.h1);
    ok('EN：阶段徽标英文', /Stage 3/.test(r.tag), r.tag);
    ok('EN：图注英文', /Three stages/i.test(r.cap), r.cap);
    ok('切回中文恢复', /平台变局/.test(r.h1zh), r.h1zh);
    r = await evalJS(`(() => {
      const miss = [];
      document.querySelectorAll('.sv-node, .sv-method, .sv-ev, .sv-scope').forEach(el => {
        el.querySelectorAll('*').forEach(k => {
          if (k.children.length === 0 && k.textContent.trim() && !k.getAttribute('data-en') && !['A','path','circle','rect','line','text'].includes(k.tagName)) {
            const t = k.textContent.trim();
            const letters = (t.match(/[a-zA-Z]/g) || []);
            const neutral = !/[\\u4e00-\\u9fff]/.test(t) && letters.every(ch => ch === 'B');
            if (!neutral) miss.push(k.className || k.tagName);
          }
        });
      });
      return [...new Set(miss)].slice(0, 8);
    })()`);
    ok('节点/方法/证据/分工区无漏翻叶子', r.length === 0, JSON.stringify(r));

    // ============ 5. 无 JS ============
    console.log('— 无 JS —');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await nav(BASE + '/platform-x.html');
    r = await evalJS(`(() => ({
      nodes: document.querySelectorAll('.sv-node').length,
      mergerTxt: (document.getElementById('px-merger')||{}).textContent?.includes('全股票') || false,
      quotes: document.querySelectorAll('.sv-node blockquote').length,
      links: document.querySelectorAll('.sv-links a').length,
      evList: document.querySelectorAll('.sv-ev li').length,
      toc: document.querySelectorAll('.lr-toc a').length,
    }))()`);
    ok('无 JS：节点/引语/深链/证据全在', r.nodes === 11 && r.mergerTxt && r.quotes === 2 && r.links === 23 && r.evList === 19 && r.toc === 9, JSON.stringify(r));
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ============ 6. 390 真视口 ============
    console.log('— 390 真视口 —');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await nav(BASE + '/platform-x.html');
    r = await evalJS(`(() => {
      const doc = document.documentElement;
      return {
        overflow: doc.scrollWidth - doc.clientWidth,
        axisHidden: getComputedStyle(document.querySelector('.sv-axis-fig')).display === 'none',
        ownHidden: getComputedStyle(document.querySelector('.sv-own-fig')).display === 'none',
        nodeVisible: document.getElementById('px-merger').getBoundingClientRect().width > 300,
        tableScroll: (() => { const w = document.querySelector('.lr-data-wrap'); return w.scrollWidth >= w.clientWidth - 2; })(),
      };
    })()`);
    ok('390 无横向溢出', r.overflow <= 1, 'overflow=' + r.overflow);
    ok('390 两图隐藏（表格+节点列表替代）', r.axisHidden && r.ownHidden);
    ok('390 节点正文满宽可读', r.nodeVisible);
    ok('390 状态口径表容器横向滚动可用', r.tableScroll);
    await send('Emulation.clearDeviceMetricsOverride');

    // ============ 7. 联动回归 ============
    console.log('— 联动回归 —');
    await nav(BASE + '/index.html');
    r = await evalJS(`(() => {
      const rows = [...document.querySelectorAll('.feature-rows a.feature-row')].map(a => a.getAttribute('href'));
      return { rows: rows.slice(0, 2), nav: !!document.querySelector('.mainnav a[href="platform-x.html"]') };
    })()`);
    ok('首页专题行前两行 = 2008 + 平台变局', r.rows[0] === 'survival-2008.html' && r.rows[1] === 'platform-x.html', JSON.stringify(r.rows));
    ok('首页导航含平台专题', r.nav);
    await nav(BASE + '/ai-strategy.html');
    r = await evalJS(`(() => !!document.querySelector('a[href="platform-x.html"]'))()`);
    ok('ai-strategy → 平台线链接', r);
    await nav(BASE + '/deep-dive-05.html');
    r = await evalJS(`(() => {
      const h2 = document.getElementById('deep-dive-05-s3');
      const sec = h2.closest('.lr-sec');
      return !!sec.querySelector('a[href="platform-x.html"]');
    })()`);
    ok('深读五第三节 → 平台线链接', r);
    await nav(BASE + '/grok.html');
    r = await evalJS(`(() => !!document.querySelector('.grok-px-link a[href="platform-x.html"]'))()`);
    ok('grok → 平台交易完整叙事链接', r);
    await nav(BASE + '/events.html');
    r = await evalJS(`(() => {
      const ev28 = document.getElementById('e2022-10-28');
      const ev328 = document.getElementById('e2025-03-28');
      return {
        both: !!ev28 && !!ev328,
        feat28: !!ev28.querySelector('.ev-materials a[href="platform-x.html"]'),
        feat328: !!ev328.querySelector('.ev-materials a[href="platform-x.html"]'),
        span: (document.querySelector('.site-version-val')||{}).textContent,
      };
    })()`);
    ok('两个平台事件档案均含平台专题材料深链', r.both && r.feat28 && r.feat328, JSON.stringify(r));
    ok('events.html span 6.17.0', r.span === '6.17.0', r.span);
    await nav(BASE + '/timeline.html');
    r = await evalJS(`({ m: window.TIMELINE_V7 ? window.TIMELINE_V7.meta : null })`);
    ok('TIMELINE_V7 口径不变：151 独立 / 18 吸收 / 9 事件', r.m && r.m.nRecords === 151 && r.m.nAbsorbed === 18 && r.m.nEvents === 9, JSON.stringify(r.m));

    // ============ 8. file:// ============
    console.log('— file:// —');
    await nav('file:///D:/vibe%20coding/musk-website/platform-x.html');
    r = await evalJS(`(() => {
      const cs = getComputedStyle(document.querySelector('.lr-hero'));
      return {
        nodes: document.querySelectorAll('.sv-node').length,
        own: !!document.querySelector('svg.sv-own'),
        styled: cs.backgroundColor,
        metaVer: ([...document.querySelectorAll('.lr-m b')].map(b => b.textContent).find(t => /v6\\./.test(t)) || ''),
      };
    })()`);
    ok('file://：结构完整 + 深色页头 --coal 渲染', r.nodes === 11 && r.own && r.styled === 'rgb(16, 19, 22)', r.styled);
    ok('file://：版本 6.17.0（页头 meta 行）', r.metaVer.includes('6.17.0'), r.metaVer);

    // ============ 9. 打印与减动效 ============
    console.log('— 打印/减动效 —');
    await nav(BASE + '/platform-x.html');
    r = await evalJS(`(() => {
      const rules = [...document.styleSheets].flatMap(s => { try { return [...s.cssRules]; } catch(e) { return []; } });
      const pr = rules.filter(r => r.media && /print/.test(r.media.mediaText));
      const ownHiddenPrint = pr.some(r => [...r.cssRules].some(c => /\\.sv-own-fig/.test(c.cssText)));
      const rm = rules.some(r => r.media && /prefers-reduced-motion/.test(r.media.mediaText));
      return { ownHiddenPrint, rm };
    })()`);
    ok('打印：所有权图隐藏（表格保留）', r.ownHiddenPrint);
    ok('sv 组件 prefers-reduced-motion 退路在册', r.rm);

    console.log('\\n== R12 PROBE: ' + PASS + ' pass / ' + FAIL + ' fail ==');
    if (failures.length) { console.log('FAILURES:'); failures.forEach(f => console.log('  - ' + f)); }
  } finally {
    chrome.kill();
  }
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
