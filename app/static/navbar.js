const hamburger = document.querySelector('.navbar-toggler');
const navbar = document.querySelector('.navbar-collapse');

hamburger.addEventListener('click', () => {
    navbar.classList.toggle('show');
});