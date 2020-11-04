from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserInfo(AbstractUser):
    gender=models.CharField(max_length=10,blank=True)
    dob=models.DateField(blank=True,null=True)
    nationality=models.CharField(max_length=100,blank=True)
    country=models.CharField(max_length=100,blank=True)
    countrycode=models.IntegerField(null=True)
    phoneno=models.IntegerField(null=True)
