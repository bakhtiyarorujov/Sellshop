from django.db import models
from accounts.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Brand(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='productcategory')
    tag = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PropertyVersion(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
PROPERTY_LIST = [
    ('CL', 'Colour'),
    ('SZ', 'Size')
]
class Property(models.Model):
    name = models.CharField(max_length=10, choices=PROPERTY_LIST)
    property = models.ForeignKey(PropertyVersion, related_name='property', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} : {self.property.name}'

class Discount(models.Model):
    name = models.CharField(max_length=50)
    discount_rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} : {self.discount}'

class ProductVersion(models.Model):
    title = models.TextField()
    stock = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True, related_name='discount')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    image = models.ImageField(blank=True, null=True)
    display = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProductImages(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.product.title
    
class PorductComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercomment')
    comment = models.TextField()
    rating = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productcomment')

    def __str__(self) -> str:
        return f'{self.user}: {self.product}'