from django.db import models


# Create your models here.

class Detail(models.Model):
    internship = True
    fulltime = False
    job_title = models.TextField()
    company = models.TextField()
    county = models.CharField(max_length=15)
    email = models.EmailField()
    phone_number = models.TextField()
    position = models.BooleanField(default=internship)

