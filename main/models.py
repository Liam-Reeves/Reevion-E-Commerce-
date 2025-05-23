from django.db import models

# Create your models here.

        
class Featured_Products(models.Model):
    image =models.ImageField(default=True, upload_to="featured_products")
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Featured Products"

class Brands(models.Model):
    brand_image= models.ImageField(upload_to="brands")
       
    def __str__(self):
        return self.brand_image.name

    class Meta:
        verbose_name_plural = "Brands"
        
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=10)
    message = models.TextField(max_length=255, default="",)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contacts" 
        
        
    