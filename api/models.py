from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime

# Create your models here.

class Noticia(models.Model):
    titol = models.CharField(max_length=400)
    cos = models.TextField()
    data = models.DateField(default=datetime.now, blank=True, null=True)

class FotoNoticia(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    imatge = models.ImageField(upload_to = 'pic_noticia/', default = 'pic_noticia/none/no-img.jpg')


class Esdeveniment(models.Model):
    titol = models.CharField(max_length=400)
    descripcio = models.TextField()
    # longitud, latitud; és a dir, el lloc
    longitud = models.DecimalField(decimal_places=5, max_digits=30)
    latitud = models.DecimalField(decimal_places=5, max_digits=30)
    # since, until; és a dir, l'horari
    since = models.DateTimeField()
    until = models.DateTimeField()

class TipusSuggeriment(models.Model):
    nom = models.CharField(max_length=100)
    descripcio = models.TextField()

class Suggeriment(models.Model):
    tipus = models.ForeignKey(TipusSuggeriment, on_delete=models.PROTECT)

    # Tots els camps podran ser nul ja que en cada suggeriment hi ha diferents camps disponibles.

    # AFEGIR RESTAURANT, CANVIAR INFO RESTAURANT
    nom_restaurant = models.CharField(max_length=100, blank=True, null=True)
    direccio = models.CharField(max_length=100, blank=True, null=True)
    horari = models.CharField(max_length=100, blank=True, null=True)
    descripcio = models.TextField(blank=True, null=True)
    telefon = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    reservaTaula = models.BooleanField(blank=True, null=True)
    responsableRestaurant = models.BooleanField(blank=True, null=True)
    ## CANVIAR IMATGE RESTAURANT
    imatge_restaurant = models.ImageField(upload_to = 'pic_restaurant/', default = 'pic_restaurant/none/no-img.jpg', blank=True, null=True)
    ## PROMOCIO_NOTICIA
    #nom_producte = models.CharField(max_length=100, blank=True, null=True)
    #nom_negoci = models.CharField(max_length=100, blank=True, null=True)
    #web = models.TextField(blank=True, null=True)
    #imatge_noticia = models.ImageField(upload_to = 'pic_noticia/', default = 'pic_noticia/none/no-img.jpg', blank=True, null=True)


class Restaurant(models.Model):

    nom = models.CharField(max_length=100)
    telefon = models.CharField(max_length=50)
    descripcio = models.TextField()
    email = models.CharField(max_length=100, blank=True, default="-")
    fax = models.CharField(max_length=50, blank=True, default="-")
    web = models.TextField(blank=True, default="-")
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