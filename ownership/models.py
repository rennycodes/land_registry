from django.db import models

# Create your models here.

class Landowner(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField(100)

    def __str__(self):
        return self.name
    

