/*global $*/
/*global event*/

// Services Section
$(function () {
    // Animate on Scroll
    new WOW().init();
});

// Work Section
$(function () {
    // Animate on Scroll
    $('#work').magnificPopup({
        delegate: 'a',
        type: 'image',
        gallery: {
            enabled: true
        }
    });
});

// Team Section
$(function () {
    $("#team-members").owlCarousel({
        items: 3,
        autoplay: true,
        autoplayHoverPause: true,
        smartSpeed: 700,
        loop: false,
        responsive: {
            0: {
                items: 1,
            },
            480: {
                items: 2,
            },
            767: {
                items: 2,
            },
            768: {
                items: 3,
            }
        }
    });
});

// Clients Section
$(function () {
    $("#clients-list").owlCarousel({
        items: 4,
        autoplay: true,
        autoplayHoverPause: true,
        smartSpeed: 700,
        loop: true,
        responsive: {
            0: {
                items: 1,
            },
            480: {
                items: 3,
            },
            767: {
                items: 2,
            },
            768: {
                items: 4,
            }
        }
    });
});

// Navigation Section
/*$(function () {
    
    $(window).scroll(function() {
        
        if($(this).scrollTop() < 50) {
           $('nav').removeClass("techarts-dark");
        } else {
           $('nav').addClass("techarts-dark");
        }
        
    });
    
});*/

// Navigation Smooth Scroll
$(function () {

    $('a.smooth-scroll').click(function () {
        event.preventDefault();

        var section = $(this).attr('href');

        $('html, body').animate({
            scrollTop: $(section).offset().top - 64
        }, 1250);

    });

});

// Closing Mobile Menu 
$(function () {

    $('.navbar-collapse ul li a').on('click touch', function () {
        $('.navbar-toggler').click();
    });

});