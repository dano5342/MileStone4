"""ms4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from pages.urls import urlpatterns as pageviews
from pages.views import home_view
from users import views as user_views
from django.contrib.auth import views as auth_views
from products.urls import urlpatterns as urls_products
from products.views import all_products
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    path('', all_products, name="home"),
    path('admin/', admin.site.urls),
    path('pageviews/', include(pageviews)),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path('profile/', user_views.profile, name="profile"),
    path('products/<int:product_id>', include(urls_products)),
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT})
]
