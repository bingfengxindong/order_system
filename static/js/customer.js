$(function () {
     // 美元大货总金额计算
    var o_dollar_price = $("#o_dollar_price");
    var o_ps_amount = $("#o_ps_amount");
    o_ps_amount.change(function () {
        dollar_calculation(o_dollar_price,o_ps_amount);
    });
    o_ps_amount.keyup(function () {
        dollar_calculation(o_dollar_price,o_ps_amount);
    });
});

function customer_info() {
    var c_info = $("#c_name").val().split(",");
    $("#c_contack").val(c_info[0]);
    $("#c_email").val(c_info[1]);
}

function dollar_calculation(o_dollar_price,o_ps_amount) {
    var o_ps_dollar_total_price_val;
    var o_dollar_price_val = o_dollar_price.val();
    var o_ps_amount_val = o_ps_amount.val();
    if(o_ps_amount && o_dollar_price_val){
        o_ps_dollar_total_price_val = parseFloat(o_dollar_price_val) * parseFloat(o_ps_amount_val);
        $("#o_ps_dollar_total_price").val(o_ps_dollar_total_price_val.toFixed(2));
    }
}