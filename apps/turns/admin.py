from django.contrib import admin
from . import models

# This decorator admins automatically the displaying of a model
@admin.register(models.Turn)
class TurnAdmin(admin.ModelAdmin):
    list_display = ('turn_number', 'personal_id', 'created', 'state')

