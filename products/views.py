from django.shortcuts import render
from .models import Product, Category
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    arguments = {"products": products}
    return render(request, "products.html", arguments)

def all_categories(request):
    categories = Category.objects.all()
    arguments = {'categories': categories}
    return render(request, 'categories.html', arguments)

