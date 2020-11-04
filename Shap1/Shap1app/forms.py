from . models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm


class UserCreation(UserCreationForm):
    class Meta:
        model = UserInfo
        fields = ['username','first_name','last_name','email','dob','nationality','country','countrycode','phoneno','gender']
