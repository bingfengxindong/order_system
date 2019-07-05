$(function () {
    q_calculation_main()
});
// 报价单计算
function q_calculation_main() {
    var q_floating_rate = $("#q_floating_rate");
    var q_fabric_quotation = $("#q_fabric_quotation");
    var q_ingredients_quotation = $("#q_ingredients_quotation");
    var q_labor_payment_quotation = $("#q_labor_payment_quotation");
    var q_water_washing_quotation = $("#q_water_washing_quotation");
    var q_embroider_quotation = $("#q_embroider_quotation");
    var q_print_quotation = $("#q_print_quotation");
    var q_packaging_quotation = $("#q_packaging_quotation");
    var q_other_quotation = $("#q_other_quotation");
    var q_reserved_profits = $("#q_reserved_profits");

    q_floating_rate.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_floating_rate.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_fabric_quotation.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_fabric_quotation.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_ingredients_quotation.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_ingredients_quotation.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_labor_payment_quotation.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_labor_payment_quotation.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_water_washing_quotation.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_water_washing_quotation.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_embroider_quotation.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_embroider_quotation.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_print_quotation.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_print_quotation.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_packaging_quotation.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_packaging_quotation.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_other_quotation.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_other_quotation.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_reserved_profits.change(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
    q_reserved_profits.keyup(function () {
        q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits)
    });
}

function q_calculation(q_floating_rate,q_fabric_quotation,q_ingredients_quotation,q_labor_payment_quotation,q_water_washing_quotation,q_embroider_quotation,q_print_quotation,q_packaging_quotation,q_other_quotation,q_reserved_profits) {
    var q_price;
    var q_offer;
    var q_end_offer;
    var q_floating_rate_val = q_floating_rate.val();
    var q_fabric_quotation_val = q_fabric_quotation.val();
    var q_ingredients_quotation_val = q_ingredients_quotation.val();
    var q_labor_payment_quotation_val = q_labor_payment_quotation.val();
    var q_water_washing_quotation_val = q_water_washing_quotation.val();
    var q_embroider_quotation_val = q_embroider_quotation.val();
    var q_print_quotation_val = q_print_quotation.val();
    var q_packaging_quotation_val = q_packaging_quotation.val();
    var q_other_quotation_val = q_other_quotation.val();
    var q_reserved_profits_val = q_reserved_profits.val();
    if(q_floating_rate_val&&q_fabric_quotation_val&&q_ingredients_quotation_val&&q_labor_payment_quotation_val&&q_water_washing_quotation_val&&q_embroider_quotation_val&&q_print_quotation_val&&q_packaging_quotation_val&&q_other_quotation_val&&q_reserved_profits_val){
        q_price = parseFloat(q_fabric_quotation_val) + parseFloat(q_ingredients_quotation_val) + parseFloat(q_labor_payment_quotation_val) + parseFloat(q_water_washing_quotation_val) + parseFloat(q_embroider_quotation_val) + parseFloat(q_print_quotation_val) + parseFloat(q_packaging_quotation_val) + parseFloat(q_other_quotation_val);
        q_offer = q_price * parseFloat(q_reserved_profits_val);
        $("#q_offer").val(q_offer.toFixed(2));
        q_end_offer = q_offer * parseFloat(q_floating_rate_val);
        $("#q_end_offer").val(q_end_offer.toFixed(2));
    }
}