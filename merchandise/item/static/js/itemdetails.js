function loadResults() {
    var search_text = $("#id_name").val();
    $("#items").load("list/?" + $.param({
        name: search_text})
    );
}

$(document).ready(function() {    
    loadResults();
    $("#id_name").keyup(function() {
        loadResults();
    });
});