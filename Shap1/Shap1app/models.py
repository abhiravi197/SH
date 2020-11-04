from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserInfo(AbstractUser):
    gender=models.CharField(max_length=10)