document.addEventListener("DOMContentLoaded", function () {
  var searchInputs = document.querySelectorAll(
    ".md-search__input, #mkdocs-search-query, input[name='q']"
  );
  var searchForms = document.querySelectorAll("form[role='search'], #rtd-search-form");
  var syncTimer = null;
  var enhancedInputs = new WeakSet();
  var composingInputs = new WeakSet();

  function getSearchQuery(query) {
    var chineseChars = query.match(/[\u4e00-\u9fff]/g);

    // Read the Docs Addons currently ignores queries shorter than 3 chars.
    // A trailing space lets two-character Chinese terms, such as "算子",
    // reach the server-side search API without changing the visible query.
    if (chineseChars && query.length < 3) {
      return query + " ";
    }

    return query;
  }

  function setInputValue(input, query) {
    var valueSetter = Object.getOwnPropertyDescriptor(
      HTMLInputElement.prototype,
      "value"
    ).set;

    valueSetter.call(input, query);
  }

  function enhanceReadTheDocsInput(input) {
    if (enhancedInputs.has(input)) {
      return;
    }

    enhancedInputs.add(input);
    input.addEventListener("compositionstart", function () {
      composingInputs.add(input);
    });
    input.addEventListener("compositionend", function () {
      composingInputs.delete(input);
    });
    input.addEventListener(
      "input",
      function () {
        if (composingInputs.has(input)) {
          return;
        }

        var query = input.value.trim();
        var rtdQuery = getSearchQuery(query);

        if (query && rtdQuery !== query) {
          setInputValue(input, rtdQuery);
          setTimeout(function () {
            setInputValue(input, query);
          }, 0);
        }
      },
      true
    );
  }

  function getReadTheDocsSearchInput() {
    // The official Addons search box is rendered inside a web component shadow
    // root. There is no public API for pre-filling it, so this bridge locates
    // the component input and dispatches its normal input event.
    var elements = document.querySelectorAll("*");

    for (var index = 0; index < elements.length; index += 1) {
      var root = elements[index].shadowRoot;
      var input = root && root.querySelector("input[type='search']");

      if (input && input.placeholder === "Search docs") {
        enhanceReadTheDocsInput(input);
        return input;
      }
    }

    return null;
  }

  function openRtdSearchWithQuery(query) {
    var input = getReadTheDocsSearchInput();

    if (!input) {
      return false;
    }

    input.focus();

    if (query) {
      var rtdQuery = getSearchQuery(query);

      setInputValue(input, rtdQuery);
      input.dispatchEvent(
        new InputEvent("input", {
          bubbles: true,
          composed: true,
          data: rtdQuery,
          inputType: "insertText",
        })
      );

      if (rtdQuery !== query) {
        setTimeout(function () {
          setInputValue(input, query);
        }, 0);
      }
    }

    return true;
  }

  function openReadTheDocsSearch(query) {
    document.dispatchEvent(new CustomEvent("readthedocs-search-show"));

    clearTimeout(syncTimer);
    syncTimer = setTimeout(function () {
      if (!openRtdSearchWithQuery(query)) {
        setTimeout(function () {
          openRtdSearchWithQuery(query);
        }, 300);
      }
    }, 50);
  }

  searchInputs.forEach(function (searchInput) {
    searchInput.addEventListener("focus", function () {
      openReadTheDocsSearch(searchInput.value.trim());
    });

    searchInput.addEventListener("click", function () {
      openReadTheDocsSearch(searchInput.value.trim());
    });
  });

  searchForms.forEach(function (searchForm) {
    searchForm.addEventListener("submit", function (event) {
      event.preventDefault();

      var input = searchForm.querySelector("input[name='q'], input[type='search']");
      openReadTheDocsSearch(input ? input.value.trim() : "");
    });
  });
});
