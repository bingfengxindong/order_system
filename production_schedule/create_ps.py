from production_schedule.models import *
import uuid

class CreatePS:
    def add_ps(self):
        return ProductionSchedule.objects.create(ps_id=uuid.uuid1())

    def add_ps_number(self,productionschedule,ps_number):
        productionschedule.ps_number = ps_number

    def add_ps_date(self,productionschedule,ps_date):
        productionschedule.ps_date = ps_date

    def add_workshop(self,productionschedule,workshop):
        productionschedule.ps_workshop_id = workshop

    def add_ps_confirm_date(self,productionschedule,ps_confirm_date):
        productionschedule.ps_confirm_date = ps_confirm_date

    def add_ps_arrival_date(self,productionschedule,ps_arrival_date):
        productionschedule.ps_arrival_date = ps_arrival_date

    def add_ps_tailor_date(self,productionschedule,ps_tailor_date):
        productionschedule.ps_tailor_date = ps_tailor_date

    def add_ps_embroider_date(self,productionschedule,ps_embroider_date):
        productionschedule.ps_embroider_date = ps_embroider_date

    def add_ps_print_date(self,productionschedule,ps_print_date):
        productionschedule.ps_print_date = ps_print_date

    def add_ps_water_washing_date(self,productionschedule,ps_water_washing_date):
        productionschedule.ps_water_washing_date = ps_water_washing_date

    def add_ps_sewing_date(self,productionschedule,ps_sewing_date):
        productionschedule.ps_sewing_date = ps_sewing_date

    def add_ps_ingredients_fabric_arrival_date(self,productionschedule,ps_ingredients_fabric_arrival_date):
        productionschedule.ps_ingredients_fabric_arrival_date = ps_ingredients_fabric_arrival_date

    def add_ps_tags_arrival_date(self,productionschedule,ps_tags_arrival_date):
        productionschedule.ps_tags_arrival_date = ps_tags_arrival_date

    def add_ps_iron_package_date(self,productionschedule,ps_iron_package_date):
        productionschedule.ps_iron_package_date = ps_iron_package_date

    def add_ps_outward_transport_date(self,productionschedule,ps_outward_transport_date):
        productionschedule.ps_outward_transport_date = ps_outward_transport_date

    def add_ps_gathering_date(self,productionschedule,ps_gathering_date):
        productionschedule.ps_gathering_date = ps_gathering_date

    def add_ps_gathering_price(self,productionschedule,ps_gathering_price):
        productionschedule.ps_gathering_price = ps_gathering_price

    def add_ps_contract_balance(self,productionschedule,ps_contract_balance):
        productionschedule.ps_contract_balance = ps_contract_balance