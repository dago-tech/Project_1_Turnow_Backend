from rest_framework import serializers
from ..desks.models import *


class WaitingTimeByDeskSerializer(serializers.Serializer):
    desk = serializers.CharField(source='name')
    waiting_time_avg = serializers.FloatField()
    duration_avg = serializers.FloatField()

    class Meta:
        model = Desk
        fields = ('name', 'waiting_time_avg', 'duration_avg')