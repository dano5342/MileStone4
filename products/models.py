from django.db import models
from django.utils import timezone


class Category(models.Model):
    product_type = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.product_type


class Product(models.Model):
    name = models.CharField(max_length=126, default="", unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    summary = models.CharField(max_length=254)
    image = models.ImageField(upload_to="images")
    started_at = models.DateTimeField(timezone.now)
    product_type = models.ForeignKey(Category, on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.name


