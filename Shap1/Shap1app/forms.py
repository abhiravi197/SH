from . models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm


class UserCreation(UserCreationForm):
    gender=(
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other')
    )
    gender=forms.ChoiceField(choices=gender,widget=forms.Select(attrs={'class':'input1'}))
    class Meta:
        model = UserInfo
        fields = ['username','first_name','last_name','email','dob','nationality','country','countrycode','phoneno','gender']
        forms.DateInput.input_type="date"
        widget={
            'dob':forms.DateInput(attrs={"class":"form-control"}),
        
        }