from rest_framework import serializers
from ..desks.models import *
from ..turns.models import *


class WaitingTimeSerializer(serializers.Serializer):
    name = serializers.CharField()
    waiting_time_avg = serializers.FloatField()
    duration_avg = serializers.FloatField()

    class Meta:
        model = Turn
        fields = ('name', 'waiting_time_avg', 'duration_avg')


class TurnCountSerializer(serializers.Serializer):
    name = serializers.CharField()
    turn_count = serializers.IntegerField()

    class Meta:
        model = Turn
        fields = ('name', 'waiting_time_avg', 'duration_avg')