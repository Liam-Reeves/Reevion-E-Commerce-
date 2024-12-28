from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email= models.EmailField(max_length=100, default=True)
    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = "Newsletters"
        
        
class FeaturedProduct(models.Model):
    image = models.ImageField(upload_to="featuredproduct"),
    title = models.CharField(max_length=100),
    price = models.DecimalField(max_digits=10, decimal_places=2),
    
    def __str__ (self):
        return self.image
   
    class Meta:
        verbose_name_plural = "Featured Products"