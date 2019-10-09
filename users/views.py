from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """ 
    Registers a new user on the backend
    """
    form = UserCreationForm()
    return render(request, 'register.html', {'form': form})