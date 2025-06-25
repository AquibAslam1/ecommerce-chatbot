from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    rating = models.FloatField()
    image_url = models.URLField()
    stock = models.BooleanField(default=True)
