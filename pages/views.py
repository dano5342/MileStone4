from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'index.html')


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html')


def about_view(request, *args, **kwargs):
    return render(request, 'about.html')
