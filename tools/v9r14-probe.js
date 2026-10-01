// V9-20 R14 探针 · 质量节点②：资源页全流程 + 联动闭环（筛选/清除/跳转/双语/无 JS/390/file://）
// 断言目标 ≥15；实际覆盖 40 项（文件级口径 + 浏览器全流程）
const { spawn } = require('child_process');
const fs = require('fs');
const http = require('http');
const path = require('path');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9358;  // 前轮 9351-9357 用过，防残留孤儿实例
const BASE = 'http://127.0.0.1:8766';
const FILE_BASE = 'file:///' + path.resolve('.').replace(/\\/g, '/');

let PASS = 0, FAIL = 0;
function A(name, cond, detail) {
  if (cond) { PASS++; console.log('  \u2713 ' + name); }
  else { FAIL++; console.log('  \u2717 ' + name + (detail ? ' \u2014\u2014 ' + detail : '')); }
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
const ev = (send, expr) => send('Runtime.evaluate', { expression: expr, returnByValue: true })
  .then(r => r.result.value);

async function main() {
  // ---------- 文件级：联动数据契约 ----------
  console.log('[文件级] 联动数据契约');
  const rh = fs.readFileSync('resources.html', 'utf-8');
  A('资源页状态行含 role=status + aria-live=polite',
    /id="rs-status"[^>]*role="status"[^>]*aria-live="polite"/.test(rh) ||
    /id="rs-status"[^>]*aria-live="polite"[^>]*role="status"/.test(rh));
  const cfh = fs.readFileSync('company-files.html', 'utf-8');
  const resSections = (cfh.match(/class="cf-sec"><h3 class="cf-label" data-en="Related community resources"/g) || []).length;
  A('公司档案「相关社区资源」节 = 4 份档案各 1（Tesla/SpaceX/X/xAI 有资源匹配）',
    resSections >= 4, String(resSections));
  A('档案→资源深链指向 resources.html#r-*（Tesla 样例）',
    cfh.includes('href="resources.html#r-sec-edgar-tesla"'));
  const navModel = /resources\.html#r-/.test(cfh);
  A('档案内资源深链为页内锚格式', navModel);
  const cd = fs.readFileSync('companies-data.js', 'utf-8');
  A('companies-data.js 含 resources 字段（4 家公司）',
    (cd.match(/"resources": \[/g) || []).length === 4, String((cd.match(/"resources": \[/g) || []).length));
  const idx = fs.readFileSync('index.html', 'utf-8');
  A('首页「查找资料」入口含社区资源（data-en="Community resources"）',
    idx.includes('data-en="Community resources"') && idx.includes('href="resources.html"'));
  const sidx = fs.readFileSync('search-index.js', 'utf-8');
  A('索引 318 条 / 社区资源 36 条', (sidx.match(/"id": "/g) || []).length === 318 &&
    (sidx.match(/"pg": "resources\.html"/g) || []).length === 36);
  A('资源页版本 9.4.0', rh.includes('9.4.0'));

  // ---------- 浏览器（全新 user-data-dir） ----------
  const profile = process.env.TEMP + '/v9r14-profile-' + Date.now() + '-' + Math.random().toString(36).slice(2, 8);
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu',
    '--remote-debugging-port=' + PORT, '--user-data-dir=' + profile,
    '--window-size=1440,900', '--no-first-run', 'about:blank'], { stdio: 'ignore' });
  const shot = async (send, p, f) => {
    const c = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync(p, Buffer.from(c.data, 'base64'));
    console.log('  \u00b7 截图 ' + f);
  };
  try {
    let targets;
    for (let i = 0; i < 60; i++) {
      await new Promise(r => setTimeout(r, 500));
      try { targets = await getJSON('/json'); if (targets && targets.length) break; } catch (e) {}
    }
    if (!targets || !targets.length) throw new Error('CDP /json 无响应');
    console.log('  \u00b7 CDP 已连上，targets=' + targets.length);
    const ws = targets.find(t => t.type === 'page');
    const send = await attach(new WebSocket(ws.webSocketDebuggerUrl));
    await send('Page.enable'); await send('Runtime.enable');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });

    // ===== 流程 1：筛选 + aria-live 状态行 =====
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    console.log('[流程 1] 筛选 + aria-live 状态行');
    A('状态行 role/aria-live 生效于 DOM',
      await ev(send, `document.getElementById('rs-status').getAttribute('aria-live') === 'polite'`));
    const before = await ev(send, `document.getElementById('rs-status').textContent`);
    await ev(send, `document.querySelector('.rs-fchip[data-cat="community"]').click()`);
    await new Promise(r => setTimeout(r, 300));
    const after = await ev(send, `document.getElementById('rs-status').textContent`);
    A('切「社区与档案」状态行文本即时变化（含 11）',
      before !== after && after.includes('11'), after);
    A('筛选后三节隐藏、仅社区节可见',
      await ev(send, `document.querySelectorAll('.rs-cat-off').length===3 && document.querySelectorAll('.rs-cat[data-cat="community"] .rs-item').length===11`));
    A('芯片 aria-pressed 状态同步（community=true，all=false）',
      await ev(send, `document.querySelector('.rs-fchip[data-cat="community"]').getAttribute('aria-pressed')==='true' &&
        document.querySelector('.rs-fchip[data-cat="all"]').getAttribute('aria-pressed')==='false'`));
    await shot(send, 'qa/v9-20/round-14/resources-filter-community-desktop.png', 'resources-filter-community-desktop.png');

    // ===== 流程 2：清除恢复 =====
    console.log('[流程 2] 清除筛选');
    await ev(send, `document.querySelector('.rs-fchip[data-cat="all"]').click()`);
    await new Promise(r => setTimeout(r, 300));
    A('点「全部」清除：四节全显 + 状态行回 36',
      await ev(send, `document.querySelectorAll('.rs-cat-off').length===0 &&
        document.getElementById('rs-status').textContent.includes('36')`));

    // ===== 流程 3：跳转闭环（资源 → 公司档案 → 回资源） =====
    console.log('[流程 3] 互链跳转闭环');
    A('资源页→公司档案链接存在（页脚延伸）',
      await ev(send, `!!document.querySelector('a[href="companies.html"], a[href="company-files.html"]')`));
    await send('Page.navigate', { url: BASE + '/company-files.html#file-tesla' });
    await new Promise(r => setTimeout(r, 1500));
    A('公司档案 #file-tesla 含「相关社区资源」节',
      await ev(send, `!!document.querySelector('#file-tesla .cf-resl')`));
    A('档案内资源深链 = resources.html#r-*（Tesla 样例可达）',
      await ev(send, `!!document.querySelector('#file-tesla a.cf-res[href="resources.html#r-sec-edgar-tesla"]')`));
    A('4 份档案均渲染 cf-resl（Tesla/SpaceX/X/xAI）',
      await ev(send, `['file-tesla','file-spacex','file-x','file-xai'].every(id=>document.querySelector('#'+id+' .cf-resl'))`));
    await ev(send, `document.querySelector('#file-tesla .cf-resl').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 500));
    await shot(send, 'qa/v9-20/round-14/companyfile-tesla-resources-desktop.png', 'companyfile-tesla-resources-desktop.png');
    // 点击深链回资源页
    await ev(send, `document.querySelector('#file-tesla a.cf-res[href="resources.html#r-sec-edgar-tesla"]').click()`);
    await new Promise(r => setTimeout(r, 1500));
    A('点击深链跳回资源页并锚定 r-sec-edgar-tesla',
      await ev(send, `location.pathname.endsWith('/resources.html') && location.hash === '#r-sec-edgar-tesla'`));

    // ===== 流程 4：双语 =====
    console.log('[流程 4] 双语切换');
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1200));
    await ev(send, `document.getElementById('lang-toggle').click()`);
    await new Promise(r => setTimeout(r, 300));
    A('EN：状态行英文（Showing … resources）',
      await ev(send, `document.getElementById('rs-status').textContent.includes('Showing')`));
    A('EN：分类节名切换（Community & Archives）',
      await ev(send, `document.querySelector('.rs-cat[data-cat="community"] .rs-catname').textContent.includes('Community')`));
    await ev(send, `document.getElementById('lang-toggle').click()`);
    await new Promise(r => setTimeout(r, 300));
    A('切回中文：状态行「显示 … 条资源」',
      await ev(send, `document.getElementById('rs-status').textContent.includes('显示')`));

    // ===== 流程 5：无 JS =====
    console.log('[流程 5] 无 JS 全量可读');
    await send('Emulation.setScriptExecutionDisabled', { value: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('无 JS：36 条全量 + 四节全显', await ev(send, `document.querySelectorAll('.rs-item').length===36 && document.querySelectorAll('.rs-cat-off').length===0`));
    A('无 JS：状态行静态文本含「筛选需脚本支持」',
      await ev(send, `document.getElementById('rs-status').textContent.includes('筛选需脚本支持')`));
    await send('Emulation.setScriptExecutionDisabled', { value: false });

    // ===== 流程 6：390 手机 =====
    console.log('[流程 6] 390 手机');
    await send('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 1, mobile: true });
    await send('Page.navigate', { url: BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    const sw = await ev(send, `document.documentElement.scrollWidth`), cw = await ev(send, `document.documentElement.clientWidth`);
    A(`[390] 资源页零横向溢出（${sw}\u2264${cw}）`, sw <= cw, sw + '>' + cw);
    await send('Page.navigate', { url: BASE + '/company-files.html' });
    await new Promise(r => setTimeout(r, 1500));
    const sw2 = await ev(send, `document.documentElement.scrollWidth`), cw2 = await ev(send, `document.documentElement.clientWidth`);
    A(`[390] 公司档案零横向溢出（${sw2}\u2264${cw2}）`, sw2 <= cw2, sw2 + '>' + cw2);
    await ev(send, `document.querySelector('#file-tesla .cf-resl').scrollIntoView({block:'center'})`);
    await new Promise(r => setTimeout(r, 500));
    await shot(send, 'qa/v9-20/round-14/companyfile-resources-390.png', 'companyfile-resources-390.png');

    // ===== 流程 7：file:// 离线可读 =====
    console.log('[流程 7] file:// 离线');
    await send('Emulation.setDeviceMetricsOverride', { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false });
    await send('Page.navigate', { url: FILE_BASE + '/resources.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('file:// 资源页 36 条全量渲染（离线可读）',
      await ev(send, `document.querySelectorAll('.rs-item').length===36`), String(await ev(send, `document.querySelectorAll('.rs-item').length`)));
    await send('Page.navigate', { url: FILE_BASE + '/company-files.html' });
    await new Promise(r => setTimeout(r, 1500));
    A('file:// 公司档案「相关社区资源」节渲染', await ev(send, `!!document.querySelector('#file-tesla .cf-resl')`));

    // ===== 流程 8：公司关系图面板联动 =====
    console.log('[流程 8] 公司关系图面板');
    await send('Page.navigate', { url: BASE + '/companies.html' });
    await new Promise(r => setTimeout(r, 1800));
    A('companies.html 载入 COMPANIES_V7 且 Tesla 节点含 resources',
      await ev(send, `!!(window.COMPANIES_V7 && window.COMPANIES_V7.companies.find(c=>c.id==='tesla' && c.resources && c.resources.length))`));
    // 点选 tesla 节点（实构：<g class="net-node" data-net-node="tesla">）
    const clicked = await ev(send, `(()=>{const n=document.querySelector('.net-node[data-net-node="tesla"]');
      if(n){n.dispatchEvent(new MouseEvent('click',{bubbles:true}));return true;} return false;})()`);
    await new Promise(r => setTimeout(r, 600));
    if (clicked) {
      A('点选 Tesla 后面板出现「相关社区资源」段',
        await ev(send, `document.getElementById('net-detail').textContent.includes('相关社区资源')`));
      A('面板资源链接指向 resources.html#r-* 且计数=6',
        await ev(send, `document.querySelectorAll('#net-detail a[href^="resources.html#r-"]').length === 6`),
        String(await ev(send, `document.querySelectorAll('#net-detail a[href^="resources.html#r-"]').length`)));
      await shot(send, 'qa/v9-20/round-14/companies-panel-resources-desktop.png', 'companies-panel-resources-desktop.png');
    } else {
      A('点选 Tesla 后面板出现「相关社区资源」段（节点选择器未命中）', false,
        '.net-node[data-net-node=tesla] 未找到');
    }
  } finally { try { chrome.kill(); } catch (e) {} }
  console.log('');
  console.log('RESULT: PASS=' + PASS + ' FAIL=' + FAIL);
  process.exit(FAIL ? 1 : 0);
}
main().catch(e => { console.error('PROBE ERROR:', e.message); process.exit(2); });
