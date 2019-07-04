from django.contrib import admin
from quotation.models import Quotation

class QuotationAdmin(admin.ModelAdmin):
    list_display = ("q_id","q_offer","q_floating_rate","q_end_offer","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(Quotation,QuotationAdmin)