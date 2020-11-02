from django.db import models
from datetime import datetime

class Contactus(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    message = models.TextField(max_length=500, blank=False)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name