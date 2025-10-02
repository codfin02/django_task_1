"""config URL Configuration."""
from django.contrib import admin
from django.urls import path

from todo.views import todo_info, todo_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
]
