from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include("product.urls")),
    path('cart/', include("cart.urls")),
    path('orders/', include("orders.urls")),
    path('authentication', include("authentication.urls")),
    path('',include("main.urls")), 
    
    #Allauth URLS
    path('accounts/', include('allauth.urls')),
    
]
