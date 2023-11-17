from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model = CustomUser
        #fields = ('email', 'user_name', 'password')
        #fields = '__all__'
        exclude = ('groups','user_permissions')
        #extra_kwargs = {'password': {'write_only': True}}

    # Override create method to hash the password
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user