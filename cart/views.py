from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from  django.contrib.auth.decorators import login_required
from product.models import Product_Listings
from .models import Cart, CartItem
# Create your views here.

def cart_view(request):
    return render(request, 'cart.html')