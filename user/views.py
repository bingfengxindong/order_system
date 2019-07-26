from django.shortcuts import render,redirect
from django.views.generic.base import View
from .models import *

def login_verify(func):
    def login_ver(self,request):
        try:
            if not request.session["user"]:
                return redirect("/user/login")
        except KeyError:
            return redirect("/user/login")
        return func(self,request)
    return login_ver

class Login(View):
    def get(self,request):
        error = """<div class="ten_space" style="color:red;">账号密码错误，请重新输入！</div>""" if request.GET.get("error","") == "error" else ""
        context = {
            "title":"登录",
            "error":error,
        }
        return render(request=request,template_name="login.html",context=context)

    def post(self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        keep_login = request.POST.get("keep_login")
        user = User.objects.filter(u_username=username,u_password=password)
        if user.exists() and len(user) == 1:
            request.session["user"] = user[0].pk
            if not keep_login:
                request.session.set_expiry(0)
            return redirect("/order/orderlist")
        else:
            return redirect("/user/login?error=error")

class Logout(View):
    def get(self,request):
        request.session.clear()
        return redirect("/user/login")