from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms

'''
class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
'''



class CustomUserAdmin(UserAdmin):
    model = User
    # add_form = CustumUserCreationForm
    list_display = ('email', 'is_superuser','is_active','is_verified')
    list_filter =  ('email', 'is_superuser','is_active','is_verified')
    searching_fields= ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication',{
            "fields":(
                'email','password'
            ),
        }),
        ('permissions',{
            "fields":(
                'is_active','is_staff','is_superuser','is_verified'
            ),
        }),
        ('group permissions',{
            "fields":(
                'groups','user_permissions'
            ),
        }),
        ('important date',{
            "fields":(
                'last_login',
            ),
        }),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('email','password1','password2','is_staff','is_superuser','is_active','is_verified')
            }),
    )




admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)
