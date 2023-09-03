from django.contrib import admin
from .models import Category, Tag, Brand, Product, ProductVersion, Property, Discount, PropertyVersion, ProductImages, PorductComment

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent_category', 'created_at']
    class Meta:
        model = Category

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    class Meta:
        model = Tag

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    class Meta:
        model = Brand

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'category', 'created_at']
    class Meta:
        model = Product

@admin.register(PropertyVersion)
class PropertyVersionAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    class Meta:
        model = PropertyVersion

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'property', 'created_at']
    class Meta:
        model = Property

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name', 'discount_rate', 'created_at']
    class Meta:
        model = Discount

@admin.register(ProductVersion)
class ProductVersionAdmin(admin.ModelAdmin):
    list_display = ['title', 'stock', 'price', 'discount', 'product', 'display', 'created_at']
    class Meta:
        model = ProductVersion

@admin.register(ProductImages)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'created_at']
    class Meta:
        model = ProductImages

@admin.register(PorductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'rating', 'product']
    class Meta:
        model = PorductComment