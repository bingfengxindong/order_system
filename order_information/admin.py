from django.contrib import admin
from .models import *
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("o_number","o_date","o_image","o_price_type","o_proofingprogress_number","o_embroiderorprint","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
    list_filter = ("o_embroiderorprint",)  # 过滤器
admin.site.register(Order,OrderAdmin)

class PriceTypeAdmin(admin.ModelAdmin):
    list_display = ("pk","pt_type","pt_type_name")
    list_per_page = 100
    date_hierarchy = "create_date"
admin.site.register(PriceType,PriceTypeAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("c_name", "c_contack","c_email","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(Customer,CustomerAdmin)

class CapTypeAdmin(admin.ModelAdmin):
    list_display = ("ct_type","create_date")
    list_per_page = 100
    date_hierarchy = "create_date"
admin.site.register(CapType,CapTypeAdmin)

class CapColorAdmin(admin.ModelAdmin):
    list_display = ("cc_color", "create_date")
    list_per_page = 100
    date_hierarchy = "create_date"
admin.site.register(CapColor,CapColorAdmin)

class EmbroiderOrPrintAdmin(admin.ModelAdmin):
    list_display = ("eop_type", "create_date")
    list_per_page = 100
    date_hierarchy = "create_date"
admin.site.register(EmbroiderOrPrint,EmbroiderOrPrintAdmin)

class CapEyebrowAdmin(admin.ModelAdmin):
    list_display = ("ce_type", "create_date")
    list_per_page = 100
    date_hierarchy = "create_date"
admin.site.register(CapEyebrow,CapEyebrowAdmin)

class VersionNumberAdmin(admin.ModelAdmin):
    list_display = ("vn_version", "create_date")
    list_per_page = 100
    date_hierarchy = "create_date"
admin.site.register(VersionNumber,VersionNumberAdmin)

class AfterDeductionAdmin(admin.ModelAdmin):
    list_display = ("ad_type", "create_date")
    list_per_page = 100
    date_hierarchy = "create_date"
admin.site.register(AfterDeduction,AfterDeductionAdmin)

class ProductInforAdmin(admin.ModelAdmin):
    list_display = ("pi_amount","pi_unit_price", "pi_date")
    list_per_page = 100
    date_hierarchy = "pi_date"
admin.site.register(ProductInfo,ProductInforAdmin)

class AccountingDocumentsAdmin(admin.ModelAdmin):
    list_display = ("ad_total_profit","ad_fabric_ingredients_total_amount", "ad_labor_paymentl_amount","ad_embroide_print_amount","ad_packaging_shipping_amount")
    list_per_page = 100
    date_hierarchy = "create_date"
admin.site.register(AccountingDocuments,AccountingDocumentsAdmin)