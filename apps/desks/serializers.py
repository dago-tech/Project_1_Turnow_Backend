from rest_framework import serializers
from .models import *


class DeskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desk
        fields = "__all__"
