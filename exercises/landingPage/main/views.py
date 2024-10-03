from django.shortcuts import render
from main.models import LandingPage


def home(request):
    pages = LandingPage.objects.all()
    return render(request, 'main/home.html', {'pages': pages})
