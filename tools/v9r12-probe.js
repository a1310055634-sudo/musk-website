// V9-20 R12 探针：resources.html +6 开源/社区/工具条目 / 结构 / 筛选 / 双语 / 无 JS / 检索联动 / 390 / revisions 导航治本
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9356;  // 9227 aDrive 占用；9333-9355 为此前轮次用过（防残留孤儿实例）
const BASE = 'http://127.0.0.1:8766';

const NEW_IDS = ['r-tesla-api-io', 'r-timdorr-tesla-api', 'r-r-spacex-api',
  'r-starlink-grpc-tools', 'r-r-spacex-wiki', 'r-tessie'];

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
  console.log('[文件级] resources + revisions 治本口径');
  const rh = fs.readFileSync('resources.html', 'utf-8');
  A('rs-item 锚=24', (rh.match(/<article class="rs-item" id="r-/g) || []).length === 24,
    String((rh.match(/<article class="rs-item" id="r-/g) || []).length));
  A('6 条新卡 id 全在册', NEW_IDS.every(id => rh.includes('id="' + id + '"')),
    NEW_IDS.filter(id => !rh.includes('id="' + id + '"')).join(','));
  A('opensource 节含 6 条（R12 主题类）', (() => {
    const start = rh.indexOf('id="cat-opensource"');
    const end = rh.indexOf('id="cat-community"');
    if (start < 0 || end < 0) return false;
    return (rh.slice(start, end).match(/<article class="rs-item"/g) || []).length === 6;
  })(), 'opensource 节计数异常');
  A('死链判定证伪注记在卡内（tesla-api.io）',
    rh.includes('证伪死链判断'), '');
  A('版本 9.2.0 在页', rh.includes('9.2.0'));
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  A('索引总数=306', (sidx.match(/"id": "/g) || []).length === 306,
    String((sidx.match(/"id": "/g) || []).length));
  A('索引含社区资源 24 条（pg=resources.html）',
    (sidx.match(/"pg": "resources\.html"/g) || []).length === 24,
    String((sidx.match(/"pg": "resources\.html"/g) || []).length));
  const rv = fs.readFileSync('revisions.html', 'utf-8');
  A('治本断言：revisions.html 导航在册（build-revisions 模板内嵌 masthead）',
    rv.includes('href="resources.html"') && rv.includes('id="site-nav"') && rv.includes('app.js'),
    'nav=' + rv.includes('id="site-nav"') + ' appjs=' + rv.includes('app.js'));
  let navPages = 0;
  for (const f of fs.readdirSync('.').filter(f => f.endsWith('.html'))) {
    if (fs.readFileSync(f, 'utf-8').includes('href="resources.html"')) navPages++;
  }
  A('resources.html 入站导航覆盖 38/38 页', navPages === 38, String(navPages));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r12-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
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
    A('hero 渲染（h1=社区资源 + 版本 9.2.0）',
      await ev(send, `document.querySelector('.lr-hero h1') && document.querySelector('.lr-hero h1').textContent === '社区资源' && document.body.textContent.includes('9.2.0')`));
    A('rs-item 总数=24', (await ev(send, `document.querySelectorAll('.rs-item').length`)) === 24,
      String(await ev(send, `document.querySelectorAll('.rs-item').length`)));
    A('四分类节 × 条目 10/6/3/5',
      await ev(send, `(()=>{const g=c=>document.querySelectorAll('.rs-cat[data-cat="'+c+'"] .rs-item').length;
        return document.querySelectorAll('.rs-cat').length===4 && g('official')===10 && g('opensource')===6 && g('community')===3 && g('tools')===5;})()`));
    A('tesla-api.io 卡：停更徽标 + 死链证伪注记（服务端读取器口径）',
      await ev(send, `(()=>{const c=document.getElementById('r-tesla-api-io');
        return c && c.querySelector('.rs-act').textContent === '停更' &&
               c.querySelector('.rs-note').textContent.includes('证伪死链判断') &&
               c.querySelector('.rs-note').textContent.includes('服务端读取器');})()`));
    A('SpaceX-API 卡：存档徽标 + ★10,912 + archived 注记',
      await ev(send, `(()=>{const c=document.getElementById('r-r-spacex-api');
        return c && c.querySelector('.rs-act').textContent === '存档' &&
               c.textContent.includes('★ 10,912') && c.textContent.includes('archived');})()`));
    A('starlink-grpc-tools 卡：★710 + Unlicense + 核活码 200',
      await ev(send, `(()=>{const c=document.getElementById('r-starlink-grpc-tools');
        return c && c.textContent.includes('★ 710') && c.textContent.includes('Unlicense') &&
               c.querySelector('.rs-check').textContent.includes('HTTP 200');})()`));
    A('Tessie 卡：tools 类 + 商业非官方口径（无 gh 字段行）',
      await ev(send, `(()=>{const c=document.getElementById('r-tessie');
        return c && c.textContent.includes('非官方') && !c.querySelector('.rs-gh');})()`));
    A('外链 href 逐字正确（tesla-api.io / Reddit wiki 双抽）',
      await ev(send, `document.querySelector('#r-tesla-api-io .rs-url').href === 'https://tesla-api.io/' &&
        document.querySelector('#r-r-spacex-wiki .rs-url').href === 'https://old.reddit.com/r/spacex/wiki/index'`));
    await ev(send, `document.getElementById('r-tesla-api-io').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 500));
    await shot(send, 'qa/v9-20/round-12/resources-opensource-desktop.png', 'resources-opensource-desktop.png');

    // ---- 筛选 ----
    console.log('[筛选] 分类芯片');
    await ev(send, `document.querySelector('.rs-fchip[data-cat="opensource"]').click()`);
    A('点「开源项目」：状态行=6 条 + 其余三节隐藏',
      await ev(send, `(()=>{const st=document.getElementById('rs-status').textContent;
        return st.includes('6') && document.querySelectorAll('.rs-cat-off').length===3;})()`));
    await ev(send, `document.querySelector('.rs-fchip[data-cat="all"]').click()`);
    A('点「全部」恢复：四节全显 + 状态行=24 条',
      await ev(send, `document.querySelectorAll('.rs-cat-off').length===0 &&
        document.getElementById('rs-status').textContent.includes('24')`));

    // ---- 双语 ----
    console.log('[双语] EN 切换');
    await ev(send, `document.getElementById('lang-toggle').click()`);
    A('EN：r/SpaceX wiki 卡名切换（community wiki）',
      await ev(send, `document.getElementById('r-r-spacex-wiki').querySelector('.rs-name a').textContent.includes('community wiki')`));
    A('EN：tesla-api.io 注记随语言（disproving the dead-link read 入文）',
      await ev(send, `document.getElementById('r-tesla-api-io').querySelector('.rs-note').textContent.includes('disproving the dead-link read')`));
    await ev(send, `document.getElementById('lang-toggle').click()`);  // 切回中文
    A('切回中文：h1 复原「社区资源」',
      await ev(send, `document.querySelector('.lr-hero h1').textContent === '社区资源'`));

    // ---- 无 JS（禁脚本重载） ----
    console.log('[无 JS] 禁脚本重载');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('无 JS：24 条全量可见（四节全在、无 rs-cat-off）',
      await ev(send, `document.querySelectorAll('.rs-item').length===24 && document.querySelectorAll('.rs-cat-off').length===0`));
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ---- 检索联动 ----
    console.log('[检索] search.html 联动');
    await send('Page.navigate', { url: BASE + '/search.html?q=Tessie' });
    await new Promise(r => setTimeout(r, 1200));
    A('检索「Tessie」命中 r-tessie',
      await ev(send, `[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-tessie'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=starlink' });
    await new Promise(r => setTimeout(r, 1200));
    A('检索「starlink」同时命中工具站与 gRPC 脚本（回归+新增）',
      await ev(send, `[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-starlink-sx')) &&
        [...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-starlink-grpc-tools'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=%E5%8F%91%E5%B0%84%E6%95%B0%E6%8D%AE' });
    await new Promise(r => setTimeout(r, 1200));
    A('检索「发射数据」命中 SpaceX-API 卡（中文简介可检索）',
      await ev(send, `[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-r-spacex-api'))`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[390] resources.html');
    const sw = await ev(send, `document.documentElement.scrollWidth`);
    const cw = await ev(send, `document.documentElement.clientWidth`);
    A(`[390] 零横向溢出（scrollWidth ${sw} ≤ clientWidth ${cw}）`, sw <= cw, sw + '>' + cw);
    A('[390] 开源节 6 卡全渲染',
      (await ev(send, `document.querySelectorAll('.rs-cat[data-cat="opensource"] .rs-item').length`)) === 6);
    await ev(send, `document.getElementById('r-r-spacex-api').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 600));
    await shot(send, 'qa/v9-20/round-12/resources-spacexapi-390.png', 'resources-spacexapi-390.png');
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
