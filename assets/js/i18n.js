/* Language switcher behaviour — language-agnostic.
 *
 * 语言列表完全由 _data/languages.yml 驱动：nav.html 把该列表注入到
 * window.SITE_LANGS，本文件只读取它。因此新增一门语言只需编辑
 * languages.yml（并在 _config_<code>.yml / _pages/<code>/ 等放好源文件），
 * 下拉菜单、路径切换、自动跳转都会自动适配，无需改动本文件。
 *
 * - 当前语言由 URL 的 /<lang>/ 前缀判定。
 * - 首次访问且无手动偏好时，按浏览器语言自动跳转到对应语言（爬虫不跳转，保 SEO 干净）。
 * - 自定义下拉：按钮 + 绝对定位菜单，固定展开在按钮正下方。
 */
(function () {
  var DEFAULT = "en";

  // 语言列表（含默认语言），由页面注入；缺失时回退到旧的 en/zh 默认值。
  var LANGS =
    window.SITE_LANGS && window.SITE_LANGS.length
      ? window.SITE_LANGS.slice()
      : [DEFAULT, "zh"];
  if (LANGS.indexOf(DEFAULT) < 0) LANGS.unshift(DEFAULT);

  function curLang(pathname) {
    for (var i = 0; i < LANGS.length; i++) {
      var l = LANGS[i];
      if (l !== DEFAULT && pathname.indexOf("/" + l + "/") === 0) return l;
    }
    return DEFAULT;
  }

  // 去掉 URL 里可能存在的 /<lang>/ 前缀，回到“无语言前缀”的基准路径。
  function stripLang(path) {
    for (var i = 0; i < LANGS.length; i++) {
      var l = LANGS[i];
      if (l !== DEFAULT && path.indexOf("/" + l + "/") === 0) {
        return path.slice(("/" + l).length);
      }
    }
    return path;
  }

  function swap(path, lang) {
    var p = stripLang(path);
    if (lang !== DEFAULT) p = "/" + lang + p;
    return p;
  }

  function isLocal() {
    return location.hostname === "localhost" || location.hostname === "127.0.0.1";
  }

  function auto() {
    if (isLocal()) return; // 本地双预览分属不同 origin（localStorage 隔离），自动跳转会乒乓，仅生产环境启用
    if (localStorage.getItem("lang-pref")) return;
    var nav = (navigator.language || DEFAULT).toLowerCase();
    var target = DEFAULT;
    for (var i = 0; i < LANGS.length; i++) {
      var l = LANGS[i];
      if (l !== DEFAULT && nav.indexOf(l) === 0) {
        target = l;
        break;
      }
    }
    if (target !== DEFAULT && curLang(location.pathname) === DEFAULT) {
      location.href =
        swap(location.pathname, target) + location.search + location.hash;
    }
  }

  function init() {
    var root = document.querySelector("[data-lang-switch]");
    if (!root) return;
    var btn = root.querySelector(".lang-switch__btn");
    var menu = root.querySelector(".lang-switch__menu");
    if (!btn || !menu) return;
    var cur = curLang(location.pathname);

    // 标记当前语言（按钮文字由模板按 site.lang 服务端渲染，无需处理）
    Array.prototype.forEach.call(
      menu.querySelectorAll("[data-lang]"),
      function (item) {
        item.setAttribute(
          "aria-selected",
          item.getAttribute("data-lang") === cur ? "true" : "false"
        );
      }
    );

    function setOpen(open) {
      root.classList.toggle("is-open", open);
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    }

    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      setOpen(!root.classList.contains("is-open"));
    });

    menu.addEventListener("click", function (e) {
      var item = e.target.closest("[data-lang]");
      if (!item) return;
      var lang = item.getAttribute("data-lang");
      localStorage.setItem("lang-pref", lang);
      location.href =
        swap(location.pathname, lang) +
        location.search +
        location.hash;
    });

    // 点击外部或按 Esc 关闭
    document.addEventListener("click", function (e) {
      if (!root.contains(e.target)) setOpen(false);
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") setOpen(false);
    });

    auto();
  }

  if (document.readyState !== "loading") init();
  else document.addEventListener("DOMContentLoaded", init);
})();
