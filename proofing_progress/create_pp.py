from proofing_progress.models import *
import uuid

class CreatePP:
    def add_pp(self):
        return ProofingProgress.objects.create(pp_id=uuid.uuid1())

    def edit_pp(self,pk):
        return ProofingProgress.objects.get(pk=pk,pp_end=False)

    def add_pp_number(self,proofingprogress,pp_number):
        proofingprogress.pp_number = pp_number

    def add_pp_erp_number(self,proofingprogress,pp_erp_number):
        proofingprogress.pp_erp_number = pp_erp_number

    def add_pp_date(self,proofingprogress,pp_date):
        proofingprogress.pp_date = pp_date

    def add_pp_delivery_date(self,proofingprogress,pp_delivery_date):
        proofingprogress.pp_delivery_date = pp_delivery_date

    def add_pp_main_fabric_arrival(self,proofingprogress,pp_main_fabric_arrival):
        proofingprogress.pp_main_fabric_arrival = pp_main_fabric_arrival

    def add_pp_ingredients_fabric_arrival(self,proofingprogress,pp_ingredients_fabric_arrival):
        proofingprogress.pp_ingredients_fabric_arrival = pp_ingredients_fabric_arrival

    def add_pp_tailor_date(self,proofingprogress,pp_tailor_date):
        proofingprogress.pp_tailor_date = pp_tailor_date

    def add_pp_send_embroide(self,proofingprogress,pp_send_embroide):
        proofingprogress.pp_send_embroide = pp_send_embroide

    def add_pp_receive_embroide(self,proofingprogress,pp_receive_embroide):
        proofingprogress.pp_receive_embroide = pp_receive_embroide

    def add_pp_send_print(self,proofingprogress,pp_send_print):
        proofingprogress.pp_send_print = pp_send_print

    def add_pp_receive_print(self,proofingprogress,pp_receive_print):
        proofingprogress.pp_receive_print = pp_receive_print

    def add_pp_delivery_proofing(self,proofingprogress,pp_delivery_proofing):
        proofingprogress.pp_delivery_proofing = pp_delivery_proofing

    def add_worker_pk(self,proofingprogress,worker_pk):
        proofingprogress.pp_worker_id = worker_pk

    def add_pp_end_date(self,proofingprogress,pp_end_date):
        proofingprogress.pp_end_date = pp_end_date

    def add_pp_express_date(self,proofingprogress,pp_express_date):
        proofingprogress.pp_express_date = pp_express_date