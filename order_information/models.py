from django.db import models
from proofing_progress.models import ProofingProgress
from production_schedule.models import ProductionSchedule
from user.models import User
# Create your models here.
class Order(models.Model):
    o_id = models.UUIDField(verbose_name="编号")
    o_number = models.CharField(max_length=200,verbose_name="订单号")
    o_date = models.DateField(blank=True,null=True,verbose_name="订单日期")
    o_price_type = models.ForeignKey("PriceType",blank=True,null=True,on_delete=models.CASCADE,verbose_name="币种")
    o_image = models.ImageField(blank=True,null=True,upload_to="%Y/%m/%d/",verbose_name="图片")
    o_proofingprogress_number = models.IntegerField(blank=True,null=True,verbose_name="打样数量")

    o_customer = models.ForeignKey("Customer",blank=True,null=True,on_delete=models.CASCADE,verbose_name="客户")
    o_captype = models.ForeignKey("CapType",blank=True,null=True,on_delete=models.CASCADE,verbose_name="帽型")
    o_capcolor = models.ManyToManyField("CapColor",blank=True,verbose_name="颜色")
    o_embroiderorprint = models.ForeignKey("EmbroiderOrPrint",blank=True,null=True,on_delete=models.CASCADE,verbose_name="绣印花")
    o_capeyebrow = models.ForeignKey("CapEyebrow",blank=True,null=True,on_delete=models.CASCADE,verbose_name="帽眉")
    o_versionnumber = models.ForeignKey("VersionNumber",blank=True,null=True,on_delete=models.CASCADE,verbose_name="版号")
    o_afterdeduction = models.ForeignKey("AfterDeduction",blank=True,null=True,on_delete=models.CASCADE,verbose_name="后扣")
    o_productinfo = models.OneToOneField("ProductInfo",blank=True,null=True,on_delete=models.CASCADE,verbose_name="大货信息")

    o_proofingprogress = models.ManyToManyField(ProofingProgress,blank=True,verbose_name="打样进度")
    o_productionschedule = models.OneToOneField(ProductionSchedule,blank=True,null=True,on_delete=models.CASCADE,verbose_name="大货进度")
    o_accountingdocuments = models.OneToOneField("AccountingDocuments",blank=True,null=True,on_delete=models.CASCADE,verbose_name="按单核算")
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

class PriceType(models.Model):
    pt_id = models.UUIDField(verbose_name="编号")
    pt_type = models.CharField(max_length=20,verbose_name="币种")
    pt_type_name = models.CharField(max_length=50,blank=True,null=True,verbose_name="名称")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.pt_type)

    class Meta:
        ordering = ["pk"]
        verbose_name = "币种"
        verbose_name_plural = "币种"

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
    pi_unit_price = models.CharField(blank=True,null=True,max_length=100,verbose_name="大货单价")
    pi_date = models.DateField(blank=True,null=True,verbose_name="交货日期")
    pi_total_price = models.CharField(blank=True,null=True,max_length=100,verbose_name="大货总金额")

    pi_offer = models.CharField(blank=True,null=True,max_length=100,verbose_name="大货报价")
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

class AccountingDocuments(models.Model):
    ad_id = models.UUIDField(verbose_name="编号")
    ad_total_profit = models.CharField(blank=True,null=True,max_length=100,verbose_name="利润总金额")

    ad_fabric_ingredients_total_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="面辅料金额")
    ad_fabric_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="面料金额")
    ad_fabric_express_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="面料快递金额")
    ad_bonding_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="粘合金额")
    ad_ingredients_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="辅料金额")
    ad_ingredients_express_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="辅料快递金额")
    ad_fabric_ingredients_other_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="面辅料其他金额")

    ad_labor_paymentl_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="工缴金额")
    ad_tailor_total_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="裁剪总金额")
    ad_tailor_start_date = models.DateTimeField(blank=True, null=True, verbose_name="裁剪开始时间")
    ad_tailor_end_date = models.DateTimeField(blank=True, null=True, verbose_name="裁剪结束时间")
    ad_tailor_number_people = models.IntegerField(blank=True, null=True, verbose_name="裁剪人数")
    ad_sewing_total_amount = models.CharField(blank=True, null=True, max_length=100, verbose_name="车缝总金额")
    ad_sewing_start_date = models.DateTimeField(blank=True, null=True, verbose_name="车缝开始时间")
    ad_sewing_end_date = models.DateTimeField(blank=True, null=True, verbose_name="车缝结束时间")
    ad_sewing_number_people = models.IntegerField(blank=True, null=True, verbose_name="车缝人数")
    ad_iron_total_amount = models.CharField(blank=True, null=True, max_length=100, verbose_name="整烫总金额")
    ad_iron_start_date = models.DateTimeField(blank=True, null=True, verbose_name="整烫开始时间")
    ad_iron_end_date = models.DateTimeField(blank=True, null=True, verbose_name="整烫结束时间")
    ad_iron_number_people = models.IntegerField(blank=True, null=True, verbose_name="整烫人数")

    ad_embroide_print_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="绣印花金额")
    ad_water_washing_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="水洗金额")
    ad_embroide_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="绣花金额")
    ad_print_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="印花金额")

    ad_packaging_shipping_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="包装船务金额")
    ad_paperboard_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="纸板金额")
    ad_physical_distribution_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="物流金额")
    ad_warehouse_entry_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="进仓金额")
    ad_customs_declaration_amount = models.CharField(blank=True,null=True,max_length=100,verbose_name="报关金额")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ad_total_profit)

    class Meta:
        ordering = ["pk"]
        verbose_name = "按单核算"
        verbose_name_plural = "按单核算"