from django.contrib import admin
from . import models

@admin.register(models.Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'priority')
    
