document.addEventListener("DOMContentLoaded", function () {
  var searchInputs = document.querySelectorAll(
    ".md-search__input, #mkdocs-search-query, input[name='q']"
  );

  searchInputs.forEach(function (searchInput) {
    searchInput.addEventListener("focus", function () {
      document.dispatchEvent(new CustomEvent("readthedocs-search-show"));
    });
  });
});
