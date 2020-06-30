from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    nama = models.CharField(max_length=200, null=True)
    alamat = models.CharField(max_length=200, null=True)
    no_hp = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pict = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama

class Client(models.Model):
    nama = models.CharField(max_length=200, null=True)
    no_hp = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nama

class Tag(models.Model):
    nama = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nama

class Masalah(models.Model):
    KATEGORI = (
                ('Pijo Mati', 'Pijo Mati'),
                ('Aplikai Error', 'Aplikasi Error'),
                )
    nama = models.CharField(max_length=200, null=True)
    kategori = models.CharField(max_length=200, null=True, choices=KATEGORI)
    deskripsi = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.nama

class Penanganan(models.Model):
    STATUS = (
            ('Online', 'Online'),
            ('TKP', 'TKP'),
            ('Selesai', 'Selesai'),
            )

    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    masalah = models.ForeignKey(Masalah, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    solusi = models.CharField(max_length=200, null=True, blank=True)
