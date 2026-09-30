// V9-20 R10 探针：resources.html 结构/筛选/双语/无 JS/检索联动/390 零溢出
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9354;  // 9227 aDrive 占用；9333-9353 为此前轮次用过（防残留孤儿实例）
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
  // ---------- 文件级：口径复算 ----------
  console.log('[文件级] resources 口径复算');
  const rh = fs.readFileSync('resources.html', 'utf-8');
  A('rs-item 锚=10', (rh.match(/<article class="rs-item" id="r-/g) || []).length === 10,
    String((rh.match(/<article class="rs-item" id="r-/g) || []).length));
  A('四分类节在册', ['cat-official', 'cat-opensource', 'cat-community', 'cat-tools']
    .every(id => rh.includes('id="' + id + '"')));
  A('生成器署名与数据源在页脚',
    rh.includes('tools/build-resources.py') && rh.includes('tools/resources-data.py'));
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  A('索引总数=292', (sidx.match(/"id": "/g) || []).length === 292,
    String((sidx.match(/"id": "/g) || []).length));
  A('索引含社区资源 10 条（pg=resources.html）',
    (sidx.match(/"pg": "resources\.html"/g) || []).length === 10,
    String((sidx.match(/"pg": "resources\.html"/g) || []).length));
  let navPages = 0;
  for (const f of fs.readdirSync('.').filter(f => f.endsWith('.html'))) {
    if (fs.readFileSync(f, 'utf-8').includes('href="resources.html"')) navPages++;
  }
  A('resources.html 入站导航覆盖 38/38 页', navPages === 38, String(navPages));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r10-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
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
    A('hero 渲染（h1=社区资源 + 版本 8.10.0）',
      await ev(send, `document.querySelector('.lr-hero h1') && document.querySelector('.lr-hero h1').textContent === '社区资源' && document.body.textContent.includes('8.10.0')`));
    A('导航 aria-current=社区资源（资料组）',
      await ev(send, `document.querySelector('#site-nav a[aria-current="page"]') && document.querySelector('#site-nav a[aria-current="page"]').getAttribute('href') === 'resources.html'`));
    A('四分类节 × 条目 2/2/2/4',
      await ev(send, `(()=>{const g=c=>document.querySelectorAll('.rs-cat[data-cat="'+c+'"] .rs-item').length;
        return document.querySelectorAll('.rs-cat').length===4 && g('official')===2 && g('opensource')===2 && g('community')===2 && g('tools')===4;})()`));
    A('rs-item 总数=10', (await ev(send, `document.querySelectorAll('.rs-item').length`)) === 10);
    A('芯片五枚（全部+四类），「全部」默认按下',
      await ev(send, `document.querySelectorAll('.rs-fchip').length===5 &&
        document.querySelector('.rs-fchip[data-cat="all"]').getAttribute('aria-pressed')==='true'`));
    A('Teslamate 卡字段行：GitHub 实测 ★9,061 · AGPL-3.0 · 核活码 200',
      await ev(send, `(()=>{const c=document.getElementById('r-teslamate');
        return c && c.textContent.includes('★ 9,061') && c.textContent.includes('AGPL-3.0') &&
               c.querySelector('.rs-check').textContent.includes('HTTP 200') &&
               c.querySelector('.rs-check').textContent.includes('2026-10-01');})()`));
    A('Grok-1 卡：Apache-2.0 + 停更徽标 + 口径备注在',
      await ev(send, `(()=>{const c=document.getElementById('r-grok-1');
        return c && c.textContent.includes('Apache-2.0') && c.querySelector('.rs-act').textContent === '停更' &&
               c.querySelector('.rs-note') && c.querySelector('.rs-note').textContent.length > 10;})()`));
    A('外链 href 逐字正确（GitHub/SEC 双抽）',
      await ev(send, `document.querySelector('#r-teslamate .rs-name a').href === 'https://github.com/teslamate-org/teslamate' &&
        document.querySelector('#r-sec-edgar-tesla .rs-url').href.startsWith('https://www.sec.gov/')`));
    await ev(send, `document.querySelector('.rs-chipbar').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 500));
    await shot(send, 'qa/v9-20/round-10/resources-desktop.png', 'resources-desktop.png');

    // ---- 筛选 ----
    console.log('[筛选] 分类芯片');
    await ev(send, `document.querySelector('.rs-fchip[data-cat="opensource"]').click()`);
    A('点「开源项目」：aria-pressed 迁移 + 其余三节隐藏 + 状态行=2 条',
      await ev(send, `(()=>{const on=[...document.querySelectorAll('.rs-fchip')].filter(c=>c.getAttribute('aria-pressed')==='true').map(c=>c.getAttribute('data-cat'));
        const off=[...document.querySelectorAll('.rs-cat-off')].map(s=>s.getAttribute('data-cat'));
        const st=document.getElementById('rs-status').textContent;
        return on.length===1 && on[0]==='opensource' && off.length===3 && off.includes('official') && st.includes('2');})()`));
    await ev(send, `document.querySelector('.rs-fchip[data-cat="all"]').click()`);
    A('点「全部」恢复：四节全显 + 状态行=10 条',
      await ev(send, `document.querySelectorAll('.rs-cat-off').length===0 &&
        document.getElementById('rs-status').textContent.includes('10')`));

    // ---- 双语 ----
    console.log('[双语] EN 切换');
    await ev(send, `document.getElementById('lang-toggle').click()`);
    A('EN：h1=Community Resources',
      await ev(send, `document.querySelector('.lr-hero h1').textContent === 'Community Resources'`));
    A('EN：Teslamate 卡名与描述切换（自托管 logger 入文）',
      await ev(send, `(()=>{const c=document.getElementById('r-teslamate');
        return c.querySelector('.rs-name a').textContent.includes('self-hosted Tesla logger') &&
               c.querySelector('.rs-desc').textContent.includes('telemetry');})()`));
    A('EN：状态行已被筛选重写为英文口径（点一次芯片验证）',
      await ev(send, `(()=>{document.querySelector('.rs-fchip[data-cat="tools"]').click();
        return document.getElementById('rs-status').textContent.includes('Showing 4 resources');})()`));
    await ev(send, `document.querySelector('.rs-fchip[data-cat="all"]').click()`);
    await ev(send, `document.getElementById('lang-toggle').click()`);  // 切回中文
    A('切回中文：h1 复原「社区资源」',
      await ev(send, `document.querySelector('.lr-hero h1').textContent === '社区资源'`));

    // ---- 无 JS（禁脚本重载） ----
    console.log('[无 JS] 禁脚本重载');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('无 JS：10 条全量可见（四节全在、无 rs-cat-off）',
      await ev(send, `document.querySelectorAll('.rs-item').length===10 && document.querySelectorAll('.rs-cat-off').length===0`));
    A('无 JS：详情字段行静态在册（SEC 行核活码可读）',
      await ev(send, `document.getElementById('r-sec-edgar-tesla').querySelector('.rs-check').textContent.includes('HTTP 200')`));
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ---- 检索联动 ----
    console.log('[检索] search.html 联动');
    await send('Page.navigate', { url: BASE + '/search.html?q=Teslamate' });
    await new Promise(r => setTimeout(r, 1200));
    A('检索「Teslamate」命中且类型=社区资源',
      await ev(send, `[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html')) &&
        [...document.querySelectorAll('#sr-results *')].some(el=>el.textContent==='社区资源')`));
    A('类型按钮 10 枚（原 9 + 社区资源）',
      (await ev(send, `document.querySelectorAll('.sr-types button').length`)) === 10,
      String(await ev(send, `document.querySelectorAll('.sr-types button').length`)));
    await send('Page.navigate', { url: BASE + '/search.html?q=starlink&type=%E7%A4%BE%E5%8C%BA%E8%B5%84%E6%BA%90' });
    await new Promise(r => setTimeout(r, 1200));
    A('URL 参数 type=社区资源 被接受且 starlink.sx 命中',
      await ev(send, `document.querySelector('.sr-types button[aria-pressed="true"]').getAttribute('data-t')==='社区资源' &&
        [...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-starlink-sx'))`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[390] resources.html');
    const sw = await ev(send, `document.documentElement.scrollWidth`);
    const cw = await ev(send, `document.documentElement.clientWidth`);
    A(`[390] 零横向溢出（scrollWidth ${sw} ≤ clientWidth ${cw}）`, sw <= cw, sw + '>' + cw);
    A('[390] 芯片行可换行不溢出（chipbar 宽 ≤ clientWidth）',
      await ev(send, `document.querySelector('.rs-chipbar').getBoundingClientRect().right <= document.documentElement.clientWidth`));
    await ev(send, `document.getElementById('r-teslamate').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 600));
    await shot(send, 'qa/v9-20/round-10/resources-390.png', 'resources-390.png');
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
