"""pa_amb_olis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.conf import settings
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.RestaurantList.as_view(), name='llista_restaurants'),
    path('quiSom/', TemplateView.as_view(template_name='html/quiSom.html')),
    path('esdeveniments/', TemplateView.as_view(template_name='html/esdeveniments.html')),
    path('suggeriments/', TemplateView.as_view(template_name='html/suggeriments.html')),
    path('suggeriments/actualitza-restaurant/', TemplateView.as_view(template_name='html/actu_restaurant.html')),
    path('suggeriments/crea-restaurant/', TemplateView.as_view(template_name='html/crea_restaurant.html')),
    path('suggeriments/actualitza-imatges/', TemplateView.as_view(template_name='html/crud_imatges_restaurant.html')),
    path('suggeriments/crea-promocio/', TemplateView.as_view(template_name='html/promocio_noticia.html')),
    path('registre/', TemplateView.as_view(template_name='html/registre.html')),
    path('perfil/', TemplateView.as_view(template_name='html/perfil.html')),

    #CRUD PERFIL
    path('perfil/crea/', views.ProfileCreate.as_view(), name='crea_perfil'),
    #path('perfil/update/<uuid:perfil_id>', views.ProfileUpdate.as_view(), name='perfil_update'),

    #GET RESTAURANTS
    path('restaurants/', views.RestaurantList.as_view(), name='llista_restaurants'),
    path('restaurants/mapa/', views.RestaurantMapaList.as_view(), name='llista_mapa_restaurants'),

    #GET NOTICIES
    path('noticies/', views.NoticiaList.as_view(), name='llista_noticies'),


    path('accounts/', include('django.contrib.auth.urls')),
]

# DEBUG-TOOLBAR. Només es fa si està en DEBUG=True
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns