from django.db import models
from accounts.models import User
from products.models import ProductVersion
# Create your models here.

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userwishlist')
    product = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, related_name='productwishlist')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartitems')
    product = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, null=True, blank=True, related_name='productcart')
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.cart

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userorder')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cartorder')
    order_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user