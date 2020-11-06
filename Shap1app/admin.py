from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import *
from . forms import *
# Register your models here.
class UserInfoAdmin(UserAdmin):
    model=UserInfo
    add_form=UserCreation

    fieldsets=(
    *UserAdmin.fieldsets,
    (
        'Fields',
        {
            'fields':(
                'dob',
                'nationality',
                'country',
                'countrycode',
                'phoneno',
                'gender'
            )
        }
    )
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
       (None, {'fields': ('dob',
                           'nationality',
                           'country',
                           'countrycode',
                           'phoneno',
                           'gender')}),
   )

admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(product)
admin.site.register(order)
admin.site.register(items)
