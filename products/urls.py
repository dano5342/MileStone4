from django.urls import path, include
from .views import all_products, all_categories


urlpatterns = [
    path('', all_products, name="products"),
]