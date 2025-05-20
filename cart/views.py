from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from  django.contrib.auth.decorators import login_required
from product.models import Product_Listings
from .models import Cart, CartItem
# Create your views here.

@login_required
def add_to_cart(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        
        product = Product_Listings.objects.get(id=product_id)
        cart,created = Cart.objects.get_or_create(user=request.user)
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'quantity': quantity}
            )
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
            return JsonResponse({
                'success': True,
                'cart_total_items': cart.items.count()
            })
            
    return JsonResponse({
        'success': False,
        
    }, status=400)