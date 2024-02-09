from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Landowner(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(default='Someone@tonek.com')
    inputter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class LandProperty(models.Model):
    landowner = models.ForeignKey(Landowner, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(default='Someone@tonek.com')
    land_type = models.CharField(max_length=255)
    inputter = models.ForeignKey(User, on_delete=models.CASCADE)
    other_details = models.TextField(blank=True, null=True)
    

    def __str__(self):
        return f"Property of {self.landowner.name}"
