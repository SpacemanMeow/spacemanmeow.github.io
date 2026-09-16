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
})();
