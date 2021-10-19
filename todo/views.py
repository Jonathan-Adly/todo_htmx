from django.shortcuts import render
from allauth.account.forms import SignupForm
from .models import Task


def home(request):
    return render(request, "home.html")
