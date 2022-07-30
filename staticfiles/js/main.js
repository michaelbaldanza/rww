// hamburger
const hamburger = document.querySelector('.ham-container');
const bars = document.getElementById('ham');
const navMenu = document.querySelector('.nav-menu');
const main = document.getElementById('main');
let on = false;

hamburger.addEventListener('click', hamMenu);

bars.addEventListener('mouseenter', e => {
  if (!on) {
    bars.style.backgroundColor = 'rgba(115, 115, 115, 0.8)';
  } else {
    bars.style.backgroundColor = 'rgba(250,177,98,.7)';
  }
})

bars.addEventListener('mouseleave', e => {
  if (!on) {
    bars.style.backgroundColor = 'rgba(250,177,98,.7)';
  } else {
    bars.style.backgroundColor = 'rgba(115, 115, 115, 0.8)';
  }
})

function hamMenu() {
  if (!on) {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
    bars.style.backgroundColor = 'rgba(115, 115, 115, 0.8)';
    main.style.display = 'none';
    on = true;
  } else {
    hamburger.classList.toggle('active');
    navMenu.classList.toggle('active');
    bars.style.backgroundColor = 'rgba(250,177,98,.7)';
    main.style.display = 'block';
    on = false;
  }
  
}


// slideshow
// let idx = 0;

// function changeSlide() {
//   let slides = document.getElementsByClassName('slide');
//   if (idx === slides.length - 1) {
//     idx = 0;
//   } else {
//     idx ++;
//   }
//   for (i = 0; i < slides.length; i++) {
//     slides[i].style.display = 'none';
//   }
//   slides[idx].style.display = 'block';
// }
// let slideChange = setInterval(changeSlide, 5000);