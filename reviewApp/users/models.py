from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255,null=True, blank=True)
    town = models.CharField(max_length=255,null=True, blank=True)
    country = models.CharField(max_length=255,null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f' Profile for {self.user.username} '