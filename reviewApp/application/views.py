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


def all_products(request):
    product_list = Product.objects.all()
   
    return render(request, 'application/product_list.html',
    {'product_list': product_list})


def show_product(request, product_id):
    product=Product.objects.get(pk=product_id)
    review=product.review_set.all()
    
    return render(request, 'application/show_product.html',
    {'product':product,
    'review':review})


def show_review(request, review_id):
    review=Review.objects.get(pk=review_id)
    
    return render(request, 'application/show_review.html',
    {'review':review})



