$(function () {
    // 单据切换
    var pp = $("#pp");
    var pp_v = $("#pp-v");
    var mo = $("#mo");
    var mo_v = $("#mo-v");
    var ps = $("#ps");
    var ps_v = $("#ps-v");
    var q = $("#q");
    var q_v = $("#q-v");
    var ad = $("#ad");
    var ad_v = $("#ad-v");
    type_switch(pp,mo,ps,q,ad,pp_v,mo_v,ps_v,q_v,ad_v);
    type_switch(mo,pp,ps,q,ad,mo_v,pp_v,ps_v,q_v,ad_v);
    type_switch(ps,pp,mo,q,ad,ps_v,pp_v,mo_v,q_v,ad_v);
    type_switch(q,pp,mo,ps,ad,q_v,pp_v,mo_v,ps_v,ad_v);
    type_switch(ad,pp,mo,ps,q,ad_v,pp_v,mo_v,ps_v,q_v);

    // 打样切换
    var pp_ids = $("#pp-ids li");
    if(pp_ids.length > 1){
        if(pp_ids.length == 2){
            var a = $("#pp-1");
            var a_1 = $("#pp-11");
            var b = $("#pp-2");
            var b_1 = $("#pp-21");
            pp_swatch_2(a,b,a_1,b_1);
            pp_swatch_2(b,a,b_1,a_1);
        }else if(pp_ids.length == 3){
            var a = $("#pp-1");
            var a_1 = $("#pp-11");
            var b = $("#pp-2");
            var b_1 = $("#pp-21");
            var c = $("#pp-3");
            var c_1 = $("#pp-31");
            pp_swatch_3(a,b,c,a_1,b_1,c_1);
            pp_swatch_3(b,a,c,b_1,a_1,c_1);
            pp_swatch_3(c,a,b,c_1,a_1,b_1);
        }
    }
});

function type_switch(a,b,c,d,e,a_v,b_v,c_v,d_v,e_v) {
    a.click(function () {
        a.addClass("active");
        b.removeClass("active");
        c.removeClass("active");
        d.removeClass("active");
        e.removeClass("active");
        a_v.show();
        b_v.hide();
        c_v.hide();
        d_v.hide();
        e_v.hide();
    });
}

function pp_swatch_2(a,b,a_1,b_1) {
    a.click(function () {
        a.addClass("active");
        b.removeClass("active");
        a_1.show();
        b_1.hide();
    });
}
function pp_swatch_3(a,b,c,a_1,b_1,c_1) {
    a.click(function () {
        a.addClass("active");
        b.removeClass("active");
        c.removeClass("active");
        a_1.show();
        b_1.hide();
        c_1.hide();
    });
}