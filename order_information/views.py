from django.shortcuts import render,HttpResponse,redirect
from django.views.generic.base import View
from .models import *
from user.models import *
from production_schedule.models import *
from .create_order import CreateOrder
from .add_order import AddOrder
from django.core.paginator import Paginator

import datetime
import uuid
# Create your views here.
class Orderlist(View):
    def get(self,request):
        pagenow = int(request.GET.get("pn",1))
        orders = Order.objects.all().order_by("-pk")
        orders = [{"pk":i.pk,
                 "o_image":i.o_image,
                 "o_number":i.o_number,
                 "o_user":i.o_user,
                 "o_price_type":i.o_price_type,
                 "o_productinfo":i.o_productinfo,
                 "o_customer":i.o_customer,
                 "o_capcolor":i.o_capcolor.all(),
                 "o_proofingprogress_number":i.o_proofingprogress_number,
                 "o_proofingprogress":i.o_proofingprogress.all().order_by("-pk")[0],
                 "o_productionschedule":i.o_productionschedule,} for i in orders]

        pagintor = Paginator(orders, 6)
        page = pagintor.page(pagenow)
        pagintor_list = page.object_list

        captypes = CapType.objects.all()
        users = User.objects.all()
        productionworkshops = ProductionWorkshop.objects.all()

        context = {
            "title": "订单列表",
            "orders": pagintor_list,
            "page": page,
            "pagenow": pagenow,
            "order_len":len(orders),
            "page_list": self.page_range_list(pagenow,pagintor,page_num=5),
            "captypes": captypes,
            "users": users,
            "productionworkshops": productionworkshops,
        }
        return render(request=request, template_name="orderlist.html", context=context)

    def page_range_list(self,pagenow,pagintor,page_num=5):
        page_count = pagintor.num_pages
        if page_count <= page_num:
            return pagintor.page_range
        else:
            if 1 <= pagenow <= page_num // 2:
                page_start = 1
                page_end = page_num
            else:
                page_start = pagenow - page_num // 2 + 1
                page_end = pagenow + page_num // 2 + 1

            if page_end > page_count:
                page_end = page_count
            if page_end == page_count:
                page_start = page_count - page_num + 1

            if page_end <= page_num:
                page_end = page_num

            return [page for page in range(page_start, page_end + 1)]


class OrderDetail(View):
    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        context = {
            "title":"订单详情",
            "order":order,
        }
        return render(request=request,template_name="orderdetail.html",context=context)

