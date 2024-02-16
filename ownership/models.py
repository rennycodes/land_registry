from django.db import models

# Create your models here.
class Land(models.Model):
    name = models.CharField(max_length=100)
    residential_address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(default='someone@someone.com')
    location = models.CharField(max_length=255)
    X1_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    Y1_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    X2_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    Y2_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    X3_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    Y3_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    X4_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    Y4_coordinate = models.DecimalField(max_digits=10, decimal_places=6)
    land_type = models.CharField(max_length=50)
    landmark = models.TextField()
    LGA = models.CharField(max_length=100, default='Unknown')
    state = models.CharField(max_length=100, default='Unknown')
    size_of_land = models.DecimalField(max_length=10, decimal_places=2)