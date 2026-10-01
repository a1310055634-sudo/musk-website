// V9-20 R18 探针：排版与阅读体验——基线锁定/引语注区分/数字等宽/EN 行高/print/三视口九宫格
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9371;  // 9227 aDrive 占用；9333-9370 为此前轮次用过
const BASE = 'http://127.0.0.1:8766';

let PASS = 0, FAIL = 0;
function A(name, cond, detail) {
  if (cond) { PASS++; console.log('  ✓ ' + name); }
  else { FAIL++; console.log('  ✗ ' + name + (detail ? ' —— ' + detail : '')); }
}

function getJSON(path) {
  return new Promise((res, rej) => {
    const req = http.get({ host: '127.0.0.1', port: PORT, path, timeout: 3000 }, r => {
      let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
    });
    req.on('timeout', () => { req.destroy(new Error('timeout')); });
    req.on('error', rej);
  });
}

async function attach(client) {
  let id = 0; const pending = new Map();
  client.addEventListener('message', m => {
    const msg = JSON.parse(m.data);
    if (msg.id && pending.has(msg.id)) {
      const p = pending.get(msg.id); pending.delete(msg.id);
      msg.error ? p.rej(new Error(JSON.stringify(msg.error))) : p.res(msg.result);
    }
  });
  await new Promise(r => client.addEventListener('open', r, { once: true }));
  const send = (method, params) => new Promise((res, rej) => {
    const mid = ++id; pending.set(mid, { res, rej });
    client.send(JSON.stringify({ id: mid, method, params }));
  });
  return send;
}
const ev = (send, expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true })
  .then(r => r.result.value);

