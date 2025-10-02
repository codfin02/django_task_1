from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cbv/', include('todo.urls')),
    path('summernote/', include('django_summernote.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', user_views.login_view, name='login'),
    path('accounts/signup/', user_views.sign_up, name='signup'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

