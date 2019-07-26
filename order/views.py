from django.shortcuts import render, redirect
from django.views.generic.base import View
from order.models import *
from user.models import *
from proofing_progress.models import ProofingProgress,ModifyOpinion
from production_schedule.models import ProductionSchedule
from quotation.models import Quotation
from accounting_documents.models import AccountingDocuments
from order.create_order import CreateOrder
from user.views import login_verify
import uuid

def order_add(request,order,createorder):
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
    createorder.addorderinfo(order=order,
                             o_date=o_date,
                             o_count=o_count,
                             o_image=o_image,
                             o_file=o_file,
                             o_main_fabric=o_main_fabric,
                             o_ps_price=o_ps_price,
                             o_dollar_exchange_rate=o_dollar_exchange_rate,
                             o_dollar_price=o_dollar_price,
                             o_ps_amount=o_ps_amount,
                             o_ps_dollar_total_price=o_ps_dollar_total_price,
                             o_delivery_date=o_delivery_date,
                             )

    user_pk = request.POST.get("user")
    if user_pk:
        createorder.add_user(order, user_pk)

    capcolor_pks = request.POST.getlist("capcolor")
    order.o_capcolor.clear()
    if len(capcolor_pks) != 0:
        createorder.add_capcolor(order, capcolor_pks)

    captype_pk = request.POST.get("captype")
    if captype_pk:
        createorder.add_captype(order, captype_pk)

    embroidererprint_pk = request.POST.get("embroidererprint")
    if embroidererprint_pk:
        createorder.add_embroidererprint(order, embroidererprint_pk)

    capeyebrow_pk = request.POST.get("capeyebrow")
    if capeyebrow_pk:
        createorder.add_capeyebrow(order, capeyebrow_pk)

    versionnumber_pk = request.POST.get("versionnumber")
    if versionnumber_pk:
        createorder.add_versionnumber(order, versionnumber_pk)

    afterdeduction_pk = request.POST.get("afterdeduction")
    if afterdeduction_pk:
        createorder.add_afterdeduction(order, afterdeduction_pk)

    order.save()

class OrderAdd(View):
    @login_verify
    def get(self,request):
        customers = Customer.objects.all()
        users = User.objects.all()
        capcolors = CapColor.objects.all()
        captypes = CapType.objects.all()
        embroiderorprints = EmbroiderOrPrint.objects.all()
        capeyebrows = CapEyebrow.objects.all()
        versionnumbers = VersionNumber.objects.all()
        afterdeductions = AfterDeduction.objects.all()
        user = User.objects.get(pk=request.session["user"])
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
            "user":user,
        }
        return render(request=request,template_name="orderadd.html",context=context)

    def post(self,request):
        createorder = CreateOrder()
        customer_pk = request.POST.get("c_name").split(",")[2]
        o_customer_number = request.POST.get("o_customer_number")
        order = createorder.createorder(customer_pk = customer_pk,
                                        o_customer_number=o_customer_number,)
        order.o_proofingprogress.add(ProofingProgress.objects.create(pp_id=uuid.uuid1()))
        order.o_modifyopinion = ModifyOpinion.objects.create(mo_id=uuid.uuid1())
        order.o_productionschedule = ProductionSchedule.objects.create(ps_id=uuid.uuid1())
        order.o_quotation = Quotation.objects.create(q_id=uuid.uuid1())
        order.o_accountingdocuments = AccountingDocuments.objects.create(ad_id=uuid.uuid1())
        order_add(request,order,createorder)
        return redirect("/order/orderlist")

class OrderList(View):
    @login_verify
    def get(self,request):
        orders = Order.objects.all().order_by("-pk")
        orders_len = len(orders)
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "订单列表",
            "orders": orders,
            "orders_len": orders_len,
            "user": user,
        }
        return render(request=request,template_name="orderlist.html",context=context)

class OrderDetail(View):
    @login_verify
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        proofingprogress_len = len(order.o_proofingprogress.all())
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "订单详情",
            "order": order,
            "proofingprogress_len": proofingprogress_len,
            "user": user,
        }
        return render(request=request,template_name="orderdetail.html",context=context)

class OrderEdit(View):
    @login_verify
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        customers = Customer.objects.all()
        users = User.objects.all()
        capcolors = CapColor.objects.all()
        captypes = CapType.objects.all()
        embroiderorprints = EmbroiderOrPrint.objects.all()
        capeyebrows = CapEyebrow.objects.all()
        versionnumbers = VersionNumber.objects.all()
        afterdeductions = AfterDeduction.objects.all()
        proofingprogresses_len = len(order.o_proofingprogress.all())
        proofingprogress = order.o_proofingprogress.all().order_by("-pk")[0] if proofingprogresses_len > 0 else None
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "订单修改",
            "order": order,
            "customers": customers,
            "users": users,
            "capcolors": capcolors,
            "captypes": captypes,
            "embroiderorprints": embroiderorprints,
            "capeyebrows": capeyebrows,
            "versionnumbers": versionnumbers,
            "afterdeductions": afterdeductions,
            "proofingprogresses_len": proofingprogresses_len,
            "proofingprogress": proofingprogress,
            "user": user,
        }
        return render(request=request,template_name="orderedit.html",context=context)

    def post(self,request):
        pk = request.POST.get("pk")
        order = Order.objects.get(pk=pk)
        createorder = CreateOrder()

        customer = request.POST.get("c_name")
        if customer:
            createorder.edit_customer(order,customer.split(",")[2])

        o_customer_number = request.POST.get("o_customer_number")
        if o_customer_number:
            createorder.edit_customer_number(order,o_customer_number)

        order_add(request, order, createorder)
        return redirect("/order/orderdetail?pk={}".format(pk))

class EndOrder(View):
    @login_verify
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        order.o_end = True
        order.save()
        return redirect("/order/orderdetail?pk={}".format(pk))