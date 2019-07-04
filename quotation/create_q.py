from quotation.models import Quotation
import uuid

class CreateQ:
    def add_quotation(self):
        return Quotation.objects.create(q_id=uuid.uuid1())

    def add_q_offer(self,quotation,q_offer):
        quotation.q_offer = q_offer

    def add_q_floating_rate(self,quotation,q_floating_rate):
        quotation.q_floating_rate = q_floating_rate

    def add_q_end_offer(self,quotation,q_end_offer):
        quotation.q_end_offer = q_end_offer

    def add_q_fabric_quotation(self,quotation,q_fabric_quotation):
        quotation.q_fabric_quotation = q_fabric_quotation

    def add_q_ingredients_quotation(self,quotation,q_ingredients_quotation):
        quotation.q_ingredients_quotation = q_ingredients_quotation

    def add_q_labor_payment_quotation(self,quotation,q_labor_payment_quotation):
        quotation.q_labor_payment_quotation = q_labor_payment_quotation

    def add_q_water_washing_quotation(self,quotation,q_water_washing_quotation):
        quotation.q_water_washing_quotation = q_water_washing_quotation

    def add_q_embroider_quotation(self,quotation,q_embroider_quotation):
        quotation.q_embroider_quotation = q_embroider_quotation

    def add_q_print_quotation(self,quotation,q_print_quotation):
        quotation.q_print_quotation = q_print_quotation

    def add_q_packaging_quotation(self,quotation,q_packaging_quotation):
        quotation.q_packaging_quotation = q_packaging_quotation

    def add_q_other_quotation(self,quotation,q_other_quotation):
        quotation.q_other_quotation = q_other_quotation

    def add_q_reserved_profits(self,quotation,q_reserved_profits):
        quotation.q_reserved_profits = q_reserved_profits