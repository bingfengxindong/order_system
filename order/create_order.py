from order.models import *
import uuid

class CreateOrder:
    def createorder(self,**kwargs):
        order = Order.objects.create(o_id=uuid.uuid1(),
                                     o_customer_id=kwargs["customer_pk"],
                                     o_customer_number=kwargs["o_customer_number"])
        return order

    def addorderinfo(self,**kwargs):
        order = kwargs["order"]
        if kwargs["o_date"]:
           order.o_date = kwargs["o_date"]
        if kwargs["o_count"]:
           order.o_count = kwargs["o_count"]
        if kwargs["o_image"]:
           order.o_image = kwargs["o_image"]
        if kwargs["o_file"]:
           order.o_file = kwargs["o_file"]
        if kwargs["o_main_fabric"]:
           order.o_main_fabric = kwargs["o_main_fabric"]
        if kwargs["o_ps_price"]:
           order.o_ps_price = kwargs["o_ps_price"]
        if kwargs["o_dollar_exchange_rate"]:
           order.o_dollar_exchange_rate = kwargs["o_dollar_exchange_rate"]
        if kwargs["o_dollar_price"]:
           order.o_dollar_price = kwargs["o_dollar_price"]
        if kwargs["o_ps_amount"]:
           order.o_ps_amount = kwargs["o_ps_amount"]
        if kwargs["o_ps_dollar_total_price"]:
           order.o_ps_dollar_total_price = kwargs["o_ps_dollar_total_price"]
        if kwargs["o_delivery_date"]:
           order.o_delivery_date = kwargs["o_delivery_date"]
        if order.o_quotation.q_offer and kwargs["o_ps_amount"]:
            accountingdocuments = order.o_accountingdocuments
            accountingdocuments.ad_ps_dollar_total_price = "%.2f" % (float(order.o_quotation.q_offer) * float(kwargs["o_ps_amount"]))
            accountingdocuments.save()
        order.save()

    def add_user(self,order,user_pk):
        order.o_user_id = user_pk

    def add_capcolor(self,order,capcolor_pks):
        for capcolor_pk in capcolor_pks:
            capcolor = CapColor.objects.get(pk=capcolor_pk)
            order.o_capcolor.add(capcolor)

    def add_captype(self,order,captype_pk):
        order.o_captype_id = captype_pk

    def add_embroidererprint(self,order,embroidererprint_pk):
        order.o_embroiderorprint_id = embroidererprint_pk

    def add_capeyebrow(self,order,capeyebrow_pk):
        order.o_capeyebrow_id = capeyebrow_pk

    def add_versionnumber(self,order,versionnumber_pk):
        order.o_versionnumber_id = versionnumber_pk

    def add_afterdeduction(self,order,afterdeduction_pk):
        order.o_afterdeduction_id = afterdeduction_pk

    def edit_customer(self,order,customer_pk):
        order.o_customer_id = customer_pk

    def edit_customer_number(self,order,o_customer_number):
        order.o_customer_number = o_customer_number