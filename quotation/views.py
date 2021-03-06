from django.shortcuts import render, redirect
from django.views.generic.base import View
from order.models import Order
from quotation.models import Quotation
from user.models import *
from quotation.create_q import CreateQ
from accounting_documents.models import AccountingDocuments
from user.views import login_verify
import uuid

def add_quotation(request,create_q,quotation,order):
    q_offer = request.POST.get("q_offer")
    if q_offer:
        create_q.add_q_offer(quotation, q_offer)

    q_floating_rate = request.POST.get("q_floating_rate")
    if q_floating_rate:
        create_q.add_q_floating_rate(quotation, q_floating_rate)

    q_end_offer = request.POST.get("q_end_offer")
    if q_end_offer:
        create_q.add_q_end_offer(quotation, q_end_offer)
        order.o_ps_price = q_end_offer
        order.o_dollar_price = "%.2f" % (float(q_end_offer) / float(order.o_dollar_exchange_rate))
        if order.o_ps_amount:
            order.o_ps_dollar_total_price = "%.2f" % (
                        float(q_end_offer) / float(order.o_dollar_exchange_rate) * float(order.o_ps_amount))
            accountingdocuments = order.o_accountingdocuments
            accountingdocuments.ad_ps_dollar_total_price = "%.2f" % (float(q_end_offer) * float(order.o_ps_amount))
            accountingdocuments.save()

    q_fabric_quotation = request.POST.get("q_fabric_quotation")
    if q_fabric_quotation:
        create_q.add_q_fabric_quotation(quotation, q_fabric_quotation)

    q_ingredients_quotation = request.POST.get("q_ingredients_quotation")
    if q_ingredients_quotation:
        create_q.add_q_ingredients_quotation(quotation, q_ingredients_quotation)

    q_labor_payment_quotation = request.POST.get("q_labor_payment_quotation")
    if q_labor_payment_quotation:
        create_q.add_q_labor_payment_quotation(quotation, q_labor_payment_quotation)

    q_water_washing_quotation = request.POST.get("q_water_washing_quotation")
    if q_water_washing_quotation:
        create_q.add_q_water_washing_quotation(quotation, q_water_washing_quotation)

    q_embroider_quotation = request.POST.get("q_embroider_quotation")
    if q_embroider_quotation:
        create_q.add_q_embroider_quotation(quotation, q_embroider_quotation)

    q_print_quotation = request.POST.get("q_print_quotation")
    if q_print_quotation:
        create_q.add_q_print_quotation(quotation, q_print_quotation)

    q_packaging_quotation = request.POST.get("q_packaging_quotation")
    if q_packaging_quotation:
        create_q.add_q_packaging_quotation(quotation, q_packaging_quotation)

    q_other_quotation = request.POST.get("q_other_quotation")
    if q_other_quotation:
        create_q.add_q_other_quotation(quotation, q_other_quotation)

    q_reserved_profits = request.POST.get("q_reserved_profits")
    if q_reserved_profits:
        create_q.add_q_reserved_profits(quotation, q_reserved_profits)

class QAdd(View):
    @login_verify
    def get(self,request):
        pk =  request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "报价单添加",
            "order": order,
            "user": user,
        }
        return render(request=request,template_name="qadd.html",context=context)

    def post(self,request):
        pk = request.POST.get("pk")
        order = Order.objects.get(pk=pk)
        create_q = CreateQ()
        quotation = create_q.add_quotation()
        add_quotation(request,create_q,quotation,order)
        quotation.save()
        order.o_quotation = quotation
        order.save()
        return redirect("/order/orderedit?pk={}".format(pk))

class QEdit(View):
    @login_verify
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "报价单修改",
            "order": order,
            "user": user,
        }
        return render(request=request,template_name="qedit.html",context=context)

    def post(self,request):
        pk = request.POST.get("pk")
        order = Order.objects.get(pk=pk)
        create_q = CreateQ()
        quotation = order.o_quotation
        add_quotation(request,create_q,quotation,order)
        quotation.save()
        order.save()
        return redirect("/order/orderedit?pk={}".format(pk))