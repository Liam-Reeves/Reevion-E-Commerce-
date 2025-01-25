from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email= models.EmailField(max_length=100, default="")
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "Newsletters"
        
        
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
        
        
    