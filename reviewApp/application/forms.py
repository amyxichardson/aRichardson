from django import forms
from django.forms import ModelForm
from .models import Review, Contact

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ('author', 'product', 'rating', 'text', 'date_reviewed')
        labels = {'author':'', 'product':'', 'rating':'', 'text':''}
        widgets = {
            'rating':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Rating out of 5'}),
        }


class UpdateForm(ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'text', 'date_reviewed')
        labels = {'rating':'', 'text':''}
        widgets = {
            'rating': forms.NumberInput(attrs={'class':'form-control'}),
            'text': forms.TextInput(attrs={'class':'form-control'}),
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'text')

        labels = {
            'name': '',
            'email': '',
            'subject': '',
            'text': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email address'}),
            'subject': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}),
            'text': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Message'}),
        }