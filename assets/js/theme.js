/* 深浅模式切换。
 * - data-theme 由 head 内联脚本在首屏前设置，避免闪烁。
 * - 点击按钮在 light / dark 间切换，并写入 localStorage。
 * - 未手动选择时，跟随系统的 prefers-color-scheme 变化。 */
(function () {
  var KEY = "theme-pref";
  var root = document.documentElement;

  function systemDark() {
    return !!(window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches);
  }

  function applyToggle() {
    var cur = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", cur);
    try { localStorage.setItem(KEY, cur); } catch (e) {}
  }

  function init() {
    var btn = document.querySelector("[data-theme-toggle]");
    if (!btn) return;
    btn.addEventListener("click", applyToggle);

    // 用户未手动选择时，系统偏好变化即同步
    if (window.matchMedia) {
      window.matchMedia("(prefers-color-scheme: dark)")
        .addEventListener("change", function () {
          var pref;
          try { pref = localStorage.getItem(KEY); } catch (e) {}
          if (!pref) root.setAttribute("data-theme", systemDark() ? "dark" : "light");
        });
    }
  }

  if (document.readyState !== "loading") init();
  else document.addEventListener("DOMContentLoaded", init);
})();
