from django.db import models

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=255) #Masukkin nama dalam bentuk string
    price=models.IntegerField() #Masukkin angka dalam bentuk integer
    description=models.TextField() #Masukkin deskripsi dalam bentuk string

@property
def __str__(self):
    return self.name