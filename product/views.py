from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def product_list(request):
    return render(request, "product_list.html")
def product_detail(request):
    return render(request, "product_detail.html")
