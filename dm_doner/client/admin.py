from django.contrib import admin

from .models import Client, Address


# Register your models here.

@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    model = Client
    list_display = ("id", 'username', 'phone_number', 'email', 'address', "is_staff")

    filter_horizontal = ['products_basket']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ("id", "street_name", 'city_name')
