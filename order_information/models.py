from django.db import models
from proofing_progress.models import ProofingProgress
from production_schedule.models import ProductionSchedule
from user.models import User
# Create your models here.
class Order(models.Model):
    o_id = models.UUIDField(verbose_name="编号")
    o_number = models.CharField(max_length=200,verbose_name="订单号")
    o_date = models.DateField(blank=True,null=True,verbose_name="订单日期")
    o_image = models.ImageField(blank=True,null=True,upload_to="%Y/%m/%d/",verbose_name="图片")
    o_proofingprogress_number = models.IntegerField(blank=True,null=True,verbose_name="打样数量")

    o_customer = models.ForeignKey("Customer",blank=True,null=True,on_delete=models.CASCADE,verbose_name="客户")
    o_captype = models.ForeignKey("CapType",blank=True,null=True,on_delete=models.CASCADE,verbose_name="帽型")
    o_capcolor = models.ManyToManyField("CapColor",blank=True,null=True,verbose_name="颜色")
    o_embroiderorprint = models.ForeignKey("EmbroiderOrPrint",blank=True,null=True,on_delete=models.CASCADE,verbose_name="绣印花")
    o_capeyebrow = models.ForeignKey("CapEyebrow",blank=True,null=True,on_delete=models.CASCADE,verbose_name="帽眉")
    o_versionnumber = models.ForeignKey("VersionNumber",blank=True,null=True,on_delete=models.CASCADE,verbose_name="版号")
    o_afterdeduction = models.ForeignKey("AfterDeduction",blank=True,null=True,on_delete=models.CASCADE,verbose_name="后扣")
    o_productinfo = models.OneToOneField("ProductInfo",blank=True,null=True,on_delete=models.CASCADE,verbose_name="大货信息")

    o_proofingprogress = models.ManyToManyField(ProofingProgress,blank=True,null=True,verbose_name="打样进度")
    o_productionschedule = models.OneToOneField(ProductionSchedule,blank=True,null=True,on_delete=models.CASCADE,verbose_name="大货进度")
    o_user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,verbose_name="业务员")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)
    def __str__(self):
        return "{}".format(self.o_number)

    class Meta:
        ordering = ["pk"]
        verbose_name = "订单"
        verbose_name_plural = "订单"

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
        verbose_name = "客人"
        verbose_name_plural = "客人"

class CapType(models.Model):
    ct_id = models.UUIDField(verbose_name="编号")
    ct_type = models.CharField(max_length=200,verbose_name="帽型")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ct_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "帽型"
        verbose_name_plural = "帽型"

class CapColor(models.Model):
    cc_id = models.UUIDField(verbose_name="编号")
    cc_color = models.CharField(max_length=200,verbose_name="颜色")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.cc_color)

    class Meta:
        ordering = ["pk"]
        verbose_name = "颜色"
        verbose_name_plural = "颜色"

class EmbroiderOrPrint(models.Model):
    eop_id = models.UUIDField(verbose_name="编号")
    eop_type = models.CharField(max_length=200, verbose_name="绣印花")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.eop_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "绣印花"
        verbose_name_plural = "绣印花"

class CapEyebrow(models.Model):
    ce_id = models.UUIDField(verbose_name="编号")
    ce_type = models.CharField(max_length=200,verbose_name="帽眉")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ce_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "帽眉"
        verbose_name_plural = "帽眉"

class VersionNumber(models.Model):
    vn_id = models.UUIDField(verbose_name="编号")
    vn_version = models.CharField(max_length=200,verbose_name="版号")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.vn_version)

    class Meta:
        ordering = ["pk"]
        verbose_name = "版号"
        verbose_name_plural = "版号"

class AfterDeduction(models.Model):
    ad_id = models.UUIDField(verbose_name="编号")
    ad_type = models.CharField(max_length=200,verbose_name="后扣")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ad_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "后扣"
        verbose_name_plural = "后扣"

class ProductInfo(models.Model):
    pi_id = models.UUIDField(verbose_name="编号")
    pi_amount = models.IntegerField(blank=True,null=True,verbose_name="大货数量")
    pi_price_type = models.CharField(blank=True,null=True,max_length=50,verbose_name="价格类型")
    pi_unit_price = models.CharField(blank=True,null=True,max_length=100,verbose_name="大货报价")
    pi_date = models.DateField(blank=True,null=True,verbose_name="交货日期")

    pi_total_price = models.CharField(blank=True,null=True,max_length=100,verbose_name="大货总金额")
    pi_fabric_quotation = models.CharField(blank=True,null=True,max_length=100,verbose_name="面料报价")
    pi_ingredients_quotation = models.CharField(blank=True,null=True,max_length=100,verbose_name="辅料报价")
    pi_labor_payment_quotation = models.CharField(blank=True,null=True,max_length=100,verbose_name="工缴报价")
    pi_water_washing_quotation = models.CharField(blank=True,null=True,max_length=100,verbose_name="水洗报价")
    pi_print_quotation = models.CharField(blank=True,null=True,max_length=100,verbose_name="印花报价")
    pi_embroider_quotation = models.CharField(blank=True,null=True,max_length=100,verbose_name="绣花报价")
    pi_packaging_quotation = models.CharField(blank=True,null=True,max_length=100,verbose_name="包装物报价")
    pi_other_quotation = models.CharField(blank=True,null=True,max_length=100,verbose_name="其他报价")
    pi_reserved_profits = models.CharField(blank=True,null=True,max_length=100,verbose_name="预留利润")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.pi_unit_price)

    class Meta:
        ordering = ["pk"]
        verbose_name = "大货信息"
        verbose_name_plural = "大货信息"