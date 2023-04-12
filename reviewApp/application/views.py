from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'application/home.html', {'title': 'Home'})

def about(request):
    return render(request, 'application/about.html')

def contact(request):
    return render(request, 'application/contact.html')

def product(request):
    return render(request, 'application/product.html')