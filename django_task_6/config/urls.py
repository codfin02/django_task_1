from django.contrib import admin
from django.urls import include, path
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # CBV Todo endpoints under /cbv/
    path('cbv/', include('todo.urls')),

    # Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', user_views.login_view, name='login'),
    path('accounts/signup/', user_views.sign_up, name='signup'),
]

