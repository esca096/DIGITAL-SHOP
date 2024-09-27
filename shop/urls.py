from django.urls import path
from shop.views import index, product_details
urlpatterns = [
    path('', index, name='home'),
    path('<int:myid>', product_details, name='detail'),
]
