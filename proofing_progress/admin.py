from django.contrib import admin
from .models import *
# Register your models here.
class ProofingProgressAdmin(admin.ModelAdmin):
    ist_display = ("pp_sample_order_date", "pp_sample_arrival_date", "pp_sample_express_date", "pp_Modify_sample_order_date", "pp_Modify_sample_arrival_date","pp_Modify_sample_express_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(ProofingProgress)