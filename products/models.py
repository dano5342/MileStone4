from django.db import models

# Create your models here.
class Product(models.Model):
    name        = models.CharField(max_length=40)
    description = models.TextField(blank=False, null=False)
    price       = models.DecimalField(max_digits=6, decimal_places=2)
    summary     = models.TextField(default="This is a test")
    featured    = models.BooleanField(default=True)