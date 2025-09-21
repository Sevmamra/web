document.addEventListener("DOMContentLoaded", () => {
  const title = document.querySelector(".title");
  let text = title.textContent;
  title.textContent = "";
  
  let i = 0;
  function typeWriter() {
    if (i < text.length) {
      title.textContent += text.charAt(i);
      i++;
      setTimeout(typeWriter, 80);
    }
  }
  typeWriter();
});
