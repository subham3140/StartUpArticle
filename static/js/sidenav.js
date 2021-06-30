$('.search_btn_app').on("click", () => {
    let sidenav = $('.side_nav_bar')
    sidenav[0].hidden = false;
    if (sidenav.hasClass("testclose")) {
        sidenav.removeClass("testclose")
    }
    setTimeout(function() {
        $('.main-content')[0].style.opacity = "0.3";
    }, 500);
})

$('.closed').on("click", () => {
    let sidenav = $('.side_nav_bar')
    sidenav[0].classList.add("testclose");
    $('.closed')[0].classList.add("rotateitclose")
    setTimeout(function() {
        sidenav[0].hidden = true
        $('.main-content')[0].style.opacity = "1";
    }, 900);
})