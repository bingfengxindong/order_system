function order_image() {
    var image = $("#o_image");
    var files;
    image.click();
    image.on("change",function () {
        files = this.files[0];
        var url = getObjectURL(files);
        if(url){
            $("#order-image").html(
                `
                    <img src="`+ url +`">
                `
            );
            $("#image-button").html(
                `
                    <a class="btn btn-default" onclick="cancel_image()">取消</a>
                `
            )
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
    $("#order-image").html(
         `
            <b>请添加图片</b>
        `
    );
    $("#image-button").html(
        `
            <a class="btn btn-default" onclick="order_image()">添加图片</a>
        `
    )
}
function upload_file() {
    var f = $("#o_file");
    var files;
    f.click();
    f.on("change",function () {
        files = this.files[0];
        var url = getObjectURL(files);
        if(url){
            $("#upload-file").val(files.name);
        }
    })
}