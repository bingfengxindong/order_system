from django.shortcuts import render,HttpResponse,redirect
from django.views.generic.base import View
from order.models import *
from .create_pp import *
from .create_mo import *

def add_proofingprogress(request,create_pp,proofingprogress):
    pp_number = request.POST.get("pp_number")
    if pp_number:
        create_pp.add_pp_number(proofingprogress, pp_number)

    pp_erp_number = request.POST.get("pp_erp_number")
    if pp_erp_number:
        create_pp.add_pp_erp_number(proofingprogress, pp_erp_number)

    pp_date = request.POST.get("pp_date")
    if pp_date:
        create_pp.add_pp_date(proofingprogress, pp_date)

    pp_delivery_date = request.POST.get("pp_delivery_date")
    if pp_delivery_date:
        create_pp.add_pp_delivery_date(proofingprogress, pp_delivery_date)

    pp_main_fabric_arrival = request.POST.get("pp_main_fabric_arrival")
    if pp_main_fabric_arrival:
        create_pp.add_pp_main_fabric_arrival(proofingprogress, pp_main_fabric_arrival)

    pp_ingredients_fabric_arrival = request.POST.get("pp_ingredients_fabric_arrival")
    if pp_ingredients_fabric_arrival:
        create_pp.add_pp_ingredients_fabric_arrival(proofingprogress, pp_ingredients_fabric_arrival)

    pp_tailor_date = request.POST.get("pp_tailor_date")
    if pp_tailor_date:
        create_pp.add_pp_tailor_date(proofingprogress, pp_tailor_date)

    pp_send_embroide = request.POST.get("pp_send_embroide")
    if pp_send_embroide:
        create_pp.add_pp_send_embroide(proofingprogress, pp_send_embroide)

    pp_receive_embroide = request.POST.get("pp_receive_embroide")
    if pp_receive_embroide:
        create_pp.add_pp_receive_embroide(proofingprogress, pp_receive_embroide)

    pp_send_print = request.POST.get("pp_send_print")
    if pp_send_print:
        create_pp.add_pp_send_print(proofingprogress, pp_send_print)

    pp_receive_print = request.POST.get("pp_receive_print")
    if pp_receive_print:
        create_pp.add_pp_receive_print(proofingprogress, pp_receive_print)

    pp_delivery_proofing = request.POST.get("pp_delivery_proofing")
    if pp_delivery_proofing:
        create_pp.add_pp_delivery_proofing(proofingprogress, pp_delivery_proofing)

    worker_pk = request.POST.get("worker")
    if worker_pk:
        create_pp.add_worker_pk(proofingprogress, worker_pk)

    pp_end_date = request.POST.get("pp_end_date")
    if pp_end_date:
        create_pp.add_pp_end_date(proofingprogress, pp_end_date)

    pp_express_date = request.POST.get("pp_express_date")
    if pp_express_date:
        create_pp.add_pp_express_date(proofingprogress, pp_express_date)

class PPAdd(View):
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        workers = Worker.objects.all()
        context = {
            "title":"打样添加",
            "order":order,
            "workers":workers,
        }
        return render(request=request,template_name="ppadd.html",context=context)

    def post(self,request):
        pk = request.POST.get("pk")
        order = Order.objects.get(pk=pk)
        create_pp = CreatePP(order)
        proofingprogress = create_pp.add_pp()
        add_proofingprogress(request, create_pp, proofingprogress)
        proofingprogress.save()
        order.o_proofingprogress.add(proofingprogress)
        return redirect("/order/orderedit?pk={}".format(pk))

class EndPP(View):
    def get(self,request):
        pp_pk = request.GET.get("pp_pk")
        proofingprogress = ProofingProgress.objects.get(pk=pp_pk)
        proofingprogress.pp_end = True
        proofingprogress.save()
        return redirect("/order/orderedit?pk={}".format(proofingprogress.order_set.all()[0].pk))

class PPEdit(View):
    def get(self,request):
        pk = request.GET.get("pk")
        pp_pk = request.GET.get("pp_pk")
        order = Order.objects.get(pk=pk)
        proofingprogress = ProofingProgress.objects.get(pk=pp_pk)
        workers = Worker.objects.all()
        context = {
            "title": "打样修改",
            "order": order,
            "proofingprogress": proofingprogress,
            "workers": workers,
        }
        return render(request=request, template_name="ppedit.html", context=context)

    def post(self,request):
        pk = request.POST.get("pk")
        pp_pk = request.POST.get("pp_pk")
        order = Order.objects.get(pk=pk)
        create_pp = CreatePP(order)
        proofingprogress = order.o_proofingprogress.get(pk=pp_pk)
        add_proofingprogress(request, create_pp, proofingprogress)
        proofingprogress.save()
        return redirect("/order/orderedit?pk={}".format(pk))

class EndAllPP(View):
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        order.o_pp_all_end = True
        order.save()
        return redirect("/order/orderedit?pk={}".format(pk))

def add_modifyopinion(request,create_mo,modifyopinion):
    mo_customer_info = request.POST.get("mo_customer_info")
    if mo_customer_info:
        create_mo.add_mo_customer_info(modifyopinion, mo_customer_info)

    mo_factory_info = request.POST.get("mo_factory_info")
    if mo_factory_info:
        create_mo.add_mo_factory_info(modifyopinion, mo_factory_info)

class MOAdd(View):
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        context = {
            "title": "打样意见添加",
            "order": order,
        }
        return render(request=request, template_name="moadd.html", context=context)

    def post(self,request):
        pk = request.POST.get("pk")
        order = Order.objects.get(pk=pk)
        create_mo = CreateMO(order)
        modifyopinion = create_mo.add_mo()
        add_modifyopinion(request,create_mo,modifyopinion)
        modifyopinion.save()
        order.o_modifyopinion = modifyopinion
        order.save()
        return redirect("/order/orderedit?pk={}".format(pk))

class MOEdit(View):
    def get(self,request):
        pk = request.GET.get("pk")
        mo_pk = request.GET.get("mo_pk")
        order = Order.objects.get(pk=pk)
        modifyopinion = ModifyOpinion.objects.get(pk=mo_pk)
        context = {
            "title": "打样意见修改",
            "order": order,
            "modifyopinion": modifyopinion,
        }
        return render(request=request, template_name="moedit.html", context=context)

    def post(self,request):
        pk = request.POST.get("pk")
        order = Order.objects.get(pk=pk)
        create_mo = CreateMO(order)
        modifyopinion = order.o_modifyopinion
        add_modifyopinion(request,create_mo,modifyopinion)
        modifyopinion.save()
        return redirect("/order/orderedit?pk={}".format(pk))