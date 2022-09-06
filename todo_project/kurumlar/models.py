from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
import requests
import pytz

STATUS=[('person','sahis'),('bigbusiness','büyükisletme'),('kobi','kobi'),('stk','stk')]

class Kuruluslar(models.Model):
    isim = models.CharField(max_length=255)
    logo= models.ImageField(upload_to='logo_img')
    tür=models.CharField(
        default="sahis",
        choices=STATUS,
        max_length=80,
    )
    ülke= models.CharField(max_length=2, choices=pytz.country_names.items())
    websitesi=models.CharField(max_length=255)
    calisansayisi=models.IntegerField(default=0)


class Kitaplar(models.Model):
    isim = models.CharField(max_length=255)
    yazar = models.CharField(max_length=255)
    aciklama = models.TextField(blank=True, null=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi =  models.DateTimeField(auto_now=True)
    yayın_tarihi = models.DateTimeField()
    

    def __str__(self):
        return f'{self.isim} - {self.yazar}'



class Yorum(models.Model):
    kitap = models.ForeignKey(Kitaplar, on_delete=models.CASCADE, related_name='yorumlar')

    # yorum_sahibi =  models.CharField(max_length=255)
    yorum_sahibi = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kullanici_yorumlari')
    yorum = models.TextField(blank=True, null=True)

    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi =  models.DateTimeField(auto_now=True)

    degerlendirme = models.PositiveIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(5)],
    )


    def __str__(self):
        return str(self.degerlendirme)