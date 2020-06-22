from django.contrib import admin
from .models import Profile, Restaurant, FotoRestaurant, Noticia, FotoNoticia, Esdeveniment, ComentariRestaurant, ValoracioRestaurant, SuggerimentRestaurant

# Perfil

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nomillinatges', 'user')

# Restaurant amb imatges i comentaris
class FotoRestaurantInline(admin.TabularInline):
    model = FotoRestaurant

class ComentariRestaurantInline(admin.TabularInline):
    list_display = ('missatge', 'visible', 'get_user')
    model = ComentariRestaurant

    def get_user(self, obj):
        return obj.profile.user
    
    get_user.admin_order_field = 'usuari__user'

class ComentariRestaurantAdmin(admin.ModelAdmin):
    list_display = ('restaurant', 'missatge', 'data', 'visible', 'usuari')
    list_editable = ('visible',)
    list_filter = ('visible', 'restaurant')
    ordering = ('-data', 'visible', 'restaurant')

    def usuari(self, obj):
        return obj.profile.user
    
    usuari.admin_order_field = 'usuari__user'

class ValoracioRestaurantInline(admin.TabularInline):
    list_display = ('get_user', 'get_restaurant', 'valoracio')
    model = ValoracioRestaurant

    def get_user(self, obj):
        return obj.profile.user

    def get_restaurant(self, obj):
        return obj.restaurant.nom
    
    get_user.admin_order_field = 'usuari__user'
    get_restaurant.admin_order_field = 'restaurant__nom'

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telefon', 'direccio', 'responsable', 'visible', 'data_alta', 'data_modificacio', 'creador')
    list_editable = ('visible',)
    list_filter = ('visible',)
    ordering = ('visible', 'nom')
    inlines = [
        FotoRestaurantInline,
        ComentariRestaurantInline,
        ValoracioRestaurantInline,
    ]

    def creador(self, obj):
        return obj.profile.user.username + ' [{email}]'.format(email=obj.profile.user.email)

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

# Suggeriments

class SuggerimentRestaurantAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_restaurant', 'explicacio')

    def get_user(self, obj):
        return obj.profile.user

    def get_restaurant(self, obj):
        return obj.restaurant.nom
    
    get_user.admin_order_field = 'usuari__user'
    get_restaurant.admin_order_field = 'restaurant__nom'

# Register your models here.

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(ComentariRestaurant, ComentariRestaurantAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Esdeveniment, EsdevenimentAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(SuggerimentRestaurant, SuggerimentRestaurantAdmin)