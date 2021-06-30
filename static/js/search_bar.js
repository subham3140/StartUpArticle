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


$(".search_bar").on("keyup", () => {
    let search_bar = $(".search_bar").find("input")[0].value

    $.ajax({
        url: "/searcharticles",
        method: "GET",
        data: { "searched": search_bar },
        success: function(response) {
            if (response.result.length != 0) {
                $('.recentarticles')[0].style.display = "";
                let result = response.result
                $('.recentcontent')[0].innerHTML = ""
                for (i = 0; i < result.length; i++) {
                    if (i == 0) {
                        var profile = result[0].fields.profile
                        var title = result[0].fields.title
                        var id = result[i].pk

                        $('.toparticle')[0].innerHTML =
                            `
                        <img src=" media/` + profile + `" alt="">
                        <h2> <a href="article/` + id + `">` + title + ` </a> </h2>
                        `
                    } else {

                        var profile = result[i].fields.profile
                        var title = result[i].fields.title

                        var id = result[i].pk
                        $('.recentcontent')[0].innerHTML +=
                            `
                        <div class="eachrecentart">
                            <div class="eachartinfo">
                                <div class="im">
                                    <img src="media/` + profile + `" alt="">
                                </div>
                                <div class="ia">
                                    <div class="profile">
                                       <a href="article/` + id + `"><button class="articlesocial"> <span>PROFILE</span> </button> </a>
                                    </div>
                                    <div class="preinfo">
                                        <a class="nav-item nav-link" href="#"><i class="fab fa-facebook-square"></i></a>
                                        <a class="nav-item nav-link" href="#"> <i class="fab fa-instagram"></i> </a>
                                        <a class="nav-item nav-link" href="#"> <i class="fab fa-twitter-square"></i></a>
                                        <a class="nav-item nav-link" href="#"> <i class="fab fa-linkedin"></i></a>
                                    </div>
                                    <h2> <a href="article/` + id + `">` + title + ` </a> </h2>
                                </div>
                            </div>
                        </div>
                        <hr>
                    `
                    }
                }
            } else {
                $('.toparticle')[0].innerHTML =
                    `
                <h2> Empty</h2> <img src="/static/svg/empty-animate.svg" alt="" width="80%" height="80%">
                `
                $('.recentarticles')[0].style.display = "none";
            }
        }
    })
})