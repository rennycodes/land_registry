from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Landowner(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Property(models.Model):
    landowner = models.ForeignKey(Landowner, on_delete=models.CASCADE)
    address = models.TextField

    def __str__(self):
        return f"Property of {self.landowner.name}"
