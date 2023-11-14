from django.contrib import admin
from . import models

# This decorator admins automatically the displaying of a model
@admin.register(models.Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'priority')
    
