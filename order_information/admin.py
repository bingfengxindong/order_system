from django.contrib import admin
from .models import *
# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ("pk","o_id","o_number","o_date","o_image","o_embroiderorprint",)
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
    list_filter = ("o_embroiderorprint",)  # 过滤器
admin.site.register(Order,OrderAdmin)
admin.site.register(Customer)
admin.site.register(CapType)
admin.site.register(CapColor)
admin.site.register(CapEyebrow)
admin.site.register(VersionNumber)
admin.site.register(AfterDeduction)
admin.site.register(ProductInfo)