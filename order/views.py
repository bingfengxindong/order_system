from django.shortcuts import render,HttpResponse,redirect
from django.views.generic.base import View
from .models import *
from user.models import *
from create_order import CreateOrder
# Create your views here.

class OrderAdd(View):
    def get(self,request):
        customers = Customer.objects.all()
        users = User.objects.all()
        capcolors = CapColor.objects.all()
        captypes = CapType.objects.all()
        embroiderorprints = EmbroiderOrPrint.objects.all()
        capeyebrows = CapEyebrow.objects.all()
        versionnumbers = VersionNumber.objects.all()
        afterdeductions = AfterDeduction.objects.all()
        context = {
            "title":"订单添加",
            "customers":customers,
            "users":users,
            "capcolors":capcolors,
            "captypes":captypes,
            "embroiderorprints":embroiderorprints,
            "capeyebrows":capeyebrows,
            "versionnumbers":versionnumbers,
            "afterdeductions":afterdeductions,
        }
        return render(request=request,template_name="orderadd.html",context=context)

    def post(self,request):
        createorder = CreateOrder()
        customer_pk = request.POST.get("c_name").split(",")[2]
        o_customer_number = request.POST.get("o_customer_number")
        order = createorder.createorder(customer_pk = customer_pk,
                                        o_customer_number=o_customer_number,)

        o_date = request.POST.get("o_date")
        o_count = request.POST.get("o_count")
        o_image = request.FILES.get("o_image")
        o_file = request.FILES.get("o_file")
        o_main_fabric = request.POST.get("o_main_fabric")
        o_ps_price = request.POST.get("o_ps_price")
        o_dollar_exchange_rate = request.POST.get("o_dollar_exchange_rate")
        o_dollar_price = request.POST.get("o_dollar_price")
        o_ps_amount = request.POST.get("o_ps_amount")
        o_ps_dollar_total_price = request.POST.get("o_ps_dollar_total_price")
        o_delivery_date = request.POST.get("o_delivery_date")
        createorder.addorderinfo(order = order,
                                 o_date = o_date,
                                 o_count = o_count,
                                 o_image = o_image,
                                 o_file = o_file,
                                 o_main_fabric = o_main_fabric,
                                 o_ps_price = o_ps_price,
                                 o_dollar_exchange_rate = o_dollar_exchange_rate,
                                 o_dollar_price = o_dollar_price,
                                 o_ps_amount = o_ps_amount,
                                 o_ps_dollar_total_price = o_ps_dollar_total_price,
                                 o_delivery_date = o_delivery_date,
                                 )

        user_pk = request.POST.get("user")
        if user_pk:
            createorder.add_user(order,user_pk)

        capcolor_pks = request.POST.getlist("capcolor")
        if len(capcolor_pks) != 0:
            createorder.add_capcolor(order,capcolor_pks)

        captype_pk = request.POST.get("captype")
        if captype_pk:
            createorder.add_captype(order,captype_pk)

        embroidererprint_pk = request.POST.get("embroidererprint")
        if embroidererprint_pk:
            createorder.add_embroidererprint(order,embroidererprint_pk)

        capeyebrow_pk = request.POST.get("capeyebrow")
        if capeyebrow_pk:
            createorder.add_capeyebrow(order,capeyebrow_pk)

        versionnumber_pk = request.POST.get("versionnumber")
        if versionnumber_pk:
            createorder.add_versionnumber(order,versionnumber_pk)

        afterdeduction_pk = request.POST.get("afterdeduction")
        if afterdeduction_pk:
            createorder.add_afterdeduction(order,afterdeduction_pk)

        order.save()
        return redirect("/order/orderlist")

class OrderList(View):
    def get(self,request):
        orders = Order.objects.all()
        context = {
            "title": "订单列表",
            "orders": orders,
        }
        return render(request=request,template_name="orderlist.html",context=context)

class OrderDetail(View):
    def get(self,request):
        context = {
            "title": "订单详情",
        }
        return render(request=request,template_name="orderdetail.html",context=context)

class OrderEdit(View):
    def get(self,request):
        context = {
            "title": "订单修改",
        }
        return render(request=request,template_name="orderedit.html",context=context)