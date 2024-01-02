from django.contrib import admin
from . import models

# This decorator admins automatically the displaying of a model
@admin.register(models.Desk)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'state', 'busy')
