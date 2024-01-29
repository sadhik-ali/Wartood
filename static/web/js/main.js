(function ($) {
    "use strict";
    
    /*-----------------
        Menu Stick
    -----------------*/
    var header = $('.sticky-bar');
    var $window = $(window);
    $window.on('scroll', function() {
        var scroll = $window.scrollTop();
        if (scroll < 200) {
            header.removeClass('stick');
        } else {
            header.addClass('stick');
        }
    });
    
    /*-------------------------------
       Header Search Toggle
    -----------------------------------*/
    var searchToggle = $('.search-toggle');
    searchToggle.on('click', function(e){
        e.preventDefault();
        if($(this).hasClass('open')){
           $(this).removeClass('open');
           $(this).siblings('.search-wrap-1').removeClass('open');
        }else{
           $(this).addClass('open');
           $(this).siblings('.search-wrap-1').addClass('open');
        }
    })

    /*====== QuickInfo ======*/
    function quickInfo() {
        var searchTrigger = $('.header-aside-button'),
            endTriggersearch = $('.aside-close'),
            container = $('.header-aside-active');
        searchTrigger.on('click', function(e) {
            e.preventDefault();
            container.addClass('inside');
        });
        endTriggersearch.on('click', function() {
            container.removeClass('inside');
        });
    };
    quickInfo();


/*---------------------
        Mobile menu
    --------------------- */
    var $offCanvasNav = $('.mobile-menu'),
        $offCanvasNavSubMenu = $offCanvasNav.find('.dropdown');
    /*Add Toggle Button With Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i></i></span>');
    /*Close Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.slideUp();
    /*Category Sub Menu Toggle*/
    $offCanvasNav.on('click', 'li a, li .menu-expand', function(e) {
        var $this = $(this);
        if (($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('menu-expand'))) {
            e.preventDefault();
            if ($this.siblings('ul:visible').length) {
                $this.parent('li').removeClass('active');
                $this.siblings('ul').slideUp();
            } else {
                $this.parent('li').addClass('active');
                $this.closest('li').siblings('li').removeClass('active').find('li').removeClass('active');
                $this.closest('li').siblings('li').find('ul:visible').slideUp();
                $this.siblings('ul').slideDown();
            }
        }
    });

    // Hero slider active
    var heroSliderActive = new Swiper('.hero-slider-active', {
        loop: true,
        speed: 750,
        effect: 'fade',
        slidesPerView: 1,
        navigation: {
            nextEl: '.home-slider-next , .home-slider-next2 , .home-slider-next3',
            prevEl: '.home-slider-prev , .home-slider-prev2 , .home-slider-prev3',
        }
    });
    
    /*====== Brand logo active ======*/
    var brandLogo = new Swiper('.brand-logo-active', {
        slidesPerView: 5,
        spaceBetween: 30,
        loop: true,
        breakpoints: {
            320: {
                slidesPerView: 2,
            },
            576: {
                slidesPerView: 3
            },
            768: {
                slidesPerView: 4
            },
            992: {
                slidesPerView: 5
            }
        },
    });
    
    // Project slider active
    var projectSliderActive = new Swiper('.project-slider-active', {
        slidesPerView: 4,
        loop: true,
        navigation: {
            nextEl: '.project-slider-next',
            prevEl: '.project-slider-prev',
        },
        breakpoints: {
            320: {
                slidesPerView: 1
            },
            576: {
                slidesPerView: 2
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 3
            },
            1200: {
                slidesPerView: 4
            }
        },
    });
    
    
    /*====== Testimonial active ======*/
    var testimonialActive = new Swiper('.testimonial-active', {
        slidesPerView: 3,
        spaceBetween: 30,
        loop: true,
        navigation: {
            nextEl: '.home-slider-next , .home-slider-next2 , .home-slider-next3',
            prevEl: '.home-slider-prev , .home-slider-prev2 , .home-slider-prev3',
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
            },
            576: {
                slidesPerView: 2
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 3
            }
        },
    });
    
    /*====== Blog active ======*/
    var blogActive = new Swiper('.blog-active', {
        slidesPerView: 3,
        spaceBetween: 30,
        loop: true,
        breakpoints: {
            320: {
                slidesPerView: 1,
            },
            576: {
                slidesPerView: 2
            },
            768: {
                slidesPerView: 2
            },
            992: {
                slidesPerView: 3
            }
        },
    });
    
    /*--
        Hover Parallax Js
    ------------------------------------*/
    if ($(".hover_plx").length > 0){
        var sceneElements = document.querySelectorAll('.hover_plx');
        var parallaxScenes = [];
        for (var i = 0; i < sceneElements.length; i++) {
            parallaxScenes.push(new Parallax(sceneElements[i]));
        }
    }
    
    
    /* ----------------------------
		Odometer Activation 
    -------------------------------*/
	if( $('.odometer').length ){
		var elemOffset = $('.odometer').offset().top;
		var winHeight = $(window).height();
		if(elemOffset < winHeight){
			$('.odometer').each(function(){
				$(this).html($(this).data('count-to'));
			});
		}
		$(window).on('scroll', function(){
			var elemOffset = $('.odometer').offset().top;
			function winScrollPosition() {
				var scrollPos = $(window).scrollTop(),
					winHeight = $(window).height();
				var scrollPosition = Math.round(scrollPos + (winHeight / 1.2));
				return scrollPosition;
			}
			if ( elemOffset < winScrollPosition()) {
				$('.odometer').each(function(){
					$(this).html($(this).data('count-to'));
				});
			}	
		});
	};
    
    /*====== Video active ======*/
    $('.video-banner').on('click', '.status', function(e) {
        e.preventDefault();
        var $el = $(this),
            $banner = $el.closest('.video-banner'),
            video = $el.closest('.video-banner').find('video')[0];
        if (video.paused) {
            $banner.addClass('playing');
            video.play();
        } else {
            $banner.removeClass('playing');
            video.pause();
        }
    });
    
   
    /*------ ScrollUp -------- */
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
    
    
    /*------ Image Conversion Active -------- */
    var beforeandafter = $('.beforeandafter');
    if(beforeandafter.length){
        var beforeAfter;
        beforeAfter = new ddbeforeandafter({
            wrapperid: 'beforeandafteractive',
        });
    }
    
    /*--
    Magnific Popup
    ------------------------*/
    $('.img-zoom').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        }
    });
    
    
    /*------ Isotope active 2 ----*/
    $('.grid').imagesLoaded( function() {
        // filter items on button click
        $('.project-menu-active').on( 'click', 'button', function() {
            var filterValue = $(this).attr('data-filter');
            $grid2.isotope({ filter: filterValue });
        });	
        // init Isotope
        var $grid2 = $('.grid').isotope({
            itemSelector: '.grid-item',
            percentPosition: true,
            layoutMode: 'masonry',
            masonry: {
                // use outer width of grid-sizer for columnWidth
                columnWidth: '.grid-item',
            }
        });
    });
    $('.isotope-btn-add-active button').on('click', function(event) {
        $(this).siblings('.active').removeClass('active');
        $(this).addClass('active');
        event.preventDefault();
    });
    
    /*-------------------------
      Scroll Animation
    --------------------------*/
    AOS.init({
        once: true,
        duration: 1000,
    });
    
    /*---------------------
        Sidebar active
    --------------------- */
    $('.sidebar-active').stickySidebar({
        topSpacing: 80,
        bottomSpacing: 30,
        minWidth: 767,
    });
    
    
    
    
})(jQuery);    
    

