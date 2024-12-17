from django.contrib import admin

from .models import Basket


# Register your models here.

@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    model = Basket
    list_display = ("id", "client")
