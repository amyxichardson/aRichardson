from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='application-home'),
    path('about', views.about, name='application-about'),
    path('contact', views.contact, name='application-contact'),
    path('product', views.product, name='application-product'),
]