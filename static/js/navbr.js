var tabs = $('.tabs');
var selector = $('.tabs').find('a').length;
var activeItem = tabs.find('.active');
var activeWidth = activeItem.innerWidth();
var default_pos = tabs.find('.default_pos')

function adjustNav() {
    $(".selector").css({
        "left": $(default_pos).position().left - 6 + "px",
        "width": default_pos.innerWidth() + "px"
    });
}
$(".tabs").on("click", "a", function(e) {
    e.preventDefault();
    $('.tabs a').removeClass("active");
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