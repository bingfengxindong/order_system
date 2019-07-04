from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):
    list_display = ("o_id","o_customer_number","o_date","o_image","o_file","o_pp_all_end","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
    # list_filter = ("o_embroiderorprint",)  # 过滤器
    fieldsets = (
        ("订单",{"fields":["o_id","o_customer","o_customer_number","o_price_type","o_date","o_user","o_capcolor","o_count","o_image","o_file",]}),
        ("产品信息",{"fields":["o_captype","o_main_fabric","o_embroiderorprint","o_capeyebrow","o_versionnumber","o_afterdeduction",]}),
        ("大货信息",{"fields":["o_ps_price","o_dollar_exchange_rate","o_dollar_type","o_dollar_price","o_ps_amount","o_ps_dollar_total_price","o_delivery_date",]}),
        ("打样信息",{"fields":["o_proofingprogress","o_pp_all_end","o_modifyopinion",]}),
        ("大货信息",{"fields":["o_productionschedule",]}),
    )
admin.site.register(Order,OrderAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("c_id","c_name","c_contack","c_email","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(Customer,CustomerAdmin)

class CapColorAdmin(admin.ModelAdmin):
    list_display = ("cc_id","cc_color","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(CapColor,CapColorAdmin)

class CapTypeAdmin(admin.ModelAdmin):
    list_display = ("ct_id","ct_type","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(CapType,CapTypeAdmin)

class EmbroiderOrPrintAdmin(admin.ModelAdmin):
    list_display = ("eop_id","eop_type","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(EmbroiderOrPrint,EmbroiderOrPrintAdmin)

class CapEyebrowAdmin(admin.ModelAdmin):
    list_display = ("ce_id","ce_type","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(CapEyebrow,CapEyebrowAdmin)

class VersionNumberAdmin(admin.ModelAdmin):
    list_display = ("vn_id","vn_version","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(VersionNumber,VersionNumberAdmin)

class AfterDeductionAdmin(admin.ModelAdmin):
    list_display = ("ad_id","ad_type","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(AfterDeduction,AfterDeductionAdmin)