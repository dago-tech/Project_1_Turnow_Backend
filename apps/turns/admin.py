from django.contrib import admin
from . import models


@admin.register(models.Turn)
class TurnAdmin(admin.ModelAdmin):
    list_display = ('turn_number', 'personal_id', 'created', 'state')

