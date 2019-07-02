from django.db import models

class ProofingProgress(models.Model):
    pp_id = models.UUIDField(verbose_name="编号")
    pp_number = models.CharField(max_length=200,blank=True,null=True,verbose_name="样品单号")
    pp_erp_number = models.CharField(max_length=200,blank=True,null=True,verbose_name="ERP单号")
    pp_date = models.DateField(blank=True,null=True,verbose_name="接单时间")
    pp_delivery_date = models.DateField(blank=True,null=True,verbose_name="交货日期")
    pp_main_fabric_arrival = models.DateField(blank=True,null=True,verbose_name="主料到货")
    pp_ingredients_fabric_arrival = models.DateField(blank=True,null=True,verbose_name="辅料到货")
    pp_tailor_date = models.DateField(blank=True,null=True,verbose_name="裁剪日期")
    pp_send_embroide = models.DateField(blank=True,null=True,verbose_name="送绣花")
    pp_receive_embroide = models.DateField(blank=True,null=True,verbose_name="绣花回")
    pp_send_print = models.DateField(blank=True,null=True,verbose_name="送印花")
    pp_receive_print = models.DateField(blank=True,null=True,verbose_name="印花回")
    pp_delivery_proofing = models.DateField(blank=True,null=True,verbose_name="发样品")
    pp_end_date = models.DateField(blank=True,null=True,verbose_name="完成日期")
    pp_express_date = models.DateField(blank=True,null=True,verbose_name="快递时间")

    pp_worker = models.ForeignKey("Worker", blank=True, null=True, on_delete=models.CASCADE, verbose_name="操作工")
    pp_end = models.BooleanField(default=False,verbose_name="本次打样是否完成/默认未完成")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.pp_number)

    class Meta:
        ordering = ["pk"]
        verbose_name = "打样表"
        verbose_name_plural = "打样表"

class Worker(models.Model):
    w_id = models.UUIDField(verbose_name="编号")
    w_worker = models.CharField(max_length=200,blank=True,null=True,verbose_name="操作工")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.w_worker)

    class Meta:
        ordering = ["pk"]
        verbose_name = "操作工表"
        verbose_name_plural = "操作工表"

class ModifyOpinion(models.Model):
    mo_id = models.UUIDField(verbose_name="编号")
    mo_customer_info = models.TextField(blank=True,null=True,verbose_name="客人反馈信息")
    mo_factory_info = models.TextField(blank=True,null=True,verbose_name="工厂修改信息")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.mo_customer_info)

    class Meta:
        ordering = ["pk"]
        verbose_name = "打样修改意见表"
        verbose_name_plural = "打样修改意见表"