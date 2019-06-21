from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from production_schedule.models import *

# Create your views here.
class PPSearch(View):
    def get(self,request):
        orders = [i for i in Order.objects.all() if len([j for j in i.o_proofingprogress.all() if j.pp_sample_order_date and not j.pp_sample_express_date]) != 0]
        orders = [{"pk": i.pk,
                   "o_image": i.o_image,
                   "o_number": i.o_number,
                   "o_user": i.o_user,
                   "o_price_type": i.o_price_type,
                   "o_productinfo": i.o_productinfo,
                   "o_customer": i.o_customer,
                   "o_capcolor": i.o_capcolor.all(),
                   "o_proofingprogress_number": i.o_proofingprogress_number,
                   "o_proofingprogress": i.o_proofingprogress.all().order_by("-pk")[0],
                   "o_productionschedule": i.o_productionschedule, } for i in orders]
        captypes = CapType.objects.all()
        users = User.objects.all()
        productionworkshops = ProductionWorkshop.objects.all()
        context = {
            "title": "订单列表",
            "orders": orders,
            "order_len": len(orders),
            "search_type": "s",
            "captypes": captypes,
            "users": users,
            "productionworkshops": productionworkshops,

            "captype_pk": 0,
            "user_pk": 0,
            "pw_workshop_pk": 0,
        }
        return render(request=request, template_name="orderlist.html", context=context)

class PSSearch(View):
    def get(self,request):
        orders = [i for i in Order.objects.all() if i.o_productionschedule.ps_order_date and not i.o_productionschedule.ps_outward_transport_date]
        orders = [{"pk": i.pk,
                   "o_image": i.o_image,
                   "o_number": i.o_number,
                   "o_user": i.o_user,
                   "o_price_type": i.o_price_type,
                   "o_productinfo": i.o_productinfo,
                   "o_customer": i.o_customer,
                   "o_capcolor": i.o_capcolor.all(),
                   "o_proofingprogress_number": i.o_proofingprogress_number,
                   "o_proofingprogress": i.o_proofingprogress.all().order_by("-pk")[0],
                   "o_productionschedule": i.o_productionschedule, } for i in orders]
        captypes = CapType.objects.all()
        users = User.objects.all()
        productionworkshops = ProductionWorkshop.objects.all()
        context = {
            "title": "订单列表",
            "orders": orders,
            "order_len": len(orders),
            "search_type": "s",
            "captypes": captypes,
            "users": users,
            "productionworkshops": productionworkshops,

            "captype_pk": 0,
            "user_pk": 0,
            "pw_workshop_pk": 0,
        }
        return render(request=request, template_name="orderlist.html", context=context)

class CPSearch(View):
    def get(self,request):
        orders = [i for i in Order.objects.all() if i.o_productionschedule.ps_outward_transport_date and not i.o_productionschedule.ps_gathering_date]
        orders = [{"pk": i.pk,
                   "o_image": i.o_image,
                   "o_number": i.o_number,
                   "o_user": i.o_user,
                   "o_price_type": i.o_price_type,
                   "o_productinfo": i.o_productinfo,
                   "o_customer": i.o_customer,
                   "o_capcolor": i.o_capcolor.all(),
                   "o_proofingprogress_number": i.o_proofingprogress_number,
                   "o_proofingprogress": i.o_proofingprogress.all().order_by("-pk")[0],
                   "o_productionschedule": i.o_productionschedule, } for i in orders]
        captypes = CapType.objects.all()
        users = User.objects.all()
        productionworkshops = ProductionWorkshop.objects.all()
        context = {
            "title": "订单列表",
            "orders": orders,
            "order_len": len(orders),
            "search_type": "s",
            "captypes": captypes,
            "users": users,
            "productionworkshops": productionworkshops,

            "captype_pk": 0,
            "user_pk": 0,
            "pw_workshop_pk": 0,
        }
        return render(request=request, template_name="orderlist.html", context=context)

class SCSearch(View):
    def get(self,request):
        pagenow = int(request.GET.get("pn", 1))
        order_date = request.GET.get("od")
        order_end_date = request.GET.get("oed")
        number = request.GET.get("on")
        customername = request.GET.get("cn")
        captype_pk = int(request.GET.get("cp", 0))
        user_pk = int(request.GET.get("up", 0))
        pw_workshop_pk = int(request.GET.get("pwp", 0))

        orders = Order.objects.filter()
        if order_date != "" and order_end_date != "":
            orders = Order.objects.filter(o_date__range=(order_date, order_end_date))
        if number != "":
            orders = [i for i in orders if number in i.o_number]
        if customername != "":
            orders = [i for i in orders if customername in i.o_customer.c_name]
        if captype_pk != 0:
            orders = [i for i in orders if i.o_captype.pk == captype_pk]
        if user_pk != 0:
            orders = [i for i in orders if i.o_user.pk == user_pk]
        if pw_workshop_pk != 0:
            orders = [i for i in orders if i.o_productionschedule.ps_workshop and i.o_productionschedule.ps_workshop.pk == pw_workshop_pk]
        orders = [{"pk": i.pk,
                   "o_image": i.o_image,
                   "o_number": i.o_number,
                   "o_user": i.o_user,
                   "o_price_type": i.o_price_type,
                   "o_productinfo": i.o_productinfo,
                   "o_customer": i.o_customer,
                   "o_capcolor": i.o_capcolor.all(),
                   "o_proofingprogress_number": i.o_proofingprogress_number,
                   "o_proofingprogress": i.o_proofingprogress.all().order_by("-pk")[0],
                   "o_productionschedule": i.o_productionschedule, } for i in orders]
        captypes = CapType.objects.all()
        users = User.objects.all()
        productionworkshops = ProductionWorkshop.objects.all()
        context = {
            "title": "订单列表",
            "orders": orders,
            "order_len": len(orders),
            "search_type": "s",
            "captypes": captypes,
            "users": users,
            "productionworkshops": productionworkshops,

            "order_date": order_date,
            "order_end_date": order_end_date,
            "number": number,
            "customername": customername,
            "captype_pk": captype_pk,
            "user_pk": user_pk,
            "pw_workshop_pk": pw_workshop_pk,
        }
        if captype_pk != 0:
            context["captype"] = CapType.objects.get(pk=captype_pk)
        if user_pk != 0:
            context["user"] = User.objects.get(pk=user_pk)
        if pw_workshop_pk != 0:
            context["pw_workshop"] = ProductionWorkshop.objects.get(pk=pw_workshop_pk)
        return render(request=request, template_name="orderlist.html", context=context)