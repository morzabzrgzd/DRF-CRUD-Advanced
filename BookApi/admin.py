from django.contrib import admin
from .models import *
# Register your models here.

class AdminMode(admin.ModelAdmin):
    list_display = ['name','store_name','image','fav','created_at']
    search_fields = ['name', 'store_name']

admin.site.register(Book, AdminMode)