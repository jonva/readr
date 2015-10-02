from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    return render(request, "home.html", {})

def details(request):
    return render(request, "details.html", {})