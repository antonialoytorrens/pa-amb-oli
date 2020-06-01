from django.contrib import admin
from .models import Profile, Restaurant, FotoRestaurant, Noticia, FotoNoticia

# Restaurant amb imatges
class FotoRestaurantInline(admin.TabularInline):
    model = FotoRestaurant

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [
        FotoRestaurantInline,
    ]

# Noticia amb imatges

class FotoNoticiaInline(admin.TabularInline):
    model = FotoNoticia

class NoticiaAdmin(admin.ModelAdmin):
    inlines = [
        FotoNoticiaInline,
    ]

# Register your models here.

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Profile)