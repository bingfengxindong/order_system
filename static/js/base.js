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
});