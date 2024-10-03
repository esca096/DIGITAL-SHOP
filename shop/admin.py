from django.contrib import admin
from shop.models import Category, Product, Commande
# Register your models here.
#custom admin side
admin.site.site_header = "ECOMMERCE"
admin.site.site_title = "SHOP"
admin.site.index_title = "Manager"

class AdminProduct(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'date_added')
    search_fields = ('title',)
    list_editable = ( 'price',)
    
class AdminCommande(admin.ModelAdmin):
    list_display = ('items', 'nom', 'ville', 'address', 'pays','total', 'date_commande')
    

admin.site.register(Category)
admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)