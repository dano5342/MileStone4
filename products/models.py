from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    summary = models.TextField(default="This is a test")
    featured = models.BooleanField(default=True)
    posted_at = models.DateTimeField(default=timezone.now)