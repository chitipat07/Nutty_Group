from django import forms
from django.forms import CheckboxInput
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

        widgets = {
        'username': forms.ClearableFileInput(attrs={'class': 'block w-full text-lg text-gray-900 border border-gray-300 cursor-pointer'}),
        'password1': forms.PasswordInput(attrs={'class': 'block w-full text-lg text-gray-900 border border-gray-300 cursor-pointer'}),
        'password2': forms.PasswordInput(attrs={'class': 'block w-full text-lg text-gray-900 border border-gray-300 cursor-pointer'}),
        
    }
    



class Loginforms(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields = ['username','password']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"

        labels = {'price':'ราคา',
                  'image':'รูปภาพ',
                  'name':'ชื่ออาหาร'}
        
        widgets = {
        'image': forms.ClearableFileInput(attrs={'class': 'block w-full text-lg text-gray-900 border border-gray-300 cursor-pointer'}),
    }