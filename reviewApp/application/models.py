from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    brand = models.CharField(max_length=250, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.CharField(max_length=255, null=True)
    date_released = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='product_pics', null=True, blank=True)

    def __str__(self):
        return  self.name
    def get_absolute_url(self):
         return reverse('product-detail', kwargs={'pk': self.pk})


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False, validators=[MinValueValidator(1), MaxValueValidator(5)] )
    text = models.TextField()
    date_reviewed = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
            return self.author.username

    def get_absolute_url(self):
            return reverse('review-detail', kwargs={'pk': self.pk})