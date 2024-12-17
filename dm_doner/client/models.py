from django.db import models


# Create your models here.
class Client(models.Model):
    full_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    image = models.ImageField(upload_to='clients/', null=True, blank=True)
    address = models.ForeignKey('Address', on_delete=models.PROTECT, related_name='clients')
    basket = models.OneToOneField('basket.Basket', on_delete=models.CASCADE, related_name='client_basket',
                                  null=True, blank=True)

    def __str__(self):
        return self.full_name


class Address(models.Model):
    street_name = models.CharField(max_length=255)
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.street_name}, {self.city_name}"
