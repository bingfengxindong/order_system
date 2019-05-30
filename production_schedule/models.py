from django.db import models

# Create your models here.
class ProductionWorkshop(models.Model):
    pw_id = models.UUIDField(verbose_name="编号")
    pw_workshop = models.CharField(max_length=200,verbose_name="生产车间")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.pw_workshop)

    class Meta:
        ordering = ["pk"]
        verbose_name = "生产车间"
        verbose_name_plural = "生产车间"

class ProductionSchedule(models.Model):
    ps_id = models.UUIDField(verbose_name="编号")
    ps_number = models.CharField(max_length=200,blank=True,null=True,verbose_name="大货单号")
    ps_order_date = models.DateField(blank=True,null=True,verbose_name="下单时间")
    ps_arrival_date = models.DateField(blank=True,null=True,verbose_name="到料时间")
    ps_tailor_date = models.DateField(blank=True,null=True,verbose_name="裁剪时间")
    ps_embroider_date = models.DateField(blank=True,null=True,verbose_name="绣花时间")
    ps_print_date = models.DateField(blank=True,null=True,verbose_name="印花时间")
    ps_Water_washing_date = models.DateField(blank=True,null=True,verbose_name="水洗时间")
    ps_sewing_date = models.DateField(blank=True,null=True,verbose_name="车缝时间")
    ps_qc_date = models.DateField(blank=True,null=True,verbose_name="QC时间")
    ps_outward_transport_date = models.DateField(blank=True,null=True,verbose_name="外运时间")
    ps_gathering_date = models.DateField(blank=True,null=True,verbose_name="收款时间")
    ps_price_type = models.CharField(blank=True,null=True,max_length=50,verbose_name="金额类型")
    ps_gathering_price = models.CharField(blank=True,null=True,max_length=100,verbose_name="收款金额")
    ps_contract_balance = models.CharField(blank=True,null=True,max_length=100,verbose_name="合同余额")
    ps_workshop = models.ForeignKey(ProductionWorkshop,blank=True,null=True,on_delete=models.CASCADE,verbose_name="生产车间")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ps_contract_balance)

    class Meta:
        ordering = ["pk"]
        verbose_name = "大货进度表"
        verbose_name_plural = "大货进度表"