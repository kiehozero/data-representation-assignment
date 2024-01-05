$(document).ready(function(){
    /* Use getElementById to store each card's chosen stat */
    var card1stat = '';
    var card2stat = '';
    var result = '';

    /* Conditional to determine result of match */
    $('#playButton').click(function(){
        /* if the user has not selected a stat, display an alert */
        if (card1stat == '' ) {
            alert('Please select a stat');
        }
        /* Use the stat chosen by the user, then use it to determine the result */
        else {
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
        }
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

     /* Same as above but for collection page */
     $('.coll-flip').click(function(){
         $('.picBox').toggleClass('d-none');
         $('.statBox').toggleClass('d-none');
         /* Logic taken from W3: https://www.w3schools.com/howto/howto_js_toggle_text.asp */
         if ($('.coll-flip').innerText == 'View Picture') {
            $('.coll-flip').innerText = 'Show Stats';
         } else {
            $('.coll-flip').innerText = 'View Picture';
         };
     });

    /* Flip button to show either stats or picture of opponent's card, but only displayed when result is non-blank */
    var oppo = document.getElementById('flipOppo');
    $('#flipOppo').click(function(){
        $('.picOppo').toggleClass('d-none');
        $('.statOppo').toggleClass('d-none');
        if (oppo.innerText == 'View Picture') {
            oppo.innerText == 'View Stats';
        } else {
            oppo.innerText == 'View Picture';
        };
    });

    /* Stat buttons to select a stat to play with, toggle between btn-info and btn-warning for selected stat */
    $('.stat-select').click(function(){
        $('.stat-select').removeClass('btn-warning');
        $('.stat-select').addClass('btn-info');
        $(this).removeClass('btn-info');
        $(this).addClass('btn-warning');
        /* Got this solution from jQuery text function docs and StackOverflow (see README) */
        card1stat = $(this).text();
        card1id = $(this).attr('id');
        console.log(card1id + ": " + card1stat);
        /* Using the selected stat to locate the stat from the other player for comparison */
        if (card1id == 'card_a') {
            card2stat = $('#oppo_a').text()
            card2id = $('#oppo_a').attr('id')
        } else if (card1id == 'card_b') {
            card2stat = $('#oppo_b').text()
            card2id = $('#oppo_b').attr('id')
            /* BUGFIX: I hate JavaScript. Literally deleting a few semi-colons rectified this */
        } else if (card1id == 'card_c') {
            card2stat = $('#oppo_c').text()
            card2id = $('#oppo_c').attr('id')
        } else if (card1id == 'card_d') {
            card2stat = $('#oppo_d').text()
            card2id = $('#oppo_d').attr('id')
        } else if (card1id == 'card_e') {
            card2stat = $('#oppo_e').text()
            card2id = $('#oppo_e').attr('id')
        };
        console.log(card2id + ": " + card2stat);
    });
});