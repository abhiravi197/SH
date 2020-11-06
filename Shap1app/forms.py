from . models import *
from django import forms

from django.contrib.auth.forms import UserCreationForm


class UserCreation(UserCreationForm):
    gender=(
        ('Male','Male'),
        ('Female','Female'),

    )
    gender=forms.ChoiceField(choices=gender,widget=forms.RadioSelect(attrs={'class':'input'}))
    class Meta:
        model = UserInfo
        fields = ['username','first_name','last_name','email','dob','nationality','country','countrycode','phoneno','gender']
        forms.DateInput.input_type="date"
        widget={
            'dob':forms.DateInput(attrs={"class":"form-control"}),
            'username':forms.TextInput(attrs={"placeholder":"Username"}),
            'first_name': forms.TextInput(attrs={'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder':'Email'}),
            'phoneno': forms.TextInput(attrs={'placeholder':'Phone Number'}),
            'country': forms.TextInput(attrs={'placeholder':'Country'}),
            'countrycode': forms.TextInput(attrs={'placeholder':'CountryCode'}),
            'nationality':forms.TextInput(attrs={'placeholder':'nationality'}),

        }
# class UserEditForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ('first_name','last_name','email',)
#
#        widgets = {
#            'first_name': forms.TextInput(attrs={'placeholder':'First Name'}),
#            'last_name': forms.TextInput(attrs={'placeholder':'Last Name'}),
#            'email': forms.TextInput(attrs={'placeholder':'Email'}),
#        }
#
#    def __init__(self, *args, **kwargs):
#        super(UserEditForm, self).__init__(*args, **kwargs)
#        self.fields['first_name'].required = False
#        self.fields['last_name'].required = False
#        self.helper = FormHelper()
#        self.helper.form_show_labels = False
#
#
#
# class ProfileForm(forms.ModelForm):
#    class Meta:
#        model = Profile
#        fields = ('phone','country','city')
#
#        widgets = {
#            'phone': forms.TextInput(attrs={'placeholder':'Phone Number'}),
#            'country': forms.TextInput(attrs={'placeholder':'Country'}),
#            'city': forms.TextInput(attrs={'placeholder':'City'}),
#        }
#
#    def __init__(self, *args, **kwargs):
#        super(ProfileForm, self).__init__(*args, **kwargs)
#        self.fields['phone'].required = True
#        self.helper = FormHelper()
#        self.helper.form_show_labels = False
