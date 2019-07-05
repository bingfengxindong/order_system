$(function () {
    materials_main();
    labor_payment_main();
    embroide_print_main();
    packaging_shipping_main();
    calculate_profit_main();
});
// 面辅料总金额计算
function materials_main() {
    var ad_total_amount_materials = $("#ad_total_amount_materials");
    var ad_total_amount_fabric = $("#ad_total_amount_fabric");
    var ad_total_amount_fabric_express = $("#ad_total_amount_fabric_express");
    var ad_total_amount_bonding = $("#ad_total_amount_bonding");
    var ad_total_amount_ingredients = $("#ad_total_amount_ingredients");
    var ad_total_amount_ingredients_express = $("#ad_total_amount_ingredients_express");
    var ad_total_amount_other = $("#ad_total_amount_other");

    ad_total_amount_fabric.change(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_fabric.keyup(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_fabric_express.change(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_fabric_express.keyup(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_bonding.change(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_bonding.keyup(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_ingredients.change(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_ingredients.keyup(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_ingredients_express.change(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_ingredients_express.keyup(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_other.change(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
    ad_total_amount_other.keyup(function () {
        materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other)
    });
}

function materials(ad_total_amount_materials,ad_total_amount_fabric,ad_total_amount_fabric_express,ad_total_amount_bonding,ad_total_amount_ingredients,ad_total_amount_ingredients_express,ad_total_amount_other) {
    var ad_total_amount_materials_val;
    var ad_total_amount_fabric_val = ad_total_amount_fabric.val();
    var ad_total_amount_fabric_express_val = ad_total_amount_fabric_express.val();
    var ad_total_amount_bonding_val = ad_total_amount_bonding.val();
    var ad_total_amount_ingredients_val = ad_total_amount_ingredients.val();
    var ad_total_amount_ingredients_express_val = ad_total_amount_ingredients_express.val();
    var ad_total_amount_other_val = ad_total_amount_other.val();
    if(ad_total_amount_fabric_val && ad_total_amount_fabric_express_val && ad_total_amount_bonding_val && ad_total_amount_ingredients_val && ad_total_amount_ingredients_express_val && ad_total_amount_other_val){
        ad_total_amount_materials_val = parseFloat(ad_total_amount_fabric_val) + parseFloat(ad_total_amount_fabric_express_val) + parseFloat(ad_total_amount_bonding_val) + parseFloat(ad_total_amount_ingredients_val) + parseFloat(ad_total_amount_ingredients_express_val) + parseFloat(ad_total_amount_other_val);
        ad_total_amount_materials.val(ad_total_amount_materials_val.toFixed(2));
        actual_cost();
    }
}

// 工缴金额计算
function labor_payment_main() {
    var ad_labor_paymentl_amount = $("#ad_total_amount_labor_payment");
    var ad_tailor_total_amount = $("#ad_total_amount_tailor");
    var ad_tailor_start_date = $("#ad_tailor_start_date");
    var ad_tailor_end_date = $("#ad_tailor_end_date");
    var ad_tailor_number_people = $("#ad_tailor_number_people");
    var ad_sewing_total_amount = $("#ad_total_amount_sewing");
    var ad_sewing_start_date = $("#ad_sewing_start_date");
    var ad_sewing_end_date = $("#ad_sewing_end_date");
    var ad_sewing_number_people = $("#ad_sewing_number_people");
    var ad_iron_total_amount = $("#ad_total_amount_iron");
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
        actual_cost();
    }
}

function tsi_total(tsi_start,tsi_end,tsi_people) {
    var tsi_date;
    var tsi_total;
    var tsi_people_val = tsi_people.val();
    tsi_date = time_calculate(tsi_start,tsi_end);
    if(tsi_date > 0){
        tsi_start.parent().css("border","none");
        tsi_end.parent().css("border","none");
        $("#tsi-error").text("");
        tsi_total = tsi_date * 14.25 * parseFloat(tsi_people_val);
        return tsi_total;
    }else{
        $("#tsi-error").text(tsi_start.prev().children("span").text() + "和" + tsi_end.prev().children("span").text() + "的时间错误，请重新填写！");
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

// 实际绣印花金额计算
function embroide_print_main() {
    // 绣印花计算
    var ad_embroide_print_amount = $("#ad_total_amount_embroide_print");
    var ad_water_washing_amount = $("#ad_total_amount_water_washing");
    var ad_embroide_amount = $("#ad_total_amount_embroide");
    var ad_print_amount = $("#ad_total_amount_print");
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
        actual_cost();
    }
}

// 实际包装船务金额计算
function packaging_shipping_main() {
    // 包装船务计算
    var ad_packaging_shipping_amount = $("#ad_total_amount_packaging_shipping");
    var ad_paperboard_amount = $("#ad_total_amount_paperboard");
    var ad_physical_distribution_amount = $("#ad_total_amount_physical_distribution");
    var ad_warehouse_entry_amount = $("#ad_total_amount_warehouse_entry");
    var ad_customs_declaration_amount = $("#ad_total_amount_customs_declaration");
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
        actual_cost();
    }
}

// 实际成本计算
function actual_cost() {
    var ad_actual_cost = $("#ad_actual_cost");
    var ad_total_amount_materials_val = $("#ad_total_amount_materials").val();
    var ad_total_amount_labor_payment_val = $("#ad_total_amount_labor_payment").val();
    var ad_total_amount_embroide_print_val = $("#ad_total_amount_embroide_print").val();
    var ad_total_amount_packaging_shipping_val = $("#ad_total_amount_packaging_shipping").val();
    if(ad_total_amount_materials_val && ad_total_amount_labor_payment_val && ad_total_amount_embroide_print_val && ad_total_amount_packaging_shipping_val){
        ad_actual_cost.val((parseFloat(ad_total_amount_materials_val) + parseFloat(ad_total_amount_labor_payment_val) + parseFloat(ad_total_amount_embroide_print_val) + parseFloat(ad_total_amount_packaging_shipping_val)).toFixed(2));
    }
}

// 总利润计算
function calculate_profit_main() {
    // 利润计算
    var ad_ps_dollar_total_price = $("#ad_ps_dollar_total_price");
    var ad_actual_cost = $("#ad_actual_cost");
    var ad_total_profit = $("#ad_total_profit");

    var ad_fabric_amount = $("#ad_total_amount_fabric");
    var ad_fabric_express_amount = $("#ad_total_amount_fabric_express");
    var ad_bonding_amount = $("#ad_total_amount_bonding");
    var ad_ingredients_amount = $("#ad_total_amount_ingredients");
    var ad_ingredients_express_amount = $("#ad_total_amount_ingredients_express");
    var ad_fabric_ingredients_other_amount = $("#ad_total_amount_other");

    var ad_tailor_start_date = $("#ad_tailor_start_date");
    var ad_tailor_end_date = $("#ad_tailor_end_date");
    var ad_tailor_number_people = $("#ad_tailor_number_people");
    var ad_sewing_start_date = $("#ad_sewing_start_date");
    var ad_sewing_end_date = $("#ad_sewing_end_date");
    var ad_sewing_number_people = $("#ad_sewing_number_people");
    var ad_iron_start_date = $("#ad_iron_start_date");
    var ad_iron_end_date = $("#ad_iron_end_date");
    var ad_iron_number_people = $("#ad_iron_number_people");

    var ad_water_washing_amount = $("#ad_total_amount_water_washing");
    var ad_embroide_amount = $("#ad_total_amount_embroide");
    var ad_print_amount = $("#ad_total_amount_print");

    var ad_paperboard_amount = $("#ad_total_amount_paperboard");
    var ad_physical_distribution_amount = $("#ad_total_amount_physical_distribution");
    var ad_warehouse_entry_amount = $("#ad_total_amount_warehouse_entry");
    var ad_customs_declaration_amount = $("#ad_total_amount_customs_declaration");
    //面辅料各个价格变化时
    ad_fabric_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_fabric_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_fabric_express_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_fabric_express_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_bonding_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_bonding_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_ingredients_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_ingredients_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_ingredients_express_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_ingredients_express_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_fabric_ingredients_other_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_fabric_ingredients_other_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    // 工缴变化时
    ad_tailor_start_date.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_tailor_start_date.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_tailor_end_date.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_tailor_end_date.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_tailor_number_people.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_tailor_number_people.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_sewing_start_date.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_sewing_start_date.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_sewing_end_date.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_sewing_end_date.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_sewing_number_people.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_sewing_number_people.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_iron_start_date.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_iron_start_date.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_iron_end_date.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_iron_end_date.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_iron_number_people.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_iron_number_people.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    // 绣印花变化时
    ad_water_washing_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_water_washing_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_embroide_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_embroide_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_print_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_print_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    // 包装变化时
    ad_paperboard_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_paperboard_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_physical_distribution_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_physical_distribution_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_warehouse_entry_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_warehouse_entry_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_customs_declaration_amount.change(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });
    ad_customs_declaration_amount.keyup(function () {
        calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit)
    });

}
function calculate_profit(ad_ps_dollar_total_price,ad_actual_cost,ad_total_profit) {
    var ad_ps_dollar_total_price_val = ad_ps_dollar_total_price.val();
    var ad_actual_cost_val = ad_actual_cost.val();
    var ad_total_profit_val;
    if(ad_ps_dollar_total_price_val && ad_actual_cost_val){
        ad_total_profit_val = parseFloat(ad_ps_dollar_total_price_val) - parseFloat(ad_actual_cost_val);
        ad_total_profit.val(parseFloat(ad_total_profit_val).toFixed(2));
    }
}