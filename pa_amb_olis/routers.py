from rest_framework import routers
from api.viewsets import UsuariViewSet, RestaurantViewSet

router = routers.DefaultRouter()
router.register(r'restaurant', RestaurantViewSet)
router.register(r'usuari', UsuariViewSet)