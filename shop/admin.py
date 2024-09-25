from django.contrib import admin
from shop.models import Category, Product
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'date_added')

admin.site.register(Category)
admin.site.register(Product, AdminProduct)