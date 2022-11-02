from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone',
                  'login',
                  'name',
                  'birth',
                  'tg',
                  'email', ]


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['login',
                  'password', ]
