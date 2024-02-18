from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Land(models.Model):
    
    # Owner Info
    name = models.CharField(max_length=100)
    residential_address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(default='someone@someone.com')

    # Land Info
    land_location = models.CharField(max_length=255)
    X1_point = models.DecimalField(max_digits=20, decimal_places=15)
    Y1_point = models.DecimalField(max_digits=20, decimal_places=15)
    X2_point = models.DecimalField(max_digits=20, decimal_places=15)
    Y2_point = models.DecimalField(max_digits=20, decimal_places=15)
    X3_point = models.DecimalField(max_digits=20, decimal_places=15)
    Y3_point = models.DecimalField(max_digits=20, decimal_places=15)
    X4_point = models.DecimalField(max_digits=20, decimal_places=15)
    Y4_point = models.DecimalField(max_digits=20, decimal_places=15)
    land_type = models.CharField(max_length=50)
    landmark = models.TextField()
    LGA = models.CharField(max_length=100, default='Unknown')
    state = models.CharField(max_length=100, default='Unknown')
    size_of_land = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=timezone.now)
    operator = models.ForeignKey(User, on_delete=models.PROTECT)
    