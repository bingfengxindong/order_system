from django.db import models

class AccountingDocuments(models.Model):
    ad_id = models.UUIDField(verbose_name="编号")
    ad_ps_dollar_total_price = models.CharField(max_length=200, blank=True, null=True, verbose_name="大货总金额")
    ad_actual_cost = models.CharField(max_length=200, blank=True, null=True, verbose_name="实际成本")
    ad_total_profit = models.CharField(max_length=200, blank=True, null=True, verbose_name="利润总金额")

    ad_total_amount_materials = models.CharField(max_length=200, blank=True, null=True, verbose_name="面辅料总金额")
    ad_total_amount_fabric = models.CharField(max_length=200, blank=True, null=True, verbose_name="面料金额")
    ad_total_amount_fabric_express = models.CharField(max_length=200, blank=True, null=True, verbose_name="面料快递金额")
    ad_total_amount_bonding = models.CharField(max_length=200, blank=True, null=True, verbose_name="粘合金额")
    ad_total_amount_ingredients = models.CharField(max_length=200, blank=True, null=True, verbose_name="辅料金额")
    ad_total_amount_ingredients_express = models.CharField(max_length=200, blank=True, null=True, verbose_name="辅料快递金额")
    ad_total_amount_other = models.CharField(max_length=200, blank=True, null=True, verbose_name="其他金额")

    ad_total_amount_labor_payment = models.CharField(max_length=200, blank=True, null=True, verbose_name="工缴金额")
    ad_total_amount_tailor = models.CharField(max_length=200, blank=True, null=True, verbose_name="裁剪总金额")
    ad_tailor_start_date = models.DateTimeField(blank=True, null=True, verbose_name="裁剪开始时间")
    ad_tailor_end_date = models.DateTimeField(blank=True, null=True, verbose_name="裁剪结束时间")
    ad_tailor_number_people = models.CharField(max_length=200, blank=True, null=True, verbose_name="裁剪人数")
    ad_total_amount_sewing = models.CharField(max_length=200, blank=True, null=True, verbose_name="车缝总金额")
    ad_sewing_start_date = models.DateTimeField(blank=True, null=True, verbose_name="车缝开始时间")
    ad_sewing_end_date = models.DateTimeField(blank=True, null=True, verbose_name="车缝结束时间")
    ad_sewing_number_people = models.CharField(max_length=200, blank=True, null=True, verbose_name="车缝人数")
    ad_total_amount_iron = models.CharField(max_length=200, blank=True, null=True, verbose_name="整烫总金额")
    ad_iron_start_date = models.DateTimeField(blank=True, null=True, verbose_name="整烫开始时间")
    ad_iron_end_date = models.DateTimeField(blank=True, null=True, verbose_name="整烫结束时间")
    ad_iron_number_people = models.CharField(max_length=200, blank=True, null=True, verbose_name="整烫人数")

    ad_total_amount_embroide_print = models.CharField(max_length=200, blank=True, null=True, verbose_name="绣印花金额")
    ad_total_amount_water_washing = models.CharField(max_length=200, blank=True, null=True, verbose_name="水洗金额")
    ad_total_amount_embroide = models.CharField(max_length=200, blank=True, null=True, verbose_name="绣花金额")
    ad_total_amount_print = models.CharField(max_length=200, blank=True, null=True, verbose_name="印花金额")

    ad_total_amount_packaging_shipping = models.CharField(max_length=200, blank=True, null=True, verbose_name="包装船务金额")
    ad_total_amount_paperboard = models.CharField(max_length=200, blank=True, null=True, verbose_name="纸板金额")
    ad_total_amount_physical_distribution = models.CharField(max_length=200, blank=True, null=True, verbose_name="物流金额")
    ad_total_amount_warehouse_entry = models.CharField(max_length=200, blank=True, null=True, verbose_name="进仓金额")
    ad_total_amount_customs_declaration = models.CharField(max_length=200, blank=True, null=True, verbose_name="报关金额")
    create_date = models.DateTimeField(auto_now_add=True)
    create_end_date = models.DateTimeField(auto_now=True)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.ad_ps_dollar_total_price)

    class Meta:
        ordering = ["pk"]
        verbose_name = "核算单表"
        verbose_name_plural = "核算单表"