class OrderEdit(View):
    def edit_date(self,date):
        return date.replace("年","-").replace("月","-").replace("日","")

    def get(self,request):
        pk = request.GET.get("pk")
        order = Order.objects.get(pk=pk)
        o_proofingprogresses = order.o_proofingprogress.all()
        customers = Customer.objects.all()
        captypes = CapType.objects.all()
        users = User.objects.all()
        capcolors = CapColor.objects.all()
        embroiderorprints = EmbroiderOrPrint.objects.all()
        capeyebrows = CapEyebrow.objects.all()
        versionnumbers = VersionNumber.objects.all()
        afterdeductions = AfterDeduction.objects.all()
        productionworkshops = ProductionWorkshop.objects.all()
        pricetypes = PriceType.objects.all()
        context = {
            "title":"订单编辑",
            "order":order,
            "o_proofingprogresses":o_proofingprogresses,
            "o_proofingprogresses_len":len(o_proofingprogresses),
            "customers": customers,
            "captypes": captypes,
            "users": users,
            "capcolors": capcolors,
            "embroiderorprints": embroiderorprints,
            "capeyebrows": capeyebrows,
            "versionnumbers": versionnumbers,
            "afterdeductions": afterdeductions,
            "productionworkshops": productionworkshops,
            "pricetypes": pricetypes,
        }
        return render(request=request,template_name="orderedit.html",context=context)

    def post(self,request):
        order_pk = request.POST.get("order_pk")
        order = Order.objects.get(pk=order_pk)
        createorder = CreateOrder()
        addorder = AddOrder(order,createorder)
        #打样数量
        order_proofingprogress_number = request.POST.get("order_proofingprogress_number")
        addorder.add_order_proofingprogress_number(order_proofingprogress_number)
        # 币种
        pricetype_pk = request.POST.get("pricetype")
        addorder.add_pricetype(pricetype_pk)
        #图片
        image_file = request.FILES.get("add_iamge")
        addorder.add_image_file(image_file)
        #客户
        customer_pk = request.POST.get("customer_pk")
        customer_contack = request.POST.get("customer_contack")
        customer_email = request.POST.get("customer_email")
        addorder.add_customer(customer_pk,customer_contack,customer_email)
        #帽型
        captype_pk = request.POST.get("captype")
        addorder.add_captype(captype_pk)
        #业务员
        user_pk = request.POST.get("user")
        addorder.add_user(user_pk)
        #颜色
        order.o_capcolor.remove(*order.o_capcolor.all())
        capcolor_pks = request.POST.getlist("capcolor")
        addorder.add_capcolors(capcolor_pks)
        #绣印花
        embroiderorprint_pk = request.POST.get("embroiderorprint")
        addorder.add_embroiderorprint(embroiderorprint_pk)
        #帽眉
        capeyebrow_pk = request.POST.get("capeyebrow")
        addorder.add_capeyebrow(capeyebrow_pk)
        #版号
        versionnumber_pk = request.POST.get("versionnumber")
        addorder.add_versionnumber(versionnumber_pk)
        #后扣
        afterdeduction_pk = request.POST.get("afterdeduction")
        addorder.add_afterdeduction(afterdeduction_pk)
        #大货信息
        pi_amount = request.POST.get("pi_amount")
        pi_unit_price = request.POST.get("pi_unit_price")
        pi_date = request.POST.get("pi_date")
        pi_total_price = request.POST.get("pi_total_price")

        pi_offer = request.POST.get("pi_offer")
        pi_fabric_quotation = request.POST.get("pi_fabric_quotation")
        pi_ingredients_quotation = request.POST.get("pi_ingredients_quotation")
        pi_labor_payment_quotation = request.POST.get("pi_labor_payment_quotation")
        pi_water_washing_quotation = request.POST.get("pi_water_washing_quotation")
        pi_print_quotation = request.POST.get("pi_print_quotation")
        pi_embroider_quotation = request.POST.get("pi_embroider_quotation")
        pi_packaging_quotation = request.POST.get("pi_packaging_quotation")
        pi_other_quotation = request.POST.get("pi_other_quotation")
        pi_reserved_profits = request.POST.get("pi_reserved_profits")
        productinfo = order.o_productinfo
        productinfo.pi_id = uuid.uuid1()
        addorder.add_productinfo(productinfo=productinfo,
                                 pi_amount=pi_amount,
                                 pi_unit_price=pi_unit_price,
                                 pi_date=pi_date,
                                 pi_total_price=pi_total_price,

                                 pi_offer=pi_offer,
                                 pi_fabric_quotation=pi_fabric_quotation,
                                 pi_ingredients_quotation=pi_ingredients_quotation,
                                 pi_labor_payment_quotation=pi_labor_payment_quotation,
                                 pi_water_washing_quotation=pi_water_washing_quotation,
                                 pi_print_quotation=pi_print_quotation,
                                 pi_embroider_quotation=pi_embroider_quotation,
                                 pi_packaging_quotation=pi_packaging_quotation,
                                 pi_other_quotation=pi_other_quotation,
                                 pi_reserved_profits=pi_reserved_profits,
                                 )

        #打样进度
        pp_pks = request.POST.getlist("pp_pk")
        for pp_pk in pp_pks:
            pp_sample_order_date = request.POST.get("pp_sample_order_date_{}".format(pp_pk))
            pp_sample_arrival_date = request.POST.get("pp_sample_arrival_date_{}".format(pp_pk))
            pp_sample_express_date = request.POST.get("pp_sample_express_date_{}".format(pp_pk))
            pp_customer_feedback = request.POST.get("pp_customer_feedback_{}".format(pp_pk))
            pp_corrective_information = request.POST.get("pp_corrective_information_{}".format(pp_pk))
            proofingprogress = order.o_proofingprogress.get(pk=pp_pk)
            proofingprogress.pp_id = uuid.uuid1()
            addorder.add_proofingprogress(proofingprogress=proofingprogress,
                                          pp_sample_order_date=pp_sample_order_date,
                                          pp_sample_arrival_date=pp_sample_arrival_date,
                                          pp_sample_express_date=pp_sample_express_date,
                                          pp_customer_feedback=pp_customer_feedback,
                                          pp_corrective_information=pp_corrective_information,)

        pp_sample_order_date = request.POST.get("pp_sample_order_date")
        pp_sample_arrival_date = request.POST.get("pp_sample_arrival_date")
        pp_sample_express_date = request.POST.get("pp_sample_express_date")
        pp_customer_feedback = request.POST.get("pp_customer_feedback")
        pp_corrective_information = request.POST.get("pp_corrective_information")
        if pp_sample_order_date or pp_sample_arrival_date or pp_sample_express_date or pp_customer_feedback or pp_corrective_information:
            proofingprogress_add = ProofingProgress()
            proofingprogress_add.pp_id = uuid.uuid1()
            addorder.add_proofingprogress(proofingprogress=proofingprogress_add,
                                          pp_sample_order_date=pp_sample_order_date,
                                          pp_sample_arrival_date=pp_sample_arrival_date,
                                          pp_sample_express_date=pp_sample_express_date,
                                          pp_customer_feedback=pp_customer_feedback,
                                          pp_corrective_information=pp_corrective_information, )
            order.o_proofingprogress.add(proofingprogress_add)
        #大货进度
        workshop_pk = request.POST.get("pw_workshop")
        ps_number = request.POST.get("ps_number")
        ps_order_date = request.POST.get("ps_order_date")
        ps_arrival_date = request.POST.get("ps_arrival_date")
        ps_tailor_date = request.POST.get("ps_tailor_date")
        ps_embroider_date = request.POST.get("ps_embroider_date")
        ps_print_date = request.POST.get("ps_print_date")
        ps_water_washing_date = request.POST.get("ps_water_washing_date")
        ps_sewing_date = request.POST.get("ps_sewing_date")
        ps_qc_date = request.POST.get("ps_qc_date")
        ps_outward_transport_date = request.POST.get("ps_outward_transport_date")
        ps_gathering_date = request.POST.get("ps_gathering_date")
        ps_gathering_price = request.POST.get("ps_gathering_price")
        ps_contract_balance = request.POST.get("ps_contract_balance")
        productionschedule = order.o_productionschedule
        productionschedule.ps_id = uuid.uuid1()
        addorder.add_productionschedule(productionschedule=productionschedule,
                                        ps_order_date=ps_order_date,
                                        ps_number=ps_number,
                                        ps_arrival_date=ps_arrival_date,
                                        ps_tailor_date=ps_tailor_date,
                                        ps_embroider_date=ps_embroider_date,
                                        ps_print_date=ps_print_date,
                                        ps_water_washing_date=ps_water_washing_date,
                                        ps_sewing_date=ps_sewing_date,
                                        ps_qc_date=ps_qc_date,
                                        ps_outward_transport_date=ps_outward_transport_date,
                                        ps_gathering_date=ps_gathering_date,
                                        ps_gathering_price=ps_gathering_price,
                                        ps_contract_balance=ps_contract_balance,
                                        workshop_pk=workshop_pk,)
        # 按单核算
        ad_total_profit = request.POST.get("ad_total_profit")

        ad_fabric_ingredients_total_amount = request.POST.get("ad_fabric_ingredients_total_amount")
        ad_fabric_amount = request.POST.get("ad_fabric_amount")
        ad_fabric_express_amount = request.POST.get("ad_fabric_express_amount")
        ad_bonding_amount = request.POST.get("ad_bonding_amount")
        ad_ingredients_amount = request.POST.get("ad_ingredients_amount")
        ad_ingredients_express_amount = request.POST.get("ad_ingredients_express_amount")
        ad_fabric_ingredients_other_amount = request.POST.get("ad_fabric_ingredients_other_amount")

        ad_labor_paymentl_amount = request.POST.get("ad_labor_paymentl_amount")
        ad_tailor_total_amount = request.POST.get("ad_tailor_total_amount")
        ad_tailor_start_date = request.POST.get("ad_tailor_start_date")
        ad_tailor_end_date = request.POST.get("ad_tailor_end_date")
        ad_tailor_number_people = request.POST.get("ad_tailor_number_people")
        ad_sewing_total_amount = request.POST.get("ad_sewing_total_amount")
        ad_sewing_start_date = request.POST.get("ad_sewing_start_date")
        ad_sewing_end_date = request.POST.get("ad_sewing_end_date")
        ad_sewing_number_people = request.POST.get("ad_sewing_number_people")
        ad_iron_total_amount = request.POST.get("ad_iron_total_amount")
        ad_iron_start_date = request.POST.get("ad_iron_start_date")
        ad_iron_end_date = request.POST.get("ad_iron_end_date")
        ad_iron_number_people = request.POST.get("ad_iron_number_people")

        ad_embroide_print_amount = request.POST.get("ad_embroide_print_amount")
        ad_water_washing_amount = request.POST.get("ad_water_washing_amount")
        ad_embroide_amount = request.POST.get("ad_embroide_amount")
        ad_print_amount = request.POST.get("ad_print_amount")

        ad_packaging_shipping_amount = request.POST.get("ad_packaging_shipping_amount")
        ad_paperboard_amount = request.POST.get("ad_paperboard_amount")
        ad_physical_distribution_amount = request.POST.get("ad_physical_distribution_amount")
        ad_warehouse_entry_amount = request.POST.get("ad_warehouse_entry_amount")
        ad_customs_declaration_amount = request.POST.get("ad_customs_declaration_amount")
        accountingdocuments = order.o_accountingdocuments
        addorder.add_accountingdocuments(accountingdocuments=accountingdocuments,
                                         ad_total_profit=ad_total_profit,

                                         ad_fabric_ingredients_total_amount=ad_fabric_ingredients_total_amount,
                                         ad_fabric_amount=ad_fabric_amount,
                                         ad_fabric_express_amount=ad_fabric_express_amount,
                                         ad_bonding_amount=ad_bonding_amount,
                                         ad_ingredients_amount=ad_ingredients_amount,
                                         ad_ingredients_express_amount=ad_ingredients_express_amount,
                                         ad_fabric_ingredients_other_amount=ad_fabric_ingredients_other_amount,

                                         ad_labor_paymentl_amount=ad_labor_paymentl_amount,
                                         ad_tailor_total_amount=ad_tailor_total_amount,
                                         ad_tailor_start_date=ad_tailor_start_date,
                                         ad_tailor_end_date=ad_tailor_end_date,
                                         ad_tailor_number_people=ad_tailor_number_people,
                                         ad_sewing_total_amount=ad_sewing_total_amount,
                                         ad_sewing_start_date=ad_sewing_start_date,
                                         ad_sewing_end_date=ad_sewing_end_date,
                                         ad_sewing_number_people=ad_sewing_number_people,
                                         ad_iron_total_amount=ad_iron_total_amount,
                                         ad_iron_start_date=ad_iron_start_date,
                                         ad_iron_end_date=ad_iron_end_date,
                                         ad_iron_number_people=ad_iron_number_people,

                                         ad_embroide_print_amount=ad_embroide_print_amount,
                                         ad_water_washing_amount=ad_water_washing_amount,
                                         ad_embroide_amount=ad_embroide_amount,
                                         ad_print_amount=ad_print_amount,

                                         ad_packaging_shipping_amount=ad_packaging_shipping_amount,
                                         ad_paperboard_amount=ad_paperboard_amount,
                                         ad_physical_distribution_amount=ad_physical_distribution_amount,
                                         ad_warehouse_entry_amount=ad_warehouse_entry_amount,
                                         ad_customs_declaration_amount=ad_customs_declaration_amount, )
        order.save()
        return redirect("/order/orderlist")

