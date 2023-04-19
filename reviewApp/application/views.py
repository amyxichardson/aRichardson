from django.shortcuts import render, redirect
from .models import Review, Product
from .forms import ReviewForm 
from .forms import UpdateForm 
from django.http import HttpResponseRedirect

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


def add_review(request):
    submitted = False
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
           form.save()
           return HttpResponseRedirect('/add_review?sumbitted=True')
    else:
        form = ReviewForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'application/add_review.html',{'form':form, 'submitted':submitted})


def update_review(request, review_id):
    review=Review.objects.get(pk=review_id)
    form = UpdateForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        return redirect('list-product')  
    
    return render(request, 'application/update_review.html',
    {'review':review, 'form':form}) 


def delete_review(request, review_id):
    review=Review.objects.get(pk=review_id)
    review.delete()
    return redirect('list-product')


