// V9-20 R11 探针：resources.html +8 官方条目 / 结构 / 筛选 / 双语 / 无 JS / 检索联动（OpenAI 实体）/ 390 零溢出
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9355;  // 9227 aDrive 占用；9333-9354 为此前轮次用过（防残留孤儿实例）
const BASE = 'http://127.0.0.1:8766';

const NEW_IDS = ['r-spacex-starship', 'r-spacex-falcon9', 'r-spacex-updates',
  'r-tesla-fleet-api', 'r-neuralink-registry', 'r-openai-2015', 'r-xai-official',
  'r-boringcompany-official'];

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
  // ---------- 文件级：口径复算 ----------
  console.log('[文件级] resources 口径复算');
  const rh = fs.readFileSync('resources.html', 'utf-8');
  A('rs-item 锚=18', (rh.match(/<article class="rs-item" id="r-/g) || []).length === 18,
    String((rh.match(/<article class="rs-item" id="r-/g) || []).length));
  A('8 条新卡 id 全在册', NEW_IDS.every(id => rh.includes('id="' + id + '"')),
    NEW_IDS.filter(id => !rh.includes('id="' + id + '"')).join(','));
  A('official 节含 10 条（R11 主题类）', (() => {
    // 以 section id 定界（筛选芯片也有 data-cat 属性，不能用其切分）
    const start = rh.indexOf('id="cat-official"');
    const end = rh.indexOf('id="cat-opensource"');
    if (start < 0 || end < 0) return false;
    const seg = rh.slice(start, end);
    return (seg.match(/<article class="rs-item"/g) || []).length === 10;
  })(), 'official 节计数异常');
  A('反爬核活路径如实注记 7 处（服务端读取器口径）',
    (rh.match(/服务端读取器核活 200/g) || []).length === 7,
    String((rh.match(/服务端读取器核活 200/g) || []).length));
  A('生成器署名与数据源在页脚 + 版本 9.1.0',
    rh.includes('tools/build-resources.py') && rh.includes('tools/resources-data.py') &&
    rh.includes('9.1.0'));
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  A('索引总数=300', (sidx.match(/"id": "/g) || []).length === 300,
    String((sidx.match(/"id": "/g) || []).length));
  A('索引含社区资源 18 条（pg=resources.html）',
    (sidx.match(/"pg": "resources\.html"/g) || []).length === 18,
    String((sidx.match(/"pg": "resources\.html"/g) || []).length));
  A('OpenAI 实体入索引（c 含 OpenAI 且仅资源条目）',
    (sidx.match(/"c": \[\s*"OpenAI"/g) || []).length === 1,
    String((sidx.match(/"c": \[\s*"OpenAI"/g) || []).length));
  let navPages = 0;
  for (const f of fs.readdirSync('.').filter(f => f.endsWith('.html'))) {
    if (fs.readFileSync(f, 'utf-8').includes('href="resources.html"')) navPages++;
  }
  A('resources.html 入站导航覆盖 38/38 页', navPages === 38, String(navPages));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r11-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'],
    { stdio: 'ignore' });
  const shot = async (send, path, file) => {
    const c = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(path, Buffer.from(c.data, 'base64'));
    console.log('  · 截图 ' + file);
  };
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

    // ---- 结构 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[结构] resources.html');
    A('hero 渲染（h1=社区资源 + 版本 9.1.0）',
      await ev(send, `document.querySelector('.lr-hero h1') && document.querySelector('.lr-hero h1').textContent === '社区资源' && document.body.textContent.includes('9.1.0')`));
    A('rs-item 总数=18', (await ev(send, `document.querySelectorAll('.rs-item').length`)) === 18,
      String(await ev(send, `document.querySelectorAll('.rs-item').length`)));
    A('四分类节 × 条目 10/2/2/4',
      await ev(send, `(()=>{const g=c=>document.querySelectorAll('.rs-cat[data-cat="'+c+'"] .rs-item').length;
        return document.querySelectorAll('.rs-cat').length===4 && g('official')===10 && g('opensource')===2 && g('community')===2 && g('tools')===4;})()`));
    A('OpenAI 2015 卡：实体徽标 OpenAI + 停更徽标 + 历史定稿注记',
      await ev(send, `(()=>{const c=document.getElementById('r-openai-2015');
        return c && c.textContent.includes('OpenAI') && c.querySelector('.rs-act').textContent === '停更' &&
               c.querySelector('.rs-note').textContent.includes('历史定稿');})()`));
    A('SpaceX Starship 卡：核活路径注记（403 + 服务端读取器）+ 官方口径 reason',
      await ev(send, `(()=>{const c=document.getElementById('r-spacex-starship');
        return c && c.querySelector('.rs-note').textContent.includes('403') &&
               c.querySelector('.rs-note').textContent.includes('服务端读取器') &&
               c.textContent.includes('官方口径');})()`));
    A('Fleet API 卡：字段行许可=Tesla 开发者条款 + 核活码 200',
      await ev(send, `(()=>{const c=document.getElementById('r-tesla-fleet-api');
        return c && c.textContent.includes('Tesla 开发者条款') &&
               c.querySelector('.rs-check').textContent.includes('HTTP 200') &&
               c.querySelector('.rs-check').textContent.includes('2026-10-01');})()`));
    A('Boring Company 卡：Prufrock 简介在（直连 200 无反爬注记）',
      await ev(send, `(()=>{const c=document.getElementById('r-boringcompany-official');
        return c && c.querySelector('.rs-desc').textContent.includes('Prufrock') && !c.querySelector('.rs-note');})()`));
    A('外链 href 逐字正确（Starship/Fleet API/OpenAI 三抽）',
      await ev(send, `document.querySelector('#r-spacex-starship .rs-url').href === 'https://www.spacex.com/vehicles/starship/' &&
        document.querySelector('#r-tesla-fleet-api .rs-url').href === 'https://developer.tesla.com/' &&
        document.querySelector('#r-openai-2015 .rs-url').href === 'https://openai.com/blog/introducing-openai/'`));
    await ev(send, `document.getElementById('r-openai-2015').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 500));
    await shot(send, 'qa/v9-20/round-11/resources-openai-desktop.png', 'resources-openai-desktop.png');

    // ---- 筛选 ----
    console.log('[筛选] 分类芯片');
    await ev(send, `document.querySelector('.rs-fchip[data-cat="official"]').click()`);
    A('点「官方与标准」：状态行=10 条 + 其余三节隐藏',
      await ev(send, `(()=>{const st=document.getElementById('rs-status').textContent;
        return st.includes('10') && document.querySelectorAll('.rs-cat-off').length===3;})()`));
    await ev(send, `document.querySelector('.rs-fchip[data-cat="all"]').click()`);
    A('点「全部」恢复：四节全显 + 状态行=18 条',
      await ev(send, `document.querySelectorAll('.rs-cat-off').length===0 &&
        document.getElementById('rs-status').textContent.includes('18')`));

    // ---- 双语 ----
    console.log('[双语] EN 切换');
    await ev(send, `document.getElementById('lang-toggle').click()`);
    A('EN：OpenAI 卡名切换（Introducing OpenAI (2015)）',
      await ev(send, `document.getElementById('r-openai-2015').querySelector('.rs-name a').textContent.includes('Introducing OpenAI (2015)')`));
    A('EN：Starship 卡名切换 + 反爬注记随语言（server-side reader 入文）',
      await ev(send, `(()=>{const c=document.getElementById('r-spacex-starship');
        return c.querySelector('.rs-name a').textContent.includes('Starship') &&
               c.querySelector('.rs-note').textContent.includes('server-side reader');})()`));
    await ev(send, `document.getElementById('lang-toggle').click()`);  // 切回中文
    A('切回中文：h1 复原「社区资源」',
      await ev(send, `document.querySelector('.lr-hero h1').textContent === '社区资源'`));

    // ---- 无 JS（禁脚本重载） ----
    console.log('[无 JS] 禁脚本重载');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('无 JS：18 条全量可见（四节全在、无 rs-cat-off）',
      await ev(send, `document.querySelectorAll('.rs-item').length===18 && document.querySelectorAll('.rs-cat-off').length===0`));
    A('无 JS：新卡详情字段行静态在册（Neuralink 行核活码可读）',
      await ev(send, `document.getElementById('r-neuralink-registry').querySelector('.rs-check').textContent.includes('HTTP 200')`));
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ---- 检索联动 ----
    console.log('[检索] search.html 联动');
    await send('Page.navigate', { url: BASE + '/search.html?q=OpenAI' });
    await new Promise(r => setTimeout(r, 1200));
    A('检索「OpenAI」命中 r-openai-2015 且类型=社区资源',
      await ev(send, `[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-openai-2015')) &&
        [...document.querySelectorAll('#sr-results *')].some(el=>el.textContent==='社区资源')`));
    A('公司过滤出现 OpenAI 按钮（实体透传）',
      await ev(send, `[...document.querySelectorAll('#sr-companies button')].some(b=>b.textContent.indexOf('OpenAI')===0)`));
    A('点 OpenAI 公司过滤后命中保留（多对多过滤可用）',
      await ev(send, `(()=>{const b=[...document.querySelectorAll('#sr-companies button')].find(b=>b.textContent.indexOf('OpenAI')===0);
        b.click();
        return b.getAttribute('aria-pressed')==='true' &&
               [...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-openai-2015'));})()`));
    await send('Page.navigate', { url: BASE + '/search.html?q=Starship' });
    await new Promise(r => setTimeout(r, 1200));
    A('检索「Starship」命中官方星舰资源卡',
      await ev(send, `[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-spacex-starship'))`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[390] resources.html');
    const sw = await ev(send, `document.documentElement.scrollWidth`);
    const cw = await ev(send, `document.documentElement.clientWidth`);
    A(`[390] 零横向溢出（scrollWidth ${sw} ≤ clientWidth ${cw}）`, sw <= cw, sw + '>' + cw);
    A('[390] 官方节 10 卡全渲染',
      (await ev(send, `document.querySelectorAll('.rs-cat[data-cat="official"] .rs-item').length`)) === 10);
    await ev(send, `document.getElementById('r-openai-2015').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 600));
    await shot(send, 'qa/v9-20/round-11/resources-openai-390.png', 'resources-openai-390.png');
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
