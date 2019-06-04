from django.contrib import admin
from .models import *
# Register your models here.
class ProductionWorkshopAdmin(admin.ModelAdmin):
    list_display = ("pw_workshop","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(ProductionWorkshop,ProductionWorkshopAdmin)

class ProductionScheduleAdmin(admin.ModelAdmin):
    list_display = ("ps_workshop","ps_order_date", "ps_outward_transport_date", "ps_gathering_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(ProductionSchedule,ProductionScheduleAdmin)