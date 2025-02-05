from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.db import models
from .models import Newsletter, Featured_Products,Brands, Contact
from .forms import NewsletterForm ,ContactForm

# Create your views here.
def index(request):
    newsletterform = NewsletterForm()
    context = {
           "newsletterform": newsletterform,
           "featured_products": Featured_Products.objects.all(),
           "brands": Brands.objects.all(),
    
    }
    if request.method == "POST":
        newsletterform = NewsletterForm(request.POST)
        if newsletterform.is_valid():
            email  = NewsletterForm.cleaned_data = ["email"]
            newsletterform.save()
            
            return render(request,'subscribe.html')
        else:
           newsletterform = NewsletterForm()
          
    return render (request, "index.html", context)

def about(request):
    return render (request, "about.html")

def contact(request):
    contactform = ContactForm()
    if request.method == "POST":
           contactform = ContactForm(request.POST)  
        
    if contactform.is_valid():
            name = contactform.cleaned_data['name']
            email = contactform.cleaned_data['email']
            message = contactform.cleaned_data['message']
            phone_number = contactform.cleaned_data['phone_number']
            
            contact = Contact(name=name, email=email, message=message,phone_number= phone_number)      
            contact.save()
            
            return redirect('contact_success')
    else:
        contactform=ContactForm()
        
    
    return render (request, 'contact.html', {'form':contactform})
def contact_success(request):
    return render(request, 'contact_success.html')
def subscribe(request):
    return render (request, "subscribe.html")



    
