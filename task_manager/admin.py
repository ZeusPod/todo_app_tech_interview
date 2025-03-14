from django.contrib import admin
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'completed', 'created_at', 'due_date')
    list_filter = ('completed',)
    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)
