from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    restaurant_nom = models.CharField(max_length=100)
    restaurant_telefon = models.CharField(max_length=50)
    restaurant_descripcio = models.TextField()
    restaurant_email = models.CharField(max_length=100)
    restaurant_web = models.TextField()
    restaurant_direccio = models.TextField()

class MultimediaRestaurant(models.Model):
    multimedia_id= models.AutoField(primary_key=True)
    multimedia_imatge= models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/none/no-img.jpg')

    # If the restaurant is erased, images will be also deleted.
    fk_restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Usuari(models.Model):
    usuari_id = models.AutoField(primary_key=True)
    usuari_nom = models.CharField(max_length=100)
    usuari_email = models.CharField(max_length=100)
    usuari_contrasenya = make_password(models.CharField(max_length=100))