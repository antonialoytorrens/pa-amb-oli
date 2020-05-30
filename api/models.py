from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomillinatges = models.CharField(max_length=50)
    datanaixement = models.DateField()
    direccio = models.CharField(max_length=100)
    #contrasenya = models.CharField(max_length=100)
    #email = models.CharField(max_length=100, unique=True)
    #uuid = models.UUIDField("uuid", unique=True)
    telefon = models.CharField(max_length=30, blank=True, null=True)
    fotoperfil = models.ImageField(upload_to = 'pic_perfil/', default = 'pic_perfil/none/no-img.jpg')
    #fotoperfil = models.CharField(max_length=100)

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    try:
#        instance.profile.save()
#    except ObjectDoesNotExist:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()