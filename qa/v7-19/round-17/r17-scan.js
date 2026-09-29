// V7-19 R17 双语审计：全站 EN 模式漏翻 + data-en 空值扫描（可复跑）
const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const CHROME = 'C:/Program Files/Google/Chrome/Application/chrome.exe';
const PORT = 9252;
const BASE = 'http://127.0.0.1:8766';

function getJSON(path) {
  return new Promise((res, rej) => {
    http.get({ host: '127.0.0.1', port: PORT, path }, r => {
      let d = ''; r.on('data', c => d += c); r.on('end', () => res(JSON.parse(d)));
    }).on('error', rej);
  });
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

// EN 模式下允许保留 CJK 的元素（设计意图：原文+译文并置/引语类）
const CJK_OK_SEL = ['.ps-zh', '.lr-quote-zh', '.iv-zh', '.pull-zh', '.cy-ev b', 'mark'].join(',');

const SCAN = `(() => {
  // 切到 EN
  var btn = document.getElementById('lang-toggle');
  if (btn && btn.textContent === 'EN') btn.click();
  var cjkRe = /[\\u4e00-\\u9fff]/;
  var okSel = ${JSON.stringify('CJK_OK_SEL')};
  var misses = [];
  var shrink = [];
  document.querySelectorAll('body *').forEach(function (el) {
    if (el.closest('.sr-evmat, .cite-box')) return;
    var direct = Array.prototype.filter.call(el.childNodes, function (n) { return n.nodeType === 3 && n.textContent.trim(); });
    if (!direct.length) return;
    var text = direct.map(function (n) { return n.textContent.trim(); }).join(' ');
    if (!cjkRe.test(text)) return;
    if (el.closest(${JSON.stringify('.ps-zh, .lr-quote-zh, .iv-zh, .pull-zh')})) return;
    var tag = el.tagName.toLowerCase();
    if (['script','style','textarea','title'].indexOf(tag) >= 0) return;
    var cls = (typeof el.className === 'string' ? el.className : '');
    var path = tag + (cls ? '.' + cls.split(' ')[0] : '');
    var de = el.getAttribute('data-en');
    if (de === null || de === undefined) {
      var key = path + ' :: ' + text.slice(0, 40);
      if (misses.indexOf(key) < 0 && misses.length < 12) misses.push(key);
    } else if (cjkRe.test(de)) {
      var key2 = path + ' [data-en含CJK] :: ' + de.slice(0, 40);
      if (misses.indexOf(key2) < 0 && misses.length < 12) misses.push(key2);
    }
  });
  // 切回中文
  var btn2 = document.getElementById('lang-toggle');
  if (btn2 && btn2.textContent === '中文') btn2.click();
  return { misses: misses };
})()`;

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
      if (r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails).slice(0, 300));
      return r.result.value;
    }

    const pages = fs.readFileSync('D:/vibe coding/v7r16-work/pages.txt', 'utf-8').trim().split('\n');
    const report = {};
    for (const pg of pages) {
      await send('Page.navigate', { url: BASE + '/' + pg });
      await sleep(650);
      if (pg === 'changelog.html') { process.stdout.write('c'); continue; } // changelog 中文维护（页顶英文说明已加）
      const r = await evalJS(`(() => {
        var btn = document.getElementById('lang-toggle');
        if (btn && btn.textContent === 'EN') btn.click();
        var cjkRe = /[\\u4e00-\\u9fff]/;
        var misses = [];
        document.querySelectorAll('body *').forEach(function (el) {
          if (el.closest('.sr-evmat, .cite-box, .cite-btn')) return;
          var direct = Array.prototype.filter.call(el.childNodes, function (n) { return n.nodeType === 3 && n.textContent.trim(); });
          if (!direct.length) return;
          var text = direct.map(function (n) { return n.textContent.trim(); }).join(' ');
          if (!cjkRe.test(text)) return;
          if (el.closest('.ps-zh, .lr-quote-zh, .iv-zh, .pull-zh, .tweet-zh, .ai-zh, .quote-zh, .qs-zh, .sv-ev li span, .ev-mat-note, .lang-toggle, figcaption, .iv-badge, .doc-badge')) return;
          if (el.id === 'lang-toggle' || tag === 'figcaption') return;
          var tag = el.tagName.toLowerCase();
          if (['script','style','textarea','title'].indexOf(tag) >= 0) return;
          var cls = (typeof el.className === 'string' ? el.className : '');
          var path = tag + (cls ? '.' + cls.split(' ')[0] : '');
          var de = el.getAttribute('data-en');
          if (de === null) {
            var key = path + ' :: ' + text.slice(0, 44);
            if (misses.indexOf(key) < 0 && misses.length < 14) misses.push(key);
          } else if (cjkRe.test(de)) {
            var key2 = path + ' [data-en含CJK] :: ' + de.slice(0, 44);
            if (misses.indexOf(key2) < 0 && misses.length < 14) misses.push(key2);
          }
        });
        var btn2 = document.getElementById('lang-toggle');
        if (btn2 && btn2.textContent === '中文') btn2.click();
        return { misses: misses };
      })()`);
      if (r.misses.length) report[pg] = r.misses;
      process.stdout.write('.');
    }
    console.log('\\nSCAN DONE');
    const out = JSON.stringify(report, null, 1);
    fs.writeFileSync('D:/vibe coding/v7r16-work/r17-misses.json', out);
    const total = Object.values(report).reduce((a, b) => a + b.length, 0);
    console.log('pages with misses: ' + Object.keys(report).length + ' / ' + pages.length + ' · total miss-types: ' + total);
    for (const [pg, arr] of Object.entries(report)) {
      console.log('== ' + pg + ' (' + arr.length + ')');
      arr.forEach(x => console.log('   ' + x));
    }
  } finally {
    chrome.kill();
  }
}
main().catch(e => { console.error('SCAN ERROR', e); process.exit(2); });
