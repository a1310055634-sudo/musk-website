/* ============================================================
   马斯克商业志 MUSK, INC. — 交互脚本
   模块：版本号 / 双语切换 / 入场动画 / 导航高亮
   约定：任何含 data-en 的元素都是叶子节点，中文为内容、英文为属性；
        切换逻辑只在这里，页面新增文案无需额外代码。
   ============================================================ */
'use strict';

(function () {
  var SITE_VERSION = '1.4.0';

  /* ---------- 版本号（页脚与报头共用 .site-version-val） ---------- */
  document.querySelectorAll('.site-version-val').forEach(function (el) {
    el.textContent = SITE_VERSION;
  });

  /* ---------- 双语切换 ---------- */
  var LANG_KEY = 'musk-inc-lang';
  var toggleBtn = document.getElementById('lang-toggle');
  var currentLang = 'zh';
  try {
    currentLang = localStorage.getItem(LANG_KEY) === 'en' ? 'en' : 'zh';
  } catch (e) { /* localStorage 不可用时保持中文 */ }

  function applyLang(lang) {
    currentLang = lang;
    try { localStorage.setItem(LANG_KEY, lang); } catch (e) { /* 忽略 */ }
    document.documentElement.lang = (lang === 'en') ? 'en' : 'zh-CN';
    document.querySelectorAll('[data-en]').forEach(function (el) {
      if (lang === 'en') {
        if (typeof el.dataset.zh === 'undefined') {
          el.dataset.zh = el.innerHTML; // 首次切换时缓存中文原稿
        }
        el.innerHTML = el.getAttribute('data-en');
      } else if (typeof el.dataset.zh !== 'undefined') {
        el.innerHTML = el.dataset.zh;
      }
    });
    if (toggleBtn) {
      toggleBtn.textContent = (lang === 'zh') ? 'EN' : '中文';
      toggleBtn.setAttribute('aria-pressed', lang === 'en' ? 'true' : 'false');
    }
  }

  applyLang(currentLang);
  if (toggleBtn) {
    toggleBtn.addEventListener('click', function () {
      applyLang(currentLang === 'zh' ? 'en' : 'zh');
    });
  }

  /* ---------- 入场动画（尊重系统减少动态偏好） ---------- */
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var revealEls = document.querySelectorAll('.reveal, .reveal-delay');
  if (reduceMotion || !('IntersectionObserver' in window)) {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  }

  /* ---------- 时间线分类筛选 ---------- */
  var filterBtns = Array.prototype.slice.call(document.querySelectorAll('.tl-btn'));
  var tlItems = Array.prototype.slice.call(document.querySelectorAll('.timeline .tl-item'));
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterBtns.forEach(function (b) { b.classList.remove('is-active'); });
      btn.classList.add('is-active');
      var f = btn.getAttribute('data-filter');
      tlItems.forEach(function (item) {
        var tag = item.querySelector('.tl-tag');
        var match = (f === 'all') || (tag && tag.classList.contains('t-' + f));
        item.classList.toggle('tl-hidden', !match);
        if (match && !reduceMotion) { // 重新触发淡入动画
          item.classList.remove('tl-pop');
          void item.offsetWidth;
          item.classList.add('tl-pop');
        }
      });
    });
  });

  /* ---------- 商战交互时间轴（点击展开/收起） ---------- */
  document.querySelectorAll('.acq-node > .acq-head').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var node = btn.parentElement;
      var open = node.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* ---------- 图表生长动画 ---------- */
  var charts = document.querySelectorAll('.chart-fig');
  if (reduceMotion || !('IntersectionObserver' in window)) {
    charts.forEach(function (el) { el.classList.add('chart-in'); });
  } else {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('chart-in');
          cio.unobserve(entry.target);
        }
      });
    }, { threshold: 0.25 });
    charts.forEach(function (el) { cio.observe(el); });
  }

  /* ---------- 导航高亮（scrollspy） ---------- */
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.mainnav a'));
  var watchedSections = navLinks
    .map(function (a) { return document.querySelector(a.getAttribute('href')); })
    .filter(Boolean);

  if ('IntersectionObserver' in window && watchedSections.length) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          navLinks.forEach(function (a) {
            var on = a.getAttribute('href') === '#' + entry.target.id;
            a.classList.toggle('active', on);
            if (on) { a.setAttribute('aria-current', 'true'); } else { a.removeAttribute('aria-current'); }
          });
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    watchedSections.forEach(function (sec) { spy.observe(sec); });
  }

  /* ---------- 顶部阅读进度条 ---------- */
  var pbar = document.querySelector('.progress');
  var ptick = false;
  function updBar() {
    var d = document.documentElement;
    var m = d.scrollHeight - d.clientHeight;
    if (pbar) pbar.style.width = (m > 0 ? (d.scrollTop / m) * 100 : 0) + '%';
    ptick = false;
  }
  window.addEventListener('scroll', function () {
    if (!ptick) { ptick = true; requestAnimationFrame(updBar); }
  }, { passive: true });
  updBar();

  /* ---------- 数字滚动 ---------- */
  var cnts = document.querySelectorAll('.cnt');
  function runCnt(el) {
    var t = parseInt(el.getAttribute('data-count'), 10) || 0, s = null;
    function step(ts) {
      if (!s) s = ts;
      var p = Math.min((ts - s) / 1200, 1);
      el.textContent = Math.round(t * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    }
    if (reduceMotion) { el.textContent = t; return; }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window && !reduceMotion) {
    var cObs = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) { runCnt(e.target); cObs.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    cnts.forEach(function (el) { cObs.observe(el); });
  }

  /* ---------- 语录横向轮播（原生滚动 + 圆点，7s 悬停暂停） ---------- */
  var strip = document.getElementById('quote-strip');
  if (strip) {
    var qs = strip.querySelectorAll('.quote');
    var dotsBox = document.createElement('div');
    dotsBox.className = 'quote-dots';
    dotsBox.setAttribute('role', 'group');
    dotsBox.setAttribute('aria-label', '语录切换');
    var qdots = [];
    qs.forEach(function (q, k) {
      var d = document.createElement('button');
      d.type = 'button';
      d.className = 'q-dot' + (k === 0 ? ' active' : '');
      d.setAttribute('aria-label', '语录 ' + (k + 1));
      d.addEventListener('click', function () { go(k); play(); });
      dotsBox.appendChild(d);
      qdots.push(d);
    });
    strip.parentNode.insertBefore(dotsBox, strip.nextSibling);
    var qi = 0, qtimer = null;
    function go(n) {
      qi = (n + qs.length) % qs.length;
      var w = strip.clientWidth;
      strip.scrollTo({ left: w * qi, behavior: reduceMotion ? 'auto' : 'smooth' });
      qdots.forEach(function (d, k) { d.classList.toggle('active', k === qi); });
    }
    function play() { if (reduceMotion) return; stop(); qtimer = setInterval(function () { go(qi + 1); }, 7000); }
    function stop() { if (qtimer) { clearInterval(qtimer); qtimer = null; } }
    strip.addEventListener('mouseenter', stop);
    strip.addEventListener('mouseleave', play);
    window.addEventListener('resize', function () { go(qi); });
    play();
  }

  /* ---------- 汉堡菜单开合 ---------- */
  var nbtn = document.getElementById('nav-toggle');
  var mh = document.querySelector('.masthead');
  if (nbtn && mh) {
    nbtn.addEventListener('click', function () {
      var open = mh.classList.toggle('nav-open');
      nbtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.querySelectorAll('#site-nav a').forEach(function (link) {
      link.addEventListener('click', function () {
        mh.classList.remove('nav-open');
        nbtn.setAttribute('aria-expanded', 'false');
      });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mh.classList.contains('nav-open')) {
        mh.classList.remove('nav-open');
        nbtn.setAttribute('aria-expanded', 'false');
        nbtn.focus();
      }
    });
    });
  }

  /* ---------- Konami 彩蛋：纸飞机掠过纸面 ---------- */
  var KONAMI = ['ArrowUp','ArrowUp','ArrowDown','ArrowDown','ArrowLeft','ArrowRight','ArrowLeft','ArrowRight','b','a'];
  var kIdx = 0;
  document.addEventListener('keydown', function (e) {
    var k = e.key.length === 1 ? e.key.toLowerCase() : e.key;
    kIdx = (k === KONAMI[kIdx]) ? kIdx + 1 : (k === KONAMI[0] ? 1 : 0);
    if (kIdx === KONAMI.length) {
      kIdx = 0;
      if (reduceMotion) return;
      var plane = document.createElement('div');
      plane.className = 'fly-plane';
      plane.setAttribute('aria-hidden', 'true');
      plane.innerHTML = '<svg width="72" height="40" viewBox="0 0 72 40" fill="none" stroke="#1a1a1a" stroke-width="1.6" stroke-linejoin="round"><path d="M2 22 L58 8 L40 26 L30 20 Z"/><path d="M30 20 L34 34 L40 26"/><path d="M44 12 L66 6" stroke="#7c2d2d" stroke-dasharray="4 4"/></svg>';
      document.body.appendChild(plane);
      setTimeout(function () { plane.remove(); }, 2800);
    }
  });

  /* ---------- 编者按随机金句 ---------- */
  var noteEl = document.getElementById('editor-note');
  var allQuotes = document.querySelectorAll('#quotes .quote');
  if (noteEl && allQuotes.length) {
    var pick = Math.floor(Math.random() * allQuotes.length);
    var en = allQuotes[pick].querySelector('.quote-en').textContent;
    var zh = allQuotes[pick].querySelector('.quote-zh').textContent;
    noteEl.innerHTML = '编者按 / Editor’s note：' + zh + '<span class="fn-en">' + en + '</span>';
  }
})();
