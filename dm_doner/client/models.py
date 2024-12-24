from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Client(AbstractUser):
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='clients/', null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.PROTECT, related_name='clients', null=True, blank=True)
    products_basket = models.ManyToManyField('product.Product',
                                             related_name='client_products',
                                             null=True, blank=True)

    def __str__(self):
        return self.first_name


class Address(models.Model):
    street_name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street_name}, {self.city_name}"
