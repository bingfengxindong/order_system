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
        search_type = request.GET.get("st","a")

        if search_type == "pp":
            orders = [i for i in Order.objects.all() if i.o_proofingprogress.pp_sample_order_date and not i.o_proofingprogress.pp_sample_express_date]
        elif search_type == "ps":
            orders = [i for i in Order.objects.all() if i.o_productionschedule.ps_order_date and not i.o_productionschedule.ps_outward_transport_date]
        elif search_type == "cp":
            orders = [i for i in Order.objects.all() if i.o_productionschedule.ps_outward_transport_date and not i.o_productionschedule.ps_gathering_date]
        elif search_type == "sc":
            order_date = request.GET.get("od")
            order_end_date = request.GET.get("oed")
            number = request.GET.get("on")
            customername = request.GET.get("cn")
            captype_pk = int(request.GET.get("cp",0))
            user_pk = int(request.GET.get("up",0))
            pw_workshop_pk = int(request.GET.get("pwp",0))
            orders = Order.objects.filter()
            if order_date != "" and order_end_date != "":
                orders = Order.objects.filter(o_date__range=(order_date,order_end_date))
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
        else:
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
            "search_type": search_type,
            "captypes": captypes,
            "users": users,
            "productionworkshops": productionworkshops,
        }
        if search_type == "sc":
            context["order_date"] = order_date
            context["order_end_date"] = order_end_date
            context["number"] = number
            context["customername"] = customername
            context["captype_pk"] = captype_pk
            context["user_pk"] = user_pk
            context["pw_workshop_pk"] = pw_workshop_pk
            if captype_pk != 0:
                context["captype"] = CapType.objects.get(pk=captype_pk)
            if user_pk != 0:
                context["user"] = User.objects.get(pk=user_pk)
            if pw_workshop_pk != 0:
                context["pw_workshop"] = ProductionWorkshop.objects.get(pk=pw_workshop_pk)
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
        addorder = AddOrder(order, createorder)
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
        productinfo = order.o_productinfo
        productinfo.pi_id = uuid.uuid1()
        addorder.add_productinfo(productinfo=productinfo,
                                 pi_amount=pi_amount,
                                 pi_unit_price=pi_unit_price,
                                 pi_date=pi_date,)

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
        ps_order_date = self.edit_date(request.POST.get("ps_order_date"))
        ps_arrival_date = self.edit_date(request.POST.get("ps_arrival_date"))
        ps_tailor_date = self.edit_date(request.POST.get("ps_tailor_date"))
        ps_embroider_date = self.edit_date(request.POST.get("ps_embroider_date"))
        ps_print_date = self.edit_date(request.POST.get("ps_print_date"))
        ps_water_washing_date = self.edit_date(request.POST.get("ps_water_washing_date"))
        ps_sewing_date = self.edit_date(request.POST.get("ps_sewing_date"))
        ps_qc_date = self.edit_date(request.POST.get("ps_qc_date"))
        ps_outward_transport_date = self.edit_date(request.POST.get("ps_outward_transport_date"))
        ps_gathering_date = self.edit_date(request.POST.get("ps_gathering_date"))
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
        order.save()
        return redirect("/order/orderlist")

class OrderAdd(View):
    def ordernumber(self):
        try:
            last_order_number = str(int(Order.objects.filter().order_by("-pk")[0].o_number.split("-")[-1]) + 1)
        except:
            last_order_number = "100"
        last_order_number_len = len(last_order_number)
        return "{}{}".format("0"*(4 - last_order_number_len),last_order_number)

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
        # order_number = "FW19-{}".format(self.ordernumber())
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
            # "order_number":order_number,
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
        print(pricetype_pk)
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
        productinfo = ProductInfo()
        productinfo.pi_id = uuid.uuid1()
        addorder.add_productinfo(productinfo=productinfo,
                                 pi_amount=pi_amount,
                                 pi_unit_price=pi_unit_price,
                                 pi_date=pi_date, )
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

        order.save()
        return redirect("/order/orderlist")