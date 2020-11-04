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

    def __str__(self):
        return self.username

class product(models.Model):
    prod_id=models.CharField(max_length=10,blank=True,)
    prod_name=models.CharField(max_length=100,blank=True)
    prod_image=models.FileField(upload_to ='')
    prod_category=models.CharField(max_length=100,blank=True)
    prod_subcategory=models.CharField(max_length=100,blank=True)
    prod_price=models.FloatField(null=True,blank=True)
    discount=models.FloatField(null=True,blank=True)
    stock_balance=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.prod_name

class order(models.Model):
    order_id=models.CharField(max_length=10,blank=True)
    username=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    product_id=models.ForeignKey(product,on_delete=models.CASCADE)
    total_price=models.FloatField(null=True,blank=True)
    discount_price=models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.order_id

class items(models.Model):
    product_id=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.product_id