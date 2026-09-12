/* ============================================================
   马斯克商业志 MUSK, INC. — 交互脚本
   模块：版本号 / 双语切换 / 入场动画 / 导航高亮
   约定：任何含 data-en 的元素都是叶子节点，中文为内容、英文为属性；
        切换逻辑只在这里，页面新增文案无需额外代码。
   ============================================================ */
'use strict';

(function () {
  var SITE_VERSION = '0.7.0';

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
            a.classList.toggle('active', a.getAttribute('href') === '#' + entry.target.id);
          });
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    watchedSections.forEach(function (sec) { spy.observe(sec); });
  }
})();
