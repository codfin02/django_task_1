from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_completed', 'start_date', 'end_date')
    list_display_links = ('title',)
    list_filter = ('is_completed', 'start_date', 'end_date')
    search_fields = ('title', 'description')
    ordering = ('start_date',)
    fieldsets = (
        ('기본 정보', {'fields': ('title', 'description', 'is_completed')}),
        ('기간', {'fields': ('start_date', 'end_date')}),
    )
