from django.shortcuts import render,HttpResponse,redirect
from django.views.generic.base import View
from .models import *
from user.models import *
from production_schedule.models import *
from .create_order import CreateOrder
from django.core.paginator import Paginator

import datetime
import uuid
# Create your views here.
class Orderlist(View):
    def get(self,request):
        pagenow = int(request.GET.get("pn",1))
        search_type = request.GET.get("st","a")
        if search_type == "pp":
            orders = [i for i in Order.objects.all() if i.o_proofingprogress.pp_sample_order_date and not i.o_proofingprogress.pp_sample_express_date]
        elif search_type == "ps":
            orders = [i for i in Order.objects.all() if i.o_productionschedule.ps_order_date and not i.o_productionschedule.ps_outward_transport_date]
        elif search_type == "cp":
            orders = [i for i in Order.objects.all() if i.o_productionschedule.ps_outward_transport_date and not i.o_productionschedule.ps_gathering_date]
        else:
            orders = Order.objects.all().order_by("-pk")

        pagintor = Paginator(orders, 6)
        page = pagintor.page(pagenow)
        pagintor_list = page.object_list
        page_list = pagintor.page_range

        page_num = 5
        page_count = pagintor.num_pages
        if page_count <= page_num:
            page_range = page_list
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

            page_range = [page for page in range(page_start, page_end + 1)]
        context = {
            "title": "订单列表",
            "orders": pagintor_list,
            "page": page,
            "pagenow": pagenow,
            "order_len":len(orders),
            "page_list": page_range,
            "search_type": search_type,
        }
        return render(request=request, template_name="orderlist.html", context=context)

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
        customers = Customer.objects.all()
        captypes = CapType.objects.all()
        users = User.objects.all()
        capcolors = CapColor.objects.all()
        capeyebrows = CapEyebrow.objects.all()
        versionnumbers = VersionNumber.objects.all()
        afterdeductions = AfterDeduction.objects.all()
        productionworkshops = ProductionWorkshop.objects.all()
        context = {
            "title":"订单编辑",
            "order":order,
            "customers": customers,
            "captypes": captypes,
            "users": users,
            "capcolors": capcolors,
            "capeyebrows": capeyebrows,
            "versionnumbers": versionnumbers,
            "afterdeductions": afterdeductions,
            "productionworkshops": productionworkshops
        }
        return render(request=request,template_name="orderedit.html",context=context)

    def post(self,request):
        order_pk = request.POST.get("order_pk")
        order = Order.objects.get(pk=order_pk)
        createorder = CreateOrder()

        image_file = request.FILES.get("add_iamge")
        if image_file:
            order.o_image = image_file

        customer_pk = request.POST.get("customer_pk")
        customer_contack = request.POST.get("customer_contack")
        customer_email = request.POST.get("customer_email")
        if customer_pk and customer_contack and customer_email:
            customer = createorder.query_customer(customer_pk=customer_pk)
            order.o_customer = customer

        captype_pk = request.POST.get("captype")
        if captype_pk:
            captype = createorder.query_captype(captype_pk=captype_pk)
            order.o_captype = captype

        user_pk = request.POST.get("user")
        if user_pk:
            user = createorder.query_user(user_pk=user_pk)
            order.o_user = user

        capcolor_pk = request.POST.get("capcolor")
        if capcolor_pk:
            capcolor = createorder.query_capcolor(capcolor_pk=capcolor_pk)
            order.o_capcolor = capcolor

        embroiderorprint = request.POST.get("embroiderorprint")
        if embroiderorprint:
            order.o_embroiderorprint = embroiderorprint

        capeyebrow_pk = request.POST.get("capeyebrow")
        if capeyebrow_pk:
            capeyebrow = createorder.query_capeyebrow(capeyebrow_pk=capeyebrow_pk)
            order.o_capeyebrow = capeyebrow

        versionnumber_pk = request.POST.get("versionnumber")
        if versionnumber_pk:
            versionnumber = createorder.query_versionnumber(versionnumber_pk=versionnumber_pk)
            order.o_versionnumber = versionnumber

        afterdeduction_pk = request.POST.get("afterdeduction")
        if afterdeduction_pk:
            afterdeduction = createorder.query_afterdeduction(afterdeduction_pk=afterdeduction_pk)
            order.o_afterdeduction = afterdeduction

        pi_amount = request.POST.get("pi_amount")
        pi_unit_price = request.POST.get("pi_unit_price")
        pi_date = request.POST.get("pi_date")
        pi_price_type = pi_unit_price[0]
        productinfo = ProductInfo()
        productinfo.pi_id = uuid.uuid1()
        if pi_amount:
            productinfo.pi_amount = pi_amount
        if len(pi_unit_price) > 1:
            productinfo.pi_unit_price = pi_unit_price[1:]
        if pi_date:
            productinfo.pi_date = self.edit_date(pi_date)
        productinfo.pi_price_type = pi_price_type
        productinfo.save()
        order.o_productinfo = productinfo

        pp_sample_order_date = self.edit_date(request.POST.get("pp_sample_order_date"))
        pp_sample_arrival_date = self.edit_date(request.POST.get("pp_sample_arrival_date"))
        pp_sample_express_date = self.edit_date(request.POST.get("pp_sample_express_date"))
        pp_customer_feedback = request.POST.get("pp_customer_feedback")
        pp_corrective_information = request.POST.get("pp_corrective_information")
        pp_Modify_sample_order_date = self.edit_date(request.POST.get("pp_Modify_sample_order_date"))
        pp_Modify_sample_arrival_date = self.edit_date(request.POST.get("pp_Modify_sample_arrival_date"))
        pp_Modify_sample_express_date = self.edit_date(request.POST.get("pp_Modify_sample_express_date"))
        proofingprogress = ProofingProgress()
        proofingprogress.pp_id = uuid.uuid1()
        proofingprogress.pp_sample_order_date = self.edit_date(pp_sample_order_date)
        if pp_sample_arrival_date:
            proofingprogress.pp_sample_arrival_date = pp_sample_arrival_date
        if pp_sample_express_date:
            proofingprogress.pp_sample_express_date = pp_sample_express_date
        if pp_customer_feedback:
            proofingprogress.pp_customer_feedback = pp_customer_feedback
        if pp_corrective_information:
            proofingprogress.pp_corrective_information = pp_corrective_information
        if pp_Modify_sample_order_date:
            proofingprogress.pp_Modify_sample_order_date = pp_Modify_sample_order_date
        if pp_Modify_sample_arrival_date:
            proofingprogress.pp_Modify_sample_arrival_date = pp_Modify_sample_arrival_date
        if pp_Modify_sample_express_date:
            proofingprogress.pp_Modify_sample_express_date = pp_Modify_sample_express_date
        proofingprogress.save()
        order.o_proofingprogress = proofingprogress

        workshop_pk = request.POST.get("pw_workshop")
        ps_order_date = self.edit_date(request.POST.get("ps_order_date"))
        ps_arrival_date = self.edit_date(request.POST.get("ps_arrival_date"))
        ps_tailor_date = self.edit_date(request.POST.get("ps_tailor_date"))
        ps_embroider_date = self.edit_date(request.POST.get("ps_embroider_date"))
        ps_print_date = self.edit_date(request.POST.get("ps_print_date"))
        ps_Water_washing_date = self.edit_date(request.POST.get("ps_Water_washing_date"))
        ps_sewing_date = self.edit_date(request.POST.get("ps_sewing_date"))
        ps_qc_date = self.edit_date(request.POST.get("ps_qc_date"))
        ps_outward_transport_date = self.edit_date(request.POST.get("ps_outward_transport_date"))
        ps_gathering_date = self.edit_date(request.POST.get("ps_gathering_date"))
        ps_gathering_price = request.POST.get("ps_gathering_price")
        ps_contract_balance = request.POST.get("ps_contract_balance")
        productionschedule = ProductionSchedule()
        productionschedule.ps_id = uuid.uuid1()
        if ps_order_date:
            productionschedule.ps_order_date = ps_order_date
        if ps_arrival_date:
            productionschedule.ps_arrival_date = ps_arrival_date
        if ps_tailor_date:
            productionschedule.ps_tailor_date = ps_tailor_date
        if ps_embroider_date:
            productionschedule.ps_embroider_date = ps_embroider_date
        if ps_print_date:
            productionschedule.ps_print_date = ps_print_date
        if ps_Water_washing_date:
            productionschedule.ps_Water_washing_date = ps_Water_washing_date
        if ps_sewing_date:
            productionschedule.ps_sewing_date = ps_sewing_date
        if ps_qc_date:
            productionschedule.ps_qc_date = ps_qc_date
        if ps_outward_transport_date:
            productionschedule.ps_outward_transport_date = ps_outward_transport_date
        if ps_gathering_date:
            productionschedule.ps_gathering_date = ps_gathering_date
        productionschedule.ps_price_type = ps_gathering_price[0]
        if len(ps_gathering_price) > 1:
            productionschedule.ps_gathering_price = ps_gathering_price[1:]
        if len(ps_contract_balance) > 1:
            productionschedule.ps_contract_balance = ps_contract_balance[1:]
        if workshop_pk:
            workshop = createorder.query_workshop(workshop_pk=workshop_pk)
            productionschedule.ps_workshop = workshop
        productionschedule.save()
        order.o_productionschedule = productionschedule

        order.save()
        return redirect("/order/orderlist")

