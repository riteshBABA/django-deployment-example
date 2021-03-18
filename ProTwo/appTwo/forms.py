from django import forms
from django.core import validators
from .models import Users,UserProfileInfo
from django.contrib.auth.models import User
# class NewUserForm(forms.ModelForm):
#     class Meta:
#         model = Users
#         fields = '__all__'

class UserFormInfo(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')