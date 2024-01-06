// File for containing AJAX operations

function addCard() {
    won_card = {}
    won_card["player_id"] = $('#two_one').text()
    won_card["first_name"] = $('#two_two').text()
    won_card["last_name"] = $('#two_three').text()
    won_card["position"] = $('#two_four').text()
    won_card["team"] = $('#two_five').text()
    won_card["logo_url"] = $('#two_six').text()
    won_card["headshot_url"] = $('#two_seven').text()
    won_card["gp"] = $('#oppo_b').text()
    won_card["goals"] = $('#oppo_b').text()
    won_card["assists"] = $('#oppo_c').text()
    won_card["points"] = $('#oppo_d').text()
    won_card["pim"] = $('#oppo_e').text()

    $.ajax({
         'url': 'http://127.0.0.1:5000/',
        'method': 'POST',
        'data': JSON.stringify(won_card),
        'dataType': "JSON",
        'success': function(won_card) {
            console.log(won_card);
        },
        'content-type': "application/json; charset=utf-8",
        'error': function(xhr, status, error) {
            console.log("error: " + status + "msg: " + error);
        }
    });
}