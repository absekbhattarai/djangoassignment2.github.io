from django.forms import ModelForm, DateField, DateInput,widgets
from django import forms
from .models import UserInfo
from datetime import date
from django.contrib.auth.models import User


class Register(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ['username','password','email','first_name','last_name']


class UserInfoForm(ModelForm):
    date_of_birth = forms.DateField(label='dd/mm/yyyy',
                 widget=forms.TextInput(attrs={'class':'datePicker'}))

    class Meta():
         model = UserInfo
         fields = ['date_of_birth']

class EditProfileBio(ModelForm):
    class Meta():
        model = UserInfo
        fields = ['bio','profile_picture','date_of_birth']