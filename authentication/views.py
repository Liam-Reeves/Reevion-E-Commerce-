from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User  #User is inbuilt authentication model provided by the guys at Django
from django.contrib import messages 
#django framework for sending one time notifications 
from django.conf import settings
from .forms import RegistrationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = RegistrationForm()
    return render(request, "register.html", {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def dashboard_view(request):
    return render(request, 'dashboard')
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('main/index')

    


