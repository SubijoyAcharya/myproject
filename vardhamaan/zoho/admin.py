from django.contrib import admin
from .models import zoho
# Register your models here.

class ZohoAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

admin.site.register(zoho,ZohoAdmin)