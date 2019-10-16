console.log("Hello, world!");

var hamburger = document.querySelector(".hamburger");
var navbar = document.querySelector(".navbar");
var navbarNav = document.querySelector(".navbar-nav");
var navbarCollapse = document.querySelector(".navbar-collapse");

//handles the hamburger button click, animation css classes for the button and menu,
//and the navbar background color css classes
hamburger.addEventListener("click", function () {
    hamburger.classList.toggle("is-active");
    navbar.classList.toggle("colorToggle", hamburger.classList.contains("is-active"));
    navbarNav.classList.replace("pulse", "flipInX");
    hamburger.classList.toggle("rubberBand");
    hamburger.classList.toggle("pulse");
    doubleClickDelay();
});

//disables the hamburger button one millasecond after it is clicked
//and remains disabled for half a second preventing double clicking by the user
function doubleClickDelay() {
    setTimeout(() => {
        $(".hamburger").attr("disabled", "disabled");
        setTimeout(() => {
            $(".hamburger").removeAttr("disabled");
        }, 500);
    }, 1);
}

//a fallback for when the screen is resized
//if the menu is expanded on a small screen,
//the menu will collapse and reset when the screen is resized
$(window).resize(function () {
    if ($(window).width() > 767) {
        if (navbar.classList.contains("colorToggle")) {
            navbar.classList.toggle("colorToggle");
            hamburger.classList.toggle("is-active");
            hamburger.classList.replace("pulse", "rubberBand");
            navbarCollapse.classList.toggle("show");
        }
        navbarNav.classList.replace("flipInX", "pulse");
    } else if ($(window).width() < 768) {
        navbarNav.classList.replace("pulse", "flipInX");
    }
});

//detects if the page is being scrolled and
//closes the nav menu if it is open
$(document).scroll(function () {
    if (navbarCollapse.classList.contains("show")) {
        navbarCollapse.classList.toggle("show");
        hamburger.classList.toggle("is-active");
        navbar.classList.toggle("colorToggle", hamburger.classList.contains("is-active"));
    }
});
