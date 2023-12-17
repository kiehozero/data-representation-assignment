// File for containing all AJAX CRUD operations

function getCard() {
    // Test
    console.log("The sick man of Kilcullen")
    // AJAX call to add card to user's collection
    $.ajax({
        url: "/add",
        method: "POST",
        data: {
            // data to be sent to the server
        },
        dataType: "JSON",
        contentType: "application/json; charset=utf-8",
        "success": function(response) {
            document.getElementById('card2').innerHTML = response;
        },
        "error": function(error) {
            console.log(error);
        }
    });
}