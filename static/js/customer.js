function customer_info() {
    var c_info = $("#c_name").val().split(",");
    $("#c_contack").val(c_info[0]);
    $("#c_email").val(c_info[1]);
}