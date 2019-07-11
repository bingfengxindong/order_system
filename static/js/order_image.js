function order_image() {
    var image = $("#o_image");
    var files;
    image.click();
    image.on("change",function () {
        file = this.files[0];
        var img_type = file.type;
        if(img_type == "image/jpeg" || img_type == "image/jpg" || img_type == "image/png") {
            var url = getObjectURL(file);
            if (url) {
                $("#order-image").html(
                    `
                        <img src="` + url + `">
                    `
                );
                $("#image-button").html(
                    `
                        <a class="btn btn-default" onclick="cancel_image()">取消</a>
                    `
                )
            }
        }else{
            alert("仅支持png和jpg格式的图片！");
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
    var o_image = $("#o_image");
    var order_image = $("#order-image");
    var image_button = $("#image-button");
    var o_img = $("#o_img").val();
    o_image.val(null);
    if(o_img){
        order_image.html(
             `
                <img src="`+ o_img +`">
            `
        );
    }else{
        order_image.html(
             `
                <b>请添加图片</b>
            `
        );
    }
    image_button.html(
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