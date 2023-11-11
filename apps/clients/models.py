from django.db import models


class Client(models.Model):

    options = (
        ('cedula', 'CC'),
        ('tarjeta_identidad', 'TI'),
        ('pasaporte', 'PA'),
        ('cedula_extrangería', 'CE'),
    )
    id_type = models.CharField(choices=options, default='cedula')
    personal_id = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.personal_id