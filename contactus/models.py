from django.db import models
from datetime import datetime

class Contactus(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    message = models.TextField(max_length=500,blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name