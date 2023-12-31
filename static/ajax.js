// File for containing AJAX operations

function createBookAjax(book) {
    console.log(JSON.stringify(book));
    $.ajax({
        "url": "http://127.0.0.1:5000/books",
        "method": "POST",
        "data": JSON.stringify(book),
        "dataType": "JSON",
        contentType: "application/json; charset=utf-8",
        "success": function(result) {
            //console.log(result);
            book.id = result.id
            addBookToTable(book)
            clearForm()
            showViewAll()
        },
        "error": function(xhr, status, error) {
            console.log("error: " + status + "msg: " + error);
        }
    });
}