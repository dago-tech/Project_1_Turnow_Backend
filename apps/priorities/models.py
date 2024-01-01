from django.db import models
from django.core.validators import MaxValueValidator


class Priority(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    priority = models.IntegerField(
        default=0, validators=[MaxValueValidator(limit_value=20)]
    )

    class Meta:
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name
