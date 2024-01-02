from django.db import models
from apps.clients.models import *
from apps.categories.models import *
from apps.priorities.models import *
from apps.desks.models import *


class Turn(models.Model):
    options = (
        ("pending", "Pending"),
        ("serving", "Serving"),
        ("served", "Served"),
        ("first to serve", "First to serve"),
        ("cancelled", "Cancelled"),
    )

    turn_number = models.CharField(max_length=4, null=True, blank=True, default="0")
    personal_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)
    desk = models.ForeignKey(Desk, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    waiting_time = models.IntegerField(null=True, blank=True)
    state = models.CharField(choices=options, default="pending")

    def __str__(self):
        return str(self.turn_number)


class TurnConfig(models.Model):
    restart_turn = models.BooleanField(default=False)

    # @... Indicates that the following method is a class method, meaning that it can
    # be called on the class instead of on an instance of the class.
    @classmethod
    def get_instance(cls):
        # get_or_create returns a tuple with the instance and a bool state that indicates
        # if instante was created or not.
        instance, created = cls.objects.get_or_create(pk=1)
        return instance

    def __str__(self):
        return str(self.restart_turn)
