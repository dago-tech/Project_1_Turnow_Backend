from rest_framework import serializers
from .models import *


class TurnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Turn
        fields = '__all__'