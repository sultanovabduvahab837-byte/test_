from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'is_done', 'created_at')  # что показывать в списке
    list_filter = ('is_done', 'created_at')  # фильтры справа
    search_fields = ('title', 'description')  # поиск по полям
