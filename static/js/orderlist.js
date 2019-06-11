$(function () {
    order_date_timepicker();
    order_start_end_date();
    customer_name_change();
});

function order_date_timepicker() {
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
}

function order_start_end_date() {
    $("#order_date").datetimepicker({
        format: 'yyyy-mm-dd',
        minView: "month",
        language:"zh-CN",
    });

    $("#order_date").change(function () {
        var sd =  $(this).val();
        $("#order_end_date").datetimepicker({
            format: 'yyyy-mm-dd',
            minView: "month",
            language:"zh-CN",
            startDate:sd,
        });
    })
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
                    <img src="`+ url +`">
                    <a onclick="cancel_image()">取消</a>
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