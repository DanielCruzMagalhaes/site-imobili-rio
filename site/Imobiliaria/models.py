from django.db import models

# Create your models here.

class Imoveis(models.Model):
    adress = models.CharField(max_length=200)
    status = models.CharField(max_length=100)
    area = models.CharField()
    bedrooms = models.CharField()
    floor = models.CharField()
    parking = models.CharField()
    value = models.CharField()
    type = models.CharField()
    path = models.CharField()