$(function () {
    $(".form_datetime").datetimepicker({
        format: 'yyyy-mm-dd',
        minView: "month",
        language:"zh-CN",
    });
    $(".form_datetime_top").datetimepicker({
        format: 'yyyy-mm-dd',
        minView: "month",
        pickerPosition: "top-left",
        language:"zh-CN",
    });
    $(".form_datetime_hi").datetimepicker({
        format: 'yyyy-mm-dd hh:ii',
        minView: "hour",
        language:"zh-CN",
    });

    var o_count = $("#o_count");
    var o_ps_amount = $("#o_ps_amount");
    var ad_tailor_number_people = $("#ad_tailor_number_people");
    var ad_sewing_number_people = $("#ad_sewing_number_people");
    var ad_iron_number_people = $("#ad_iron_number_people");
    num(o_count);
    num(o_ps_amount);
    num(ad_tailor_number_people);
    num(ad_sewing_number_people);
    num(ad_iron_number_people);
});

function num(a) {
    a.change(function () {
        if(parseInt(a.val()) < 0) {
            a.val(0);
        }
    });
    a.keyup(function () {
        if(parseInt(a.val()) < 0) {
            a.val(0);
        }
    });
}