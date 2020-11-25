from django.db import models


# Create your models here.

class Detail(models.Model):
    field = models.TextField(max_length=50)
    subfield = models.TextField(max_length=100)
    company_name = models.TextField(max_length=50)
    county = models.TextField(max_length=50)
    email = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    salary = models.IntegerField()
    years = models.FloatField()

