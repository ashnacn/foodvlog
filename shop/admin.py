from django.contrib import admin

# Register your models here.
from .models import *
class c_admin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('cat_name',)}
admin.site.register(Category,c_admin)
class P_admin(admin.ModelAdmin):
    list_display = ['P_name','slug','P_price','P_stock','P_image']
    list_editable = ['P_price','P_stock','P_image']
    prepopulated_fields = {'slug':('P_name',)}
admin.site.register(Product,P_admin)

