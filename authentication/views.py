from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User  #User is inbuilt authentication model provided by the guys at Django
from django.contrib import messages   #django framework for sending one time notifications 
from django.conf import settings

# Create your views here.


def register(request):

    
    return render(request, "register.html") 

def login(request):
    return render(request, 'login.html')
    
def logout(request):

     return render(request, 'logout.html')

    