class OrderAdd(View):
    def edit_date(self,date):
        return date.replace("年","-").replace("月","-").replace("日","")

    def get(self,request):
        customers = Customer.objects.all()
        captypes = CapType.objects.all()
        users = User.objects.all()
        capcolors = CapColor.objects.all()
        embroiderorprints = EmbroiderOrPrint.objects.all()
        capeyebrows = CapEyebrow.objects.all()
        versionnumbers = VersionNumber.objects.all()
        afterdeductions = AfterDeduction.objects.all()
        productionworkshops = ProductionWorkshop.objects.all()
        pricetypes = PriceType.objects.all()
        context = {
            "title":"添加订单",
            "customers":customers,
            "captypes":captypes,
            "users":users,
            "capcolors":capcolors,
            "embroiderorprints":embroiderorprints,
            "capeyebrows":capeyebrows,
            "versionnumbers":versionnumbers,
            "afterdeductions":afterdeductions,
            "productionworkshops":productionworkshops,
            "pricetypes":pricetypes,
            "today":datetime.date.today().strftime("%Y-%m-%d"),
        }
        return render(request=request,template_name="orderadd.html",context=context)

    def post(self,request):
        createorder = CreateOrder()
        order_number = request.POST.get("order_number")
        order_date = request.POST.get("order_date")
        order = createorder.create_order(order_number=order_number,order_date=self.edit_date(order_date))
        addorder = AddOrder(order,createorder)
        #币种
        pricetype_pk = request.POST.get("pricetype",1)
        addorder.add_pricetype(pricetype_pk)
        #打样数量
        order_proofingprogress_number = request.POST.get("order_proofingprogress_number")
        addorder.add_order_proofingprogress_number(order_proofingprogress_number)
        #图片
        image_file = request.FILES.get("add_iamge")
        addorder.add_image_file(image_file)
        #客户
        customer_pk = request.POST.get("customer_pk")
        customer_contack = request.POST.get("customer_contack")
        customer_email = request.POST.get("customer_email")
        addorder.add_customer(customer_pk,customer_contack,customer_email)
        #帽型
        captype_pk = request.POST.get("captype")
        addorder.add_captype(captype_pk)
        #业务员
        user_pk = request.POST.get("user")
        addorder.add_user(user_pk)
        #颜色
        capcolor_pks = request.POST.getlist("capcolor")
        addorder.add_capcolors(capcolor_pks)
        #绣印花
        embroiderorprint_pk = request.POST.get("embroiderorprint")
        addorder.add_embroiderorprint(embroiderorprint_pk)
        #帽眉
        capeyebrow_pk = request.POST.get("capeyebrow")
        addorder.add_capeyebrow(capeyebrow_pk)
        #版号
        versionnumber_pk = request.POST.get("versionnumber")
        addorder.add_versionnumber(versionnumber_pk)
        #后扣
        afterdeduction_pk = request.POST.get("afterdeduction")
        addorder.add_afterdeduction(afterdeduction_pk)
        #大货信息
        pi_amount = request.POST.get("pi_amount")
        pi_unit_price = request.POST.get("pi_unit_price")
        pi_date = request.POST.get("pi_date")
        pi_total_price = request.POST.get("pi_total_price")

        pi_offer = request.POST.get("pi_offer")
        pi_fabric_quotation = request.POST.get("pi_fabric_quotation")
        pi_ingredients_quotation = request.POST.get("pi_ingredients_quotation")
        pi_labor_payment_quotation = request.POST.get("pi_labor_payment_quotation")
        pi_water_washing_quotation = request.POST.get("pi_water_washing_quotation")
        pi_print_quotation = request.POST.get("pi_print_quotation")
        pi_embroider_quotation = request.POST.get("pi_embroider_quotation")
        pi_packaging_quotation = request.POST.get("pi_packaging_quotation")
        pi_other_quotation = request.POST.get("pi_other_quotation")
        pi_reserved_profits = request.POST.get("pi_reserved_profits")
        productinfo = ProductInfo()
        productinfo.pi_id = uuid.uuid1()
        addorder.add_productinfo(productinfo=productinfo,
                                 pi_amount=pi_amount,
                                 pi_unit_price=pi_unit_price,
                                 pi_date=pi_date,
                                 pi_total_price=pi_total_price,

                                 pi_offer=pi_offer,
                                 pi_fabric_quotation=pi_fabric_quotation,
                                 pi_ingredients_quotation=pi_ingredients_quotation,
                                 pi_labor_payment_quotation=pi_labor_payment_quotation,
                                 pi_water_washing_quotation=pi_water_washing_quotation,
                                 pi_print_quotation=pi_print_quotation,
                                 pi_embroider_quotation=pi_embroider_quotation,
                                 pi_packaging_quotation=pi_packaging_quotation,
                                 pi_other_quotation=pi_other_quotation,
                                 pi_reserved_profits=pi_reserved_profits,)
        order.o_productinfo = productinfo
        #打样进度
        pp_sample_order_date = request.POST.get("pp_sample_order_date")
        pp_sample_arrival_date = request.POST.get("pp_sample_arrival_date")
        pp_sample_express_date = request.POST.get("pp_sample_express_date")
        pp_customer_feedback = request.POST.get("pp_customer_feedback")
        pp_corrective_information = request.POST.get("pp_corrective_information")
        proofingprogress = ProofingProgress()
        proofingprogress.pp_id = uuid.uuid1()
        addorder.add_proofingprogress(proofingprogress=proofingprogress,
                                      pp_sample_order_date=pp_sample_order_date,
                                      pp_sample_arrival_date=pp_sample_arrival_date,
                                      pp_sample_express_date=pp_sample_express_date,
                                      pp_customer_feedback=pp_customer_feedback,
                                      pp_corrective_information=pp_corrective_information, )
        order.o_proofingprogress.add(proofingprogress)
        #大货进度
        workshop_pk = request.POST.get("pw_workshop")
        ps_number = request.POST.get("ps_number")
        ps_order_date = request.POST.get("ps_order_date")
        ps_arrival_date = request.POST.get("ps_arrival_date")
        ps_tailor_date = request.POST.get("ps_tailor_date")
        ps_embroider_date = request.POST.get("ps_embroider_date")
        ps_print_date = request.POST.get("ps_print_date")
        ps_water_washing_date = request.POST.get("ps_water_washing_date")
        ps_sewing_date = request.POST.get("ps_sewing_date")
        ps_qc_date = request.POST.get("ps_qc_date")
        ps_outward_transport_date = request.POST.get("ps_outward_transport_date")
        ps_gathering_date = request.POST.get("ps_gathering_date")
        ps_gathering_price = request.POST.get("ps_gathering_price")
        ps_contract_balance = request.POST.get("ps_contract_balance")
        productionschedule = ProductionSchedule()
        productionschedule.ps_id = uuid.uuid1()
        addorder.add_productionschedule(productionschedule=productionschedule,
                                        ps_order_date=ps_order_date,
                                        ps_number=ps_number,
                                        ps_arrival_date=ps_arrival_date,
                                        ps_tailor_date=ps_tailor_date,
                                        ps_embroider_date=ps_embroider_date,
                                        ps_print_date=ps_print_date,
                                        ps_water_washing_date=ps_water_washing_date,
                                        ps_sewing_date=ps_sewing_date,
                                        ps_qc_date=ps_qc_date,
                                        ps_outward_transport_date=ps_outward_transport_date,
                                        ps_gathering_date=ps_gathering_date,
                                        ps_gathering_price=ps_gathering_price,
                                        ps_contract_balance=ps_contract_balance,
                                        workshop_pk=workshop_pk, )
        order.o_productionschedule = productionschedule
        #按单核算
        ad_total_profit = request.POST.get("ad_total_profit")

        ad_fabric_ingredients_total_amount = request.POST.get("ad_fabric_ingredients_total_amount")
        ad_fabric_amount = request.POST.get("ad_fabric_amount")
        ad_fabric_express_amount = request.POST.get("ad_fabric_express_amount")
        ad_bonding_amount = request.POST.get("ad_bonding_amount")
        ad_ingredients_amount = request.POST.get("ad_ingredients_amount")
        ad_ingredients_express_amount = request.POST.get("ad_ingredients_express_amount")
        ad_fabric_ingredients_other_amount = request.POST.get("ad_fabric_ingredients_other_amount")

        ad_labor_paymentl_amount = request.POST.get("ad_labor_paymentl_amount")
        ad_tailor_total_amount = request.POST.get("ad_tailor_total_amount")
        ad_tailor_start_date = request.POST.get("ad_tailor_start_date")
        ad_tailor_end_date = request.POST.get("ad_tailor_end_date")
        ad_tailor_number_people = request.POST.get("ad_tailor_number_people")
        ad_sewing_total_amount = request.POST.get("ad_sewing_total_amount")
        ad_sewing_start_date = request.POST.get("ad_sewing_start_date")
        ad_sewing_end_date = request.POST.get("ad_sewing_end_date")
        ad_sewing_number_people = request.POST.get("ad_sewing_number_people")
        ad_iron_total_amount = request.POST.get("ad_iron_total_amount")
        ad_iron_start_date = request.POST.get("ad_iron_start_date")
        ad_iron_end_date = request.POST.get("ad_iron_end_date")
        ad_iron_number_people = request.POST.get("ad_iron_number_people")

        ad_embroide_print_amount = request.POST.get("ad_embroide_print_amount")
        ad_water_washing_amount = request.POST.get("ad_water_washing_amount")
        ad_embroide_amount = request.POST.get("ad_embroide_amount")
        ad_print_amount = request.POST.get("ad_print_amount")

        ad_packaging_shipping_amount = request.POST.get("ad_packaging_shipping_amount")
        ad_paperboard_amount = request.POST.get("ad_paperboard_amount")
        ad_physical_distribution_amount = request.POST.get("ad_physical_distribution_amount")
        ad_warehouse_entry_amount = request.POST.get("ad_warehouse_entry_amount")
        ad_customs_declaration_amount = request.POST.get("ad_customs_declaration_amount")
        accountingdocuments = AccountingDocuments()
        accountingdocuments.ad_id = uuid.uuid1()
        addorder.add_accountingdocuments(accountingdocuments=accountingdocuments,
                                         ad_total_profit=ad_total_profit,

                                         ad_fabric_ingredients_total_amount=ad_fabric_ingredients_total_amount,
                                         ad_fabric_amount=ad_fabric_amount,
                                         ad_fabric_express_amount=ad_fabric_express_amount,
                                         ad_bonding_amount=ad_bonding_amount,
                                         ad_ingredients_amount=ad_ingredients_amount,
                                         ad_ingredients_express_amount=ad_ingredients_express_amount,
                                         ad_fabric_ingredients_other_amount=ad_fabric_ingredients_other_amount,

                                         ad_labor_paymentl_amount=ad_labor_paymentl_amount,
                                         ad_tailor_total_amount=ad_tailor_total_amount,
                                         ad_tailor_start_date=ad_tailor_start_date,
                                         ad_tailor_end_date=ad_tailor_end_date,
                                         ad_tailor_number_people=ad_tailor_number_people,
                                         ad_sewing_total_amount=ad_sewing_total_amount,
                                         ad_sewing_start_date=ad_sewing_start_date,
                                         ad_sewing_end_date=ad_sewing_end_date,
                                         ad_sewing_number_people=ad_sewing_number_people,
                                         ad_iron_total_amount=ad_iron_total_amount,
                                         ad_iron_start_date=ad_iron_start_date,
                                         ad_iron_end_date=ad_iron_end_date,
                                         ad_iron_number_people=ad_iron_number_people,

                                         ad_embroide_print_amount=ad_embroide_print_amount,
                                         ad_water_washing_amount=ad_water_washing_amount,
                                         ad_embroide_amount=ad_embroide_amount,
                                         ad_print_amount=ad_print_amount,

                                         ad_packaging_shipping_amount=ad_packaging_shipping_amount,
                                         ad_paperboard_amount=ad_paperboard_amount,
                                         ad_physical_distribution_amount=ad_physical_distribution_amount,
                                         ad_warehouse_entry_amount=ad_warehouse_entry_amount,
                                         ad_customs_declaration_amount=ad_customs_declaration_amount,)
        order.o_accountingdocuments = accountingdocuments
        order.save()
        return redirect("/order/orderlist")