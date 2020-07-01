from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class AdminForm(ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
        exclude = ['user', 'profile_pict']

class PenangananForm(ModelForm):
    class Meta:
        model = Penanganan
        fields = ['solusi']

class StatusForm(ModelForm):
    class Meta:
        model = Penanganan
        fields = '__all__'
        exclude = ['solusi']

class MasalahForm(ModelForm):
    class Meta:
        model = Masalah
        fields = '__all__'
