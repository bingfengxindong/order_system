from django.contrib import admin
from .models import *

class ProductionScheduleAdmin(admin.ModelAdmin):
    list_display = ("ps_id", "ps_number", "ps_date", "ps_confirm_date", "ps_gathering_date", "ps_end", "create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(ProductionSchedule,ProductionScheduleAdmin)

class ProductionWorkshopAdmin(admin.ModelAdmin):
    list_display = ("pw_id", "pw_workshop", "create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(ProductionWorkshop,ProductionWorkshopAdmin)