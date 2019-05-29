from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("u_name", "u_username", "u_password", "create_date")
    list_per_page = 100
    date_hierarchy = "create_date"
admin.site.register(User,UserAdmin)