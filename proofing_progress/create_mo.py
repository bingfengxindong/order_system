from proofing_progress.models import *
import uuid

class CreateMO:
    def __init__(self,order):
        self.order = order

    def add_mo(self):
        return ModifyOpinion.objects.create(mo_id=uuid.uuid1())

    def edit_mo(self,pk):
        return ModifyOpinion.objects.get(pk=pk)

    def add_mo_customer_info(self,modifyopinion,mo_customer_info):
        modifyopinion.mo_customer_info = mo_customer_info

    def add_mo_factory_info(self,modifyopinion,mo_factory_info):
        modifyopinion.mo_factory_info = mo_factory_info