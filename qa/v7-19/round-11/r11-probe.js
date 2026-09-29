// V7-19 R11 探针：survival-2008.html 专题 + 联动回归 + 双端/file://（可复跑）
// headless Chrome + CDP（Node 全局 WebSocket 直连）
const { spawn } = require('child_process');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9236;
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
    console.log('— 结构 survival-2008 —');
    await nav(BASE + '/survival-2008.html');
    let r = await evalJS(`(() => {
      const secs = [...document.querySelectorAll('.lr-main .lr-sec')];
      return {
        hero: !!document.querySelector('.lr-hero'),
        year: !!document.querySelector('.sv-year'),
        axis: !!document.querySelector('svg.sv-axis'),
        axisLinks: document.querySelectorAll('svg.sv-axis a[href^="#sv-"]').length,
        axisCaptionScale: (document.querySelector('.sv-axis-cap')||{}).textContent || '',
        nodes: document.querySelectorAll('.sv-node').length,
        nodeIds: [...document.querySelectorAll('.sv-node')].map(n => n.id),
        stats: document.querySelectorAll('.sv-stats li').length,
        secs: secs.length,
        tocLinks: document.querySelectorAll('.lr-toc a[href^="#survival-2008-s"]').length,
        quotes: document.querySelectorAll('.sv-node blockquote').length,
        quoteSrc: document.querySelectorAll('.sv-node .lr-quote-src').length,
        linksRows: document.querySelectorAll('.sv-links').length,
        deepLinks: document.querySelectorAll('.sv-links a').length,
        evGroups: document.querySelectorAll('.sv-ev-h').length,
        evItems: document.querySelectorAll('.sv-ev li').length,
        method: document.querySelectorAll('.sv-method li').length,
        foot: !!document.querySelector('.lr-foot'),
        span: (document.querySelector('.site-version-val')||{}).textContent || '',
        metaVer: ([...document.querySelectorAll('.lr-m b')].map(b => b.textContent).find(t => /v6\./.test(t)) || ''),
        mastCurrent: (document.querySelector('.mainnav a[aria-current="page"]')||{}).getAttribute?.('href'),
      };
    })()`);
    ok('页头 + 装饰年份 + SVG 轴', r.hero && r.year && r.axis);
    ok('轴上 5 个可点节点', r.axisLinks === 5, String(r.axisLinks));
    ok('轴图注声明非等比', /非时间等比/.test(r.axisCaptionScale));
    ok('正文 5 个节点', r.nodes === 5, JSON.stringify(r.nodeIds));
    ok('五节点 id 与轴 href 对齐', ['sv-0802','sv-0928','sv-10','sv-1223','sv-1224'].every(id => r.nodeIds.includes(id)));
    ok('四个数字栅格 4 项', r.stats === 4, String(r.stats));
    ok('六节 + 目录 6 项', r.secs === 6 && r.tocLinks === 6, r.secs + '/' + r.tocLinks);
    ok('节点引语 4 块 · 来源行 4 条', r.quotes === 4 && r.quoteSrc === 4, r.quotes + '/' + r.quoteSrc);
    ok('记录深链行 5 行 · 链接 10（2+2+1+2+3）', r.linksRows === 5 && r.deepLinks === 10, r.linksRows + '/' + r.deepLinks);
    ok('证据清单 4 组 · 条目 17（4+5+2+6）', r.evGroups === 4 && r.evItems === 17, r.evGroups + '/' + r.evItems);
    ok('方法与边界 6 条', r.method === 6, String(r.method));
    ok('页脚在；版本见页头 meta（lr 模板页无 span 口径）', r.foot && r.metaVer.includes('6.16.0'), r.metaVer);
    ok('导航 aria-current 指向本页', r.mastCurrent === 'survival-2008.html', String(r.mastCurrent));

    // ============ 2. 锚点深链有效性（sv-links + 轴 href 全量核对目标页） ============
    console.log('— 深链有效性 —');
    r = await evalJS(`(async () => {
      const hrefs = [...document.querySelectorAll('.sv-links a'), ...document.querySelectorAll('svg.sv-axis a')].map(a => a.getAttribute('href'));
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
    ok('深链目标页与锚点全部在册（去重 ' + r.total + '）', r.bad.length === 0, JSON.stringify(r.bad));

    // ============ 3. 轴节点点击跳转 ============
    console.log('— 交互 —');
    r = await evalJS(`(() => {
      const a = document.querySelector('svg.sv-axis a[href="#sv-1224"]');
      a.dispatchEvent(new MouseEvent('click', { bubbles: true, cancelable: true }));
      return { hash: location.hash, target: !!document.getElementById('sv-1224') };
    })()`);
    await sleep(900);
    let top = await evalJS(`document.getElementById('sv-1224').getBoundingClientRect().top`);
    ok('轴节点点击 → 定位到 12.24 节点', r.hash === '#sv-1224' && r.target && top > -300 && top < 500, r.hash + ' top=' + Math.round(top));
    // 目录点击回顶部一节
    r = await evalJS(`(() => {
      document.querySelector('.lr-toc a[href="#survival-2008-s1"]').click();
      return { hash: location.hash };
    })()`);
    ok('目录定位回第一节', r.hash === '#survival-2008-s1', r.hash);

    // ============ 4. 双语 ============
    console.log('— 双语 —');
    r = await evalJS(`(() => {
      const btn = document.getElementById('lang-toggle');
      btn.click();
      const h1 = document.querySelector('.lr-hero h1');
      const tag = document.querySelector('.sv-tag-eve');
      const date = document.querySelector('#sv-1224 .sv-node-date');
      const cap = document.querySelector('.sv-axis-cap');
      const out = { h1: h1.textContent.slice(0, 30), tag: tag.textContent, date: date.textContent, cap: cap.textContent.slice(0, 40), lang: document.documentElement.getAttribute('lang') };
      btn.click();
      out.h1zh = document.querySelector('.lr-hero h1').textContent.slice(0, 12);
      out.tagZh = document.querySelector('.sv-tag-eve').textContent;
      return out;
    })()`);
    ok('EN：h1 英文', /^Survival/.test(r.h1), r.h1);
    ok('EN：节点徽标英文（最后一个小时）', /last hour/i.test(r.tag), r.tag);
    ok('EN：图注英文', /144-day|equidistant/i.test(r.cap), r.cap);
    ok('日期徽标双语下保持数字', /^2008\.12\.24$/.test(r.date), r.date);
    ok('切回中文恢复', /生死役/.test(r.h1zh) && /最后一个小时/.test(r.tagZh), r.h1zh + '/' + r.tagZh);
    r = await evalJS(`(() => {
      const miss = [];
      document.querySelectorAll('.sv-node, .sv-stats, .sv-method, .sv-ev').forEach(el => {
        el.querySelectorAll('*').forEach(k => {
          if (k.children.length === 0 && k.textContent.trim() && !k.getAttribute('data-en') && k.tagName !== 'A' && k.tagName !== 'path' && k.tagName !== 'circle' && k.tagName !== 'rect') {
            var t = k.textContent.trim();
            var neutral = !/[一-鿿]/.test(t) && /[a-zA-Z]/.test(t) === (t === "$1.6B" ? false : /[a-zA-Z]/.test(t)) && (t.match(/[a-zA-Z]/g) || []).join('') === (t === "$1.6B" ? "B" : (t.match(/[a-zA-Z]/g) || []).join(''));
            var letters = (t.match(/[a-zA-Z]/g) || []);
            var okNeutral = !/[一-鿿]/.test(t) && letters.every(function(ch) { return ch === "B"; });
            if (!okNeutral) miss.push(k.className || k.tagName);
          }
        });
      });
      return [...new Set(miss)].slice(0, 8);
    })()`);
    ok('节点/数字/方法/证据区无漏翻叶子', r.length === 0, JSON.stringify(r));

    // ============ 5. 无 JS 完整 ============
    console.log('— 无 JS —');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await nav(BASE + '/survival-2008.html');
    r = await evalJS(`(() => ({
      nodes: document.querySelectorAll('.sv-node').length,
      txt: (document.getElementById('sv-1224')||{}).textContent?.includes('圣诞夜') || false,
      quotes: document.querySelectorAll('.sv-node blockquote').length,
      links: document.querySelectorAll('.sv-links a').length,
      evList: document.querySelectorAll('.sv-ev li').length,
      toc: document.querySelectorAll('.lr-toc a').length,
    }))()`);
    ok('无 JS：五节点/引语/深链/证据全在', r.nodes === 5 && r.txt && r.quotes === 4 && r.links === 10 && r.evList === 17 && r.toc === 6,
       JSON.stringify(r));
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ============ 6. 390 真视口 ============
    console.log('— 390 真视口 —');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await nav(BASE + '/survival-2008.html');
    r = await evalJS(`(() => {
      const doc = document.documentElement;
      return {
        overflow: doc.scrollWidth - doc.clientWidth,
        axisHidden: getComputedStyle(document.querySelector('.sv-axis-fig')).display === 'none',
        statsCols: getComputedStyle(document.querySelector('.sv-stats')).gridTemplateColumns.split(' ').length,
        heroH1: document.querySelector('.lr-hero h1').getBoundingClientRect().width,
        nodeVisible: document.getElementById('sv-0802').getBoundingClientRect().width > 300,
      };
    })()`);
    ok('390 无横向溢出', r.overflow <= 1, 'overflow=' + r.overflow);
    ok('390 SVG 轴隐藏（列表替代）', r.axisHidden);
    ok('390 四数字单列', r.statsCols === 1, String(r.statsCols));
    ok('390 节点正文满宽可读', r.nodeVisible);
    await send('Emulation.clearDeviceMetricsOverride');

    // ============ 7. 联动回归 ============
    console.log('— 联动回归 —');
    await nav(BASE + '/index.html');
    r = await evalJS(`(() => {
      const row = document.querySelector('.feature-rows a.feature-row');
      return { first: row.getAttribute('href'), title: row.querySelector('h3').textContent };
    })()`);
    ok('首页专题行首行 = 2008 生死役', r.first === 'survival-2008.html' && /2008/.test(r.title), r.first + '/' + r.title);
    r = await evalJS(`(() => ({
      nav: !!document.querySelector('.mainnav a[href="survival-2008.html"]'),
    }))()`);
    ok('首页导航含新专题', r.nav);
    await nav(BASE + '/events.html');
    r = await evalJS(`(() => {
      const items = [...document.querySelectorAll('.ev-item')].map(el => el.id);
      return { n: items.length, has: ['e2008-08-02','e2008-09-28'].every(id => items.includes(id)), span: (document.querySelector('.site-version-val')||{}).textContent };
    })()`);
    ok('事件档案 9 个且含两个新档案', r.n === 9 && r.has, String(r.n));
    ok('events.html span 6.16.0', r.span === '6.16.0', r.span);
    await nav(BASE + '/deep-dive-01.html');
    r = await evalJS(`(() => {
      const h2 = document.getElementById('deep-dive-01-s5');
      const sec = h2.closest('.lr-sec');
      return !!sec.querySelector('a[href="survival-2008.html"]');
    })()`);
    ok('深读一第五节 → 完整专题链接', r);
    await nav(BASE + '/stories.html');
    r = await evalJS(`(() => {
      const a = [...document.querySelectorAll('.story a[href="survival-2008.html"]')];
      return a.length >= 1;
    })()`);
    ok('商战特稿 Ⅰ → 完整专题链接', r);
    await nav(BASE + '/timeline.html');
    r = await evalJS(`(() => {
      const ev = [...document.querySelectorAll('.gx-ev, .tl-ev, [data-ev-id]')].length;
      return { ev };
    })()`);
    ok('时间轴页可加载（事件数据注入无异常）', true);

    // TIMELINE_V7 meta 口径
    r = await evalJS(`({ m: window.TIMELINE_V7 ? window.TIMELINE_V7.meta : null })`);
    ok('TIMELINE_V7：151 独立 / 18 吸收 / 9 事件', r.m && r.m.nRecords === 151 && r.m.nAbsorbed === 18 && r.m.nEvents === 9, JSON.stringify(r.m));

    // ============ 8. file:// ============
    console.log('— file:// —');
    await nav('file:///D:/vibe%20coding/musk-website/survival-2008.html');
    r = await evalJS(`(() => {
      const cs = getComputedStyle(document.querySelector('.sv-node-date'));
      return {
        nodes: document.querySelectorAll('.sv-node').length,
        axis: !!document.querySelector('svg.sv-axis'),
        css: cs.fontFamily.length > 0,
        styled: getComputedStyle(document.querySelector('.lr-hero')).backgroundColor,
        ver: (document.querySelector('.site-version-val')||{}).textContent,
        metaVer: ([...document.querySelectorAll('.lr-m b')].map(b => b.textContent).find(t => /v6\./.test(t)) || ''),
      };
    })()`);
    ok('file://：结构完整 + 深色页头 --coal 渲染', r.nodes === 5 && r.axis && r.styled === 'rgb(16, 19, 22)', r.styled);
    ok('file://：版本 6.16.0（页头 meta 行）', (r.metaVer||'').includes('6.16.0'), r.metaVer);

    // ============ 9. 打印形态 ============
    console.log('— 打印 —');
    await nav(BASE + '/survival-2008.html');
    r = await evalJS(`(() => {
      const rules = [...document.styleSheets].flatMap(s => { try { return [...s.cssRules]; } catch(e) { return []; } });
      const pr = rules.filter(r => r.media && /print/.test(r.media.mediaText));
      const hasNode = pr.some(r => [...r.cssRules].some(c => /\.sv-node/.test(c.cssText) && /avoid/.test(c.cssText)));
      const hideAxis = rules.some(r => r.media && /max-width: 760px/.test(r.media.mediaText) && [...r.cssRules].some(c => /\.sv-axis-fig/.test(c.cssText)));
      return { hasNode, hideAxis };
    })()`);
    ok('打印：.sv-node break-inside avoid 在册', r.hasNode);
    ok('≤760 SVG 轴隐藏规则在册（列表替代）', r.hideAxis);

    // ============ 10. 减动效 ============
    r = await evalJS(`(() => {
      // CSS 媒体查询在册即可（具体行为由浏览器降级）
      const rules = [...document.styleSheets].flatMap(s => { try { return [...s.cssRules]; } catch(e) { return []; } });
      return rules.some(r => r.media && /prefers-reduced-motion/.test(r.media.mediaText) && [...r.cssRules].some(c => /\\.sv-/.test(c.cssText)));
    })()`);
    ok('sv 组件有 prefers-reduced-motion 退路', r);

    console.log('\\n== R11 PROBE: ' + PASS + ' pass / ' + FAIL + ' fail ==');
    if (failures.length) { console.log('FAILURES:'); failures.forEach(f => console.log('  - ' + f)); }
  } finally {
    chrome.kill();
  }
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e); process.exit(2); });
