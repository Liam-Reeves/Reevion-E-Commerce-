from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, default="")
  
    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "User Registration"
    

