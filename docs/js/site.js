(function () {
  "use strict";

  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = !nav.classList.contains("is-open");
      nav.classList.toggle("is-open", open);
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    nav.addEventListener("click", function (event) {
      if (event.target.closest("a") && nav.classList.contains("is-open")) {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  document.querySelectorAll("[data-copy]").forEach(function (button) {
    button.addEventListener("click", function () {
      var targetId = button.getAttribute("data-copy");
      var source = targetId ? document.getElementById(targetId) : null;
      if (!source) {
        return;
      }
      var text = source.textContent || "";
      var done = function () {
        var original = button.getAttribute("data-label") || "复制";
        button.textContent = "已复制";
        window.setTimeout(function () {
          button.textContent = original;
        }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done).catch(function () {
          fallbackCopy(text, done);
        });
      } else {
        fallbackCopy(text, done);
      }
    });
  });

  function fallbackCopy(text, done) {
    var area = document.createElement("textarea");
    area.value = text;
    area.setAttribute("readonly", "");
    area.style.position = "absolute";
    area.style.left = "-9999px";
    document.body.appendChild(area);
    area.select();
    try {
      document.execCommand("copy");
      done();
    } finally {
      document.body.removeChild(area);
    }
  }
})();
