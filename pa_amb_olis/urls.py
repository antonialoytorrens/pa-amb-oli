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
from .routers import router
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='html/restaurants.html')),
    path('quiSom/', TemplateView.as_view(template_name='html/quiSom.html')),
    path('noticies/', TemplateView.as_view(template_name='html/noticies.html')),
    path('restaurants/', TemplateView.as_view(template_name='html/restaurants.html')),
    path('esdeveniments/', TemplateView.as_view(template_name='html/esdeveniments.html')),
    path('suggeriments/', TemplateView.as_view(template_name='html/suggeriments.html')),
    path('suggeriments/actualitza-restaurant/', TemplateView.as_view(template_name='html/actu_restaurant.html')),
    path('suggeriments/crea-restaurant/', TemplateView.as_view(template_name='html/crea_restaurant.html')),
    path('suggeriments/actualitza-imatges/', TemplateView.as_view(template_name='html/crud_imatges_restaurant.html')),
    path('suggeriments/crea-promocio/', TemplateView.as_view(template_name='html/promocio_noticia.html')),
    path('registre/', TemplateView.as_view(template_name='html/registre.html')),
    path('login/', TemplateView.as_view(template_name='html/login.html')),
    path('perfil/', TemplateView.as_view(template_name='html/perfil.html')),
]
