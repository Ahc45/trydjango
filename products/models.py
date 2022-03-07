from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=255)
    description = models.TextField(blank=True)  
    price       = models.DecimalField(decimal_places=2, max_digits=12)  
    summary     = models.TextField(blank=True)  
    feature     =  models.BooleanField(default=True)