from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings
from .views import add_to_cart

urlpatterns= [
    path('add/', add_to_cart, name="add_to_cart"),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)