from django.db import models
from .constants import OS_CHOICES
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description= models.TextField(blank=True)
    os = models.CharField(max_length = 8, choices = OS_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name