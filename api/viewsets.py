from rest_framework import viewsets, filters

from .models import Restaurant, Usuari
from .serializers import RestaurantSerializer, UsuariSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class UsuariViewSet(viewsets.ModelViewSet):
    queryset = Usuari.objects.all()
    serializer_class = UsuariSerializer