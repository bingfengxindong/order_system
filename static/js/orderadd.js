$(function () {
    var proofing_progress_click = $("#proofing-progress-click");
    var proofing_progress = $("#proofing-progress");
    var production_schedule_click = $("#production-schedule-click");
    var production_schedule = $("#production-schedule");
    var quotation_click = $("#quotation-click");
    var quotation = $("#quotation");
    var accounting_documents_click = $("#accounting-documents-click");
    var accounting_documents = $("#accounting-documents");

    // 各表重叠切换
    proofing_progress_click.click(function () {
        switch_navigation(proofing_progress_click,proofing_progress,production_schedule_click,production_schedule,quotation_click,quotation,accounting_documents_click,accounting_documents);
    });
    production_schedule_click.click(function () {
        switch_navigation(production_schedule_click,production_schedule,proofing_progress_click,proofing_progress,quotation_click,quotation,accounting_documents_click,accounting_documents);
    });
    quotation_click.click(function () {
        switch_navigation(quotation_click,quotation,production_schedule_click,production_schedule,proofing_progress_click,proofing_progress,accounting_documents_click,accounting_documents);
    });
    accounting_documents_click.click(function () {
        switch_navigation(accounting_documents_click,accounting_documents,quotation_click,quotation,production_schedule_click,production_schedule,proofing_progress_click,proofing_progress);
    });

    var order_number = $(".order-number");
    // 数量不能为负数
    no_negative(order_number);

    // 数量单价覆盖全表 总价计算
    var pi_amount = $("#pi_amount");
    var pi_amount_1 = $("#pi_amount_1");
    var pi_unit_price = $("#pi_unit_price");
    var pi_unit_price_1 = $("#pi_unit_price_1");
    var pi_total_price = $("#pi_total_price");
    // 数量
    pi_amount.change(function () {
        change_amount(pi_amount,pi_amount_1,pi_unit_price,pi_total_price)
    });
    pi_amount.keyup(function () {
        change_amount(pi_amount,pi_amount_1,pi_unit_price,pi_total_price)
    });

    pi_amount_1.change(function () {
        change_amount(pi_amount_1,pi_amount,pi_unit_price,pi_total_price)
    });
    pi_amount_1.keyup(function () {
        change_amount(pi_amount_1,pi_amount,pi_unit_price,pi_total_price)
    });
    // 单价
    pi_unit_price.change(function () {
        change_unit_price(pi_unit_price,pi_unit_price_1,pi_amount,pi_total_price)
    });
    pi_unit_price.keyup(function () {
        change_unit_price(pi_unit_price,pi_unit_price_1,pi_amount,pi_total_price)
    });

    pi_unit_price_1.change(function () {
        change_unit_price(pi_unit_price_1,pi_unit_price,pi_amount,pi_total_price)
    });
    pi_unit_price_1.keyup(function () {
        change_unit_price(pi_unit_price_1,pi_unit_price,pi_amount,pi_total_price)
    });
});

function switch_navigation(sc,s,hc1,h1,hc2,h2,hc3,h3){
    sc.attr("class","center-title-in-now");
    hc1.attr("class","center-title-in");
    hc2.attr("class","center-title-in");
    hc3.attr("class","center-title-in");
    s.show();
    h1.hide();
    h2.hide();
    h3.hide();
}
function no_negative(a) {
    a.change(function () {
        var num_val = $(this).val();
        if(num_val < 0){
            $(this).val(0);
        }
    });
    a.keyup(function () {
        var num_val = $(this).val();
        if(num_val < 0){
            $(this).val(0);
        }
    });
}
function change_amount(pi_amount,pi_amount_1,pi_unit_price,pi_total_price) {
    var pi_amount_val = pi_amount.val();
    pi_amount_1.val(pi_amount_val);

    // 总价
    var unit_price;
    var pi_unit_price_val = pi_unit_price.val();
    if(pi_unit_price_val.length == 0){

    }else{
        unit_price = parseFloat(pi_unit_price_val);
        pi_total_price.val((pi_amount_val * unit_price).toFixed(2));
    }
}

function change_unit_price(pi_unit_price,pi_unit_price_1,pi_amount,pi_total_price) {
    var pi_unit_price_val = pi_unit_price.val();
    pi_unit_price_1.val(pi_unit_price_val);

    // 总价
    var unit_price;
    var pi_amount_val = pi_amount.val();
    if(pi_amount_val == 0){

    }else{
        unit_price = parseFloat(pi_unit_price_val);
        pi_total_price.val((pi_amount_val * unit_price).toFixed(2));
    }
}