from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Product_Listings
# Create your views here.

def product_list(request):
    context ={
        'productlistings':Product_Listings.objects.all(),
        
    }
    
    return render(request, "product_list.html", context)
def product_detail(request):
    return render(request, "product_detail.html")
