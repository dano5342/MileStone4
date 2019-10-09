from django.shortcuts import render
from .models import Product


def all_products(request, *args, **kwargs):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})