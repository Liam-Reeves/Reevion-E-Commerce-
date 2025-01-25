from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import View

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


# Importing models for authentication app
from django.db import models 
from .models import UserRegistration

# importing forms file from auhentication app
from .forms import RegistrationForm
# Create your views here.


def register(request):
    registrationform = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = UserRegistration.objects.create_user(username=username, password=password)
            
            login(request, user)
            form.save()
            
            return redirect('index')
        else :
            form =RegistrationForm()
            
            
    return render(request, "register.html", {'form': form})

def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                
                request.POST.get('next') or request.GET.get('next') or 'index'
                return redirect('next_url')
            else:
                error_message = 'Invalid Credentials'
                
              
        return render(request, "login", {'error': error_message})
    
def logout(request):
      if request.method =="POST":
          logout(request)
          return redirect('login')
      else:
            return render(request, "index")
    

# using decorators
@login_required
def home_view(request):
    return render(request, 'index.html')

#Protected View
class ProtectedView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    
def get(self, request, *args, **kwargs):
        return render(request, 'protected_view.html')



