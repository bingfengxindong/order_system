$(function () {
    $("#proofing-progress-click").click(function () {
        $(this).attr("class","center-title-in-now");
        $("#production-schedule-click").attr("class","center-title-in");
        $("#proofing-progress").show();
        $("#production-schedule").hide();
    });
    $("#production-schedule-click").click(function () {
        $(this).attr("class","center-title-in-now");
        $("#proofing-progress-click").attr("class","center-title-in");
        $("#production-schedule").show();
        $("#proofing-progress").hide();
    });
});