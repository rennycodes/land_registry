from django.db import models

# Create your models here.
class Land(models.Model):
    name = models.CharField(max_length=100)
    residential_address = models.TextField()
    phone_number = models.CharField(max_lenght=15)
    location = models.CharField(max_length=255)
    X1_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    Y1_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    X2_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    Y2_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    X3_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    Y3_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    X4_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    Y4_coordinate = models.DecimalField(max_digits=10, decimal_places=6)