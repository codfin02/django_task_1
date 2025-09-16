from django.contrib import admin
from django.urls import include, path

from blog import views as blog_views
from todo import views as todo_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_views.blog_list, name='blog_list'),
    path('<int:pk>/', blog_views.blog_detail, name='blog_detail'),
    path('todo/', todo_views.todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_views.todo_info, name='todo_info'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', user_views.login_view, name='login'),
    path('accounts/signup/', user_views.sign_up, name='signup'),
]
