$(document).ready(function () {
    $('.next1').on('click', function () {
        console.log('clicked');
        var currentImg = $('.active1');
        var nextImg = currentImg.next();

        if (nextImg.length) {
            currentImg.removeClass('active1').css('z-index', -10);
            nextImg.addClass('active1').css('z-index', 10);

        }
    });

    $('.prev1').on('click', function () {
        console.log('clicked');
        var currentImg = $('.active1');
        var prevImg = currentImg.prev();

        if (prevImg.length) {
            currentImg.removeClass('active1').css('z-index', -10);
            prevImg.addClass('active1').css('z-index', 10);

        }
    });


    $('.next2').on('click', function () {
        console.log('clicked');
        var currentImg = $('.active2');
        var nextImg = currentImg.next();

        if (nextImg.length) {
            currentImg.removeClass('active2').css('z-index', -10);
            nextImg.addClass('active2').css('z-index', 10);

        }
    });


    $('.prev2').on('click', function () {
        console.log('clicked');
        var currentImg = $('.active2');
        var prevImg = currentImg.prev();

        if (prevImg.length) {
            currentImg.removeClass('active2').css('z-index', -10);
            prevImg.addClass('active2').css('z-index', 10);

        }
    });

    $('.next3').on('click', function () {
        console.log('clicked');
        var currentImg = $('.active3');
        var nextImg = currentImg.next();

        if (nextImg.length) {
            currentImg.removeClass('active3').css('z-index', -10);
            nextImg.addClass('active3').css('z-index', 10);

        }
    });


    $('.prev3').on('click', function () {
        console.log('clicked');
        var currentImg = $('.active3');
        var prevImg = currentImg.prev();

        if (prevImg.length) {
            currentImg.removeClass('active3').css('z-index', -10);
            prevImg.addClass('active3').css('z-index', 10);

        }
    });


    $('.next4').on('click', function () {
        console.log('clicked');
        var currentImg = $('.active4');
        var nextImg = currentImg.next();

        if (nextImg.length) {
            currentImg.removeClass('active4').css('z-index', -10);
            nextImg.addClass('active4').css('z-index', 10);

        }
    });


    $('.prev4').on('click', function () {
        console.log('clicked');
        var currentImg = $('.active4');
        var prevImg = currentImg.prev();

        if (prevImg.length) {
            currentImg.removeClass('active4').css('z-index', -10);
            prevImg.addClass('active4').css('z-index', 10);

        }
    });





});


