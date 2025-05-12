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

    
   
name = forms.CharField(
      label="",
      max_length=100,
      widget=forms.TextInput(
            attrs={'placeholder': 'Name',
                   'class': ' contact-input',
                   'style': 'width: 200px; height: 40px;',
                   }
            )
      ,
   
      )

email = forms.EmailField(
      label="",
      max_length=100,
      widget=forms.EmailInput(
            attrs={'class': 'contact-input',
                   'placeholder': 'Email address', 
                     'style': 'width: 200px; height: 40px;',
       }
), 
      )
phone_number = forms.CharField(
      label="",
      max_length=10,
      widget=forms.TextInput(
            attrs={
                  'class': 'contact-input',
                   'placeholder': 'Phone number',
                     'style': 'width: 200px; height: 40px;', 
   }),
      )
message = forms.CharField(
      label="",
      max_length=500,
      widget=forms.Textarea(
            attrs={
            'class': 'contact-input',
            'placeholder': 'Message',
            'style': 'width: 400px; height: 100px;',
            }
      ),
 )


              