from django.db import models

# Create your models here.

class Dishes(models.Model):

    
    noon = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    offer = models.BooleanField(default=False)