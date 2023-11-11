from django.contrib import admin
from . import models

@admin.register(models.Desk)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'state', 'busy')
