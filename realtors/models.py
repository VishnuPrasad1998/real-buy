from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=200, default="Adam")
    last_name = models.CharField(max_length=200, default="John")
    username = models.CharField(max_length=200, default="adj111")
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50)
    address = models.TextField(max_length=500,blank=True)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name