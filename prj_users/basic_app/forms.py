from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(label='암호',widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {
            'username':'사용자이름',
            'email':'이메일',
            'password':'암호',
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
        labels = {
            'portfolio_site':'포트폴리오 사이트',
            'profile_pic':'사진',
        }