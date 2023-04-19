from django import forms
from django.forms import ModelForm
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('author', 'product', 'rating', 'text', 'date_reviewed')

class UpdateForm(ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'text', 'date_reviewed')