$(document).ready(function () {
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
