from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name
