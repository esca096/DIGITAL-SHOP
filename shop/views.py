from django.shortcuts import render
from .models import Product

from django.core.paginator import Paginator
# Create your views here.

def index(request):
    
    #Affiche tout les product du db
    product_object = Product.objects.all()
    
    #Execute la Recherche des Product
    item_name = request.GET.get('item-name')
    if item_name  !='' and item_name is not None:
        product_object = Product.objects.filter(title__icontains=item_name)
    
    #Pour la parginer les pages
    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    
    return render(request, 'products/index.html', {'product_object':product_object})