from django.contrib import admin
from .models import Profile, Restaurant, FotoRestaurant, Noticia, FotoNoticia, Esdeveniment

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
    list_display = ('titol', 'data')
    inlines = [
        FotoNoticiaInline,
    ]

# Esdeveniment amb horaris

class EsdevenimentAdmin(admin.ModelAdmin):
    list_display = ('titol', 'since', 'until')

# Register your models here.

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Esdeveniment, EsdevenimentAdmin)
admin.site.register(Profile)