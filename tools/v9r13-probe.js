// V9-20 R13 探针：resources.html +12（community 3→11 主） / 结构 / 筛选 / 双语 / 无 JS / 检索联动 / 390
//            + 关键回归：wikipedia 条目群在册、Reddit 假活不收（页内无该条）、revisions 导航治本保持
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9357;  // 前轮 9351-9356 用过，防残留孤儿实例
const BASE = 'http://127.0.0.1:8766';

const WIKI_IDS = ['r-wikipedia-elon-musk', 'r-wikipedia-spacex', 'r-wikipedia-tesla',
  'r-wikipedia-starship', 'r-wikipedia-twitter-acquisition', 'r-wikipedia-spacex-launches',
  'r-wikipedia-grok', 'r-wikipedia-neuralink'];
const NEW_IDS = WIKI_IDS.concat(['r-tesla-json-api-docs', 'r-tdorssers-teslapy',
  'r-powerwall2-local-api', 'r-planet4589-space']);

let PASS = 0, FAIL = 0;
function A(name, cond, detail) {
  if (cond) { PASS++; console.log('  \u2713 ' + name); }
  else { FAIL++; console.log('  \u2717 ' + name + (detail ? ' \u2014\u2014 ' + detail : '')); }
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
  console.log('[文件级] resources 口径 + 治本回归');
  const rh = fs.readFileSync('resources.html', 'utf-8');
  A('rs-item 锚=36', (rh.match(/<article class="rs-item" id="r-/g) || []).length === 36,
    String((rh.match(/<article class="rs-item" id="r-/g) || []).length));
  A('12 条新卡 id 全在册', NEW_IDS.every(id => rh.includes('id="' + id + '"')),
    NEW_IDS.filter(id => !rh.includes('id="' + id + '"')).join(','));
  A('community 节计数=11（R13 主题类）',
    (rh.match(/id="cat-community"[\s\S]*?<span class="rs-catcount">(\d+)<\/span>/) || [])[1] === '11',
    String((rh.match(/id="cat-community"[\s\S]*?rs-catcount">(\d+)</) || [])[1]));
  A('Reddit「假活」两项不收（teslamotors / SpaceXLounge wiki 不在页）',
    !/r\/teslamotors\/wiki/.test(rh) && !/r\/SpaceXLounge\/wiki/.test(rh),
    '误收空壳 wiki');
  A('R12 已收 r/SpaceX wiki 保留（回归不误删）',
    rh.includes('https://old.reddit.com/r/spacex/wiki/index'));
  A('wikipedia 判定证伪注记在卡内',
    rh.includes('DNS \u6c61\u67d3') && rh.includes('\u63a8\u7ffb'), '');
  A('版本 9.3.0 在页', rh.includes('9.3.0'));
  A('xAI / Neuralink 条目带公司标签（检索过滤用）',
    /id="r-wikipedia-grok"[\s\S]{0,2500}?xAI/.test(rh) && /id="r-wikipedia-neuralink"[\s\S]{0,2500}?Neuralink/.test(rh));
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  A('索引总数=318', (sidx.match(/"id": "/g) || []).length === 318,
    String((sidx.match(/"id": "/g) || []).length));
  A('索引含社区资源 36 条（pg=resources.html）',
    (sidx.match(/"pg": "resources\.html"/g) || []).length === 36,
    String((sidx.match(/"pg": "resources\.html"/g) || []).length));
  A('索引含 wikipedia-elon-musk 条目',
    sidx.includes('r-wikipedia-elon-musk'));
  // ---- 治本回归：revisions 导航（R12 修，防复发） ----
  const rv = fs.readFileSync('revisions.html', 'utf-8');
  A('治本保持：revisions.html 导航在册（含 resources 链接 + app.js）',
    rv.includes('href="resources.html"') && rv.includes('id="site-nav"') && rv.includes('app.js'),
    'nav=' + rv.includes('id="site-nav"') + ' appjs=' + rv.includes('app.js'));
  let navPages = 0;
  for (const f of fs.readdirSync('.').filter(f => f.endsWith('.html'))) {
    if (fs.readFileSync(f, 'utf-8').includes('href="resources.html"')) navPages++;
  }
  A('resources.html 入站导航覆盖 38/38 页', navPages === 38, String(navPages));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r13-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'],
    { stdio: 'ignore' });
  const shot = async (send, path, file) => {
    const c = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(path, Buffer.from(c.data, 'base64'));
    console.log('  \u00b7 截图 ' + file);
  };
  try {
    let targets;
    for (let i = 0; i < 60; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
    }
    if (!targets || !targets.length) throw new Error('CDP /json 60 次无响应');
    console.log('  \u00b7 CDP 已连上，targets=' + targets.length);
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
    A('hero 渲染（h1=社区资源 + 版本 9.3.0）',
      await ev(send, `document.querySelector('.lr-hero h1') && document.querySelector('.lr-hero h1').textContent === '社区资源' && document.body.textContent.includes('9.3.0')`));
    A('rs-item 总数=36', (await ev(send, `document.querySelectorAll('.rs-item').length`)) === 36,
      String(await ev(send, `document.querySelectorAll('.rs-item').length`)));
    A('四分类节 × 条目 10/9/11/6',
      await ev(send, `(()=>{const g=c=>document.querySelectorAll('.rs-cat[data-cat="'+c+'"] .rs-item').length;
        return document.querySelectorAll('.rs-cat').length===4 && g('official')===10 && g('opensource')===9 && g('community')===11 && g('tools')===6;})()`));
    A('wikipedia-elon-musk 卡：community 类 + 二手口径注记（DNS 污染证伪 + 非一手）',
      await ev(send, `(()=>{const c=document.getElementById('r-wikipedia-elon-musk');
        return c && c.querySelector('.rs-note').textContent.includes('DNS 污染') &&
               c.querySelector('.rs-note').textContent.includes('推翻');})()`));
    A('wikipedia 8 卡全渲染且均在 community 节',
      await ev(send, `${JSON.stringify(WIKI_IDS)}.every(id=>{const c=document.getElementById(id);
        return c && c.closest('.rs-cat[data-cat="community"]');})`));
    A('TeslaPy 卡：★417 + MIT + 核活码 200',
      await ev(send, `(()=>{const c=document.getElementById('r-tdorssers-teslapy');
        return c && c.textContent.includes('★ 417') && c.textContent.includes('MIT') &&
               c.querySelector('.rs-check').textContent.includes('HTTP 200');})()`));
    A('Powerwall 2 卡：★290 + Apache-2.0 + 停更徽标',
      await ev(send, `(()=>{const c=document.getElementById('r-powerwall2-local-api');
        return c && c.textContent.includes('★ 290') && c.textContent.includes('Apache-2.0') &&
               c.querySelector('.rs-act').textContent === '停更';})()`));
    A('planet4589 卡：tools 类 + 无 gh 字段行（非 GitHub 项目）',
      await ev(send, `(()=>{const c=document.getElementById('r-planet4589-space');
        return c && c.closest('.rs-cat[data-cat="tools"]') && !c.querySelector('.rs-gh');})()`));
    A('外链 href 逐字正确（wikipedia / tesla-api 文档站双抽）',
      await ev(send, `document.querySelector('#r-wikipedia-elon-musk .rs-url').href === 'https://en.wikipedia.org/wiki/Elon_Musk' &&
        document.querySelector('#r-tesla-json-api-docs .rs-url').href === 'https://tesla-api.timdorr.com/'`));
    await ev(send, `document.getElementById('r-wikipedia-elon-musk').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 500));
    await shot(send, 'qa/v9-20/round-13/resources-community-desktop.png', 'resources-community-desktop.png');

    // ---- 筛选 ----
    console.log('[筛选] 分类芯片');
    await ev(send, `document.querySelector('.rs-fchip[data-cat="community"]').click()`);
    A('点「社区与档案」：状态行=11 条 + 其余三节隐藏',
      await ev(send, `(()=>{const st=document.getElementById('rs-status').textContent;
        return st.includes('11') && document.querySelectorAll('.rs-cat-off').length===3;})()`));
    A('筛选后 wikipedia 8 卡仍可见',
      await ev(send, `${JSON.stringify(WIKI_IDS)}.every(id=>document.getElementById(id).offsetParent !== null)`));
    await ev(send, `document.querySelector('.rs-fchip[data-cat="all"]').click()`);
    A('点「全部」恢复：四节全显 + 状态行=36 条',
      await ev(send, `document.querySelectorAll('.rs-cat-off').length===0 &&
        document.getElementById('rs-status').textContent.includes('36')`));

    // ---- 双语 ----
    console.log('[双语] EN 切换');
    await ev(send, `document.getElementById('lang-toggle').click()`);
    A('EN：wikipedia 卡名切换（Wikipedia — Elon Musk）',
      await ev(send, `document.getElementById('r-wikipedia-elon-musk').querySelector('.rs-name a').textContent.includes('Wikipedia')`));
    A('EN：wikipedia 注记随语言（overturning 入文）',
      await ev(send, `document.getElementById('r-wikipedia-elon-musk').querySelector('.rs-note').textContent.includes('overturning')`));
    A('EN：community 节名显示 Community & Archives',
      await ev(send, `document.querySelector('.rs-cat[data-cat="community"] .rs-catname').textContent.includes('Community')`));
    await ev(send, `document.getElementById('lang-toggle').click()`);  // 切回中文
    A('切回中文：h1 复原「社区资源」',
      await ev(send, `document.querySelector('.lr-hero h1').textContent === '社区资源'`));

    // ---- 无 JS（禁脚本重载） ----
    console.log('[无 JS] 禁脚本重载');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('无 JS：36 条全量可见（四节全在、无 rs-cat-off）',
      await ev(send, `document.querySelectorAll('.rs-item').length===36 && document.querySelectorAll('.rs-cat-off').length===0`));
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ---- 检索联动 ----
    console.log('[检索] search.html 联动');
    await send('Page.navigate', { url: BASE + '/search.html?q=%E7%BB%B4%E5%9F%BA%E7%99%BE%E7%A7%91' });
    await new Promise(r => setTimeout(r, 1200));
    A('检索「维基百科」命中 wikipedia 卡',
      await ev(send, `[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-wikipedia-elon-musk'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=TeslaPy' });
    await new Promise(r => setTimeout(r, 1200));
    A('检索「TeslaPy」命中新增开源卡',
      await ev(send, `[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-tdorssers-teslapy'))`));
    await send('Page.navigate', { url: BASE + '/search.html?q=Grok' });
    await new Promise(r => setTimeout(r, 1200));
    A('检索「Grok」命中 wikipedia-Grok 卡（新旧同词）',
      await ev(send, `[...document.querySelectorAll('#sr-results a')].some(a=>a.href.includes('resources.html#r-wikipedia-grok'))`));

    // ---- 390 手机 ----
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[390] resources.html');
    const sw = await ev(send, `document.documentElement.scrollWidth`);
    const cw = await ev(send, `document.documentElement.clientWidth`);
    A(`[390] 零横向溢出（scrollWidth ${sw} \u2264 clientWidth ${cw}）`, sw <= cw, sw + '>' + cw);
    A('[390] community 节 11 卡全渲染',
      (await ev(send, `document.querySelectorAll('.rs-cat[data-cat="community"] .rs-item').length`)) === 11);
    await ev(send, `document.getElementById('r-wikipedia-elon-musk').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 600));
    await shot(send, 'qa/v9-20/round-13/resources-wikipedia-390.png', 'resources-wikipedia-390.png');
  } finally {
    try { chrome.kill(); } catch (e) {}
  }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
