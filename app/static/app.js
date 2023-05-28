document.addEventListener("DOMContentLoaded", () => {

  document.querySelectorAll("a.color").forEach(button => {
    button.addEventListener("click", event => {
      console.log("button");
      console.log(button.dataset.color);
      fetch("/color/" + button.dataset.color, {method: "POST"});
    });
  });

});

