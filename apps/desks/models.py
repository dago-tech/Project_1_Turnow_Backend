from django.db import models
from django.conf import settings
from apps.categories.models import *


class Desk(models.Model):
    name = models.CharField(max_length=30, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    state = models.BooleanField(default=True)
    busy = models.BooleanField(default=False)

    def __str__(self):
        return self.name
