/* ============================================================
   马斯克商业志 MUSK, INC. — 交互脚本
   模块：版本号 / 双语切换 / 入场动画 / 导航高亮
   约定：任何含 data-en 的元素都是叶子节点，中文为内容、英文为属性；
        切换逻辑只在这里，页面新增文案无需额外代码。
   ============================================================ */
'use strict';

(function () {
  var SITE_VERSION = '7.4.0';

  /* JS 可用标记：.reveal 入场动画仅在 html.js 下隐藏（脚本失败正文照常可见） */
  document.documentElement.classList.add('js');

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
    .map(function (a) {
      var href = a.getAttribute('href') || '';
      return (href.charAt(0) === '#') ? document.querySelector(href) : null;
    })
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

  /* ---------- 长文目录滚动定位（R5：.lr-toc 链接 ↔ 文内章节） ---------- */
  document.querySelectorAll('.lr-toc').forEach(function (toc) {
    var links = Array.prototype.slice.call(toc.querySelectorAll('a[href^="#"]'));
    if (!links.length || !('IntersectionObserver' in window)) return;
    /* 链接↔章节配对：id 在标题上，观察对象取整节（高亮带需要足够高的元素穿过） */
    var pairs = [];
    links.forEach(function (a) {
      var el = document.getElementById(a.getAttribute('href').slice(1));
      if (!el) return;
      pairs.push({ sec: el.closest('.lr-sec') || el, link: a });
    });
    if (!pairs.length) return;
    var lspy = new IntersectionObserver(function (entries) {
      /* 相邻短章节可能同时触带：取与高亮带相交最多的一节；
         不足 8px 的擦边相交无参选资格（状态变化分批送达时会单独成批，防其覆盖真胜者） */
      var best = null;
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        var h = en.intersectionRect.height;
        if (h < 8) return;
        if (!best || h > best.h) best = { t: en.target, h: h };
      });
      if (!best) return;
      pairs.forEach(function (p) {
        p.link.classList.toggle('lr-on', p.sec === best.t);
      });
    }, { rootMargin: '-25% 0px -65% 0px' });
    pairs.forEach(function (p) { lspy.observe(p.sec); });
  });

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
    strip.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); go(qi + 1); stop(); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); go(qi - 1); stop(); }
      else if (e.key === 'Home') { e.preventDefault(); go(0); stop(); }
      else if (e.key === 'End') { e.preventDefault(); go(qs.length - 1); stop(); }
    });
    strip.addEventListener('focus', stop);
    strip.addEventListener('blur', play);
    window.addEventListener('resize', function () { go(qi); });
    play();
  }

  /* ---------- 汉堡菜单开合 ---------- */
  var nbtn = document.getElementById('nav-toggle');
  var mh = document.querySelector('.masthead');
  /* 打开面板时自动展开含当前页的分组 */
  function openCurrentGroup() {
    var cur = document.querySelector('#site-nav a[aria-current="page"]');
    var g = cur ? cur.closest('.nav-group') : null;
    if (g) {
      g.classList.add('open');
      var l = g.querySelector('.nav-label');
      if (l) l.setAttribute('aria-expanded', 'true');
    }
  }
  if (nbtn && mh) {
    nbtn.addEventListener('click', function () {
      var open = mh.classList.toggle('nav-open');
      nbtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      if (open) { openCurrentGroup(); } else { closeAllGroups(); }
    });
    document.querySelectorAll('#site-nav a').forEach(function (link) {
      link.addEventListener('click', function () {
        mh.classList.remove('nav-open');
        nbtn.setAttribute('aria-expanded', 'false');
        closeAllGroups();
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

  /* ---------- 全局导航分组下拉（R4：点击开合 / 外点关闭 / Esc 归位） ----------
     桌面 hover 与键盘 focus-within 由 CSS 负责；这里补触屏点击与关闭语义。 */
  var navLabels = Array.prototype.slice.call(document.querySelectorAll('.nav-label'));
  function closeAllGroups() {
    navLabels.forEach(function (l) {
      l.setAttribute('aria-expanded', 'false');
      var g = l.closest('.nav-group');
      if (g) g.classList.remove('open');
    });
  }
  navLabels.forEach(function (label) {
    label.addEventListener('click', function (e) {
      e.stopPropagation();
      var g = label.closest('.nav-group');
      if (!g) return;
      var willOpen = !g.classList.contains('open');
      closeAllGroups();
      if (willOpen) {
        g.classList.add('open');
        label.setAttribute('aria-expanded', 'true');
      }
    });
  });
  document.addEventListener('click', function (e) {
    if (e.target.closest('#nav-toggle')) return; /* 汉堡开合不触发外点关闭（否则清掉自动展开的当前组） */
    if (!e.target.closest('.nav-group')) closeAllGroups();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      var opened = document.querySelector('.nav-group.open');
      if (opened) {
        closeAllGroups();
        var l = opened.querySelector('.nav-label');
        if (l) l.focus();
      }
    }
  });

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
      plane.innerHTML = '<svg width="72" height="40" viewBox="0 0 72 40" fill="none" stroke="#17191d" stroke-width="1.6" stroke-linejoin="round"><path d="M2 22 L58 8 L40 26 L30 20 Z"/><path d="M30 20 L34 34 L40 26"/><path d="M44 12 L66 6" stroke="#C84032" stroke-dasharray="4 4"/></svg>';
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

  /* ---------- 实录实时检索 ---------- */
  var psInput = document.getElementById('ps-search');
  var psCount = document.getElementById('ps-count');
  var psItems = Array.prototype.slice.call(document.querySelectorAll('.ps-ledger .ps-row'));
  if (psInput && psCount) {
    var total = psItems.length;
    psInput.addEventListener('input', function () {
      var q = psInput.value.trim().toLowerCase();
      var visible = 0;
      psItems.forEach(function (item) {
        var hit = !q || item.textContent.toLowerCase().indexOf(q) !== -1;
        item.classList.toggle('tl-hidden', !hit);
        if (hit) visible++;
      });
      psCount.textContent = visible + ' / ' + total;
      if (reduceMotion) return;
    });
  }

  /* ---------- 检索清空按钮 ---------- */
  var psClear = document.getElementById('ps-clear');
  if (psClear && psInput) {
    psClear.addEventListener('click', function () {
      psInput.value = '';
      psInput.dispatchEvent(new Event('input', { bubbles: true }));
      psInput.focus();
    });
  }

  /* ---------- V7-R7 公司关系图交互（companies.html#network） ---------- */
  var netSvg = document.querySelector('.net-graph');
  var netDetail = document.getElementById('net-detail');
  if (netSvg && netDetail && window.COMPANIES_V7) {
    var NET = window.COMPANIES_V7;
    var netById = {};
    NET.companies.forEach(function (c) { netById[c.id] = c; });
    var netCurrent = null;

    function netT(s) { return (document.documentElement.lang === 'en') ? s.en : s.zh; }
    function netEsc(s) {
      var d = document.createElement('div');
      d.textContent = (s == null) ? '' : String(s);
      return d.innerHTML;
    }

    function netRender(cid) {
      var c = netById[cid];
      if (!c) return;
      var links = NET.links.filter(function (l) { return l.from === cid || l.to === cid; });
      var h = '<div class="net-d-head">'
        + '<span class="net-d-dot" style="background:var(' + c.colorVar + ')"></span>'
        + '<span class="net-d-name">' + netEsc(c.name) + '</span>'
        + '<span class="net-d-status">' + netEsc(netT(c.statusLabel)) + '</span>'
        + '<button type="button" class="net-d-close" data-net-close>' + (document.documentElement.lang === 'en' ? 'Close' : '关闭') + '</button>'
        + '</div>'
        + '<p class="net-d-blurb">' + netEsc(netT(c.blurb)) + '</p>'
        + '<p class="net-d-meta">' + netEsc(netT(c.sector)) + ' · ' + netEsc(netT(c.era)) + '</p>';
      if (c.href) {
        h += '<p class="net-d-file"><a href="' + netEsc(c.href) + '" data-en="Open the company file →">查看公司档案 →</a></p>';
      }
      if (c.id !== 'musk') {
        h += '<p class="net-d-file"><a href="capital-evolution.html#flow" data-en="See its capital flows →">查看它的资本流向 →</a></p>';
      }
      if (c.events.length) {
        h += '<p class="net-d-sec">' + (document.documentElement.lang === 'en' ? 'RELATED EVENTS' : '相关事件') + '</p><div class="net-d-links">';
        c.events.forEach(function (e) {
          h += '<a href="events.html#' + netEsc(e.id) + '">' + netEsc(e.date) + ' · ' + netEsc(netT(e.title)) + ' →</a>';
        });
        h += '</div>';
      }
      if (links.length) {
        h += '<p class="net-d-sec">' + (document.documentElement.lang === 'en' ? 'RELATIONSHIPS (' + links.length + ')' : '关系（' + links.length + '）') + '</p><div class="net-d-links">';
        links.forEach(function (l) {
          var other = netById[l.from === cid ? l.to : l.from];
          var arrow = (l.from === cid) ? '→ ' : '← ';
          var evTag = (l.evidence === 'editorial') ? ' · <em>' + netEsc(netT(l.evidenceLabel)) + '</em>' : '';
          h += '<span>' + arrow + '<b>' + netEsc(other.name) + '</b> · ' + netEsc(netT(l.label)) + evTag
            + ' · <a href="' + netEsc(l.source.href) + '">' + (document.documentElement.lang === 'en' ? 'source' : '来源') + '</a></span>';
        });
        h += '</div>';
      }
      netDetail.innerHTML = h;
      var closeBtn = netDetail.querySelector('[data-net-close]');
      if (closeBtn) closeBtn.addEventListener('click', netClose);
    }

    function netClose() {
      netCurrent = null;
      var en = document.documentElement.lang === 'en';
      netDetail.innerHTML = '<p class="net-detail-empty">' + (en
        ? 'Select a company in the chart — or browse the list below. No JS: the full list below is complete on its own.'
        : '在图上点选一家公司（支持 Tab + Enter）——或直接阅读下方清单；无脚本环境下列表即完整信息。')
        + '</p>';
      netSvg.querySelectorAll('.net-node.on').forEach(function (n) { n.classList.remove('on'); });
    }

    netSvg.querySelectorAll('.net-node').forEach(function (n) {
      var cid = n.getAttribute('data-net-node');
      function toggle() {
        if (netCurrent === cid) { netClose(); return; }
        netCurrent = cid;
        netSvg.querySelectorAll('.net-node.on').forEach(function (m) { m.classList.remove('on'); });
        n.classList.add('on');
        netRender(cid);
      }
      n.addEventListener('click', toggle);
      n.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); }
        if (e.key === 'Escape') { netClose(); }
      });
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && netCurrent) {
        var was = netSvg.querySelector('.net-node.on');
        netClose();
        if (was) was.focus();
      }
    });
    // 语言切换后重渲染已打开的详情（数据双语，直接换字段）
    new MutationObserver(function () {
      if (netCurrent) netRender(netCurrent);
    }).observe(document.documentElement, { attributes: true, attributeFilter: ['lang'] });
  }

  /* ---------- V7-R10 资本流向交互（capital-evolution.html#flow） ---------- */
  var capSvg = document.querySelector('.cap-graph');
  var capDetail = document.getElementById('cap-detail');
  if (capSvg && capDetail && window.CAPITAL_V7) {
    var CAPD = window.CAPITAL_V7;
    var capFlowById = {};
    var capNodeById = {};
    CAPD.flows.forEach(function (f) { capFlowById[f.id] = f; });
    CAPD.srcNodes.concat(CAPD.coNodes).forEach(function (n) { capNodeById[n.id] = n; });
    var capCurrent = null;   // { type: 'flow' | 'node', id }
    var capTrigger = null;   // Esc 关闭后焦点归还目标
    var capFilter = 'all';

    function capT(s) { return (document.documentElement.lang === 'en') ? s.en : s.zh; }
    function capEsc(s) {
      var d = document.createElement('div');
      d.textContent = (s == null) ? '' : String(s);
      return d.innerHTML;
    }
    function capNodeLabel(nid) {
      var n = capNodeById[nid];
      return n ? capT(n.label) : nid;
    }
    function capFromLabel(f) {
      return f.fromNote ? capT(f.fromNote) : capNodeLabel(f.from);
    }
    function capGroupOf(fid) {
      var f = capFlowById[fid];
      for (var i = 0; i < CAPD.groups.length; i++) {
        if (CAPD.groups[i].id === f.group) return CAPD.groups[i];
      }
      return null;
    }

    function capRenderFlow(fid) {
      var f = capFlowById[fid];
      if (!f) return;
      var en = document.documentElement.lang === 'en';
      var g = capGroupOf(fid);
      var h = '<div class="cap-d-head">'
        + '<span class="cap-d-dot" style="background:' + g.color + '"></span>'
        + '<span class="cap-d-name">' + capEsc(capFromLabel(f)) + ' → ' + capEsc(capNodeLabel(f.to)) + '</span>'
        + '<span class="cap-li-badge">' + capEsc(capT(f.kindLabel)) + '</span>'
        + '<span class="cap-li-badge cap-li-badge--p">' + capEsc(capT(f.precisionLabel)) + '</span>'
        + '<button type="button" class="cap-d-close" data-cap-close>' + (en ? 'Close' : '关闭') + '</button></div>'
        + '<p class="cap-d-amt"><b>' + capEsc(capT(f.amount)) + '</b> · ' + capEsc(f.date) + ' · ' + (en ? 'currency ' : '币种 ') + capEsc(f.currency) + '</p>'
        + '<p class="cap-d-caliber"><b>' + (en ? 'CALIBER' : '口径') + '</b>' + capEsc(capT(f.caliber)) + '</p>';
      if (f.sources && f.sources.length) {
        h += '<p class="cap-d-src">' + (en ? 'Sources: ' : '来源：');
        f.sources.forEach(function (s) {
          h += '<a href="' + capEsc(s.href) + '">' + capEsc(capT(s.label)) + '</a>';
        });
        h += '</p>';
      }
      h += '<p class="cap-d-sec">' + (en ? 'GO DEEPER' : '继续深入') + '</p><div class="cap-d-links">';
      if (f.event) h += '<a href="events.html#' + capEsc(f.event) + '">' + (en ? 'Open the event file →' : '打开事件档案 →') + '</a>';
      if (f.file) h += '<a href="company-files.html#' + capEsc(f.file) + '">' + (en ? 'Open the company file →' : '查看公司档案 →') + '</a>';
      h += '</div>';
      capDetail.innerHTML = h;
      var cb = capDetail.querySelector('[data-cap-close]');
      if (cb) cb.addEventListener('click', capClose);
    }

    function capRenderNode(nid) {
      var n = capNodeById[nid];
      if (!n) return;
      var en = document.documentElement.lang === 'en';
      var color = n.colorVar ? ('var(' + n.colorVar + ')') : '#C84032';
      var mine = CAPD.flows.filter(function (f) { return f.from === nid || f.to === nid; });
      var h = '<div class="cap-d-head">'
        + '<span class="cap-d-dot" style="background:' + color + '"></span>'
        + '<span class="cap-d-name">' + capEsc(capT(n.label)) + '</span>'
        + '<button type="button" class="cap-d-close" data-cap-close>' + (en ? 'Close' : '关闭') + '</button></div>';
      if (n.desc) h += '<p class="cap-d-caliber">' + capEsc(capT(n.desc)) + '</p>';
      if (n.href) {
        h += '<p class="cap-d-sec">' + (en ? 'COMPANY FILE' : '公司档案') + '</p>'
          + '<div class="cap-d-links"><a href="' + capEsc(n.href) + '">'
          + (en ? 'Open the company file →' : '查看公司档案 →') + '</a></div>';
      }
      h += '<p class="cap-d-sec">' + (en ? 'FLOWS (' + mine.length + ')' : '相关流向（' + mine.length + '）') + '</p><div class="cap-d-links">';
      mine.forEach(function (f) {
        var dir = (f.to === nid)
          ? '← ' + capEsc(capFromLabel(f))
          : '→ ' + capEsc(capNodeLabel(f.to));
        h += '<button type="button" class="cap-d-jump" data-cap-jump="' + f.id + '">'
          + capEsc(f.date) + ' · ' + capEsc(capT(f.amount)) + ' · ' + dir + '</button>';
      });
      h += '</div>';
      capDetail.innerHTML = h;
      var cb = capDetail.querySelector('[data-cap-close]');
      if (cb) cb.addEventListener('click', capClose);
      capDetail.querySelectorAll('[data-cap-jump]').forEach(function (b) {
        b.addEventListener('click', function () {
          // 触发元素 = 该流向自己的图上组：Esc 关闭后焦点回到线上
          var target = capSvg.querySelector('[data-cap-flow="' + b.getAttribute('data-cap-jump') + '"]');
          capSelect('flow', b.getAttribute('data-cap-jump'), target);
        });
      });
    }

    function capMark() {
      capSvg.querySelectorAll('.cap-flow.on, .cap-flow.hl, .cap-node.on').forEach(function (el) {
        el.classList.remove('on', 'hl');
      });
      if (!capCurrent) return;
      if (capCurrent.type === 'flow') {
        var el = capSvg.querySelector('[data-cap-flow="' + capCurrent.id + '"]');
        if (el) el.classList.add('on');
      } else {
        var nel = capSvg.querySelector('[data-cap-node="' + capCurrent.id + '"]');
        if (nel) nel.classList.add('on');
        CAPD.flows.forEach(function (f) {
          if (f.from === capCurrent.id || f.to === capCurrent.id) {
            var fe = capSvg.querySelector('[data-cap-flow="' + f.id + '"]');
            if (fe) fe.classList.add('hl');
          }
        });
      }
    }

    function capSelect(type, id, trigger) {
      if (capCurrent && capCurrent.type === type && capCurrent.id === id) { capClose(); return; }
      capCurrent = { type: type, id: id };
      if (trigger) capTrigger = trigger;
      if (type === 'flow') capRenderFlow(id); else capRenderNode(id);
      capMark();
    }

    function capClose() {
      var prevOn = capSvg.querySelector('.cap-flow.on, .cap-node.on');
      capCurrent = null;
      var en = document.documentElement.lang === 'en';
      capDetail.innerHTML = '<p class="cap-detail-empty">' + (en
        ? 'Select a flow line or a node in the chart — or read the list below. No JS: the full list below is complete on its own.'
        : '在图上点选一条流向线或一个节点（支持 Tab + Enter）——或直接阅读下方清单；无脚本环境下列表即完整信息。')
        + '</p>';
      capMark();
      // 焦点归还：优先触发元素；jump 路径触发元素已随面板重渲染消失，退回选中的流向/节点
      if (capTrigger && capTrigger.isConnected) capTrigger.focus();
      else if (prevOn && prevOn.isConnected) prevOn.focus();
      capTrigger = null;
    }

    capSvg.querySelectorAll('.cap-flow').forEach(function (el) {
      var fid = el.getAttribute('data-cap-flow');
      el.addEventListener('click', function () { capSelect('flow', fid, el); });
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); capSelect('flow', fid, el); }
        if (e.key === 'Escape') { capClose(); }
      });
    });
    capSvg.querySelectorAll('.cap-node').forEach(function (el) {
      var nid = el.getAttribute('data-cap-node');
      el.addEventListener('click', function () { capSelect('node', nid, el); });
      el.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); capSelect('node', nid, el); }
        if (e.key === 'Escape') { capClose(); }
      });
    });
    // 清单行点击 = 打开同一详情（行内链接照常跳转）
    document.querySelectorAll('.cap-li[data-cap-flow]').forEach(function (li) {
      li.addEventListener('click', function (e) {
        if (e.target.closest('a')) return;
        capSelect('flow', li.getAttribute('data-cap-flow'), li);
        if (capDetail.offsetParent) capDetail.scrollIntoView({ block: 'nearest' });
      });
    });
    // 分组筛选（芯片 / 清除 / 状态行 aria-live）
    var capChips = Array.prototype.slice.call(document.querySelectorAll('.cap-chip[data-cap-filter]'));
    var capClearBtn = document.querySelector('[data-cap-clear]');
    var capStatus = document.getElementById('cap-status');
    function capApplyFilter(gid) {
      capFilter = gid;
      capChips.forEach(function (c) {
        c.setAttribute('aria-pressed', c.getAttribute('data-cap-filter') === gid ? 'true' : 'false');
      });
      var visible = 0;
      var glabel = null;
      if (gid !== 'all') {
        var g = capGroupOf(CAPD.flows.filter(function (f) { return f.group === gid; })[0].id);
        glabel = g.label;
      }
      CAPD.flows.forEach(function (f) {
        var show = (gid === 'all') || (f.group === gid);
        if (show) visible++;
        var el = capSvg.querySelector('[data-cap-flow="' + f.id + '"]');
        if (el) el.classList.toggle('dim', !show);
        var row = document.querySelector('.cap-li[data-cap-flow="' + f.id + '"]');
        if (row) row.classList.toggle('cap-hidden', !show);
      });
      capSvg.querySelectorAll('.cap-node').forEach(function (nel) {
        var nid = nel.getAttribute('data-cap-node');
        var any = CAPD.flows.some(function (f) {
          return (f.from === nid || f.to === nid) && ((gid === 'all') || f.group === gid);
        });
        nel.classList.toggle('dim', !any);
      });
      document.querySelectorAll('.cap-group').forEach(function (gel) {
        gel.classList.toggle('cap-hidden', !(gid === 'all' || gel.id === 'cap-g-' + gid));
      });
      if (capStatus) {
        var en = document.documentElement.lang === 'en';
        capStatus.textContent = (gid === 'all')
          ? (en ? 'Showing all ' + visible + ' flows · 1999–2026 · currency USD unless noted. Select a line or a node for caliber and sources.'
                : '显示全部 ' + visible + ' 笔流向 · 1999–2026 · 币种 USD（除注明外）。点击线条或节点查看口径与出处。')
          : (en ? 'Showing ' + visible + ' “' + capT(glabel) + '” flows · select a line for caliber and sources.'
                : '显示「' + capT(glabel) + '」' + visible + ' 笔流向 · 点击线条查看口径与出处。');
      }
      if (capCurrent && capCurrent.type === 'flow') {
        var cf = capFlowById[capCurrent.id];
        if (cf && capFilter !== 'all' && cf.group !== capFilter) capClose();
      }
    }
    capChips.forEach(function (c) {
      c.addEventListener('click', function () { capApplyFilter(c.getAttribute('data-cap-filter')); });
    });
    if (capClearBtn) capClearBtn.addEventListener('click', function () { capApplyFilter('all'); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && capCurrent) capClose();
    });
    // 语言切换后重渲染已打开的详情
    new MutationObserver(function () {
      if (!capCurrent) return;
      if (capCurrent.type === 'flow') capRenderFlow(capCurrent.id);
      else capRenderNode(capCurrent.id);
    }).observe(document.documentElement, { attributes: true, attributeFilter: ['lang'] });
  }
})();