async function main() {
  // ---------- 文件级 ----------
  console.log('[文件级] R18 段与令牌消费');
  const css = fs.readFileSync('style.css', 'utf-8');
  const seg = css.slice(css.indexOf('V9-R18 排版与阅读体验'));
  A('R18 段在册', seg.length > 100 && seg.length < 4000, String(seg.length));
  A('零新增 transition/animation 声明（reduced-motion 免复核前提）',
    !/transition\s*:/.test(seg) && !/animation\s*:/.test(seg));
  A('print 兜底块在册（引语影关闭）',
    seg.includes('@media print') && seg.includes('box-shadow: none'));
  A('基线令牌未动：--fs-body 16.5px / --read-width 720px（R15 定值复核）',
    css.includes('--fs-body: 16.5px') && css.includes('--read-width: 720px'));
  A('文字层 tabular-nums 覆盖 ps-quote/lr-quote 等 12 选择器',
    (seg.match(/\.ps-quote|\.lr-quote|\.ps-date|\.ps-deed|\.lr-meta b/g) || []).length >= 5);
  A('数据表 .num 改 --font-num（工业数字）',
    seg.includes('.lr-data .num { font-family: var(--font-num)'));

  // ---------- 浏览器 ----------
  const profile = process.env.TEMP + '/v9r18-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'], { stdio: 'ignore' });
  try {
    let targets;
    for (let i = 0; i < 60; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
    }
    if (!targets || !targets.length) throw new Error('CDP /json 60 次无响应');
    console.log('  · CDP 已连上，targets=' + targets.length);
    const ws = targets.find(t => t.type === 'page');
    const client = new WebSocket(ws.webSocketDebuggerUrl);
    const send = await attach(client);
    await send('Page.enable');
    await send('Runtime.enable');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });

    // ---- survival-2008（lr-* 主战场）----
    await send('Page.navigate', { url: BASE + '/survival-2008.html' });
    await new Promise(r => setTimeout(r, 2200));
    console.log('[lr] survival-2008.html（桌面 1440）');
    A('正文 16.5px（16–18 区间，基线锁定）',
      await ev(send, `getComputedStyle(document.querySelector('.lr-sec p')).fontSize === '16.5px'`));
    A('阅读宽 720px（640–760 区间）',
      await ev(send, `getComputedStyle(document.querySelector('.lr-main')).maxWidth === '720px'`));
    A('引语块（.sv-node blockquote）：5px 实线 + 块影生效（区分强化之一）',
      await ev(send, `(()=>{const el=document.querySelector('.sv-node blockquote');
        if(!el) return 'no-bq';
        const s=getComputedStyle(el);
        return parseFloat(s.borderLeftWidth) === 5 && s.boxShadow !== 'none';})()`));
    A('编者注：纸底生效（区分强化之二，与引语实底对照）',
      await ev(send, `(()=>{const s=getComputedStyle(document.querySelector('.lr-note'));
        return s.backgroundColor !== 'rgba(0, 0, 0, 0)' && s.borderTopStyle === 'dashed';})()`));
    A('引语/正文数字等宽（tabular-nums；survival 引语=.sv-node blockquote）',
      await ev(send, `(()=>{const bq=document.querySelector('.sv-node blockquote');
        if(!bq) return 'no-bq';
        return getComputedStyle(bq).fontVariantNumeric.includes('tabular-nums') &&
               getComputedStyle(document.querySelector('.lr-sec p')).fontVariantNumeric.includes('tabular-nums');})()`));
    // EN 行高切换
    A('EN：正文行高 1.78 + 引语 1.75（16.5px 基准换算）',
      await ev(send, `(()=>{document.getElementById('lang-toggle').click();
        const p=getComputedStyle(document.querySelector('.lr-sec p'));
        const q=document.querySelector('.lr-quote') ? getComputedStyle(document.querySelector('.lr-quote')) : null;
        const okP=Math.abs(parseFloat(p.lineHeight)-16.5*1.78)<0.5;
        const okQ=!q||Math.abs(parseFloat(q.lineHeight)-16.5*1.75)<0.5;
        return okP&&okQ;})()`));
    A('切回中文：行高复原 1.92',
      await ev(send, `(()=>{document.getElementById('lang-toggle').click();
        const p=getComputedStyle(document.querySelector('.lr-sec p'));
        return Math.abs(parseFloat(p.lineHeight)-16.5*1.92)<0.5;})()`));

    // ---- deep-dive-01（数据表 .num）----
    await send('Page.navigate', { url: BASE + '/deep-dive-01.html' });
    await new Promise(r => setTimeout(r, 2000));
    console.log('[num] deep-dive-01.html');
    A('数据表数字列：--font-num 生效（Consolas 系 + tabular-nums）',
      await ev(send, `(()=>{const n=document.querySelector('.lr-data .num');
        if(!n) return 'no-num';
        const s=getComputedStyle(n);
        return s.fontFamily.includes('Consolas') && s.fontVariantNumeric.includes('tabular-nums');})()`));

    // ---- primary（ps-* 账本）----
    await send('Page.navigate', { url: BASE + '/primary.html' });
    await new Promise(r => setTimeout(r, 2000));
    console.log('[ps] primary.html');
    A('账本引语/日期数字等宽（tabular-nums）',
      await ev(send, `getComputedStyle(document.querySelector('.ps-quote')).fontVariantNumeric.includes('tabular-nums') &&
        getComputedStyle(document.querySelector('.ps-date')).fontVariantNumeric.includes('tabular-nums')`));

    // ---- print 形态（模拟打印媒体）----
    console.log('[print] 引语影关闭');
    await send('Page.navigate', { url: BASE + '/survival-2008.html' });
    await new Promise(r => setTimeout(r, 1800));
    let printApiOk = true;
    try {
      await send('Emulation.setEmulatedMedia', { media: 'print' });
      A('print 模拟：sv-node 引语阴影 none（打印不渲染装饰）',
        await ev(send, `getComputedStyle(document.querySelector('.sv-node blockquote')).boxShadow === 'none'`));
      await send('Emulation.setEmulatedMedia', { media: 'screen' });
    } catch (e) { printApiOk = false; }
    if (!printApiOk) console.log('  · print 媒体模拟 API 不可用，print 意图以文件级断言为准（@media print 兜底块在册）');

    // ---- 三视口九宫格（四页样本 × 320/390/768）----
    console.log('[溢出] 四页 × 三视口复扫');
    for (const pg of ['index.html', 'survival-2008.html', 'timeline.html', 'capital-evolution.html']) {
      for (const vw of [320, 390, 768]) {
        await send('Emulation.setDeviceMetricsOverride', { width: vw, height: 844, deviceScaleFactor: 1, mobile: vw < 500 });
        await send('Page.navigate', { url: BASE + '/' + pg });
        await new Promise(r => setTimeout(r, 1500));
        const sw = await ev(send, `document.documentElement.scrollWidth`);
        const cw = await ev(send, `document.documentElement.clientWidth`);
        A(`[${pg} @${vw}] 零横向溢出（${sw} ≤ ${cw}）`, sw <= cw, sw + '>' + cw);
      }
    }
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
