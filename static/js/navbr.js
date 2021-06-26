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


$('.search_btn').on("click", () => {
    let tabs = $('.tabs')
    let search_bar = $('.search_bar')
    let search_btn = $('.search_btn')[0]
    if (tabs[0].hidden == true) {
        tabs[0].hidden = false
        search_bar[0].hidden = true
        search_btn.innerHTML =
            `
        <span class="material-icons">
            zoom_in
        </span>
        `
    } else {
        tabs[0].hidden = true
        search_bar[0].hidden = false
        search_btn.innerHTML =
            `
        <span class="material-icons">
            highlight_off
        </span>
        `
    }
})

$(window).resize(function() {
    adjustNav()
})
adjustNav()