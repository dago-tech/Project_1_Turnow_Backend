from django.contrib import admin
from . import models

# This decorator admins automatically the displaying of a model
@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id_type', 'personal_id')
