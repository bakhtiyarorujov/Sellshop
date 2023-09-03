from django.urls import path
from .views import home, product, products

urlpatterns = [
    path('home/', home, name='home'),
    path('products/', products, name='products'),
    path('product/', product, name='product'),
]