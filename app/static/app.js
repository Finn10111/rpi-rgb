document.addEventListener("DOMContentLoaded", () => {

  document.querySelectorAll("a.color").forEach(button => {
    button.addEventListener("click", () => {
      fetch("/color/" + button.dataset.color, {method: "POST"});
    });
  });

});

