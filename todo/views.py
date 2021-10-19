from django.shortcuts import render
from allauth.account.forms import SignupForm


def home(request):
    form = SignupForm()
    return render(request, "base.html", {"form": form})
