from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Noticia(models.Model):
    titol = models.TextField()
    cos = models.TextField()

class FotoNoticia(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    imatge = models.ImageField(upload_to = 'pic_noticia/', default = 'pic_noticia/none/no-img.jpg')


class Restaurant(models.Model):
    nom = models.CharField(max_length=100)
    telefon = models.CharField(max_length=50)
    descripcio = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    web = models.CharField(max_length=200, blank=True, null=True)
    direccio = models.CharField(max_length=100)
    longitud = models.DecimalField(decimal_places=5, max_digits=30)
    latitud = models.DecimalField(decimal_places=5, max_digits=30)

class FotoRestaurant(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    imatge = models.ImageField(upload_to = 'pic_restaurant/', default = 'pic_restaurant/none/no-img.jpg')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomillinatges = models.CharField(max_length=50)
    datanaixement = models.DateField()
    direccio = models.CharField(max_length=100)
    telefon = models.CharField(max_length=30, blank=True, null=True)
    fotoperfil = models.ImageField(upload_to = 'pic_perfil/', default = 'pic_perfil/none/no-img.jpg')