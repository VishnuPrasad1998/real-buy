from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Listing(models.Model):
    ACTION_CHOICES = (('ONSALE', 'SELL'),('ONRENT', 'RENT'))
    PT_CHOICES = (('COMMERCIAL', 'COMMERCIAL'),('FURNISHED HOME', 'FURNISHED HOME'), ('LAND AND PLOT', 'LAND & PLOT'), ('RENTAL', 'RENTAL'))
    PRICE_CHOICES = (('10000', '10000'),('20000', '20000'), ('30000', '30000'), ('40000', '40000'), ('50000', '50000'), ('60000', '60000'), ('70000', '70000'), ('80000', '80000'), ('90000', '90000'), ('100000', '100000'), ('200000', '200000'))
    BEDROOM_CHOICES = ((1,1),(2,2),(3,3), (4,4), (5,5), (6,6), (7,7))
    BATHROOM_CHOICES = ((1,1),(2,2),(3,3), (4,4), (5,5), (6,6), (7,7))
    UNIT_CHOICES = (('yards', 'yards'), ('cents', 'cents'), ('acres', 'acres'))
    PTFLOOR_CHOICES = ((1,1),(2,2),(3,3), (4,4), (5,5), (6,6), (7,7))
    TRANSACTION_CHOICES = (('Resale', 'Resale'), ('new', 'New Booking'))
    OWNERSHIP_CHOICES = (('Individual', 'Individual'), ('Joint', 'Joint'))
    TOTALFLOOR_CHOICES = ((1,1),(2,2),(3,3), (4,4), (5,5), (6,6), (7,7))
    AVAILABILITY_CHOICES = (('ready', 'Ready to move'), ('construction', 'Under construction'))

    action_type = models.CharField(max_length=200, choices=ACTION_CHOICES)
    title = models.CharField(max_length=200, blank=False)
    property_type = models.CharField(max_length=200, choices=PT_CHOICES)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False)
    city = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=200, blank=False)
    location = models.CharField(max_length=200, blank=False)
    address = models.CharField(max_length=200, blank=False)
    price = models.FloatField()
    bedrooms = models.IntegerField(choices=BEDROOM_CHOICES)
    bathrooms = models.IntegerField(choices=BATHROOM_CHOICES)
    built_up_area = models.FloatField(blank=False)
    carpet_area = models.FloatField(blank=False)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_CHOICES)
    property_floor = models.IntegerField(choices=PTFLOOR_CHOICES)
    ownership = models.CharField(max_length=200, choices=OWNERSHIP_CHOICES)
    total_floors = models.IntegerField(choices=TOTALFLOOR_CHOICES)
    availability = models.CharField(max_length=200, choices=AVAILABILITY_CHOICES)
    description = models.TextField(blank=True)
    posting_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title