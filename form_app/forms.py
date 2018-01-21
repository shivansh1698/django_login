from django import forms
from django.forms import ModelForm
from django.core import validators
from form_app.models import UserInfo,UserTextData,UserImageData
from django.contrib.auth.models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']

class TextForm(ModelForm):
    class Meta:
        model = UserTextData
        fields = ['user','text']

class ImageForm(ModelForm):
    class Meta:
        model = UserImageData
        fields = ['user','image']



    