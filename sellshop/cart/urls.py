from django.urls import path
from .views import cart, checkout, wishlist, order_complete

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('order-complete/', order_complete, name='order-comlete'),
    path('wishlist/', wishlist, name='wishlist')
]