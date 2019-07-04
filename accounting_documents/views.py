from django.shortcuts import render, redirect
from django.views.generic.base import View
from order.models import Order
from accounting_documents.models import AccountingDocuments
from accounting_documents.create_ad import CreateAD

def add_quotation(request,create_ad,accountingdocuments):
    ad_ps_dollar_total_price = request.POST.get("ad_ps_dollar_total_price")
    if ad_ps_dollar_total_price:
        create_ad.add_ad_ps_dollar_total_price(accountingdocuments,ad_ps_dollar_total_price)

    ad_actual_cost = request.POST.get("ad_actual_cost")
    if ad_actual_cost:
        create_ad.add_ad_actual_cost(accountingdocuments,ad_actual_cost)

    ad_total_profit = request.POST.get("ad_total_profit")
    if ad_total_profit:
        create_ad.add_ad_total_profit(accountingdocuments,ad_total_profit)


    ad_total_amount_materials = request.POST.get("ad_total_amount_materials")
    if ad_total_amount_materials:
        create_ad.add_ad_total_amount_materials(accountingdocuments,ad_total_amount_materials)

    ad_total_amount_fabric = request.POST.get("ad_total_amount_fabric")
    if ad_total_amount_fabric:
        create_ad.add_ad_total_amount_fabric(accountingdocuments,ad_total_amount_fabric)

    ad_total_amount_fabric_express = request.POST.get("ad_total_amount_fabric_express")
    if ad_total_amount_fabric_express:
        create_ad.add_ad_total_amount_fabric_express(accountingdocuments,ad_total_amount_fabric_express)

    ad_total_amount_bonding = request.POST.get("ad_total_amount_bonding")
    if ad_total_amount_bonding:
        create_ad.add_ad_total_amount_bonding(accountingdocuments,ad_total_amount_bonding)

    ad_total_amount_ingredients = request.POST.get("ad_total_amount_ingredients")
    if ad_total_amount_ingredients:
        create_ad.add_ad_total_amount_ingredients(accountingdocuments,ad_total_amount_ingredients)

    ad_total_amount_ingredients_express = request.POST.get("ad_total_amount_ingredients_express")
    if ad_total_amount_ingredients_express:
        create_ad.add_ad_total_amount_ingredients_express(accountingdocuments,ad_total_amount_ingredients_express)

    ad_total_amount_other = request.POST.get("ad_total_amount_other")
    if ad_total_amount_other:
        create_ad.add_ad_total_amount_other(accountingdocuments,ad_total_amount_other)


    ad_total_amount_labor_payment = request.POST.get("ad_total_amount_labor_payment")
    if ad_total_amount_labor_payment:
        create_ad.add_ad_total_amount_labor_payment(accountingdocuments,ad_total_amount_labor_payment)

    ad_total_amount_tailor = request.POST.get("ad_total_amount_tailor")
    if ad_total_amount_tailor:
        create_ad.add_ad_total_amount_tailor(accountingdocuments,ad_total_amount_tailor)

    ad_tailor_start_date = request.POST.get("ad_tailor_start_date")
    if ad_tailor_start_date:
        create_ad.add_ad_tailor_start_date(accountingdocuments,ad_tailor_start_date)

    ad_tailor_end_date = request.POST.get("ad_tailor_end_date")
    if ad_tailor_end_date:
        create_ad.add_ad_tailor_end_date(accountingdocuments,ad_tailor_end_date)

    ad_tailor_number_people = request.POST.get("ad_tailor_number_people")
    if ad_tailor_number_people:
        create_ad.add_ad_tailor_number_people(accountingdocuments,ad_tailor_number_people)

    ad_total_amount_sewing = request.POST.get("ad_total_amount_sewing")
    if ad_total_amount_sewing:
        create_ad.add_ad_total_amount_sewing(accountingdocuments,ad_total_amount_sewing)

    ad_sewing_start_date = request.POST.get("ad_sewing_start_date")
    if ad_sewing_start_date:
        create_ad.add_ad_sewing_start_date(accountingdocuments,ad_sewing_start_date)

    ad_sewing_end_date = request.POST.get("ad_sewing_end_date")
    if ad_sewing_end_date:
        create_ad.add_ad_sewing_end_date(accountingdocuments,ad_sewing_end_date)

    ad_sewing_number_people = request.POST.get("ad_sewing_number_people")
    if ad_sewing_number_people:
        create_ad.add_ad_sewing_number_people(accountingdocuments,ad_sewing_number_people)

    ad_total_amount_iron = request.POST.get("ad_total_amount_iron")
    if ad_total_amount_iron:
        create_ad.add_ad_total_amount_iron(accountingdocuments,ad_total_amount_iron)

    ad_iron_start_date = request.POST.get("ad_iron_start_date")
    if ad_iron_start_date:
        create_ad.add_ad_iron_start_date(accountingdocuments,ad_iron_start_date)

    ad_iron_end_date = request.POST.get("ad_iron_end_date")
    if ad_iron_end_date:
        create_ad.add_ad_iron_end_date(accountingdocuments,ad_iron_end_date)

    ad_iron_number_people = request.POST.get("ad_iron_number_people")
    if ad_iron_number_people:
        create_ad.add_ad_iron_number_people(accountingdocuments,ad_iron_number_people)


    ad_total_amount_embroide_print = request.POST.get("ad_total_amount_embroide_print")
    if ad_total_amount_embroide_print:
        create_ad.add_ad_total_amount_embroide_print(accountingdocuments,ad_total_amount_embroide_print)

    ad_total_amount_water_washing = request.POST.get("ad_total_amount_water_washing")
    if ad_total_amount_water_washing:
        create_ad.add_ad_total_amount_water_washing(accountingdocuments,ad_total_amount_water_washing)

    ad_total_amount_embroide = request.POST.get("ad_total_amount_embroide")
    if ad_total_amount_embroide:
        create_ad.add_ad_total_amount_embroide(accountingdocuments,ad_total_amount_embroide)

    ad_total_amount_print = request.POST.get("ad_total_amount_print")
    if ad_total_amount_print:
        create_ad.add_ad_total_amount_print(accountingdocuments,ad_total_amount_print)


    ad_total_amount_packaging_shipping = request.POST.get("ad_total_amount_packaging_shipping")
    if ad_total_amount_packaging_shipping:
        create_ad.add_ad_total_amount_packaging_shipping(accountingdocuments,ad_total_amount_packaging_shipping)

    ad_total_amount_paperboard = request.POST.get("ad_total_amount_paperboard")
    if ad_total_amount_paperboard:
        create_ad.add_ad_total_amount_paperboard(accountingdocuments,ad_total_amount_paperboard)

    ad_total_amount_physical_distribution = request.POST.get("ad_total_amount_physical_distribution")
    if ad_total_amount_physical_distribution:
        create_ad.add_ad_total_amount_physical_distribution(accountingdocuments,ad_total_amount_physical_distribution)

    ad_total_amount_warehouse_entry = request.POST.get("ad_total_amount_warehouse_entry")
    if ad_total_amount_warehouse_entry:
        create_ad.add_ad_total_amount_warehouse_entry(accountingdocuments,ad_total_amount_warehouse_entry)

    ad_total_amount_customs_declaration = request.POST.get("ad_total_amount_customs_declaration")
    if ad_total_amount_customs_declaration:
        create_ad.add_ad_total_amount_customs_declaration(accountingdocuments,ad_total_amount_customs_declaration)

class ADAdd(View):
    def get(self,request):
        pk =  request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        context = {
            "title": "核算单添加",
            "order": order,
        }
        return render(request=request,template_name="adadd.html",context=context)

    def post(self,request):
        pk = request.POST.get("pk")
        order = Order.objects.get(pk=pk)
        create_ad = CreateAD()
        accountingdocuments = create_ad.add_ad()
        add_quotation(request,create_ad,accountingdocuments)
        accountingdocuments.save()
        order.o_accountingdocuments = accountingdocuments
        order.save()
        return redirect("/order/orderedit?pk={}".format(pk))

class ADEdit(View):
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        context = {
            "title": "核算单修改",
            "order": order,
        }
        return render(request=request,template_name="adedit.html",context=context)

    def post(self,request):
        pk = request.POST.get("pk")
        order = Order.objects.get(pk=pk)
        create_ad = CreateAD()
        accountingdocuments = order.o_accountingdocuments
        add_quotation(request,create_ad,accountingdocuments)
        accountingdocuments.save()
        return redirect("/order/orderedit?pk={}".format(pk))