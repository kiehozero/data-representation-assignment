// File for containing AJAX operations

function callPlayer() {
    var statUrl = 'https://api-web.nhle.com/v1/player/';
    var player = 8482201; /*need to return a player id from players DB */
    var landing = '/landing';
    var url = statUrl + player + landing;
    $.ajax({
        "url": url,
        "method": "GET",
        "data": "",
        "dataType": "JSONP",
        "success": function(playerData) {
            console.log(playerData);
        },
        "error": function(xhr, status, error) {
            console.log("error: " + status + "msg: " + error);
        }
    });
}

/* need an initial API call for the player name and card, then a second for stats. Or could just load it all in one go, as the stats box is not displayed anyway */