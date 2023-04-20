from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='application-home'),
    path('about', views.about, name='application-about'),
    path('contact', views.contact, name='application-contact'),
    path('product_list', views.all_products, name='list-product'),
    path('show_product/<product_id>', views.show_product, name="show-product"),
    path('show_review/<review_id>', views.show_review, name="show-review"),
    path('add_review/', views.add_review, name="add-review"),
    path('update_review/<review_id>', views.update_review, name="update-review"),
    path('delete_review/<review_id>', views.delete_review, name="delete-review"),
    path('search_products/', views.search_products, name="search-products"),
]