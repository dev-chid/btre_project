from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True, max_length=200)
    price = models.CharField(max_length=200)
    bedrooms = models.CharField(max_length=200)
    bathrooms = models.CharField(max_length=200)
    garage = models.CharField(max_length=200)
    sqft = models.CharField(max_length=200)
    lot_size = models.CharField(max_length=200)
    photo_main = models.ImageField(upload_to='photos/%Y/%M/%d')
    photo_1 = models.ImageField(upload_to='photos/%Y/%M/%d')
    photo_2 = models.ImageField(upload_to='photos/%Y/%M/%d')
    photo_3 = models.ImageField(upload_to='photos/%Y/%M/%d')
    photo_4 = models.ImageField(upload_to='photos/%Y/%M/%d')
    photo_5 = models.ImageField(upload_to='photos/%Y/%M/%d')
    photo_6 = models.ImageField(upload_to='photos/%Y/%M/%d')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
    