from django.db import models

# Create your models here.
class ProofingProgress(models.Model):
    pp_id = models.UUIDField(verbose_name="编号")
    pp_sample_order_date = models.DateField(blank=True,null=True,verbose_name="下单时间")
    pp_sample_arrival_date = models.DateField(blank=True,null=True,verbose_name="到料时间")
    pp_sample_express_date = models.DateField(blank=True,null=True,verbose_name="快递时间")
    pp_customer_feedback = models.TextField(blank=True,null=True,verbose_name="客人反馈信息")
    pp_corrective_information = models.TextField(blank=True,null=True,verbose_name="整改信息")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.pp_id)

    class Meta:
        ordering = ["pk"]
        verbose_name = "打样进度表"
        verbose_name_plural = "打样进度表"