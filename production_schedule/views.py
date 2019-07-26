from django.shortcuts import render,redirect
from django.views.generic.base import View
from order.models import Order
from user.models import *
from production_schedule.models import *
from production_schedule.create_ps import CreatePS
from user.views import login_verify

def add_productionschedule(request,create_ps,productionschedule):
    ps_number = request.POST.get("ps_number")
    if ps_number:
        create_ps.add_ps_number(productionschedule, ps_number)

    ps_date = request.POST.get("ps_date")
    if ps_date:
        create_ps.add_ps_date(productionschedule, ps_date)

    workshop = request.POST.get("workshop")
    if workshop:
        create_ps.add_workshop(productionschedule, workshop)

    ps_confirm_date = request.POST.get("ps_confirm_date")
    if ps_confirm_date:
        create_ps.add_ps_confirm_date(productionschedule, ps_confirm_date)

    ps_arrival_date = request.POST.get("ps_arrival_date")
    if ps_arrival_date:
        create_ps.add_ps_arrival_date(productionschedule, ps_arrival_date)

    ps_tailor_date = request.POST.get("ps_tailor_date")
    if ps_tailor_date:
        create_ps.add_ps_tailor_date(productionschedule, ps_tailor_date)

    ps_embroider_date = request.POST.get("ps_embroider_date")
    if ps_embroider_date:
        create_ps.add_ps_embroider_date(productionschedule, ps_embroider_date)

    ps_print_date = request.POST.get("ps_print_date")
    if ps_print_date:
        create_ps.add_ps_print_date(productionschedule, ps_print_date)

    ps_water_washing_date = request.POST.get("ps_water_washing_date")
    if ps_water_washing_date:
        create_ps.add_ps_water_washing_date(productionschedule, ps_water_washing_date)

    ps_sewing_date = request.POST.get("ps_sewing_date")
    if ps_sewing_date:
        create_ps.add_ps_sewing_date(productionschedule, ps_sewing_date)

    ps_ingredients_fabric_arrival_date = request.POST.get("ps_ingredients_fabric_arrival_date")
    if ps_ingredients_fabric_arrival_date:
        create_ps.add_ps_ingredients_fabric_arrival_date(productionschedule, ps_ingredients_fabric_arrival_date)

    ps_tags_arrival_date = request.POST.get("ps_tags_arrival_date")
    if ps_tags_arrival_date:
        create_ps.add_ps_tags_arrival_date(productionschedule, ps_tags_arrival_date)

    ps_iron_package_date = request.POST.get("ps_iron_package_date")
    if ps_iron_package_date:
        create_ps.add_ps_iron_package_date(productionschedule, ps_iron_package_date)

    ps_outward_transport_date = request.POST.get("ps_outward_transport_date")
    if ps_outward_transport_date:
        create_ps.add_ps_outward_transport_date(productionschedule, ps_outward_transport_date)

    ps_gathering_date = request.POST.get("ps_gathering_date")
    if ps_gathering_date:
        create_ps.add_ps_gathering_date(productionschedule, ps_gathering_date)

    ps_gathering_price = request.POST.get("ps_gathering_price")
    if ps_gathering_price:
        create_ps.add_ps_gathering_price(productionschedule, ps_gathering_price)

    ps_contract_balance = request.POST.get("ps_contract_balance")
    if ps_contract_balance:
        create_ps.add_ps_contract_balance(productionschedule, ps_contract_balance)

class PSAdd(View):
    @login_verify
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        productionworkshops = ProductionWorkshop.objects.all()
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "大货添加",
            "order": order,
            "productionworkshops": productionworkshops,
            "user": user,
        }
        return render(request=request, template_name="psadd.html", context=context)

    def post(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        create_ps = CreatePS()
        productionschedule = create_ps.add_ps()
        add_productionschedule(request,create_ps,productionschedule)
        productionschedule.save()
        order.o_productionschedule = productionschedule
        order.save()
        return redirect("/order/orderedit?pk={}".format(pk))

class PSEdit(View):
    @login_verify
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        productionworkshops = ProductionWorkshop.objects.all()
        user = User.objects.get(pk=request.session["user"])
        context = {
            "title": "大货修改",
            "order": order,
            "productionworkshops": productionworkshops,
            "user": user,
        }
        return render(request=request, template_name="psedit.html", context=context)

    def post(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        create_ps = CreatePS()
        productionschedule = order.o_productionschedule
        add_productionschedule(request, create_ps, productionschedule)
        productionschedule.save()
        return redirect("/order/orderedit?pk={}".format(pk))

class EndPS(View):
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        productionschedule = order.o_productionschedule
        productionschedule.ps_end = True
        productionschedule.save()
        return redirect("/order/orderedit?pk={}".format(pk))