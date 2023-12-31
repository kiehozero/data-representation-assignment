$(document).ready(function(){
    /* Use getElementById to store each card's chosen stat */
    var card1stat = 3;
    var card2stat = 7;
    var result = '';

    /* Conditional to determine result of match */
    $('#playButton').click(function(){
        /* StatChoice stores the stat chosen by the user, then use it to determine the result */
        /* Add IF statement to check if statChoice is empty, if so, display 'Please select a stat' */
        var statChoice = [];
        $('#card2').removeClass('d-none');
        $('#playButton').removeClass('btn-dark');
        if (card1stat > card2stat) {
            result = 'YOU WIN!';
            $('#playButton').addClass('btn-success');
            $('#addCard').removeClass('d-none');
            /* Add logic - if ID is aleady in DB, display 'You already have this card' and disable button */
        } else if (card1stat == card2stat) {
            result = 'DRAW!';
            $('#playButton').addClass('btn-secondary');
        } else if (card1stat < card2stat) {
            result = 'YOU LOSE!';
            $('#playButton').addClass('btn-danger');
        };
        document.getElementById('playButton').innerText = result;
        document.getElementById('againButton').classList.remove('d-none');
        document.getElementById('flipOppo').classList.remove('d-none');
    });

    /* Play Again button to reset the game's variables and visible styles, pretty much the opposite of the above */
    $('#againButton').click(function(){
        result = '';
        $('#playButton').addClass('btn-dark');
        $('#playButton').removeClass('btn-success');
        $('#playButton').removeClass('btn-secondary');
        $('#playButton').removeClass('btn-danger');
        document.getElementById('playButton').innerText = 'PLAY';
        document.getElementById('againButton').classList.add('d-none');
        document.getElementById('addCard').classList.add('d-none');
        document.getElementById('flipOppo').classList.add('d-none');
        document.getElementById('flipButton').innerText = 'Show Stats';
        $('.stat-select').removeClass('btn-warning');
        $('.stat-select').addClass('btn-info');
        $('#flipButton').innerText = 'View Picture';
        $('.picBox').removeClass('d-none');
        $('.statBox').addClass('d-none');
        $('#flipOppo').innerText = 'View Picture';
        $('.picOppo').removeClass('d-none');
        $('.statOppo').addClass('d-none');
    });

    /* Flip button to show either stats or picture of player's chosen card */
    var flip = document.getElementById('flipButton');
    $('#flipButton').click(function(){
        $('.picBox').toggleClass('d-none');
        $('.statBox').toggleClass('d-none');
        /* Logic taken from W3: https://www.w3schools.com/howto/howto_js_toggle_text.asp */
        if (flip.innerText == 'View Picture') {
            flip.innerText = 'Show Stats';
        } else {
            flip.innerText = 'View Picture';
        };
    });

    /* Flip button to show either stats or picture of opponent's card, but only displayed when result is non-blank */
    var oppo = document.getElementById('flipOppo');
    $('#flipOppo').removeClass('d-none');
    $('#flipOppo').click(function(){
        $('.picOppo').toggleClass('d-none');
        $('.statOppo').toggleClass('d-none');
        if (oppo.innerText == 'View Picture') {
            oppo.innerText = 'View Stats';
        } else {
            oppo.innerText = 'View Picture';
        };
    });

    /* Stat buttons to select a stat to play with, toggle between btn-info and btn-warning for selected stat */
    $('.stat-select').click(function(){
        $('.stat-select').removeClass('btn-warning');
        $('.stat-select').addClass('btn-info');
        $(this).removeClass('btn-info');
        $(this).addClass('btn-warning');
        /* can be removed, just for testing, it also causes an error in how the win/loss button is styled above,
        although it will be useful once you start pushing items up to SQL
        card1stat = $(this).parent().prev().text();
        console.log(card1stat); */
    });
});