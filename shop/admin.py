from django.contrib import admin
from shop.models import Category, Product, Commande
# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'date_added')
    
class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'ville', 'address', 'pays', 'date_commande')

admin.site.register(Category)
admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)