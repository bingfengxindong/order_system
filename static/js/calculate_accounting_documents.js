$(function () {
    fabric_ingredient_main();
    embroide_print_main();
    labor_payment_main();
    packaging_shipping_main();
    calculate_profit_main();
});
function labor_payment_main() {
    var ad_labor_paymentl_amount = $("#ad_labor_paymentl_amount");
    var ad_tailor_total_amount = $("#ad_tailor_total_amount");
    var ad_tailor_start_date = $("#ad_tailor_start_date");
    var ad_tailor_end_date = $("#ad_tailor_end_date");
    var ad_tailor_number_people = $("#ad_tailor_number_people");
    var ad_sewing_total_amount = $("#ad_sewing_total_amount");
    var ad_sewing_start_date = $("#ad_sewing_start_date");
    var ad_sewing_end_date = $("#ad_sewing_end_date");
    var ad_sewing_number_people = $("#ad_sewing_number_people");
    var ad_iron_total_amount = $("#ad_iron_total_amount");
    var ad_iron_start_date = $("#ad_iron_start_date");
    var ad_iron_end_date = $("#ad_iron_end_date");
    var ad_iron_number_people = $("#ad_iron_number_people");
    ad_tailor_start_date.change(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_tailor_start_date.keyup(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_tailor_end_date.change(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_tailor_end_date.keyup(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_tailor_number_people.change(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_tailor_number_people.keyup(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_sewing_start_date.change(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_sewing_start_date.keyup(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_sewing_end_date.change(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_sewing_end_date.keyup(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_sewing_number_people.change(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_sewing_number_people.keyup(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_iron_start_date.change(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_iron_start_date.keyup(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_iron_end_date.change(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_iron_end_date.keyup(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_iron_number_people.change(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
    ad_iron_number_people.keyup(function () {
        labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,);
    });
}

function labor_payment(ad_labor_paymentl_amount, ad_tailor_total_amount, ad_tailor_start_date, ad_tailor_end_date, ad_tailor_number_people, ad_sewing_total_amount, ad_sewing_start_date, ad_sewing_end_date, ad_sewing_number_people, ad_iron_total_amount, ad_iron_start_date, ad_iron_end_date, ad_iron_number_people,) {
    var labor_paymentl;
    var tailor_total;
    var sewing_total;
    var iron_total;
    var ad_tailor_total_amount_val;
    var ad_tailor_start_date_val = ad_tailor_start_date.val();
    var ad_tailor_end_date_val = ad_tailor_end_date.val();
    var ad_tailor_number_people_val = ad_tailor_number_people.val();
    var ad_sewing_total_amount_val;
    var ad_sewing_start_date_val = ad_sewing_start_date.val();
    var ad_sewing_end_date_val = ad_sewing_end_date.val();
    var ad_sewing_number_people_val = ad_sewing_number_people.val();
    var ad_iron_total_amount_val;
    var ad_iron_start_date_val = ad_iron_start_date.val();
    var ad_iron_end_date_val = ad_iron_end_date.val();
    var ad_iron_number_people_val = ad_iron_number_people.val();
    if(ad_tailor_start_date_val && ad_tailor_end_date_val && ad_tailor_number_people_val){
        tailor_total = tsi_total(ad_tailor_start_date,ad_tailor_end_date,ad_tailor_number_people);
        ad_tailor_total_amount.val(parseFloat(tailor_total).toFixed(2));
    }
    if(ad_sewing_start_date_val && ad_sewing_end_date_val && ad_sewing_number_people_val){
        sewing_total = tsi_total(ad_sewing_start_date,ad_sewing_end_date,ad_sewing_number_people);
        ad_sewing_total_amount.val(parseFloat(sewing_total).toFixed(2));
    }
    if(ad_iron_start_date_val && ad_iron_end_date_val && ad_iron_number_people_val){
        iron_total = tsi_total(ad_iron_start_date,ad_iron_end_date,ad_iron_number_people);
        ad_iron_total_amount.val(parseFloat(iron_total).toFixed(2));
    }
    ad_tailor_total_amount_val = ad_tailor_total_amount.val();
    ad_sewing_total_amount_val = ad_sewing_total_amount.val();
    ad_iron_total_amount_val = ad_iron_total_amount.val();
    if(ad_tailor_total_amount_val && ad_sewing_total_amount_val && ad_iron_total_amount_val){
        labor_paymentl = parseFloat(ad_tailor_total_amount_val) + parseFloat(ad_sewing_total_amount_val) + parseFloat(ad_iron_total_amount_val);
        ad_labor_paymentl_amount.val(parseFloat(labor_paymentl).toFixed(2));
    }
}

function tsi_total(tsi_start,tsi_end,tsi_people) {
    var tsi_date;
    var tsi_total;
    var tsi_people_val = tsi_people.val();
    tsi_date = time_calculate(tsi_start,tsi_end);
    if(tsi_date > 0){
        tsi_start.parent().css("border","1px solid black");
        tsi_end.parent().css("border","1px solid black");
        $("#tsi-error").text("");
        tsi_total = tsi_date * 14.25 * parseFloat(tsi_people_val);
        return tsi_total;
    }else{
        $("#tsi-error").text(tsi_start.parent().parent().prev().children("div").children("b").text() + "和" + tsi_end.parent().parent().prev().children("div").children("b").text() + "的时间错误，请重新填写！");
        tsi_start.parent().css("border","1px solid red");
        tsi_end.parent().css("border","1px solid red");
        return 0
    }
}

function time_calculate(start,end) {
    var start_time = start.val();
    var end_time = end.val();
    if(start_time && end_time) {
        var start_date = new Date(Date.parse(start_time.replace("-", "/").replace("-", "/"))).valueOf();
        var end_date = new Date(Date.parse(end_time.replace("-", "/").replace("-", "/"))).valueOf();
        var use_date = (end_date - start_date) / 3600000;
        return use_date
    }else{
        return 0
    }
}
function packaging_shipping_main() {
    // 包装船务计算
    var ad_packaging_shipping_amount = $("#ad_packaging_shipping_amount");
    var ad_paperboard_amount = $("#ad_paperboard_amount");
    var ad_physical_distribution_amount = $("#ad_physical_distribution_amount");
    var ad_warehouse_entry_amount = $("#ad_warehouse_entry_amount");
    var ad_customs_declaration_amount = $("#ad_customs_declaration_amount");
    ad_paperboard_amount.change(function () {
        packaging_shipping(ad_packaging_shipping_amount,ad_paperboard_amount,ad_physical_distribution_amount,ad_warehouse_entry_amount,ad_customs_declaration_amount);
    });
    ad_paperboard_amount.keyup(function () {
        packaging_shipping(ad_packaging_shipping_amount,ad_paperboard_amount,ad_physical_distribution_amount,ad_warehouse_entry_amount,ad_customs_declaration_amount);
    });
    ad_physical_distribution_amount.change(function () {
        packaging_shipping(ad_packaging_shipping_amount,ad_paperboard_amount,ad_physical_distribution_amount,ad_warehouse_entry_amount,ad_customs_declaration_amount);
    });
    ad_physical_distribution_amount.keyup(function () {
        packaging_shipping(ad_packaging_shipping_amount,ad_paperboard_amount,ad_physical_distribution_amount,ad_warehouse_entry_amount,ad_customs_declaration_amount);
    });
    ad_warehouse_entry_amount.change(function () {
        packaging_shipping(ad_packaging_shipping_amount,ad_paperboard_amount,ad_physical_distribution_amount,ad_warehouse_entry_amount,ad_customs_declaration_amount);
    });
    ad_warehouse_entry_amount.keyup(function () {
        packaging_shipping(ad_packaging_shipping_amount,ad_paperboard_amount,ad_physical_distribution_amount,ad_warehouse_entry_amount,ad_customs_declaration_amount);
    });
    ad_customs_declaration_amount.change(function () {
        packaging_shipping(ad_packaging_shipping_amount,ad_paperboard_amount,ad_physical_distribution_amount,ad_warehouse_entry_amount,ad_customs_declaration_amount);
    });
    ad_customs_declaration_amount.keyup(function () {
        packaging_shipping(ad_packaging_shipping_amount,ad_paperboard_amount,ad_physical_distribution_amount,ad_warehouse_entry_amount,ad_customs_declaration_amount);
    });
}

function packaging_shipping(ad_packaging_shipping_amount,ad_paperboard_amount,ad_physical_distribution_amount,ad_warehouse_entry_amount,ad_customs_declaration_amount) {
    var ad_packaging_shipping_amount_val;
    var ad_paperboard_amount_val = ad_paperboard_amount.val();
    var ad_physical_distribution_amount_val = ad_physical_distribution_amount.val();
    var ad_warehouse_entry_amount_val = ad_warehouse_entry_amount.val();
    var ad_customs_declaration_amount_val = ad_customs_declaration_amount.val();
    if(ad_paperboard_amount_val && ad_physical_distribution_amount_val && ad_warehouse_entry_amount_val && ad_customs_declaration_amount_val){
        ad_packaging_shipping_amount_val = parseFloat(ad_paperboard_amount_val) + parseFloat(ad_physical_distribution_amount_val) + parseFloat(ad_warehouse_entry_amount_val) + parseFloat(ad_customs_declaration_amount_val);
        ad_packaging_shipping_amount.val(parseFloat(ad_packaging_shipping_amount_val).toFixed(2));
    }
}

function embroide_print_main() {
    // 绣印花计算
    var ad_embroide_print_amount = $("#ad_embroide_print_amount");
    var ad_water_washing_amount = $("#ad_water_washing_amount");
    var ad_embroide_amount = $("#ad_embroide_amount");
    var ad_print_amount = $("#ad_print_amount");
    ad_water_washing_amount.change(function () {
        embroide_print(ad_embroide_print_amount,ad_water_washing_amount,ad_embroide_amount,ad_print_amount);
    });
    ad_water_washing_amount.keyup(function () {
        embroide_print(ad_embroide_print_amount,ad_water_washing_amount,ad_embroide_amount,ad_print_amount);
    });
    ad_embroide_amount.change(function () {
        embroide_print(ad_embroide_print_amount,ad_water_washing_amount,ad_embroide_amount,ad_print_amount);
    });
    ad_embroide_amount.keyup(function () {
        embroide_print(ad_embroide_print_amount,ad_water_washing_amount,ad_embroide_amount,ad_print_amount);
    });
    ad_print_amount.change(function () {
        embroide_print(ad_embroide_print_amount,ad_water_washing_amount,ad_embroide_amount,ad_print_amount);
    });
    ad_print_amount.keyup(function () {
        embroide_print(ad_embroide_print_amount,ad_water_washing_amount,ad_embroide_amount,ad_print_amount);
    });
}

function embroide_print(ad_embroide_print_amount,ad_water_washing_amount,ad_embroide_amount,ad_print_amount) {
    var ad_embroide_print_amount_val;
    var ad_water_washing_amount_val = ad_water_washing_amount.val();
    var ad_embroide_amount_val = ad_embroide_amount.val();
    var ad_print_amount_val = ad_print_amount.val();
    if(ad_water_washing_amount_val && ad_embroide_amount_val &&ad_print_amount_val){
        ad_embroide_print_amount_val = parseFloat(ad_water_washing_amount_val) + parseFloat(ad_embroide_amount_val) + parseFloat(ad_print_amount_val);
        ad_embroide_print_amount.val(parseFloat(ad_embroide_print_amount_val).toFixed(2));
    }
}

function fabric_ingredient_main() {
    // 面辅料计算
    var ad_fabric_ingredients_total_amount = $("#ad_fabric_ingredients_total_amount");
    var ad_fabric_amount = $("#ad_fabric_amount");
    var ad_fabric_express_amount = $("#ad_fabric_express_amount");
    var ad_bonding_amount = $("#ad_bonding_amount");
    var ad_ingredients_amount = $("#ad_ingredients_amount");
    var ad_ingredients_express_amount = $("#ad_ingredients_express_amount");
    var ad_fabric_ingredients_other_amount = $("#ad_fabric_ingredients_other_amount");
    ad_fabric_amount.change(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_fabric_amount.keyup(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_fabric_express_amount.change(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_fabric_express_amount.keyup(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_bonding_amount.change(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_bonding_amount.keyup(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_ingredients_amount.change(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_ingredients_amount.keyup(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_ingredients_express_amount.change(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_ingredients_express_amount.keyup(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_fabric_ingredients_other_amount.change(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
    ad_fabric_ingredients_other_amount.keyup(function () {
        fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount);
    });
}

function fabric_ingredient(ad_fabric_ingredients_total_amount,ad_fabric_amount,ad_fabric_express_amount,ad_bonding_amount,ad_ingredients_amount,ad_ingredients_express_amount,ad_fabric_ingredients_other_amount) {
    var ad_fabric_ingredients_total_amount_val;
    var ad_fabric_amount_val = ad_fabric_amount.val();
    var ad_fabric_express_amount_val = ad_fabric_express_amount.val();
    var ad_bonding_amount_val = ad_bonding_amount.val();
    var ad_ingredients_amountt_val = ad_ingredients_amount.val();
    var ad_ingredients_express_amount_val = ad_ingredients_express_amount.val();
    var ad_fabric_ingredients_other_amount_val = ad_fabric_ingredients_other_amount.val();
    if(ad_fabric_amount_val && ad_fabric_express_amount_val && ad_bonding_amount_val && ad_ingredients_amountt_val && ad_ingredients_express_amount_val && ad_fabric_ingredients_other_amount_val){
        ad_fabric_ingredients_total_amount_val = parseFloat(ad_fabric_amount_val) + parseFloat(ad_fabric_express_amount_val) + parseFloat(ad_bonding_amount_val) + parseFloat(ad_ingredients_amountt_val) + parseFloat(ad_ingredients_express_amount_val) + parseFloat(ad_fabric_ingredients_other_amount_val);
        ad_fabric_ingredients_total_amount.val(parseFloat(ad_fabric_ingredients_total_amount_val).toFixed(2));
    }
}

function calculate_profit_main() {
    // 利润计算
    var pi_amount = $("#pi_amount");
    var pi_unit_price = $("#pi_unit_price");
    var pi_total_price = $("#pi_total_price");
    var ad_total_profit = $("#ad_total_profit");

    var ad_fabric_ingredients_total_amount = $("#ad_fabric_ingredients_total_amount");
    var ad_fabric_amount = $("#ad_fabric_amount");
    var ad_fabric_express_amount = $("#ad_fabric_express_amount");
    var ad_bonding_amount = $("#ad_bonding_amount");
    var ad_ingredients_amount = $("#ad_ingredients_amount");
    var ad_ingredients_express_amount = $("#ad_ingredients_express_amount");
    var ad_fabric_ingredients_other_amount = $("#ad_fabric_ingredients_other_amount");

    var ad_labor_paymentl_amount = $("#ad_labor_paymentl_amount");
    var ad_tailor_start_date = $("#ad_tailor_start_date");
    var ad_tailor_end_date = $("#ad_tailor_end_date");
    var ad_tailor_number_people = $("#ad_tailor_number_people");
    var ad_sewing_start_date = $("#ad_sewing_start_date");
    var ad_sewing_end_date = $("#ad_sewing_end_date");
    var ad_sewing_number_people = $("#ad_sewing_number_people");
    var ad_iron_start_date = $("#ad_iron_start_date");
    var ad_iron_end_date = $("#ad_iron_end_date");
    var ad_iron_number_people = $("#ad_iron_number_people");

    var ad_embroide_print_amount = $("#ad_embroide_print_amount");
    var ad_water_washing_amount = $("#ad_water_washing_amount");
    var ad_embroide_amount = $("#ad_embroide_amount");
    var ad_print_amount = $("#ad_print_amount");

    var ad_packaging_shipping_amount = $("#ad_packaging_shipping_amount");
    var ad_paperboard_amount = $("#ad_paperboard_amount");
    var ad_physical_distribution_amount = $("#ad_physical_distribution_amount");
    var ad_warehouse_entry_amount = $("#ad_warehouse_entry_amount");
    var ad_customs_declaration_amount = $("#ad_customs_declaration_amount");
    //价格的数量和单价变化时
    pi_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    pi_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    pi_unit_price.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    pi_unit_price.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    //面辅料各个价格变化时
    ad_fabric_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_fabric_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_fabric_express_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_fabric_express_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_bonding_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_bonding_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_ingredients_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_ingredients_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_ingredients_express_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_ingredients_express_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_fabric_ingredients_other_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_fabric_ingredients_other_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    // 工缴变化时
    ad_tailor_start_date.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_tailor_start_date.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_tailor_end_date.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_tailor_end_date.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_tailor_number_people.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_tailor_number_people.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_sewing_start_date.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_sewing_start_date.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_sewing_end_date.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_sewing_end_date.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_sewing_number_people.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_sewing_number_people.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_iron_start_date.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_iron_start_date.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_iron_end_date.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_iron_end_date.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_iron_number_people.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_iron_number_people.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    // 绣印花变化时
    ad_water_washing_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_water_washing_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_embroide_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_embroide_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_print_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_print_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    // 包装变化时
    ad_paperboard_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_paperboard_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_physical_distribution_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_physical_distribution_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_warehouse_entry_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_warehouse_entry_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_customs_declaration_amount.change(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });
    ad_customs_declaration_amount.keyup(function () {
        calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount)
    });

}
function calculate_profit(pi_total_price,ad_total_profit,ad_fabric_ingredients_total_amount,ad_labor_paymentl_amount,ad_embroide_print_amount,ad_packaging_shipping_amount) {
    var pi_total_price_val = pi_total_price.val();
    var ad_fabric_ingredients_total_amount_val = ad_fabric_ingredients_total_amount.val();
    var ad_labor_paymentl_amount_val = ad_labor_paymentl_amount.val();
    var ad_embroide_print_amount_val = ad_embroide_print_amount.val();
    var ad_packaging_shipping_amount_val = ad_packaging_shipping_amount.val();
    var ad_total_profit_val;
    if(pi_total_price_val && ad_fabric_ingredients_total_amount_val && ad_labor_paymentl_amount_val && ad_embroide_print_amount_val && ad_packaging_shipping_amount_val){
        ad_total_profit_val = parseFloat(pi_total_price_val) - parseFloat(ad_fabric_ingredients_total_amount_val) - parseFloat(ad_labor_paymentl_amount_val) - parseFloat(ad_embroide_print_amount_val) - parseFloat(ad_packaging_shipping_amount_val)
        ad_total_profit.val(parseFloat(ad_total_profit_val).toFixed(2));
    }
}