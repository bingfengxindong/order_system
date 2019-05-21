from order_information.models import *
from production_schedule.models import *
from proofing_progress.models import *
import uuid

class CreateOrder:
    def create_order(self,order_number,order_date):
        return Order.objects.create(o_id=uuid.uuid1(),
                                    o_number=order_number,
                                    o_date=order_date)

    def query_customer(self,customer_pk):
        return Customer.objects.get(pk=customer_pk)

    def query_captype(self,captype_pk):
        return CapType.objects.get(pk=captype_pk)

    def query_user(self,user_pk):
        return User.objects.get(pk=user_pk)

    def query_capcolor(self,capcolor_pk):
        return CapColor.objects.get(pk=capcolor_pk)

    def query_capeyebrow(self,capeyebrow_pk):
        return CapEyebrow.objects.get(pk=capeyebrow_pk)

    def query_versionnumber(self,versionnumber_pk):
        return VersionNumber.objects.get(pk=versionnumber_pk)

    def query_afterdeduction(self,afterdeduction_pk):
        return AfterDeduction.objects.get(pk=afterdeduction_pk)

    def query_workshop(self,workshop_pk):
        return ProductionWorkshop.objects.get(pk=workshop_pk)