    $('.prod').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    navText: ["<img src='assets/images/icons/left.png'>","<img src='assets/images/icons/right.png'>"],
    autoPlay: 1000,
    responsive:{
        0:{
            items:1
        },
        1000:{
            items:1
        }
    }
    });
   $('.owl-carousel').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    navText: ["<img src='assets/images/icons/left.png'>","<img src='assets/images/icons/right.png'>"],
    autoPlay: 1000,
    responsive:{
        0:{
            items:2
        },
        330:{
            items:2
        },
        375:{
          items: 3
        },
        424:{
          items:3
        },
        700:{
            items:4
        },
        1000:{
            items:4
        }
    }
    });