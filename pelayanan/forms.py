from django.forms import ModelForm
from django import forms
from .models import *

class PelayananForm(ModelForm):
    class Meta:
        model = Pengaduan
        fields = '__all__'

class DeletePelayananForm(ModelForm):
    class Meta:
        model = Pengaduan
        fields = '__all__'

class StatusForm(ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['kategori_penanganan']
