import os
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime

# Create your models here.

# https://search.creativecommons.org/photos/bde3c525-03c9-41f5-8ab6-659c44f1f881

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomillinatges = models.CharField(max_length=50)
    datanaixement = models.DateField()
    direccio = models.CharField(max_length=100)
    telefon = models.CharField(max_length=30, blank=True, default="-")
    fotoperfil = models.ImageField(upload_to = 'pic_perfil/', default = 'pic_perfil/none/no-img.jpg')

    def __str__(self):
        return '{} [{}]'.format(self.user.username, self.user.email)

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

class Restaurant(models.Model):

    ## Profile dins restaurant indica qui ha fet el restaurant (suggeriment). En certes ocasions (per donar les gràcies o en cas contrari, un baneig), pot ser útil.

    #profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="restaurant_usuari")
    nom = models.CharField(max_length=100)
    telefon = models.CharField(max_length=50)
    descripcio = models.TextField()
    horari = models.CharField(max_length=500, blank=True, default="L'horari no està disponible")
    email = models.CharField(max_length=100, blank=True, default="-")
    fax = models.CharField(max_length=50, blank=True, default="-")
    web = models.CharField(max_length=1000, blank=True, default="-")
    direccio = models.CharField(max_length=100)
    longitud = models.DecimalField(decimal_places=5, max_digits=30, blank=True, null=True)
    latitud = models.DecimalField(decimal_places=5, max_digits=30, blank=True, null=True)
    reserva = models.BooleanField(default=False)
    responsable = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)
    imatge = models.ImageField(upload_to = 'pic_restaurant/', default = 'pic_restaurant/none/no-img.jpg')

    # DATA ALTA, DATA MODIFICACIÓ
    data_alta = models.DateTimeField(auto_now_add=True)
    data_modificacio = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom
        
    # avg (mitjana) és un camp calculat
    @property
    def valoracio(self):
        try:
            avg=sum(t.valoracio for t in self.valoracio_restaurant.all())/self.valoracio_restaurant.count()
        except ZeroDivisionError:
            avg=-1
        return avg

class FotoRestaurant(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="fotos_restaurant")
    imatge = models.ImageField(upload_to = 'pic_restaurant/', default = 'pic_restaurant/none/no-img.jpg')

class ComentariRestaurant(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="comentaris_restaurant")
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="comentaris_restaurant_usuari")
    missatge = models.CharField(max_length=500)
    visible = models.BooleanField(default=True)
    data = models.DateTimeField(auto_now=True)

class ValoracioRestaurant(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="valoracio_restaurant")
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="valoracio_restaurant_usuari")
    valoracio = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

    # Evitar que un usuari pugui valorar el mateix restaurant més d'un cop (atributs únics conjunts)
    class Meta:
        unique_together = ['profile', 'valoracio']

class SuggerimentRestaurant(models.Model):

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="suggeriment_restaurant")
    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name="suggeriment_restaurant_usuari")
    explicacio = models.TextField()