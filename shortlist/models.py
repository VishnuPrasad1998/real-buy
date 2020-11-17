from django.db import models
from datetime import datetime
# Create your models here.
class Shortlist(models.Model):
    SLOT = (('FORENOON', 'FORENOON'), ('AFTERNOON', 'AFTERNOON'))

    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    user_id = models.IntegerField(blank=True)
    shortlist_date = models.DateTimeField(default=datetime.now, blank=True)
    slot = models.CharField(max_length=50, choices=SLOT)
    message = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.name