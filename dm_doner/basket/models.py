from django.db import models


# Create your models here.
class Basket(models.Model):
    client = models.OneToOneField('client.Client', on_delete=models.CASCADE, related_name='basket_client')

    def __str__(self):
        return f"Basket for {self.client.full_name}"


class BasketProduct(models.Model):
    basket = models.ForeignKey('basket.Basket', on_delete=models.CASCADE)
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} in basket of {self.basket.client.full_name}"
