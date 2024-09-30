from django.urls import path
from shop.views import index, product_details, Checkout
urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', product_details, name='detail'),
    path('checkout', Checkout, name='checkout'),
]
