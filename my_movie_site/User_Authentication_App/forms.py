from django import forms
from django.contrib.auth.models import User
from .models import UserProfileExtraInfo

class UserInputForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileExtraInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileExtraInfo
        fields = ('portfolio_mobnumber','profile_pic')
