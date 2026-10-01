// V9-20 R15 探针 · 设计系统令牌层验收
// 覆盖：令牌解析/语义别名等价性/公司色标未变/对比度修正落地/焦点环统一/三视口零溢出/截图与版本
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const path = require('path');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9362;   // 前轮 9351-9358 用过，防残留孤儿实例
const BASE = 'http://127.0.0.1:8766';

let PASS = 0, FAIL = 0;
const FAILED = [];
function A(name, cond, detail) {
  if (cond) { PASS++; console.log('  \u2713 ' + name); }
  else { FAIL++; FAILED.push(name); console.log('  \u2717 ' + name + (detail ? ' \u2014\u2014 ' + detail : '')); }
}
function getJSON(p) {
  return new Promise((res, rej) => {
    const req = http.get({ host: '127.0.0.1', port: PORT, path: p, timeout: 3000 }, r => {
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
  return (method, params) => new Promise((res, rej) => {
    const mid = ++id; pending.set(mid, { res, rej });
    client.send(JSON.stringify({ id: mid, method, params }));
  });
}

async function main() {
  // ================= 文件级 =================
  console.log('[文件级] 令牌层与产物');
  const css = fs.readFileSync('style.css', 'utf-8');
  const root = css.slice(css.indexOf(':root'), css.indexOf('}', css.indexOf(':root')));
  const bodyCss = css.slice(css.indexOf('}', css.indexOf(':root')));

  A('style.css 声明三层令牌结构（刻度/语义/焦点）',
    /刻度令牌/.test(css) && /语义别名|语义令牌/.test(css) && /焦点环/.test(css));
  const tokCount = (css.match(/^\s*--[a-z0-9-]+:/gm) || []).length;
  A('令牌项 ≥ 100（本轮 37 -> 100+）', tokCount >= 100, '实测 ' + tokCount);
  A('暖白刻度 5 档', ['--paper-0:', '--paper-50:', '--paper-100:', '--paper-150:', '--paper-200:'].every(t => root.includes(t)));
  A('近黑刻度 4 档', ['--coal-soft:', '--coal-0:', '--coal-100:', '--coal-200:'].every(t => root.includes(t)));
  A('朱红刻度 5 档', ['--accent-deep:', '--accent:', '--accent-bright:', '--accent-soft:', '--accent-glow:'].every(t => root.includes(t)));
  A('字号阶梯含 clamp 标题体系 + 固定正文阶梯',
    /--fs-h1: clamp\(/.test(root) && /--fs-h3: clamp\(/.test(root) && /--fs-body: 16\.5px/.test(root) && /--fs-3xs: 10px/.test(root));
  A('间距标尺 4/8 基（主阶 + 半阶 + 语义别名）',
    /--space-1: 4px/.test(root) && /--space-8: 64px/.test(root) && /--space-1h: 6px/.test(root) && /--gap-inline:/.test(root));
  A('圆角 6 档 / 阴影 6 档 / 描边 6 阶',
    /--r-1: 2px/.test(root) && /--r-circle: 50%/.test(root) && /--shadow-1:/.test(root) && /--shadow-accent-lg:/.test(root) && /--wash:/.test(root) && /--hairline-paper:/.test(root));
  A('焦点令牌统一出口（宽度 3/2 + 偏移 3/2/4 + 三态颜色）',
    /--focus-w: 3px/.test(root) && /--focus-w-tight: 2px/.test(root) && /--focus-offset-wide: 4px/.test(root) &&
    /--focus-color:/.test(root) && /--focus-color-dark:/.test(root) && /--focus-color-invert:/.test(root));

  console.log('[文件级] 公司色标红线未动（V7-R7 定稿值与语义）');
  const CO = [['--co-musk: #17191d'], ['--co-tesla: #C8102E'], ['--co-spacex: #1f3a5f'], ['--co-x: #43464d'],
              ['--co-xai: #5B4A8A'], ['--co-neuralink: #A04E77'], ['--co-boring: #7A601A'],
              ['--co-solarcity: #2E7D4F'], ['--co-paypal: #1476A8'], ['--co-history: #6B6558']];
  CO.forEach(([t]) => A('公司色标 ' + t, root.includes(t)));

  console.log('[文件级] 正文硬编码清零');
  A('无硬编码事件类型色（#4a6b3a/#8a5a00/#55524c/#1c7c40）',
    !/#4a6b3a|#8a5a00|#55524c|#1c7c40/i.test(bodyCss));
  A('无 font-size 像素字面值（全走 --fs-*；em/pt 相对单位保留）', !/font-size: \d+(\.\d+)?px/.test(bodyCss));
  A('无 outline 像素字面值（全走 --focus-*）', !/outline: \d+px/.test(bodyCss));
  A('无 border-radius 像素字面值（全走 --r-*；允许 0 重置）', !/border-radius: [1-9]/.test(bodyCss));
  A('无旧浅底小字色 #8a857c/#9a948b/#b3aea3/#a8a399/#d8d4cb/#d9d4cc/#d9a7a7',
    !/#8a857c|#9a948b|#b3aea3|#a8a399|#d8d4cb|#d9d4cc|#d9a7a7/i.test(bodyCss));
  A('无 #6f6a62（页脚彩蛋行，原 3.47:1 不达标）', !/#6f6a62/i.test(bodyCss));

  console.log('[文件级] 版本与产物');
  const VER = fs.readFileSync('VERSION', 'utf-8').trim();
  A('VERSION = 9.5.0', VER === '9.5.0', VER);
  A('app.js SITE_VERSION = 9.5.0', /SITE_VERSION = '9\.5\.0'/.test(fs.readFileSync('app.js', 'utf-8')));
  const pages = fs.readdirSync('.').filter(f => f.endsWith('.html'));
  const withSpan = pages.filter(f => fs.readFileSync(f, 'utf-8').includes('class="site-version-val">9.5.0<'));
  A('站点版本 span 覆盖 15 页（changelog.html 由正文提及而非 span）', withSpan.length === 15, String(withSpan.length));
  A('CHANGELOG 首条 = v9.5.0', /## v9\.5\.0 —/.test(fs.readFileSync('CHANGELOG.md', 'utf-8')));
  const shots = ['before', 'after'];
  A('before/after 截图各 16 张（4 页 × 2 视口 × 中英）',
    shots.every(d => fs.readdirSync(path.join('qa/v9-20/round-15', d)).filter(f => f.endsWith('.png')).length === 16));

  // ================= 浏览器 =================
  const profile = (process.env.TEMP || '/tmp') + '/v9r15-probe-' + Date.now();
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'], { stdio: 'ignore' });
  let targets;
  for (let i = 0; i < 60; i++) {
    await new Promise(r => setTimeout(r, 500));
    try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
  }
  if (!targets || !targets.length) throw new Error('CDP 无响应');
  const ws = targets.find(t => t.type === 'page');
  const client = new WebSocket(ws.webSocketDebuggerUrl);
  const send = await attach(client);
  const ev = (expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true }).then(r => r.result.value);

  await send('Page.enable');
  await send('Emulation.setEmulatedMedia', { features: [{ name: 'prefers-reduced-motion', value: 'reduce' }] });

  const goto = async (page, w, h) => {
    await send('Emulation.setDeviceMetricsOverride', { width: w, height: h, deviceScaleFactor: 1, mobile: w < 500 });
    await send('Page.navigate', { url: BASE + '/' + page });
    await new Promise(r => setTimeout(r, 1400));
  };
  const tok = (name) => ev(`getComputedStyle(document.documentElement).getPropertyValue('${name}').trim()`);

  console.log('[浏览器] 语义别名等价性（值与本轮之前一致）');
  await goto('index.html', 1440, 900);
  A('--paper = #F3F0E8', (await tok('--paper')).toLowerCase() === '#f3f0e8', await tok('--paper'));
  A('--coal = #101316', (await tok('--coal')).toLowerCase() === '#101316', await tok('--coal'));
  A('--ink = #17191d', (await tok('--ink')).toLowerCase() === '#17191d', await tok('--ink'));
  A('--muted = #5b5850', (await tok('--muted')).toLowerCase() === '#5b5850', await tok('--muted'));
  A('--card = #EBE7DC', (await tok('--card')).toLowerCase() === '#ebe7dc', await tok('--card'));
  A('--mist = rgba(243, 240, 232, 0.74)', (await tok('--mist')).replace(/\s/g, '') === 'rgba(243,240,232,0.74)', await tok('--mist'));
  A('--navy = #1f3a5f', (await tok('--navy')).toLowerCase() === '#1f3a5f', await tok('--navy'));
  A('--accent-text = #A63628', (await tok('--accent-text')).toLowerCase() === '#a63628', await tok('--accent-text'));
  const tyStart = await tok('--ty-start');
  A('--ty-start 指向色相刻度 #4a6b3a（或 var(--hue-olive) 引用）',
    /#4a6b3a/i.test(tyStart) || /--hue-olive/.test(tyStart), tyStart);
  const tyMile = await tok('--ty-milestone');
  A('--ty-milestone 指向 #55524c（或 var(--hue-graphite) 引用）',
    /#55524c/i.test(tyMile) || /--hue-graphite/.test(tyMile), tyMile);
  A('--accent 未变 #C84032', (await tok('--accent')).toLowerCase() === '#c84032', await tok('--accent'));
  A('--r-pill = 999px', (await tok('--r-pill')) === '999px', await tok('--r-pill'));
  A('--shadow-2 含 0.08 块影', /8px 8px 0 rgba\(23, 25, 29, 0\.08\)/.test(await tok('--shadow-2')));
  A('--focus-w = 3px', (await tok('--focus-w')) === '3px', await tok('--focus-w'));

  console.log('[浏览器] 体感令牌消费（实际元素计算值）');
  await goto('index.html', 1440, 900);
  A('页脚正文色 = --txd-3 rgb(217,212,204)',
    (await ev(`getComputedStyle(document.querySelector('.site-footer')).color`)) === 'rgb(217, 212, 204)',
    await ev(`getComputedStyle(document.querySelector('.site-footer')).color`));
  A('页脚 .footer-note 色 = --txd-5 rgb(168,163,153)',
    (await ev(`getComputedStyle(document.querySelector('.footer-note')).color`)) === 'rgb(168, 163, 153)',
    await ev(`getComputedStyle(document.querySelector('.footer-note')).color`));
  A('页脚 .footer-hint 色 = --txd-6 rgb(138,133,124)（原 3.47:1 修复）',
    (await ev(`getComputedStyle(document.querySelector('.footer-hint')).color`)) === 'rgb(138, 133, 124)',
    await ev(`getComputedStyle(document.querySelector('.footer-hint')).color`));
  A('页脚 .footer-disclaimer 色 = rgb(168,163,153)',
    (await ev(`getComputedStyle(document.querySelector('.footer-disclaimer')).color`)) === 'rgb(168, 163, 153)');

  console.log('[浏览器] 对比度修正落地（timeline / 账本轴标）');
  await goto('timeline.html', 1440, 900);
  A('timeline .gx-axis span 色 = --tx-3 rgb(106,102,93)（原 #8a857c 3.22:1）',
    (await ev(`getComputedStyle(document.querySelector('.gx-axis span')).color`)) === 'rgb(106, 102, 93)',
    await ev(`getComputedStyle(document.querySelector('.gx-axis span')).color`));
  A('timeline .gxl-q 引语行色 = rgb(106,102,93)（266 处）',
    (await ev(`getComputedStyle(document.querySelector('.gxl-q')).color`)) === 'rgb(106, 102, 93)',
    await ev(`getComputedStyle(document.querySelector('.gxl-q')).color`));
  A('timeline 不再出现旧灰 rgb(138,133,124) 作为正文/标注色',
    (await ev(`(function(){var els=document.querySelectorAll('.gx-axis span,.gxl-q,.gx-empty');for(var i=0;i<els.length;i++){if(getComputedStyle(els[i]).color==='rgb(138, 133, 124)')return false;}return true;})()`)));
  A('timeline tag 色 = --ty-*（.t-milestone = rgb(85,82,76)）',
    (await ev(`getComputedStyle(document.querySelector('.t-milestone')).color`)) === 'rgb(85, 82, 76)',
    await ev(`getComputedStyle(document.querySelector('.t-milestone')).color`));

  await goto('capital-evolution.html', 1440, 900);
  A('capital 图例线 = --tx-4 rgb(138,133,124)（装饰，非文字）',
    (await ev(`getComputedStyle(document.querySelector('.cap-lg-line')).backgroundColor`)) === 'rgb(138, 133, 124)',
    await ev(`getComputedStyle(document.querySelector('.cap-lg-line')).backgroundColor`));
  A('capital 图节点底色 = --paper-0 rgb(255,253,248)（原纯白 #fff）',
    (await ev(`getComputedStyle(document.querySelector('.cap-node-bg')).fill`)) === 'rgb(255, 253, 248)',
    await ev(`getComputedStyle(document.querySelector('.cap-node-bg')).fill`));
  A('capital 详情空态色 = --tx-3 rgb(106,102,93)',
    (await ev(`getComputedStyle(document.querySelector('.cap-detail-empty')).color`)) === 'rgb(106, 102, 93)',
    await ev(`getComputedStyle(document.querySelector('.cap-detail-empty')).color`));

  await goto('primary.html', 1440, 900);
  A('账本轴标 .pt-year 色 = --tx-3 rgb(106,102,93)',
    (await ev(`getComputedStyle(document.querySelector('.pt-year')).color`)) === 'rgb(106, 102, 93)',
    await ev(`getComputedStyle(document.querySelector('.pt-year')).color`));

  console.log('[浏览器] 焦点环统一（实聚焦读取）');
  await goto('index.html', 1440, 900);
  // 程序化 .focus() 不触发 :focus-visible，须用真实 Tab 键事件
  await send('Input.dispatchKeyEvent', { type: 'rawKeyDown', windowsVirtualKeyCode: 9, key: 'Tab', code: 'Tab', nativeVirtualKeyCode: 9 });
  await send('Input.dispatchKeyEvent', { type: 'keyUp', windowsVirtualKeyCode: 9, key: 'Tab', code: 'Tab', nativeVirtualKeyCode: 9 });
  await new Promise(r => setTimeout(r, 250));
  const focused = await ev(`(function(){var a=document.activeElement;return a? (a.tagName+'.'+(a.className||'')+'|'+(a.getAttribute('href')||'')) : 'none';})()`);
  A('Tab 聚焦命中可聚焦元素（skip-link/导航）', focused !== 'none' && focused !== 'BODY.', String(focused));
  const focusInfo = await ev(`(function(){
    var a=document.activeElement; if(!a) return null;
    var cs=getComputedStyle(a);
    return {w:cs.outlineWidth, style:cs.outlineStyle, off:cs.outlineOffset, col:cs.outlineColor};
  })()`);
  A('导航链接聚焦 outlineWidth = 3px（--focus-w）', focusInfo && focusInfo.w === '3px', JSON.stringify(focusInfo));
  A('导航链接聚焦 outlineStyle = solid 且颜色 = --accent rgb(200,64,50)',
    focusInfo && focusInfo.style === 'solid' && focusInfo.col === 'rgb(200, 64, 50)', JSON.stringify(focusInfo));
  A('导航链接聚焦 outlineOffset = 3px（--focus-offset）', focusInfo && focusInfo.off === '3px', JSON.stringify(focusInfo));

  console.log('[浏览器] 对比度抽测（浏览器实算，WCAG 2.1 公式）');
  await goto('timeline.html', 1440, 900);
  const cRatios = await ev(`(function(){
    function lum(c){var m=c.slice(c.indexOf('(')+1,c.indexOf(')')).split(',').map(Number);m=m.slice(0,3).map(function(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);});return 0.2126*m[0]+0.7152*m[1]+0.0722*m[2];}
    function ratio(a,b){var x=lum(a),y=lum(b);return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05);}
    var paper=getComputedStyle(document.body).backgroundColor;
    var out={};
    var targets={gxAxis:'.gx-axis span', gxlq:'.gxl-q', gxEmpty:'.gx-empty', muted:'.gxl-co'};
    var synth=document.createElement('p'); synth.className='gx-empty'; synth.textContent='x';
    document.body.appendChild(synth);
    for(var k in targets){var el=document.querySelector(targets[k]); if(el){out[k]=Math.round(ratio(getComputedStyle(el).color,paper)*100)/100;}}
    synth.parentNode.removeChild(synth);
    return out;
  })()`);
  A('timeline .gx-axis span 对比度 ≥4.5（原 3.22）', cRatios && cRatios.gxAxis >= 4.5, JSON.stringify(cRatios));
  A('timeline .gxl-q 对比度 ≥4.5（原 3.22）', cRatios && cRatios.gxlq >= 4.5, JSON.stringify(cRatios));
  A('timeline .gx-empty 对比度 ≥4.5（原 2.64）', cRatios && cRatios.gxEmpty >= 4.5, JSON.stringify(cRatios));
  A('timeline .gxl-co（--muted）对比度 ≥4.5', cRatios && cRatios.muted >= 4.5, JSON.stringify(cRatios));
  await goto('index.html', 1440, 900);
  const footRatio = await ev(`(function(){
    function lum(c){var m=c.slice(c.indexOf('(')+1,c.indexOf(')')).split(',').map(Number);m=m.slice(0,3).map(function(v){v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4);});return 0.2126*m[0]+0.7152*m[1]+0.0722*m[2];}
    function ratio(a,b){var x=lum(a),y=lum(b);return (Math.max(x,y)+0.05)/(Math.min(x,y)+0.05);}
    var bg=getComputedStyle(document.querySelector('.site-footer')).backgroundColor;
    var el=document.querySelector('.footer-hint');
    return Math.round(ratio(getComputedStyle(el).color,bg)*100)/100;
  })()`);
  A('页脚 .footer-hint 对比度 ≥4.5（原 3.47 不达标）', footRatio >= 4.5, String(footRatio));

  console.log('[浏览器] 三视口零横向溢出（320 / 390 / 768）');
  for (const [tag, w] of [['320', 320], ['390', 390], ['768', 768]]) {
    let bad = [];
    for (const p of ['index.html', 'survival-2008.html', 'timeline.html', 'capital-evolution.html']) {
      await goto(p, w, 900);
      const over = await ev(`document.documentElement.scrollWidth - document.documentElement.clientWidth`);
      if (over > 1) bad.push(p + ':' + over + 'px');
    }
    A(`四页 ${tag}px 零横向溢出`, bad.length === 0, bad.join(' '));
  }

  // 截图（桌面样板：tokens 落地证据）
  await goto('index.html', 1440, 900);
  const shot = await send('Page.captureScreenshot', { format: 'png' });
  fs.mkdirSync('qa/v9-20/round-15/probe', { recursive: true });
  fs.writeFileSync('qa/v9-20/round-15/probe/probe-index-desktop.png', Buffer.from(shot.data, 'base64'));
  A('探针截图落盘', fs.existsSync('qa/v9-20/round-15/probe/probe-index-desktop.png'));

  console.log(`\n结果：${PASS}/${PASS + FAIL} 通过` + (FAIL ? `，失败 ${FAIL}：${FAILED.join(' | ')}` : ''));
  client.close(); chrome.kill();
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR', e.message); process.exit(1); });
