from django.contrib import admin

from .models import Client, Address


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ("id", "full_name", 'nickname', 'phone_number', 'email', 'address', 'created_at')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    model = Address
    list_display = ("id", "street_name", 'city_name')
