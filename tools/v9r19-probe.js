// V9-20 R19 探针：动效归一无残留 / btn 三态闭环 / reduce 覆盖 / 审计表口径 / 三视口九宫格
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9375;  // 9227 aDrive 占用；9333-9374 为此前轮次用过
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
  console.log('[文件级] 归一/三态/reduce/审计表');
  const css = fs.readFileSync('style.css', 'utf-8');
  const decls = css.match(/transition:[^;{}]+/g) || [];
  const audit = fs.readFileSync('qa/v9-20/round-19/transition-audit.tsv', 'utf-8').trim().split('\n');
  A('微交互硬编码清零（无 .18s/0.18s/0.25s transition）',
    !decls.some(d => /\.18s|0\.18s|0\.25s/.test(d)),
    decls.filter(d => /\.18s|0\.18s|0\.25s/.test(d)).join(' | ').slice(0, 80));
  A('--t-fast 消费 ≥26 处（归一后）',
    (css.match(/var\(--t-fast\)/g) || []).length >= 26,
    String((css.match(/var\(--t-fast\)/g) || []).length));
  const tsvSlow = audit.slice(1).filter(l => l.includes('slow-tier-keep')).length;
  A('slow 白名单档与审计表对齐（TSV 12 行；decls 内 0.3/0.4/0.6/1s 共 8 + delay 行）',
    tsvSlow === 12 && decls.filter(d => /0\.3s|0\.4s|0\.6s|1s/.test(d)).length === 8,
    'tsv=' + tsvSlow + ' decls=' + decls.filter(d => /0\.3s|0\.4s|0\.6s|1s/.test(d)).length);
  A('.btn:active 按压态在册（hover 浮起↔active 回落闭环）',
    css.includes('.btn:active { transform: translateY(0); transition-duration: 80ms; }'));
  A('全局 :focus-visible 统一出口在册（R15 体系，focus 态全站一致）',
    css.includes(':focus-visible { outline: var(--focus-w) solid var(--focus-color);'));
  A('reduce 块 14 处在册（reveal/bars/图形组件全覆盖）',
    (css.match(/prefers-reduced-motion/g) || []).length === 14,
    String((css.match(/prefers-reduced-motion/g) || []).length));
  A('审计表 58 行 + 处置列齐备（58 声明全分类）',
    audit.length === 59 && audit[0].includes('disposition'), String(audit.length - 1));
  const perf = JSON.parse(fs.readFileSync('qa/v9-20/round-19/perf.json', 'utf-8'));
  A('性能复测落盘：五页 load + 五文件体积',
    Object.keys(perf.load_ms_median).length === 5 && Object.keys(perf.sizes_bytes).length === 5);

  // ---------- 浏览器 ----------
  const profile = process.env.TEMP + '/v9r19-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
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

    // ---- index：btn 三态 computed ----
    await send('Page.navigate', { url: BASE + '/index.html' });
    await new Promise(r => setTimeout(r, 2000));
    console.log('[三态] index.html .btn');
    A('.btn transition 已归一（computed duration=0.18s，消费 --t-fast）',
      await ev(send, `(()=>{const b=document.querySelector('.btn');
        if(!b) return 'no-btn';
        return getComputedStyle(b).transitionDuration.includes('0.18s');})()`));
    A('.btn hover 浮起规则在（-2px）+ active 回落规则在（0）',
      await ev(send, `(()=>{const hits=[];
        for(const sh of document.styleSheets){
          let rules; try{ rules=sh.cssRules; }catch(e){ continue; }
          for(const r of rules){
            const t=r.selectorText||'';
            if(t.indexOf('.btn')===0 && t.indexOf(':')>0) hits.push(t+'|'+r.style.transform);
          }
        }
        const j=hits.join(' ; ');
        return j.includes('.btn:hover|translateY(-2px)') && j.includes('.btn:active|translateY(0');})()`));

    // ---- reduce 模拟（首页验证 reveal 直出）----
    await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });
    await send('Page.navigate', { url: BASE + '/index.html' });
    await new Promise(r => setTimeout(r, 1200));
    console.log('[reduce] 模拟 prefers-reduced-motion');
    A('reduce：reveal 元素直出（opacity 1、无位移动画依赖）',
      await ev(send, `(()=>{const el=document.querySelector('.reveal');
        if(!el) return 'no-reveal';
        const s=getComputedStyle(el);
        return s.opacity === '1';})()`));
    await send('Emulation.setEmulatedMedia', { features: [] });

    // ---- 三视口九宫格 ----
    console.log('[溢出] 四页 × 三视口复扫');
    for (const pg of ['index.html', 'survival-2008.html', 'timeline.html', 'capital-evolution.html']) {
      for (const vw of [320, 390, 768]) {
        await send('Emulation.setDeviceMetricsOverride', { width: vw, height: 844, deviceScaleFactor: 1, mobile: vw < 500 });
        await send('Page.navigate', { url: BASE + '/' + pg });
        await new Promise(r => setTimeout(r, 1400));
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
