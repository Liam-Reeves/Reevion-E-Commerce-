from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User  #User is inbuilt authentication model provided by the guys at Django
from django.contrib import messages   #django framework for sending one time notifications 
from django.conf import settings

# Create your views here.


def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        #checking here that you do not register with existing users
        
    user_data_has_error = False  # user_data_has_error is user-defined variable set to a boolean value
    
    if User.objects.filter(username=username).exists():
        user_data_has_error = True
        messages.error(request, 'Username already exists')
        
    if User.objects.filter(email=email).exists():
        user_data_has_error = True
        messages.error(request, 'Email already exists')
        
        # making sure the set password meets the required length
            
        if len(password) < 8:
                user_data_has_error = True
                messages.error(request, 'Password must be at least 8 characters long')
            
        if not user_data_has_error:
            new_user =User.objects.create_user(
                full_name = full_name,
                username = username,
                email = email,
                password =password,
              
            )
            messages.success(request, 'Account created. Login now')
            return redirect('login')
        else:
            return redirect('register')
        
     
   
    
    
    
    
    return render(request, "register.html") 

def login(request):
    return render(request, 'login.html')
    
def logout(request):

     return render(request, 'logout.html')

    


