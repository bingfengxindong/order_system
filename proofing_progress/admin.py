from django.contrib import admin
from .models import *

class ProofingProgressAdmin(admin.ModelAdmin):
    list_display = ("pp_id", "pp_number", "pp_erp_number", "pp_worker", "pp_end", "create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(ProofingProgress,ProofingProgressAdmin)

class WorkerAdmin(admin.ModelAdmin):
    list_display = ("w_id", "w_worker", "create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(Worker,WorkerAdmin)

class ModifyOpinionAdmin(admin.ModelAdmin):
    list_display = ("mo_id", "mo_customer_info", "mo_factory_info", "create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(ModifyOpinion,ModifyOpinionAdmin)