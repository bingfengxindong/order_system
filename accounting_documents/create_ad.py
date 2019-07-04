from accounting_documents.models import AccountingDocuments
import uuid

class CreateAD:
    def add_ad(self):
        return AccountingDocuments.objects.create(ad_id=uuid.uuid1())

    def add_ad_ps_dollar_total_price(self,accountingdocuments,ad_ps_dollar_total_price):
        accountingdocuments.ad_ps_dollar_total_price = ad_ps_dollar_total_price

    def add_ad_actual_cost(self,accountingdocuments,ad_actual_cost):
        accountingdocuments.ad_actual_cost = ad_actual_cost

    def add_ad_total_profit(self,accountingdocuments,ad_total_profit):
        accountingdocuments.ad_total_profit = ad_total_profit

    def add_ad_total_amount_materials(self,accountingdocuments,ad_total_amount_materials):
        accountingdocuments.ad_total_amount_materials = ad_total_amount_materials

    def add_ad_total_amount_fabric(self,accountingdocuments,ad_total_amount_fabric):
        accountingdocuments.ad_total_amount_fabric = ad_total_amount_fabric

    def add_ad_total_amount_fabric_express(self,accountingdocuments,ad_total_amount_fabric_express):
        accountingdocuments.ad_total_amount_fabric_express = ad_total_amount_fabric_express

    def add_ad_total_amount_bonding(self,accountingdocuments,ad_total_amount_bonding):
        accountingdocuments.ad_total_amount_bonding = ad_total_amount_bonding

    def add_ad_total_amount_ingredients(self,accountingdocuments,ad_total_amount_ingredients):
        accountingdocuments.ad_total_amount_ingredients = ad_total_amount_ingredients

    def add_ad_total_amount_ingredients_express(self,accountingdocuments,ad_total_amount_ingredients_express):
        accountingdocuments.ad_total_amount_ingredients_express = ad_total_amount_ingredients_express

    def add_ad_total_amount_other(self,accountingdocuments,ad_total_amount_other):
        accountingdocuments.ad_total_amount_other = ad_total_amount_other

    def add_ad_total_amount_labor_payment(self,accountingdocuments,ad_total_amount_labor_payment):
        accountingdocuments.ad_total_amount_labor_payment = ad_total_amount_labor_payment

    def add_ad_total_amount_tailor(self,accountingdocuments,ad_total_amount_tailor):
        accountingdocuments.ad_total_amount_tailor = ad_total_amount_tailor

    def add_ad_tailor_start_date(self,accountingdocuments,ad_tailor_start_date):
        accountingdocuments.ad_tailor_start_date = ad_tailor_start_date

    def add_ad_tailor_end_date(self,accountingdocuments,ad_tailor_end_date):
        accountingdocuments.ad_tailor_end_date = ad_tailor_end_date

    def add_ad_tailor_number_people(self,accountingdocuments,ad_tailor_number_people):
        accountingdocuments.ad_tailor_number_people = ad_tailor_number_people

    def add_ad_total_amount_sewing(self,accountingdocuments,ad_total_amount_sewing):
        accountingdocuments.ad_total_amount_sewing = ad_total_amount_sewing

    def add_ad_sewing_start_date(self,accountingdocuments,ad_sewing_start_date):
        accountingdocuments.ad_sewing_start_date = ad_sewing_start_date

    def add_ad_sewing_end_date(self,accountingdocuments,ad_sewing_end_date):
        accountingdocuments.ad_sewing_end_date = ad_sewing_end_date

    def add_ad_sewing_number_people(self,accountingdocuments,ad_sewing_number_people):
        accountingdocuments.ad_sewing_number_people = ad_sewing_number_people

    def add_ad_total_amount_iron(self,accountingdocuments,ad_total_amount_iron):
        accountingdocuments.ad_total_amount_iron = ad_total_amount_iron

    def add_ad_iron_start_date(self,accountingdocuments,ad_iron_start_date):
        accountingdocuments.ad_iron_start_date = ad_iron_start_date

    def add_ad_iron_end_date(self,accountingdocuments,ad_iron_end_date):
        accountingdocuments.ad_iron_end_date = ad_iron_end_date

    def add_ad_iron_number_people(self,accountingdocuments,ad_iron_number_people):
        accountingdocuments.ad_iron_number_people = ad_iron_number_people

    def add_ad_total_amount_embroide_print(self,accountingdocuments,ad_total_amount_embroide_print):
        accountingdocuments.ad_total_amount_embroide_print = ad_total_amount_embroide_print

    def add_ad_total_amount_water_washing(self,accountingdocuments,ad_total_amount_water_washing):
        accountingdocuments.ad_total_amount_water_washing = ad_total_amount_water_washing

    def add_ad_total_amount_embroide(self,accountingdocuments,ad_total_amount_embroide):
        accountingdocuments.ad_total_amount_embroide = ad_total_amount_embroide

    def add_ad_total_amount_print(self,accountingdocuments,ad_total_amount_print):
        accountingdocuments.ad_total_amount_print = ad_total_amount_print

    def add_ad_total_amount_packaging_shipping(self,accountingdocuments,ad_total_amount_packaging_shipping):
        accountingdocuments.ad_total_amount_packaging_shipping = ad_total_amount_packaging_shipping

    def add_ad_total_amount_paperboard(self,accountingdocuments,ad_total_amount_paperboard):
        accountingdocuments.ad_total_amount_paperboard = ad_total_amount_paperboard

    def add_ad_total_amount_physical_distribution(self,accountingdocuments,ad_total_amount_physical_distribution):
        accountingdocuments.ad_total_amount_physical_distribution = ad_total_amount_physical_distribution

    def add_ad_total_amount_warehouse_entry(self,accountingdocuments,ad_total_amount_warehouse_entry):
        accountingdocuments.ad_total_amount_warehouse_entry = ad_total_amount_warehouse_entry

    def add_ad_total_amount_customs_declaration(self,accountingdocuments,ad_total_amount_customs_declaration):
        accountingdocuments.ad_total_amount_customs_declaration = ad_total_amount_customs_declaration