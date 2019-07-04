from django.db import models

class ProductionSchedule(models.Model):
    ps_id = models.UUIDField(verbose_name="编号")
    ps_number = models.CharField(max_length=200,blank=True,null=True,verbose_name="大货单号")
    ps_date = models.DateField(blank=True,null=True,verbose_name="大货交期")
    ps_confirm_date = models.DateField(blank=True,null=True,verbose_name="大货确认时间")
    ps_arrival_date = models.DateField(blank=True,null=True,verbose_name="面料到货")
    ps_tailor_date = models.DateField(blank=True,null=True,verbose_name="裁剪时间")
    ps_embroider_date = models.DateField(blank=True,null=True,verbose_name="绣花时间")
    ps_print_date = models.DateField(blank=True,null=True,verbose_name="印花时间")
    ps_water_washing_date = models.DateField(blank=True,null=True,verbose_name="水洗时间")
    ps_sewing_date = models.DateField(blank=True,null=True,verbose_name="车缝时间")
    ps_ingredients_fabric_arrival_date = models.DateField(blank=True,null=True,verbose_name="辅料到货")
    ps_tags_arrival_date = models.DateField(blank=True,null=True,verbose_name="吊牌到货")
    ps_iron_package_date = models.DateField(blank=True,null=True,verbose_name="整烫包装")
    ps_outward_transport_date = models.DateField(blank=True,null=True,verbose_name="外运时间")
    ps_gathering_date = models.DateField(blank=True,null=True,verbose_name="收款时间")
    ps_gathering_price = models.CharField(max_length=200, blank=True, null=True, verbose_name="收款金额")
    ps_contract_balance = models.CharField(max_length=200, blank=True, null=True, verbose_name="合同金额")
    ps_workshop = models.OneToOneField("ProductionWorkshop",blank=True,null=True,on_delete=models.CASCADE,verbose_name="生产车间")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ps_number)

    class Meta:
        ordering = ["pk"]
        verbose_name = "大货表"
        verbose_name_plural = "大货表"

class ProductionWorkshop(models.Model):
    pw_id = models.UUIDField(verbose_name="编号")
    pw_workshop = models.CharField(max_length=200, blank=True, null=True, verbose_name="生产车间")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.pw_workshop)

    class Meta:
        ordering = ["pk"]
        verbose_name = "生产车间表"
        verbose_name_plural = "生产车间表"