class OrderAdd(View):
    def ordernumber(self):
        last_order_number = str(int(Order.objects.filter().order_by("-pk")[0].o_number.split("-")[-1]) + 1)
        last_order_number_len = len(last_order_number)
        return "{}{}".format("0"*(4 - last_order_number_len),last_order_number)

    def edit_date(self,date):
        return date.replace("年","-").replace("月","-").replace("日","")

    def get(self,request):
        customers = Customer.objects.all()
        captypes = CapType.objects.all()
        users = User.objects.all()
        capcolors = CapColor.objects.all()
        capeyebrows = CapEyebrow.objects.all()
        versionnumbers = VersionNumber.objects.all()
        afterdeductions = AfterDeduction.objects.all()
        productionworkshops = ProductionWorkshop.objects.all()
        order_number = "KS19-{}".format(self.ordernumber())
        context = {
            "title":"添加订单",
            "customers":customers,
            "captypes":captypes,
            "users":users,
            "capcolors":capcolors,
            "capeyebrows":capeyebrows,
            "versionnumbers":versionnumbers,
            "afterdeductions":afterdeductions,
            "productionworkshops":productionworkshops,
            "order_number":order_number,
            "today":datetime.date.today(),
        }
        return render(request=request,template_name="orderadd.html",context=context)

    def post(self,request):
        createorder = CreateOrder()
        order_number = request.POST.get("order_number")
        order_date = request.POST.get("order_date")
        order = createorder.create_order(order_number=order_number,order_date=self.edit_date(order_date))

        image_file = request.FILES.get("add_iamge")
        if image_file:
            order.o_image = image_file

        customer_pk = request.POST.get("customer_pk")
        customer_contack = request.POST.get("customer_contack")
        customer_email = request.POST.get("customer_email")
        if customer_pk and customer_contack and customer_email:
            customer = createorder.query_customer(customer_pk=customer_pk)
            order.o_customer = customer

        captype_pk = request.POST.get("captype")
        if captype_pk:
            captype = createorder.query_captype(captype_pk=captype_pk)
            order.o_captype = captype

        user_pk = request.POST.get("user")
        if user_pk:
            user = createorder.query_user(user_pk=user_pk)
            order.o_user = user

        capcolor_pk = request.POST.get("capcolor")
        if capcolor_pk:
            capcolor = createorder.query_capcolor(capcolor_pk=capcolor_pk)
            order.o_capcolor = capcolor

        embroiderorprint = request.POST.get("embroiderorprint")
        if embroiderorprint:
            order.o_embroiderorprint = embroiderorprint

        capeyebrow_pk = request.POST.get("capeyebrow")
        if capeyebrow_pk:
            capeyebrow = createorder.query_capeyebrow(capeyebrow_pk=capeyebrow_pk)
            order.o_capeyebrow = capeyebrow

        versionnumber_pk = request.POST.get("versionnumber")
        if versionnumber_pk:
            versionnumber = createorder.query_versionnumber(versionnumber_pk=versionnumber_pk)
            order.o_versionnumber = versionnumber

        afterdeduction_pk = request.POST.get("afterdeduction")
        if afterdeduction_pk:
            afterdeduction = createorder.query_afterdeduction(afterdeduction_pk=afterdeduction_pk)
            order.o_afterdeduction = afterdeduction

        pi_amount = request.POST.get("pi_amount")
        pi_unit_price = request.POST.get("pi_unit_price")
        pi_date = request.POST.get("pi_date")
        pi_price_type = pi_unit_price[0]
        productinfo = ProductInfo()
        productinfo.pi_id = uuid.uuid1()
        if pi_amount:
            productinfo.pi_amount = pi_amount
        if len(pi_unit_price) > 1:
            productinfo.pi_unit_price = pi_unit_price[1:]
        if pi_date:
            productinfo.pi_date = pi_date
        productinfo.pi_price_type = pi_price_type
        productinfo.save()
        order.o_productinfo = productinfo

        pp_sample_order_date = request.POST.get("pp_sample_order_date")
        pp_sample_arrival_date = request.POST.get("pp_sample_arrival_date")
        pp_sample_express_date = request.POST.get("pp_sample_express_date")
        pp_customer_feedback = request.POST.get("pp_customer_feedback")
        pp_corrective_information = request.POST.get("pp_corrective_information")
        pp_Modify_sample_order_date = request.POST.get("pp_Modify_sample_order_date")
        pp_Modify_sample_arrival_date = request.POST.get("pp_Modify_sample_arrival_date")
        pp_Modify_sample_express_date = request.POST.get("pp_Modify_sample_express_date")
        proofingprogress = ProofingProgress()
        proofingprogress.pp_id = uuid.uuid1()
        proofingprogress.pp_sample_order_date = self.edit_date(pp_sample_order_date)
        if pp_sample_arrival_date:
            proofingprogress.pp_sample_arrival_date = pp_sample_arrival_date
        if pp_sample_express_date:
            proofingprogress.pp_sample_express_date = pp_sample_express_date
        if pp_customer_feedback:
            proofingprogress.pp_customer_feedback = pp_customer_feedback
        if pp_corrective_information:
            proofingprogress.pp_corrective_information = pp_corrective_information
        if pp_Modify_sample_order_date:
            proofingprogress.pp_Modify_sample_order_date = pp_Modify_sample_order_date
        if pp_Modify_sample_arrival_date:
            proofingprogress.pp_Modify_sample_arrival_date = pp_Modify_sample_arrival_date
        if pp_Modify_sample_express_date:
            proofingprogress.pp_Modify_sample_express_date = pp_Modify_sample_express_date
        proofingprogress.save()
        order.o_proofingprogress = proofingprogress

        workshop_pk = request.POST.get("pw_workshop")
        ps_order_date = request.POST.get("ps_order_date")
        ps_arrival_date = request.POST.get("ps_arrival_date")
        ps_tailor_date = request.POST.get("ps_tailor_date")
        ps_embroider_date = request.POST.get("ps_embroider_date")
        ps_print_date = request.POST.get("ps_print_date")
        ps_Water_washing_date = request.POST.get("ps_Water_washing_date")
        ps_sewing_date = request.POST.get("ps_sewing_date")
        ps_qc_date = request.POST.get("ps_qc_date")
        ps_outward_transport_date = request.POST.get("ps_outward_transport_date")
        ps_gathering_date = request.POST.get("ps_gathering_date")
        ps_gathering_price = request.POST.get("ps_gathering_price")
        ps_contract_balance = request.POST.get("ps_contract_balance")
        productionschedule = ProductionSchedule()
        productionschedule.ps_id = uuid.uuid1()
        if ps_order_date:
            productionschedule.ps_order_date = ps_order_date
        if ps_arrival_date:
            productionschedule.ps_arrival_date = ps_arrival_date
        if ps_tailor_date:
            productionschedule.ps_tailor_date = ps_tailor_date
        if ps_embroider_date:
            productionschedule.ps_embroider_date = ps_embroider_date
        if ps_print_date:
            productionschedule.ps_print_date = ps_print_date
        if ps_Water_washing_date:
            productionschedule.ps_Water_washing_date = ps_Water_washing_date
        if ps_sewing_date:
            productionschedule.ps_sewing_date = ps_sewing_date
        if ps_qc_date:
            productionschedule.ps_qc_date = ps_qc_date
        if ps_outward_transport_date:
            productionschedule.ps_outward_transport_date = ps_outward_transport_date
        if ps_gathering_date:
            productionschedule.ps_gathering_date = ps_gathering_date
        productionschedule.ps_price_type = ps_gathering_price[0]
        if len(ps_gathering_price) > 1:
            productionschedule.ps_gathering_price = ps_gathering_price[1:]
        if len(ps_contract_balance) > 1:
            productionschedule.ps_contract_balance = ps_contract_balance[1:]
        if workshop_pk:
            workshop = createorder.query_workshop(workshop_pk=workshop_pk)
            productionschedule.ps_workshop = workshop
        productionschedule.save()
        order.o_productionschedule = productionschedule

        order.save()
        return redirect("/order/orderlist")