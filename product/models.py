from django.db import models

# Create your models here.

class ProductImages(models.Model):
    image= models.ImageField(upload_to='productimages'),
    title= models.CharField(max_length=255, blank=False, null=True),
    
    def __str__(self):
        return self.title
    
    
    
    


