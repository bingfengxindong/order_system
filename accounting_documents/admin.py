from django.contrib import admin
from accounting_documents.models import AccountingDocuments

class AccountingDocumentsAdmin(admin.ModelAdmin):
    list_display = ("ad_id","ad_ps_dollar_total_price","ad_actual_cost","ad_total_profit","create_date")
    list_per_page = 100  # 设置每页记录
    date_hierarchy = "create_date"  # 详细时间分层筛选
admin.site.register(AccountingDocuments,AccountingDocumentsAdmin)