from django.contrib import admin
from django.db import models
from .models import Newsletter, Featured_Products,Brands,Contact

# Register your models here.
admin.site.register(Newsletter),
admin.site.register(Featured_Products),
admin.site.register(Brands)
admin.site.register(Contact)
