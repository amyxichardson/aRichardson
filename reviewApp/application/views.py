from django.shortcuts import render
from .models import Review, Product

# Create your views here.
def home(request):
    return render(request, 'application/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'application/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'application/contact.html', {'title': 'Contact'})

def product(request):
    return render(request, 'application/product.html', {'title': 'Product'})
