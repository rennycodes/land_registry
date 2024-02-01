from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Landowner(models.Model):
    name = models.CharField(max_length=100, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    address = models.TextField

    def __str__(self):
        return self.name
    

