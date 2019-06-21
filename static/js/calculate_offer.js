$(function () {
    calculate_offer_main();
});
function calculate_offer_main() {
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