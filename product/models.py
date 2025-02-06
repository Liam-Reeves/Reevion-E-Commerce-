from django.db import models

# Create your models here.

class Product_Listings(models.Model):
    product_name = models.CharField(max_length=255, default='')
    product_image= models.ImageField(default=True, null=True,  upload_to='productlistings/')
    product_price = models.IntegerField(default= 0)
    product_description = models.TextField(blank=True, max_length= 500, default='')
    
    def __str__(self):
        return self.product_name
        
    class Meta:
        verbose_name_plural = "Product_Listings"

    
    

