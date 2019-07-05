from django.db import models
from user.models import User
from proofing_progress.models import *
from production_schedule.models import ProductionSchedule
from quotation.models import Quotation
from accounting_documents.models import AccountingDocuments

# Create your models here.
class Order(models.Model):
    o_id = models.UUIDField(verbose_name="编号")
    o_customer_number = models.CharField(max_length=200,verbose_name="客户款号")
    o_date = models.DateField(blank=True,null=True,verbose_name="下单日期")
    o_price_type = models.CharField(max_length=200,default="￥",verbose_name="人民币单位")
    o_dollar_type = models.CharField(max_length=200,default="$",verbose_name="美金单位")
    o_count = models.IntegerField(blank=True,null=True,verbose_name="颜色数量")
    o_image = models.ImageField(blank=True,null=True,upload_to="image/%Y/%m/%d/",verbose_name="图片")
    o_file = models.FileField(blank=True,null=True,upload_to="file/%Y/%m/%d/",verbose_name="文件")
    o_main_fabric = models.CharField(max_length=200,blank=True,null=True,verbose_name="主面料")
    o_ps_price = models.CharField(max_length=200,blank=True,null=True,verbose_name="大货单价")
    o_dollar_exchange_rate = models.CharField(max_length=200,blank=True,null=True,default="6.9",verbose_name="美元汇率")
    o_dollar_price = models.CharField(max_length=200,blank=True,null=True,verbose_name="美元单价")
    o_ps_amount = models.CharField(max_length=200,blank=True,null=True,verbose_name="大货数量")
    o_ps_dollar_total_price = models.CharField(max_length=200,blank=True,null=True,verbose_name="大货总金额（美元）")
    o_delivery_date = models.DateField(blank=True,null=True,verbose_name="交货期")

    o_customer = models.ForeignKey("Customer", blank=True, null=True, on_delete=models.CASCADE, verbose_name="客户")
    o_capcolor = models.ManyToManyField("CapColor", blank=True, verbose_name="颜色")
    o_captype = models.ForeignKey("CapType", blank=True, null=True, on_delete=models.CASCADE, verbose_name="帽型")
    o_embroiderorprint = models.ForeignKey("EmbroiderOrPrint", blank=True, null=True, on_delete=models.CASCADE, verbose_name="绣印花")
    o_capeyebrow = models.ForeignKey("CapEyebrow", blank=True, null=True, on_delete=models.CASCADE, verbose_name="帽眉")
    o_versionnumber = models.ForeignKey("VersionNumber", blank=True, null=True, on_delete=models.CASCADE,verbose_name="版号")
    o_afterdeduction = models.ForeignKey("AfterDeduction", blank=True, null=True, on_delete=models.CASCADE,verbose_name="后扣")
    o_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name="业务员")

    o_proofingprogress = models.ManyToManyField(ProofingProgress, blank=True, verbose_name="打样")
    o_pp_all_end = models.BooleanField(default=False,verbose_name="打样是否完成/默认未完成")
    o_modifyopinion = models.OneToOneField(ModifyOpinion, blank=True, null=True, on_delete=models.CASCADE, verbose_name="打样修改意见")
    o_productionschedule = models.OneToOneField(ProductionSchedule, blank=True, null=True, on_delete=models.CASCADE, verbose_name="大货表")
    o_quotation = models.OneToOneField(Quotation, blank=True, null=True, on_delete=models.CASCADE, verbose_name="报价单表")
    o_accountingdocuments = models.OneToOneField(AccountingDocuments, blank=True, null=True, on_delete=models.CASCADE, verbose_name="核算单表")
    o_end = models.BooleanField(default=False,verbose_name="订单是否完成/默认未完成")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.o_customer_number)

    class Meta:
        ordering = ["-pk"]
        verbose_name = "订单表"
        verbose_name_plural = "订单表"

class Customer(models.Model):
    c_id = models.UUIDField(verbose_name="编号")
    c_name = models.CharField(max_length=200,verbose_name="客户名")
    c_contack = models.CharField(max_length=200,verbose_name="联系人")
    c_email = models.EmailField(verbose_name="邮箱")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.c_name)

    class Meta:
        ordering = ["pk"]
        verbose_name = "客户表"
        verbose_name_plural = "客户表"

class CapColor(models.Model):
    cc_id = models.UUIDField(verbose_name="编号")
    cc_color= models.CharField(max_length=200,blank=True,null=True,verbose_name="颜色")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.cc_color)

    class Meta:
        ordering = ["pk"]
        verbose_name = "帽子颜色表"
        verbose_name_plural = "帽子颜色表"

class CapType(models.Model):
    ct_id = models.UUIDField(verbose_name="编号")
    ct_type= models.CharField(max_length=200,blank=True,null=True,verbose_name="帽型")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ct_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "帽型表"
        verbose_name_plural = "帽型表"

class EmbroiderOrPrint(models.Model):
    eop_id = models.UUIDField(verbose_name="编号")
    eop_type= models.CharField(max_length=200,blank=True,null=True,verbose_name="绣印花")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.eop_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "绣印花表"
        verbose_name_plural = "绣印花表"

class CapEyebrow(models.Model):
    ce_id = models.UUIDField(verbose_name="编号")
    ce_type= models.CharField(max_length=200,blank=True,null=True,verbose_name="帽眉")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ce_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "帽眉表"
        verbose_name_plural = "帽眉表"

class VersionNumber(models.Model):
    vn_id = models.UUIDField(verbose_name="编号")
    vn_version= models.CharField(max_length=200,blank=True,null=True,verbose_name="版号")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.vn_version)

    class Meta:
        ordering = ["pk"]
        verbose_name = "版号表"
        verbose_name_plural = "版号表"

class AfterDeduction(models.Model):
    ad_id = models.UUIDField(verbose_name="编号")
    ad_type= models.CharField(max_length=200,blank=True,null=True,verbose_name="后扣")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ad_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "后扣表"
        verbose_name_plural = "后扣表"