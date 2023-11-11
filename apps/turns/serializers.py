from rest_framework import serializers
from .models import *


class TurnSerializer(serializers.ModelSerializer):
    # start_time = serializers.DateTimeField(allow_null=True, required=False)
    # end_time = serializers.DateTimeField(allow_null=True, required=False)
    # duration = serializers.DateTimeField(allow_null=True, required=False)
    
    class Meta:
        model = Turn
        fields = '__all__'