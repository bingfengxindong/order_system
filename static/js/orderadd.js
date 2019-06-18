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
    var pi_unit_price = $("#pi_unit_price");
    var pi_total_price = $("#pi_total_price");
    // 数量
    pi_amount.change(function () {
        change_amount(pi_amount,pi_unit_price,pi_total_price)
    });
    pi_amount.keyup(function () {
        change_amount(pi_amount,pi_unit_price,pi_total_price)
    });

    // 单价
    pi_unit_price.change(function () {
        change_unit_price(pi_unit_price,pi_amount,pi_total_price)
    });
    pi_unit_price.keyup(function () {
        change_unit_price(pi_unit_price,pi_amount,pi_total_price)
    });

    // 大货报价计算
    var pi_offer = $("#pi_offer");
    var pi_fabric_quotation = $("#pi_fabric_quotation");
    var pi_ingredients_quotation = $("#pi_ingredients_quotation");
    var pi_labor_payment_quotation = $("#pi_labor_payment_quotation");
    var pi_water_washing_quotation = $("#pi_water_washing_quotation");
    var pi_print_quotation = $("#pi_print_quotation");
    var pi_embroider_quotation = $("#pi_embroider_quotation");
    var pi_packaging_quotation = $("#pi_packaging_quotation");
    var pi_other_quotation = $("#pi_other_quotation");
    var pi_reserved_profits = $("#pi_reserved_profits");

    pi_fabric_quotation.change(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });
    pi_fabric_quotation.keyup(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });

    pi_ingredients_quotation.change(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });
    pi_ingredients_quotation.keyup(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });

    pi_labor_payment_quotation.change(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });
    pi_labor_payment_quotation.keyup(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });

    pi_water_washing_quotation.change(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });
    pi_water_washing_quotation.keyup(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });

    pi_print_quotation.change(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });
    pi_print_quotation.keyup(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });

    pi_embroider_quotation.change(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });
    pi_embroider_quotation.keyup(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });

    pi_packaging_quotation.change(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });
    pi_packaging_quotation.keyup(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });

    pi_other_quotation.change(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });
    pi_other_quotation.keyup(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });

    pi_reserved_profits.change(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
    });
    pi_reserved_profits.keyup(function () {
        calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits)
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
function change_amount(pi_amount,pi_unit_price,pi_total_price) {
    var pi_amount_val = pi_amount.val();

    // 总价
    var unit_price;
    var pi_unit_price_val = pi_unit_price.val();
    if(pi_unit_price_val.length == 0){

    }else{
        unit_price = parseFloat(pi_unit_price_val);
        pi_total_price.val((pi_amount_val * unit_price).toFixed(2));
    }
}

function change_unit_price(pi_unit_price,pi_amount,pi_total_price) {
    var pi_unit_price_val = pi_unit_price.val();

    // 总价
    var unit_price;
    var pi_amount_val = pi_amount.val();
    if(pi_amount_val == 0){

    }else{
        unit_price = parseFloat(pi_unit_price_val);
        pi_total_price.val((pi_amount_val * unit_price).toFixed(2));
    }
}
function calculate_offer(pi_offer,pi_fabric_quotation,pi_ingredients_quotation,pi_labor_payment_quotation,pi_water_washing_quotation,pi_print_quotation,pi_embroider_quotation,pi_packaging_quotation,pi_other_quotation,pi_reserved_profits) {
    var pi_offer_val = pi_offer.val();
    var pi_fabric_quotation_val = pi_fabric_quotation.val();
    var pi_ingredients_quotation_val = pi_ingredients_quotation.val();
    var pi_labor_payment_quotation_val = pi_labor_payment_quotation.val();
    var pi_water_washing_quotation_val = pi_water_washing_quotation.val();
    var pi_print_quotation_val = pi_print_quotation.val();
    var pi_embroider_quotation_val = pi_embroider_quotation.val();
    var pi_packaging_quotation_val = pi_packaging_quotation.val();
    var pi_other_quotation_val = pi_other_quotation.val();
    var pi_reserved_profits_val = pi_reserved_profits.val();

    if(pi_fabric_quotation_val && pi_ingredients_quotation_val && pi_labor_payment_quotation_val && pi_water_washing_quotation_val && pi_print_quotation_val && pi_embroider_quotation_val && pi_packaging_quotation_val && pi_other_quotation_val && pi_reserved_profits_val){
        pi_offer_val = parseFloat(pi_fabric_quotation_val) + parseFloat(pi_ingredients_quotation_val) + parseFloat(pi_labor_payment_quotation_val) + parseFloat(pi_water_washing_quotation_val) + parseFloat(pi_print_quotation_val) + parseFloat(pi_embroider_quotation_val) + parseFloat(pi_packaging_quotation_val) + parseFloat(pi_other_quotation_val) + parseFloat(pi_reserved_profits_val);
        pi_offer.val(parseFloat(pi_offer_val).toFixed(2));
    }
}