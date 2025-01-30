from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Newsletter

class NewsletterForm(ModelForm):
   class Meta:
         model = Newsletter
         fields = ['email',]
email =forms.EmailField(
      widget= forms.EmailInput(
            attrs={
                  'class': 'nls-input',
                  'placeholder': 'Enter your email adddress',
            }
      )
)     
    
              