// Whatsapp Enquiry

// document.addEventListener("DOMContentLoaded", function () {
//     document.getElementById("commentForm").addEventListener("submit", function (e) {
//       e.preventDefault(); // Prevent form submission
  
//       var form = this;
//       var formData = new FormData(form);
  
//       var whatsappMessage = "Enquiry:\n\n";
//       formData.forEach(function (value, key) {
//         whatsappMessage += key + ": " + value + "\n";
//       });
  
//       var whatsappNumber = "+917510240707"; // Replace with your WhatsApp number
//       var templateMessage = encodeURIComponent(whatsappMessage);
  
//       var whatsappURL =
//         "https://api.whatsapp.com/send?phone=" +
//         whatsappNumber +
//         "&text=" +
//         templateMessage;
  
//       window.open(whatsappURL, "_blank");
//     });
//   });


// Navbar activate positive sticky // css 835

 function setActiveNav() {
    var links = document.querySelectorAll('.nav-link');
    var currentPath = window.location.pathname;

    links.forEach(function(link) {
        var linkPath = link.getAttribute('href');
        if (currentPath === linkPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}

// Call the function to set the initial active class
setActiveNav();

// Add an event listener for changes in the URL (e.g., when navigating)
window.addEventListener('popstate', setActiveNav);

// Add a scroll event listener for the sticky navigation
window.addEventListener('scroll', function() {
    var navbar = document.querySelector('.sticky-bar');
    if (window.scrollY > 100) { // Adjust the scroll threshold as needed
        navbar.classList.add('stick');
    } else {
        navbar.classList.remove('stick');
    }
});


// Navbar activate // css 630

$(document).ready(function() {
    var currentUrl = window.location.href;

    $('.mobile-menu li a').each(function() {
        if ($(this).attr('href') === currentUrl) {
            $(this).parent().addClass('active');
        }
    });
});


// Email footer

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("mc-embedded-subscribe-form").addEventListener("submit", function(e) {
        const emailInput = document.querySelector("#mc-embedded-subscribe-form .email");
        const emailError = document.getElementById("emailError");

        if (emailInput.value.trim() === "") {
            e.preventDefault();
            emailError.style.display = "block";
        } else {
            emailError.style.display = "none";
        }
    });
});

// thank you popup

document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("contactForm");         
    form.addEventListener("submit", function (event) {
        event.preventDefault();
        setTimeout(function () {
            // Display SweetAlert thank you popup
            Swal.fire({
                title: 'Thank You!',
                text: 'Your message has been sent successfully.',
                icon: 'success',
                showCancelButton: false,
                confirmButtonColor: '#b45100',
                confirmButtonText: 'OK'
            }).then((result) => {
                if (result.isConfirmed) {
                    form.submit();
                }
            });
        }, 500); // Display the SweetAlert popup after 1 second
    });
});