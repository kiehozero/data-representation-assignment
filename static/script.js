$(document).ready(function(){
    /* Use getElementById to store each card's chosen stat */
    card1stat = 4;
    card2stat = 3;

    /* Conditional to determine result of match */
    $('#playButton').click(function(){
        $('#playButton').removeClass('btn-dark');
        if (card1stat > card2stat) {
            result = 'YOU WIN!';
            $('#playButton').addClass('btn-success');
            $('#addCard').removeClass('d-none');
            /* add logic - if ID is aleady in DB, display 'You already have this card' and disable button */
        } else if (card1stat == card2stat) {
            result = 'DRAW!';
            $('#playButton').addClass('btn-secondary');
        } else if (card1stat < card2stat) {
            result = 'YOU LOSE!';
            $('#playButton').addClass('btn-danger');
        };
        document.getElementById('playButton').innerText = result;
        document.getElementById('againButton').classList.remove('d-none');
    });

    /* Play Again button to reset the game, pretty much the opposite of the above */
    $('#againButton').click(function(){
        $('#playButton').addClass('btn-dark');
        $('#playButton').removeClass('btn-success');
        $('#playButton').removeClass('btn-secondary');
        $('#playButton').removeClass('btn-danger');
        document.getElementById('playButton').innerText = 'PLAY';
        document.getElementById('againButton').classList.add('d-none');
        document.getElementById('addCard').classList.add('d-none');
    });

    /* Flip button to show eother stats or picture */
    $('#flipButton').click(function(){
        $('.picBox').toggleClass('d-none');
        $('.statBox').toggleClass('d-none');
        $('#flipButton').toggleClass('fa-rotate');
        document.getElementById('flipButton').innerText = 'View Picture';
    });

    /* Stat buttons to select a stat to play with, toggle between btn-info and btn-warning for selected stat */
    $('.stat-select').click(function(){
        $('.stat-select').removeClass('btn-warning');
        $('.stat-select').addClass('btn-info');
        $(this).removeClass('btn-info');
        $(this).addClass('btn-warning');
        /* can be removed, just for testing, it also causes an error in how the win/loss button is styled above
        card1stat = $(this).parent().prev().text();
        console.log(card1stat); */
    });
});