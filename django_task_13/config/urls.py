from django.contrib import admin
from django.urls import path, include

try:
    from restaurants.urls import router as restaurants_router
except Exception:  # pragma: no cover - allows import order before app exists
    restaurants_router = None

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]

if restaurants_router:
    urlpatterns += [path('', include(restaurants_router.urls))]

urlpatterns += [path('', include('reviews.urls'))]

