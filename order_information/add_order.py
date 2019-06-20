from .models import *

class AddOrder:
    def __init__(self,order,createorder):
        self.order = order
        self.createorder = createorder

    def add_order_proofingprogress_number(self,order_proofingprogress_number):
        if order_proofingprogress_number:
            self.order.o_proofingprogress_number = order_proofingprogress_number

    def add_pricetype(self,pricetype_pk):
        if pricetype_pk:
            pricetype = self.createorder.query_pricetype(pricetype_pk=pricetype_pk)
            self.order.o_price_type = pricetype

    def add_image_file(self,image_file):
        if image_file:
            self.order.o_image = image_file

    def add_customer(self,customer_pk,customer_contack,customer_email):
        if customer_pk and customer_contack and customer_email:
            customer = self.createorder.query_customer(customer_pk=customer_pk)
            self.order.o_customer = customer

    def add_captype(self,captype_pk):
        if captype_pk:
            captype = self.createorder.query_captype(captype_pk=captype_pk)
            self.order.o_captype = captype

    def add_user(self,user_pk):
        if user_pk:
            user = self.createorder.query_user(user_pk=user_pk)
            self.order.o_user = user

    def add_capcolors(self,capcolor_pks):
        if len(capcolor_pks) != 0:
            capcolors = CapColor.objects.filter(pk__in=capcolor_pks)
            self.order.o_capcolor.add(*capcolors)

    def add_embroiderorprint(self,embroiderorprint_pk):
        if embroiderorprint_pk:
            embroiderorprint = EmbroiderOrPrint.objects.get(pk=embroiderorprint_pk)
            self.order.o_embroiderorprint = embroiderorprint

    def add_capeyebrow(self,capeyebrow_pk):
        if capeyebrow_pk:
            capeyebrow = self.createorder.query_capeyebrow(capeyebrow_pk=capeyebrow_pk)
            self.order.o_capeyebrow = capeyebrow

    def add_versionnumber(self,versionnumber_pk):
        if versionnumber_pk:
            versionnumber = self.createorder.query_versionnumber(versionnumber_pk=versionnumber_pk)
            self.order.o_versionnumber = versionnumber

    def add_afterdeduction(self,afterdeduction_pk):
        if afterdeduction_pk:
            afterdeduction = self.createorder.query_afterdeduction(afterdeduction_pk=afterdeduction_pk)
            self.order.o_afterdeduction = afterdeduction

    def add_productinfo(self,**kwargs):
        if kwargs["pi_amount"]:
            kwargs["productinfo"].pi_amount = kwargs["pi_amount"]
        if kwargs["pi_unit_price"]:
            kwargs["productinfo"].pi_unit_price = kwargs["pi_unit_price"]
        if kwargs["pi_date"]:
            kwargs["productinfo"].pi_date = self.edit_date(kwargs["pi_date"])
        if kwargs["pi_total_price"]:
            kwargs["productinfo"].pi_total_price = kwargs["pi_total_price"]

        if kwargs["pi_offer"]:
            kwargs["productinfo"].pi_offer = kwargs["pi_offer"]
        if kwargs["pi_fabric_quotation"]:
            kwargs["productinfo"].pi_fabric_quotation = kwargs["pi_fabric_quotation"]
        if kwargs["pi_ingredients_quotation"]:
            kwargs["productinfo"].pi_ingredients_quotation = kwargs["pi_ingredients_quotation"]
        if kwargs["pi_labor_payment_quotation"]:
            kwargs["productinfo"].pi_labor_payment_quotation = kwargs["pi_labor_payment_quotation"]
        if kwargs["pi_water_washing_quotation"]:
            kwargs["productinfo"].pi_water_washing_quotation = kwargs["pi_water_washing_quotation"]
        if kwargs["pi_print_quotation"]:
            kwargs["productinfo"].pi_print_quotation = kwargs["pi_print_quotation"]
        if kwargs["pi_embroider_quotation"]:
            kwargs["productinfo"].pi_embroider_quotation = kwargs["pi_embroider_quotation"]
        if kwargs["pi_packaging_quotation"]:
            kwargs["productinfo"].pi_packaging_quotation = kwargs["pi_packaging_quotation"]
        if kwargs["pi_other_quotation"]:
            kwargs["productinfo"].pi_other_quotation = kwargs["pi_other_quotation"]
        if kwargs["pi_reserved_profits"]:
            kwargs["productinfo"].pi_reserved_profits = kwargs["pi_reserved_profits"]
        kwargs["productinfo"].save()

    def add_proofingprogress(self,**kwargs):
        if kwargs["pp_sample_order_date"]:
            kwargs["proofingprogress"].pp_sample_order_date = self.edit_date(kwargs["pp_sample_order_date"])
        if kwargs["pp_sample_arrival_date"]:
            kwargs["proofingprogress"].pp_sample_arrival_date = self.edit_date(kwargs["pp_sample_arrival_date"])
        if kwargs["pp_sample_express_date"]:
            kwargs["proofingprogress"].pp_sample_express_date = self.edit_date(kwargs["pp_sample_express_date"])
        if kwargs["pp_customer_feedback"]:
            kwargs["proofingprogress"].pp_customer_feedback = kwargs["pp_customer_feedback"]
        if kwargs["pp_corrective_information"]:
            kwargs["proofingprogress"].pp_corrective_information = kwargs["pp_corrective_information"]
        kwargs["proofingprogress"].save()

    def add_productionschedule(self,**kwargs):
        if kwargs["ps_order_date"]:
            kwargs["productionschedule"].ps_order_date = self.edit_date(kwargs["ps_order_date"])
        if kwargs["ps_number"]:
            kwargs["productionschedule"].ps_number = kwargs["ps_number"]
        if kwargs["ps_arrival_date"]:
            kwargs["productionschedule"].ps_arrival_date = self.edit_date(kwargs["ps_arrival_date"])
        if kwargs["ps_tailor_date"]:
            kwargs["productionschedule"].ps_tailor_date = self.edit_date(kwargs["ps_tailor_date"])
        if kwargs["ps_embroider_date"]:
            kwargs["productionschedule"].ps_embroider_date = self.edit_date(kwargs["ps_embroider_date"])
        if kwargs["ps_print_date"]:
            kwargs["productionschedule"].ps_print_date = self.edit_date(kwargs["ps_print_date"])
        if kwargs["ps_water_washing_date"]:
            kwargs["productionschedule"].ps_water_washing_date = self.edit_date(kwargs["ps_water_washing_date"])
        if kwargs["ps_sewing_date"]:
            kwargs["productionschedule"].ps_sewing_date = self.edit_date(kwargs["ps_sewing_date"])
        if kwargs["ps_qc_date"]:
            kwargs["productionschedule"].ps_qc_date = self.edit_date(kwargs["ps_qc_date"])
        if kwargs["ps_outward_transport_date"]:
            kwargs["productionschedule"].ps_outward_transport_date = self.edit_date(kwargs["ps_outward_transport_date"])
        if kwargs["ps_gathering_date"]:
            kwargs["productionschedule"].ps_gathering_date = self.edit_date(kwargs["ps_gathering_date"])
        if kwargs["ps_gathering_price"]:
            kwargs["productionschedule"].ps_gathering_price = kwargs["ps_gathering_price"]
        if kwargs["ps_contract_balance"]:
            kwargs["productionschedule"].ps_contract_balance = kwargs["ps_contract_balance"]
        if kwargs["workshop_pk"]:
            workshop = self.createorder.query_workshop(workshop_pk=kwargs["workshop_pk"])
            kwargs["productionschedule"].ps_workshop = workshop
        kwargs["productionschedule"].save()

    def add_accountingdocuments(self,**kwargs):
        if kwargs["ad_total_profit"]:
            kwargs["accountingdocuments"].ad_total_profit = kwargs["ad_total_profit"]

        if kwargs["ad_fabric_ingredients_total_amount"]:
            kwargs["accountingdocuments"].ad_fabric_ingredients_total_amount = kwargs["ad_fabric_ingredients_total_amount"]
        if kwargs["ad_fabric_amount"]:
            kwargs["accountingdocuments"].ad_fabric_amount = kwargs["ad_fabric_amount"]
        if kwargs["ad_fabric_express_amount"]:
            kwargs["accountingdocuments"].ad_fabric_express_amount = kwargs["ad_fabric_express_amount"]
        if kwargs["ad_bonding_amount"]:
            kwargs["accountingdocuments"].ad_bonding_amount = kwargs["ad_bonding_amount"]
        if kwargs["ad_ingredients_amount"]:
            kwargs["accountingdocuments"].ad_ingredients_amount = kwargs["ad_ingredients_amount"]
        if kwargs["ad_ingredients_express_amount"]:
            kwargs["accountingdocuments"].ad_ingredients_express_amount = kwargs["ad_ingredients_express_amount"]
        if kwargs["ad_fabric_ingredients_other_amount"]:
            kwargs["accountingdocuments"].ad_fabric_ingredients_other_amount = kwargs["ad_fabric_ingredients_other_amount"]

        if kwargs["ad_labor_paymentl_amount"]:
            kwargs["accountingdocuments"].ad_labor_paymentl_amount = kwargs["ad_totalad_labor_paymentl_amount_profit"]
        if kwargs["ad_tailor_total_amount"]:
            kwargs["accountingdocuments"].ad_tailor_total_amount = kwargs["ad_tailor_total_amount"]
        if kwargs["ad_tailor_start_date"]:
            kwargs["accountingdocuments"].ad_tailor_start_date = self.edit_date(kwargs["ad_tailor_start_date"])
        if kwargs["ad_tailor_end_date"]:
            kwargs["accountingdocuments"].ad_tailor_end_date = self.edit_date(kwargs["ad_tailor_end_date"])
        if kwargs["ad_tailor_number_people"]:
            kwargs["accountingdocuments"].ad_tailor_number_people = kwargs["ad_tailor_number_people"]
        if kwargs["ad_sewing_total_amount"]:
            kwargs["accountingdocuments"].ad_sewing_total_amount = kwargs["ad_sewing_total_amount"]
        if kwargs["ad_sewing_start_date"]:
            kwargs["accountingdocuments"].ad_sewing_start_date = self.edit_date(kwargs["ad_sewing_start_date"])
        if kwargs["ad_sewing_end_date"]:
            kwargs["accountingdocuments"].ad_sewing_end_date = self.edit_date(kwargs["ad_sewing_end_date"])
        if kwargs["ad_sewing_number_people"]:
            kwargs["accountingdocuments"].ad_sewing_number_people = kwargs["ad_sewing_number_people"]
        if kwargs["ad_iron_total_amount"]:
            kwargs["accountingdocuments"].ad_iron_total_amount = kwargs["ad_iron_total_amount"]
        if kwargs["ad_iron_start_date"]:
            kwargs["accountingdocuments"].ad_iron_start_date = self.edit_date(kwargs["ad_iron_start_date"])
        if kwargs["ad_iron_end_date"]:
            kwargs["accountingdocuments"].ad_iron_end_date = self.edit_date(kwargs["ad_iron_end_date"])
        if kwargs["ad_iron_number_people"]:
            kwargs["accountingdocuments"].ad_iron_number_people = kwargs["ad_iron_number_people"]

        if kwargs["ad_embroide_print_amount"]:
            kwargs["accountingdocuments"].ad_embroide_print_amount = kwargs["ad_embroide_print_amount"]
        if kwargs["ad_water_washing_amount"]:
            kwargs["accountingdocuments"].ad_water_washing_amount = kwargs["ad_water_washing_amount"]
        if kwargs["ad_embroide_amount"]:
            kwargs["accountingdocuments"].ad_embroide_amount = kwargs["ad_embroide_amount"]
        if kwargs["ad_print_amount"]:
            kwargs["accountingdocuments"].ad_print_amount = kwargs["ad_print_amount"]

        if kwargs["ad_packaging_shipping_amount"]:
            kwargs["accountingdocuments"].ad_packaging_shipping_amount = kwargs["ad_packaging_shipping_amount"]
        if kwargs["ad_paperboard_amount"]:
            kwargs["accountingdocuments"].ad_paperboard_amount = kwargs["ad_paperboard_amount"]
        if kwargs["ad_physical_distribution_amount"]:
            kwargs["accountingdocuments"].ad_physical_distribution_amount = kwargs["ad_physical_distribution_amount"]
        if kwargs["ad_warehouse_entry_amount"]:
            kwargs["accountingdocuments"].ad_warehouse_entry_amount = kwargs["ad_warehouse_entry_amount"]
        if kwargs["ad_customs_declaration_amount"]:
            kwargs["accountingdocuments"].ad_customs_declaration_amount = kwargs["ad_customs_declaration_amount"]
        kwargs["accountingdocuments"].save()


    def edit_date(self,date):
        try:
            ed = date.replace("年","-").replace("月","-").replace("日","")
        except:
            return
        else:
            return ed