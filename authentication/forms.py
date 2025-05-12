from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    
    username = forms.CharField(
            label="",
            max_length=100,
            widget =forms.TextInput(
                 attrs={
                  'class': 'register-input',
                  'placeholder': 'Username',
                  'style': 'width: 200px; height: 40px;',
                  
                }
                
             ),

            )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                'class': 'register-input',
                'placeholder': 'Email',
                'style': 'width: 200px; height: 40px;',
              
                
            }
        )
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
               attrs={
                  'class': 'register-input',
                  'placeholder': 'Password',
                  'style': 'width: 200px; height: 40px;',
                
                  
                 }
        )
        )
    password_confirm = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                  'class': 'register-input',
                  'placeholder': 'Confirm Password',
                  'style': 'width: 200px; height: 40px;',                }   
            ),
        )
     
    class Meta:
        model = UserRegistration
        fields = ['username','email','password','password_confirm']

    
               
        

        