$('.tabs-interview').find("a[name=article]").removeClass("default_pos")
$('.tabs-interview').find("a[name=interview]").addClass("default_pos")
$('.content-saperator')[0].style.display = "none";
var tabs = $('.tabs-interview');
var selector = $('.tabs-interview').find('a').length;
var activeItem = tabs.find('.active');
var activeWidth = activeItem.innerWidth();
var default_pos = tabs.find('.default_pos')

function adjustNav() {
    $(".selector").css({
        "left": $(default_pos).position().left - 1 + "px",
        "width": default_pos.innerWidth() + "px"
    });
}
$(".tabs-interview").on("click", "a", function(e) {
    $('.tabs-interview a').removeClass("active");
    $(this).addClass('active');
    var activeWidth = $(this).innerWidth();
    var itemPos = $(this).position();
    $(".selector").css({
        "left": itemPos.left + "px",
        "width": activeWidth + "px"
    });
});

$(window).resize(function() {
    adjustNav()
})
adjustNav()