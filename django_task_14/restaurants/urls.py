from rest_framework import routers
from restaurants.views import RestaurantViewSet

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
