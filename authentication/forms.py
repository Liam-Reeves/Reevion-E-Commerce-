from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from .models import UserRegistration

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.
    PasswordInput, label="Confirm Password")
     
    class Meta:
        model = UserRegistration
        fields = ['username','password','password_confirm']
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        # matching of password
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
            
        return cleaned_data            
        

        