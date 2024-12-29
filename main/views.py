from django.shortcuts import render
from django.http import HttpResponse

from django.db import models
from .models import Newsletter, Featured_Products,Brands
from .forms import NewsletterForm  

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
    return render (request, 'contact.html')
def subscribe(request):
    return render (request, "subscribe.html")

    

