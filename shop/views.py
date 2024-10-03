from django.shortcuts import render, redirect
from .models import Product, Commande

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


def product_details(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'products/details.html', {'product':product_object})


def Checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        address = request.POST.get('address')
        com = Commande(items=items,total=total, nom=nom, email=email, ville=ville, pays=pays, zipcode=zipcode, address=address)
        com.save()
        return redirect('confirm')
    return render(request, 'products/checkout.html')

def confirm(request):
    info = Commande.objects.all()[:1]
    for item in info:
        nom = item.nom
    return render(request, 'products/confirm.html', {'name':nom})