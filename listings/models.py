from django.db import models
from realtors.models import Realtor

# Create your models here.


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
