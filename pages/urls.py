from django.urls import path
from .views import contact_view, about_view

urlpatterns = [
    path('about/', about_view, name="about"),
    path('contact/', contact_view, name="contact") 
]