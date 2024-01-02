from rest_framework import serializers
from .models import *


class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = "__all__"


class TurnDeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = ["id", "turn_number", "desk"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["desk"] = instance.desk.name
        return representation


class TurnConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnConfig
        fields = "__all__"
