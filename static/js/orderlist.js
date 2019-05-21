$(function () {
    order_date_timepicker();
    customer_name_change();
    var order_date = $("#order_date");
    var order_end_date = $("#order_end_date");
    order_end_date.on("change",function () {
        var order_date_val = $("#order_date").val();
        var order_end_date_val = $("#order_end_date").val();
        if(order_date_val == ""){
            $("#time-prompt").text("请选择开始时间！");
        }else{
            if(Date.parse(order_date_val) > Date.parse(order_end_date_val)){
                $("#time-prompt").text("开始时间不应该大于结束时间！");
            }else{
                $("#time-prompt").text("");
            }
        }
    });
});

function order_date_timepicker() {
    $(".form_datetime").datetimepicker({
        format: 'yyyy-mm-dd',
        minView: "month",
    });
    $(".form_datetime_top").datetimepicker({
        format: 'yyyy-mm-dd',
        minView: "month",
        pickerPosition: "top-left"
    });
}

function customer_name_change() {
    $("#customer_name").change(function () {
        var pk = $(this).val();
        $.ajax({
            url:"/order/ordercustomer",
            type:"GET",
            data:{
                "pk":pk,
            },
            success:function (data) {
                c_info = eval(data);
                $("#customer_contack").val(data.c_contack);
                $("#customer_email").val(data.c_email);
            }
        })
    });
}

function add_image() {
    var img = $("#add_image");
    var files;
    img.click();
    img.on("change",function () {
        files = this.files[0];
        var url = getObjectURL(files);
        if(url){
            $(".order-image").html(
                `
                    <a onclick="cancel_image()">取消</a>
                    <img src="`+ url +`">
                `
            );
        }
    })
}

function getObjectURL(file) {
var url = null ;
if (window.createObjectURL != undefined) { // basic
    url = window.createObjectURL(file) ;
} else if (window.URL != undefined) { // mozilla(firefox)
    url = window.URL.createObjectURL(file) ;
} else if (window.webkitURL != undefined) { // webkit or chrome
    url = window.webkitURL.createObjectURL(file) ;
}
return url ;
}

function cancel_image() {
    $(".order-image").html(
         `
            <a onclick="add_image()">
                <span class="glyphicon glyphicon-plus" aria-hidden="true"></span>
            </a>
        `
    );
}