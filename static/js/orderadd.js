$(function () {
    // 各表重叠切换
    $("#proofing-progress-click").click(function () {
        $(this).attr("class","center-title-in-now");
        $("#production-schedule-click").attr("class","center-title-in");
        $("#quotation-click").attr("class","center-title-in");
        $("#accounting-documents-click").attr("class","center-title-in");
        $("#proofing-progress").show();
        $("#production-schedule").hide();
        $("#quotation").hide();
        $("#accounting-documents").hide();
    });
    $("#production-schedule-click").click(function () {
        $(this).attr("class","center-title-in-now");
        $("#proofing-progress-click").attr("class","center-title-in");
        $("#quotation-click").attr("class","center-title-in");
        $("#accounting-documents-click").attr("class","center-title-in");
        $("#production-schedule").show();
        $("#proofing-progress").hide();
        $("#quotation").hide();
        $("#accounting-documents").hide();
    });
    $("#quotation-click").click(function () {
        $(this).attr("class","center-title-in-now");
        $("#proofing-progress-click").attr("class","center-title-in");
        $("#production-schedule-click").attr("class","center-title-in");
        $("#accounting-documents-click").attr("class","center-title-in");
        $("#quotation").show();
        $("#proofing-progress").hide();
        $("#production-schedule").hide();
        $("#accounting-documents").hide();
    });
    $("#accounting-documents-click").click(function () {
        $(this).attr("class","center-title-in-now");
        $("#proofing-progress-click").attr("class","center-title-in");
        $("#production-schedule-click").attr("class","center-title-in");
        $("#quotation-click").attr("class","center-title-in");
        $("#accounting-documents").show();
        $("#proofing-progress").hide();
        $("#production-schedule").hide();
        $("#quotation").hide();
    });

    // 数量不能为负数
    $(".order-number").change(function () {
        var num_val = $(this).val();
        if(num_val < 0){
            $(this).val(0);
        }
    });
    $(".order-number").keyup(function () {
        var num_val = $(this).val();
        if(num_val < 0){
            $(this).val(0);
        }
    });

    // 数量单价覆盖全表 总价计算
    // 数量
    $("#pi_amount").change(function () {
        var pi_amount_val = $(this).val();
        $("#pi_amount_1").val(pi_amount_val);

        // 总价
        var unit_price;
        var pi_unit_price = $("#pi_unit_price").val().replace("$","");
        if(pi_unit_price.length == 0){

        }else{
            unit_price = parseFloat(pi_unit_price);
            $("#pi_total_price").val("$" + (pi_amount_val * unit_price).toFixed(2).toString());
        }
    });
    $("#pi_amount").keyup(function () {
        var pi_amount_val = $(this).val();
        $("#pi_amount_1").val(pi_amount_val);

        // 总价
        var unit_price;
        var pi_unit_price = $("#pi_unit_price").val().replace("$","");
        if(pi_unit_price.length == 0){

        }else{
            unit_price = parseFloat(pi_unit_price);
            $("#pi_total_price").val("$" + (pi_amount_val * unit_price).toFixed(2).toString());
        }
    });
    // 单价
    $("#pi_unit_price").change(function () {
        var pi_unit_price = $(this).val();
        $("#pi_unit_price_1").val(pi_unit_price);

        // 总价
        var unit_price;
        var pi_amount_val = $("#pi_amount").val();
        if(pi_amount_val == 0){

        }else{
            unit_price = parseFloat(pi_unit_price.replace("$",""));
            $("#pi_total_price").val("$" + (pi_amount_val * unit_price).toFixed(2).toString());
        }
    });
    $("#pi_unit_price").keyup(function () {
        var pi_unit_price = $(this).val();
        $("#pi_unit_price_1").val(pi_unit_price);

        // 总价
        var unit_price;
        var pi_amount_val = $("#pi_amount").val();
        if(pi_amount_val == 0){

        }else{
            unit_price = parseFloat(pi_unit_price.replace("$",""));
            $("#pi_total_price").val("$" + (pi_amount_val * unit_price).toFixed(2).toString());
        }
    });

});