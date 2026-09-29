// V7-19 R13 探针：promises.html 专题 + 联动回归 + 双端/file://（可复跑）
const { spawn } = require('child_process');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9243;
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
    console.log('— 结构 promises —');
    await nav(BASE + '/promises.html');
    let r = await evalJS(`(() => {
      const secs = [...document.querySelectorAll('.lr-main .lr-sec')];
      return {
        hero: !!document.querySelector('.lr-hero'),
        year5: (document.querySelector('.sv-year')||{}).textContent,
        axisLinks: document.querySelectorAll('svg.sv-axis a[href^="#pv-"]').length,
        cases: document.querySelectorAll('.pv-case').length,
        caseIds: [...document.querySelectorAll('.pv-case')].map(n => n.id),
        quotes: document.querySelectorAll('.pv-case blockquote').length,
        quoteSrc: document.querySelectorAll('.pv-case .lr-quote-src').length,
        linksRows: document.querySelectorAll('.sv-links').length,
        deepLinks: document.querySelectorAll('.sv-links a').length,
        buckets: document.querySelectorAll('.sv-stats--4 li').length,
        overviewRows: document.querySelectorAll('.lr-data tr').length - 1,
        secs: secs.length,
        tocLinks: document.querySelectorAll('.lr-toc a').length,
        evGroups: document.querySelectorAll('.sv-ev-h').length,
        evItems: document.querySelectorAll('.sv-ev li').length,
        exclusions: (() => { const el = document.getElementById('promises-s5'); if (!el) return false; const sec = el.closest('.lr-sec'); return sec.textContent.includes('Cybertruck') && sec.textContent.includes('Starship'); })(),
        metaVer: ([...document.querySelectorAll('.lr-m b')].map(b => b.textContent).find(t => /v6\\./.test(t)) || ''),
        mastCurrent: (document.querySelector('.mainnav a[aria-current="page"]')||{}).getAttribute?.('href'),
      };
    })()`);
    ok('页头 + 装饰 5 + 五案轴', r.hero && r.year5 === '5' && r.axisLinks === 5, r.year5 + '/' + r.axisLinks);
    ok('五案卡片（01–05）', r.cases === 5 && ['pv-2008','pv-2017','pv-2018','pv-2014','pv-2025'].every(id => r.caseIds.includes(id)), JSON.stringify(r.caseIds));
    ok('引语 5 块 · 来源行 5 条', r.quotes === 5 && r.quoteSrc === 5, r.quotes + '/' + r.quoteSrc);
    ok('深链行 5 · 链接 12（3+2+3+1+3）', r.linksRows === 5 && r.deepLinks === 12, r.linksRows + '/' + r.deepLinks);
    ok('四类归类卡 4 项', r.buckets === 4, String(r.buckets));
    ok('总览表 5 行（不含表头）', r.overviewRows === 5, String(r.overviewRows));
    ok('五节 + 目录 5 项', r.secs === 5 && r.tocLinks === 5, r.secs + '/' + r.tocLinks);
    ok('证据清单 3 组 · 条目 16', r.evGroups === 3 && r.evItems === 16, r.evGroups + '/' + r.evItems);
    ok('排除项点名 Cybertruck 与 Starship', r.exclusions);
    ok('版本 meta 6.18.0', r.metaVer.includes('6.18.0'), r.metaVer);
    ok('导航 aria-current 指向本页', r.mastCurrent === 'promises.html', String(r.mastCurrent));

    // ============ 2. 深链有效性 ============
    console.log('— 深链有效性 —');
    r = await evalJS(`(async () => {
      const hrefs = [...document.querySelectorAll('.sv-links a'), ...document.querySelectorAll('svg.sv-axis a'), ...document.querySelectorAll('.sv-ev li a')].map(a => a.getAttribute('href')).filter(h => h && !h.startsWith('#'));
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

    // ============ 3. 轴节点点击 ============
    console.log('— 交互 —');
    r = await evalJS(`(() => {
      const a = document.querySelector('svg.sv-axis a[href="#pv-2018"]');
      a.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
      return { hash: location.hash, target: !!document.getElementById('pv-2018') };
    })()`);
    await sleep(900);
    let top = await evalJS(`document.getElementById('pv-2018').getBoundingClientRect().top`);
    ok('轴节点点击 → 定位到第 03 案', r.hash === '#pv-2018' && r.target && top > -300 && top < 500, r.hash + ' top=' + Math.round(top));

    // ============ 4. 双语 ============
    console.log('— 双语 —');
    r = await evalJS(`(() => {
      const btn = document.getElementById('lang-toggle');
      btn.click();
      const h1 = document.querySelector('.lr-hero h1');
      const tag = document.querySelector('#pv-2025 .sv-node-tag');
      const out = { h1: h1.textContent.slice(0, 20), tag: tag.textContent };
      btn.click();
      out.h1zh = document.querySelector('.lr-hero h1').textContent.slice(0, 8);
      return out;
    })()`);
    ok('EN：h1 英文', /^Promises/.test(r.h1), r.h1);
    ok('EN：案 05 徽标英文', /No evidence yet/i.test(r.tag), r.tag);
    ok('切回中文恢复', /承诺与结果/.test(r.h1zh), r.h1zh);
    r = await evalJS(`(() => {
      const miss = [];
      document.querySelectorAll('.pv-case, .sv-method, .sv-ev, .sv-stats').forEach(el => {
        el.querySelectorAll('*').forEach(k => {
          if (k.children.length === 0 && k.textContent.trim() && !k.getAttribute('data-en') && !['A','path','circle','rect','line','text'].includes(k.tagName)) {
            const t = k.textContent.trim();
            const letters = (t.match(/[a-zA-Z]/g) || []);
            const neutral = !/[\\u4e00-\\u9fff]/.test(t) && letters.every(ch => ['B','b','x','v'].includes(ch));
            if (!neutral) miss.push(k.className || k.tagName);
          }
        });
      });
      return [...new Set(miss)].slice(0, 8);
    })()`);
    ok('案例/方法/证据/归类区无漏翻叶子', r.length === 0, JSON.stringify(r));

    // ============ 5. 无 JS ============
    console.log('— 无 JS —');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await nav(BASE + '/promises.html');
    r = await evalJS(`(() => ({
      cases: document.querySelectorAll('.pv-case').length,
      sec3: (document.getElementById('pv-2008')||{}).textContent?.includes('六周') || false,
      quotes: document.querySelectorAll('.pv-case blockquote').length,
      links: document.querySelectorAll('.sv-links a').length,
      evList: document.querySelectorAll('.sv-ev li').length,
      toc: document.querySelectorAll('.lr-toc a').length,
    }))()`);
    ok('无 JS：五案/引语/深链/证据全在', r.cases === 5 && r.sec3 && r.quotes === 5 && r.links === 12 && r.evList === 16 && r.toc === 5, JSON.stringify(r));
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ============ 6. 390 真视口 ============
    console.log('— 390 真视口 —');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await nav(BASE + '/promises.html');
    r = await evalJS(`(() => {
      const doc = document.documentElement;
      return {
        overflow: doc.scrollWidth - doc.clientWidth,
        axisHidden: getComputedStyle(document.querySelector('.sv-axis-fig')).display === 'none',
        caseVisible: document.getElementById('pv-2008').getBoundingClientRect().width > 300,
        tableScroll: (() => { const w = document.querySelector('.lr-data-wrap'); return w.scrollWidth >= w.clientWidth - 2; })(),
      };
    })()`);
    ok('390 无横向溢出', r.overflow <= 1, 'overflow=' + r.overflow);
    ok('390 SVG 轴隐藏', r.axisHidden);
    ok('390 案例卡满宽可读', r.caseVisible);
    ok('390 总览表容器横向滚动可用', r.tableScroll);
    await send('Emulation.clearDeviceMetricsOverride');

    // ============ 7. 联动回归 ============
    console.log('— 联动回归 —');
    await nav(BASE + '/index.html');
    r = await evalJS(`(() => {
      const rows = [...document.querySelectorAll('.feature-rows a.feature-row')].map(a => a.getAttribute('href'));
      return { rows: rows.slice(0, 3), nav: !!document.querySelector('.mainnav a[href="promises.html"]') };
    })()`);
    ok('首页专题行前三行 = 2008 + 平台 + 承诺', r.rows[0] === 'survival-2008.html' && r.rows[1] === 'platform-x.html' && r.rows[2] === 'promises.html', JSON.stringify(r.rows));
    ok('首页导航含承诺专题', r.nav);
    await nav(BASE + '/controversy.html');
    r = await evalJS(`(() => {
      const a = [...document.querySelectorAll('a[href="promises.html"]')];
      return a.length >= 1;
    })()`);
    ok('争议页 SEC 段 → 第 03 案链接', r);
    await nav(BASE + '/survival-2008.html');
    r = await evalJS(`(() => {
      const n = document.getElementById('sv-0802');
      return !!n.querySelector('a[href="promises.html"]');
    })()`);
    ok('2008 专题节点 → 第 01 案互链', r);
    await nav(BASE + '/events.html');
    r = await evalJS(`(() => {
      const ev802 = document.getElementById('e2008-08-02');
      const ev807 = document.getElementById('e2018-08-07');
      return {
        both: !!ev802 && !!ev807,
        p802: !!ev802.querySelector('.ev-materials a[href="promises.html"]'),
        p807: !!ev807.querySelector('.ev-materials a[href="promises.html"]'),
        span: (document.querySelector('.site-version-val')||{}).textContent,
      };
    })()`);
    ok('两个事件档案均含承诺专题材料深链', r.both && r.p802 && r.p807, JSON.stringify(r));
    ok('events.html span 6.18.0', r.span === '6.18.0', r.span);
    await nav(BASE + '/timeline.html');
    r = await evalJS(`({ m: window.TIMELINE_V7 ? window.TIMELINE_V7.meta : null })`);
    ok('TIMELINE_V7 口径不变：151 独立 / 18 吸收 / 9 事件', r.m && r.m.nRecords === 151 && r.m.nAbsorbed === 18 && r.m.nEvents === 9, JSON.stringify(r.m));

    // ============ 8. file:// ============
    console.log('— file:// —');
    await nav('file:///D:/vibe%20coding/musk-website/promises.html');
    r = await evalJS(`(() => {
      const cs = getComputedStyle(document.querySelector('.lr-hero'));
      return {
        cases: document.querySelectorAll('.pv-case').length,
        styled: cs.backgroundColor,
        metaVer: ([...document.querySelectorAll('.lr-m b')].map(b => b.textContent).find(t => /v6\\./.test(t)) || ''),
      };
    })()`);
    ok('file://：结构完整 + 深色页头 --coal 渲染', r.cases === 5 && r.styled === 'rgb(16, 19, 22)', r.styled);
    ok('file://：版本 6.18.0（页头 meta 行）', r.metaVer.includes('6.18.0'), r.metaVer);

    // ============ 9. 打印/减动效 ============
    console.log('— 打印/减动效 —');
    await nav(BASE + '/promises.html');
    r = await evalJS(`(() => {
      const rules = [...document.styleSheets].flatMap(s => { try { return [...s.cssRules]; } catch(e) { return []; } });
      const pr = rules.filter(r => r.media && /print/.test(r.media.mediaText));
      const caseAvoid = pr.some(r => [...r.cssRules].some(c => /\\.pv-case/.test(c.cssText) && /avoid/.test(c.cssText)));
      const rm = rules.some(r => r.media && /prefers-reduced-motion/.test(r.media.mediaText));
      return { caseAvoid, rm };
    })()`);
    ok('打印：.pv-case break-inside avoid 在册', r.caseAvoid);
    ok('sv 组件 prefers-reduced-motion 退路在册', r.rm);

    console.log('\\n== R13 PROBE: ' + PASS + ' pass / ' + FAIL + ' fail ==');
    if (failures.length) { console.log('FAILURES:'); failures.forEach(f => console.log('  - ' + f)); }
  } finally {
    chrome.kill();
  }
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
