from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.db import models
from .models import  Featured_Products,Brands, Contact
from .forms import ContactForm

# Create your views here.
def index(request):
   
    context = {
           "featured_products": Featured_Products.objects.all(),
           "brands": Brands.objects.all(),
        }
               
    return render (request, "index.html", context)

def about(request):
    return render (request, "about.html")

def contact(request):
    contactform = ContactForm()
    
    if(request.method == 'POST'):
        #place the form in a parameter
        contactform =ContactForm(request.POST)
        
        #VALIDATING THE FORM
        if contactform.is_valid():
            #CHECK WHETHER DATA IS CORRECT
            
            name= contactform.cleaned_data['name']
            email= contactform.cleaned_data['email']
            phone_number= contactform.cleaned_data['phone_number']
            message= contactform.cleaned_data['message']
                   
            contactform.save()
            return redirect('contact_success')
        else:
            contactform = ContactForm()
 
    return render (request, 'contact.html', {'contactform':contactform})
def contact_success(request):
    return render(request, 'contact_success.html')
def subscribe(request):
    return render (request, "subscribe.html")



    
