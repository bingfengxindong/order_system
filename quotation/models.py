from django.db import models

class Quotation(models.Model):
    q_id = models.UUIDField(verbose_name="编号")
    q_offer = models.CharField(max_length=200,blank=True,null=True,verbose_name="大货单价")
    q_floating_rate = models.CharField(max_length=200,blank=True,null=True,verbose_name="浮动率")
    q_end_offer = models.CharField(max_length=200,blank=True,null=True,verbose_name="最终报价")
    q_fabric_quotation = models.CharField(max_length=200,blank=True,null=True,verbose_name="面料报价")
    q_ingredients_quotation = models.CharField(max_length=200,blank=True,null=True,verbose_name="辅料报价")
    q_labor_payment_quotation = models.CharField(max_length=200,blank=True,null=True,verbose_name="工缴报价")
    q_water_washing_quotation = models.CharField(max_length=200,blank=True,null=True,verbose_name="水洗报价")
    q_embroider_quotation = models.CharField(max_length=200,blank=True,null=True,verbose_name="绣花报价")
    q_print_quotation = models.CharField(max_length=200,blank=True,null=True,verbose_name="印花报价")
    q_packaging_quotation = models.CharField(max_length=200,blank=True,null=True,verbose_name="包装物报价")
    q_other_quotation = models.CharField(max_length=200,blank=True,null=True,verbose_name="其他报价")
    q_reserved_profits = models.CharField(max_length=200,blank=True,null=True,verbose_name="预留利润")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.q_offer)

    class Meta:
        ordering = ["pk"]
        verbose_name = "报价单表"
        verbose_name_plural = "报价单表"