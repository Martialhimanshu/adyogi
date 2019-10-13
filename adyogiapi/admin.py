from django.contrib import admin
from adyogiapi.models import *


admin.site.register(Product)
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'product_type'
    )