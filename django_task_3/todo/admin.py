from django.contrib import admin

from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'owner', 'is_completed', 'due_date')
    list_filter = ('is_completed', 'due_date')
    search_fields = ('title', 'description')
    ordering = ('is_completed', 'due_date')

