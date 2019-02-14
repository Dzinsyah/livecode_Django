from django.db import models
from django.utils import timezone

class Home(models.Model):
    nama = models.CharField(max_length =100)
    images = models.CharField(max_length =255)
    harga = models.CharField(max_length =255)
    deskripsi1 = models.TextField(max_length =1000)
    deskripsi2 = models.TextField(max_length =1000)
    deskripsi3 = models.TextField(max_length =1000)
    deskripsi4 = models.TextField(max_length =1000)
    deskripsi5 = models.TextField(max_length =1000)
    def __str__(self):
        return self.nama

# Create your models here.
