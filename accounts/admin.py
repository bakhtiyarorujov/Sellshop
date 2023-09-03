from django.contrib import admin
from .models import User, Address
# Register your models here.



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone', 'newsletter']
    class Meta:
        model = User

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'country', 'address']
    class Meta:
        model = Address