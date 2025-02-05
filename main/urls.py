from django.urls import path
from .import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name= "index"),
    path('about/', views.about, name= "about"),
    path('contact/', views.contact, name= "contact"),
    path('contact_success/', views.contact_success, name= "contact_success"),
    path('subscribe/',views.subscribe, name="subscribe"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)