from django.shortcuts import render,HttpResponse

def returnhttp(title,content):
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset{}</title>
    </head>
    <body>
        <p>{}</p><a href="{}">index</a>
    </body>
    </html>
    """.format(title,content,"/order/orderlist")

def page_not_found(request,exception):
    rt = returnhttp("404","HTTP 404- 无法找到文件！")
    return HttpResponse(rt)

def page_permission_denied(request,exception):
    rt = returnhttp("403","HTTP 403 - 禁止访问！")
    return HttpResponse(rt)

def page_inter_error(request,exception):
    rt = returnhttp("500", "HTTP 500 - 内部服务器错误！")
    return HttpResponse(rt)