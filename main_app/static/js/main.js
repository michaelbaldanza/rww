let idx = 0;

function changeSlide() {
  let slides = document.getElementsByClassName('slide');
  if (idx === slides.length - 1) {
    idx = 0;
  } else {
    idx++;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';
  }
  console.log(idx);
  console.log(slides[idx]);
  slides[idx].style.display = 'block';
}
let slideChange = setInterval(changeSlide, 5000);