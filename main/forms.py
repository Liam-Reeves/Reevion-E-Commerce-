from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Newsletter,Contact

class NewsletterForm(forms.ModelForm):
   class Meta:
         model = Newsletter
         fields = ['email',]
         
email =forms.EmailField(
      label="",
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

    
      name = forms.CharField( label="",  max_length=255,
      widget=forms.TextInput(
            attrs={'placeholder': 'Name',
                   'class': ' contact-input',
                
                   }
            )
      ,
   
      )

      email = forms.EmailField(label="", max_length=255,
      widget= forms.EmailInput(
            attrs={
                  'class': 'contact-input',
                   'placeholder': 'Email address', 
            }
), 
      )
      phone_number = forms.CharField(label="", max_length=10,
      widget=forms.TextInput(
            attrs={
                  'class': 'contact-input',
                   'placeholder': 'Phone number',
            }
      )
      )
      message = forms.CharField(label="",max_length=255,
      widget= forms.Textarea(
            attrs={
            'class': 'contact-message',
            'placeholder': 'Message',
       
            }
      ),
 )


              