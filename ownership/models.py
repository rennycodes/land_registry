from django.db import models

# Create your models here.

class Landowner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(default='Someone@tonek.com')


    def __str__(self):
        return self.name

class LandProperty(models.Model):
    id = models.AutoField(primary_key=True)
    landowner = models.ForeignKey(Landowner, on_delete=models.CASCADE)
    coordinates = models.DecimalField(max_digits=10, decimal_places=6, null=True)
    land_type = models.CharField(max_length=255)
    other_details = models.TextField(blank=True, null=True)
    inputter_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Property of {self.landowner.name}"
