from django.db import models
from master.models import *
from accounts.models import *
from django.contrib.auth.models import User

# Create your models here.

class Pengaduan(models.Model):
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    kategori_pengaduan = models.ForeignKey(KategoriPengaduan, null=True, on_delete=models.SET_NULL)
    keluhan = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    selesai = models.BooleanField(null=True)
    kategori_penanganan = models.ForeignKey(KategoriPenanganan, null=True, on_delete=models.SET_NULL)

class Respon(models.Model):
    pengaduan = models.ForeignKey(Pengaduan, null=True, on_delete=models.SET_NULL)
    oleh = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    respon = models.TextField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
