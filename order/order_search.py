from django.shortcuts import render
from django.views.generic.base import View
from order.models import *

class OrderPP(View):
    def get(self,request):
        orders = Order.objects.filter(o_pp_all_end=False).order_by("-pk")
        orders_len = len(orders)
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "订单打样中",
            "orders": orders,
            "orders_len": orders_len,
            "user": user,
        }
        return render(request=request,template_name="orderlist.html",context=context)

class OrderPS(View):
    def get(self,request):
        orders = Order.objects.filter(o_pp_all_end=True,o_productionschedule__ps_end=False).order_by("-pk")
        orders_len = len(orders)
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "订单大货中",
            "orders": orders,
            "orders_len": orders_len,
            "user": user,
        }
        return render(request=request,template_name="orderlist.html",context=context)

class OrderO(View):
    def get(self,request):
        orders = Order.objects.filter(o_productionschedule__ps_end=True,o_end=False).order_by("-pk")
        orders_len = len(orders)
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "订单未完成",
            "orders": orders,
            "orders_len": orders_len,
            "user": user,
        }
        return render(request=request,template_name="orderlist.html",context=context)

class OrderEnd(View):
    def get(self,request):
        orders = Order.objects.filter(o_end=True).order_by("-pk")
        orders_len = len(orders)
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "订单已完成",
            "orders": orders,
            "orders_len": orders_len,
            "user": user,
        }
        return render(request=request,template_name="orderlist.html",context=context)