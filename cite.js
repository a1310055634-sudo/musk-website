/* ============================================================
   马斯克商业志 MUSK, INC. — 引用组件（V7-19 R14）
   挂载页：primary / documents / interviews / x-posts
   功能：给每个带稳定 id 的资料单元注入「复制引用」按钮；
        引用文本含 标题 · 日期 · 出处页 · 稳定链接；
        复制三级退路：clipboard API → execCommand → 内嵌文本框手选。
   约定：无 id 的单元不注入（引用必须有稳定锚点）。
   ============================================================ */
'use strict';

(function () {
  var PAGES = {
    'primary.html':   { zh: '言行账本', en: 'Ledger' },
    'documents.html': { zh: '一手文档馆', en: 'Documents' },
    'interviews.html':{ zh: '访谈与表态', en: 'Interviews' },
    'x-posts.html':   { zh: 'X 帖史', en: 'X Posts' }
  };
  var KINDS = {
    'ps-row':      { zh: '言行账本条目', en: 'Ledger entry' },
    'doc-article': { zh: '一手文档',     en: 'Document' },
    'tweet-card':  { zh: 'X 帖收录',     en: 'X post (archived)' },
    'iv-item':     { zh: '访谈与表态',   en: 'Interview record' }
  };
  var page = (location.pathname.split('/').pop() || 'index.html').toLowerCase();
  if (!PAGES[page]) return;

  function lang() {
    return document.documentElement.getAttribute('lang') === 'en' ||
      (document.getElementById('lang-toggle') &&
       document.getElementById('lang-toggle').textContent === '中文') ? 'en' : 'zh';
  }

  function unitTitle(el) {
    var h = el.querySelector('h2, h3');
    if (h) {
      var t = h.textContent.trim().replace(/\s+/g, ' ');
      return t.length > 90 ? t.slice(0, 90) + '…' : t;
    }
    return '';
  }
  function unitDate(el, id) {
    var d = el.querySelector('.ps-date, .iv-date, .tw-date, .doc-date');
    if (d) return d.textContent.trim();
    var m = id.match(/(\d{4})-?(\d{2})?-?(\d{2})?/);
    if (m) return m[1] + (m[2] ? '.' + m[2] : '') + (m[3] ? '.' + m[3] : '');
    return '日期见原文';
  }
  function permalink(id) {
    if (/^https?:/.test(location.protocol)) {
      return location.origin + location.pathname + '#' + id;
    }
    return '离线文件 ' + page + '#' + id;
  }
  function buildCite(el) {
    var id = el.id;
    var kind = null;
    Object.keys(KINDS).forEach(function (k) { if (el.classList.contains(k)) kind = KINDS[k]; });
    if (!kind) kind = { zh: '资料条目', en: 'Record' };
    var L = lang();
    var title = unitTitle(el);
    var date = unitDate(el, id);
    var src = el.querySelector('.ps-src, .iv-meta, .tw-meta, .doc-meta');
    var srcText = src ? src.textContent.trim().replace(/\s+/g, ' ') : '';
    if (srcText.length > 120) srcText = srcText.slice(0, 120) + '…';
    if (L === 'en') {
      return 'MUSK, INC. · ' + kind.en + ' ' + id +
        (title ? ' · "' + title + '"' : '') +
        ' · ' + date +
        (srcText ? ' · ' + srcText : '') +
        ' · via ' + PAGES[page].en + ' (' + page + ')' +
        ' · Permalink: ' + permalink(id);
    }
    return '《马斯克商业志 MUSK, INC.》' + kind.zh + ' ' + id +
      (title ? ' ·「' + title + '」' : '') +
      ' · ' + date +
      (srcText ? ' · ' + srcText : '') +
      ' · 见本站「' + PAGES[page].zh + '」（' + page + '）' +
      ' · 稳定链接：' + permalink(id);
  }

  /* ---------- 复制三级退路 ---------- */
  function flash(btn, ok, text) {
    var old = btn.getAttribute('data-label') || btn.textContent;
    btn.setAttribute('data-label', old);
    btn.textContent = ok ? '已复制 ✓' : '请手动复制';
    btn.classList.add(ok ? 'cite-ok' : 'cite-fail');
    var box = el_getBox(btn);
    if (!ok && text) {
      box.value = text;
      box.style.display = 'block';
      box.focus();
      box.select();
    }
    setTimeout(function () {
      btn.textContent = btn.getAttribute('data-label');
      btn.classList.remove('cite-ok', 'cite-fail');
    }, 2200);
  }
  function el_getBox(btn) {
    var unit = btn.closest('.ps-row, .doc-article, .tweet-card, .iv-item');
    var box = unit.querySelector('.cite-box');
    if (!box) {
      box = document.createElement('textarea');
      box.className = 'cite-box';
      box.setAttribute('readonly', '');
      box.setAttribute('aria-label', '引用文本（可手动复制）');
      unit.appendChild(box);
    }
    return box;
  }
  function legacyCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.cssText = 'position:fixed;left:-999px;top:0';
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    var done = false;
    try { done = document.execCommand('copy'); } catch (e) { done = false; }
    document.body.removeChild(ta);
    return done;
  }
  function doCopy(btn) {
    var unit = btn.closest('.ps-row, .doc-article, .tweet-card, .iv-item');
    var text = buildCite(unit);
    function legacy() {
      if (legacyCopy(text)) flash(btn, true);
      else flash(btn, false, text);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      var settled = false;
      var timer = setTimeout(function () {
        if (!settled) { settled = true; legacy(); }
      }, 900);
      navigator.clipboard.writeText(text).then(
        function () {
          if (settled) return;
          settled = true;
          clearTimeout(timer);
          flash(btn, true);
        },
        function () {
          if (settled) return;
          settled = true;
          clearTimeout(timer);
          legacy();
        }
      );
    } else {
      legacy();
    }
  }

  /* ---------- 注入 ---------- */
  var units = document.querySelectorAll('.ps-row[id], .doc-article[id], .tweet-card[id], .iv-item[id]');
  var n = 0;
  units.forEach(function (el) {
    if (el.querySelector('.cite-btn')) return;
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'cite-btn';
    btn.textContent = '复制引用';
    btn.setAttribute('data-en', 'Cite');
    btn.setAttribute('aria-label', '复制本条引用文本 / Copy citation');
    btn.addEventListener('click', function () { doCopy(btn); });
    var head = el.querySelector('.ps-head, .iv-meta, .tw-head, .doc-head');
    if (head) head.appendChild(btn);
    else el.insertBefore(btn, el.firstChild);
    n++;
  });
  if (n) {
    var style = document.createElement('style');
    style.textContent = '.cite-box{display:none;width:100%;margin-top:8px;font:12px/1.6 monospace;color:var(--muted);border:1px dashed var(--hairline);background:#fff;padding:8px}';
    document.head.appendChild(style);
  }
})();
