from django.contrib import admin
from django.urls import path, include
from config.schema import swagger_patterns

try:
    from restaurants.urls import router as restaurants_router
except Exception:
    restaurants_router = None

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]

if restaurants_router:
    urlpatterns += [path('', include(restaurants_router.urls))]

urlpatterns += [path('', include('reviews.urls'))]
urlpatterns += swagger_patterns

