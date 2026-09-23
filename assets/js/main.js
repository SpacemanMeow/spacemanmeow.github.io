/* 站点交互脚本：应用截图横向滚动、移动端菜单 */
(function () {
  'use strict';

  /* ---------- 移动端导航菜单 ---------- */
  document.querySelectorAll('[data-nav-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var nav = document.querySelector('[data-nav]');
      if (nav) {
        nav.classList.toggle('is-open');
        btn.classList.toggle('is-open');
      }
    });
  });

  /* ---------- 应用截图横向滚动 ---------- */
  document.querySelectorAll('[data-shots]').forEach(function (root) {
    var track = root.querySelector('.shots__track');
    var prev = root.querySelector('.shots__nav--prev');
    var next = root.querySelector('.shots__nav--next');
    if (!track) return;

    function step() {
      var item = track.querySelector('.shot');
      var size = item ? item.offsetWidth + 16 : 200;
      var count = Math.max(1, Math.floor(track.clientWidth / size));
      return size * count;
    }

    function sync() {
      var max = track.scrollWidth - track.clientWidth;
      if (prev) prev.hidden = track.scrollLeft <= 4;
      if (next) next.hidden = track.scrollLeft >= max - 4;
    }

    if (prev) {
      prev.addEventListener('click', function () {
        track.scrollBy({ left: -step(), behavior: 'smooth' });
      });
    }
    if (next) {
      next.addEventListener('click', function () {
        track.scrollBy({ left: step(), behavior: 'smooth' });
      });
    }

    track.addEventListener('scroll', sync, { passive: true });
    window.addEventListener('resize', sync);
    sync();
  });

  /* ---------- 截图画廊：点击预览 Lightbox ---------- */
  var shotItems = Array.prototype.slice.call(document.querySelectorAll('[data-shots-item]'));
  if (shotItems.length) {
    // 按所在画廊分组（支持同一页面存在多个画廊）
    var groups = [];
    shotItems.forEach(function (el) {
      var root = el.closest('[data-shots]') || document;
      var g = null;
      for (var i = 0; i < groups.length; i++) {
        if (groups[i].root === root) { g = groups[i]; break; }
      }
      if (!g) { g = { root: root, list: [] }; groups.push(g); }
      g.list.push(el);
    });

    var lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-hidden', 'true');
    lb.innerHTML =
      '<button class="lightbox__close" type="button" aria-label="Close preview">&times;</button>' +
      '<button class="lightbox__nav lightbox__nav--prev" type="button" aria-label="Previous">&lsaquo;</button>' +
      '<figure class="lightbox__stage">' +
        '<img class="lightbox__img" alt="" />' +
        '<figcaption class="lightbox__caption" hidden></figcaption>' +
      '</figure>' +
      '<button class="lightbox__nav lightbox__nav--next" type="button" aria-label="Next">&rsaquo;</button>';
    document.body.appendChild(lb);

    var lbImg = lb.querySelector('.lightbox__img');
    var lbCap = lb.querySelector('.lightbox__caption');
    var lbPrev = lb.querySelector('.lightbox__nav--prev');
    var lbNext = lb.querySelector('.lightbox__nav--next');
    var lbClose = lb.querySelector('.lightbox__close');
    var cur = null;

    function render() {
      var el = cur.list[cur.index];
      var inner = el.querySelector('img');
      lbImg.src = el.getAttribute('data-full') || (inner ? inner.src : '');
      lbImg.alt = inner ? inner.alt : '';
      var cap = el.getAttribute('data-caption') || '';
      lbCap.textContent = cap;
      lbCap.hidden = !cap;
      lbPrev.hidden = cur.index === 0;
      lbNext.hidden = cur.index === cur.list.length - 1;
    }
    function openLb(el) {
      var grp = null;
      for (var i = 0; i < groups.length; i++) {
        if (groups[i].list.indexOf(el) !== -1) { grp = groups[i]; break; }
      }
      if (!grp) return;
      cur = { list: grp.list, index: grp.list.indexOf(el) };
      render();
      lb.classList.add('is-open');
      lb.setAttribute('aria-hidden', 'false');
      document.body.classList.add('no-scroll');
      lbClose.focus();
    }
    function closeLb() {
      lb.classList.remove('is-open');
      lb.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('no-scroll');
    }
    function moveLb(d) {
      var ni = cur.index + d;
      if (ni < 0 || ni >= cur.list.length) return;
      cur.index = ni;
      render();
    }

    shotItems.forEach(function (el) {
      el.addEventListener('click', function () { openLb(el); });
    });
    lbClose.addEventListener('click', closeLb);
    lbPrev.addEventListener('click', function (e) { e.stopPropagation(); moveLb(-1); });
    lbNext.addEventListener('click', function (e) { e.stopPropagation(); moveLb(1); });
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    document.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') closeLb();
      else if (e.key === 'ArrowLeft') moveLb(-1);
      else if (e.key === 'ArrowRight') moveLb(1);
    });
  }
})();
