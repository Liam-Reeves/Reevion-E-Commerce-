from django.contrib import admin
from django.db import models
from .models import Newsletter, FeaturedProduct

# Register your models here.
admin.site.register(Newsletter),
admin.site.register(FeaturedProduct)