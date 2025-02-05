from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Newsletter,Contact

class NewsletterForm(forms.ModelForm):
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

class ContactForm(forms.ModelForm):
      
 class Meta:
         model = Contact
         fields = ['name','email','phone_number','message']
         
name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your name"} ),max_length=100)

email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',"placeholder": "Enter your email adddress", }), max_length=100)

phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',"placeholder": "Enter your phone number", }), max_length=10)

message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message',}),max_length=500)

    
              