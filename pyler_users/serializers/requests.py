from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainSerializer

from pyler_users.models import PylerUser


class LoginSerializer(TokenObtainSerializer):
    username = serializers.CharField(min_length=5, max_length=20, required=True)
    password = serializers.CharField(min_length=8, max_length=20, required=True)


class RegisterRequestSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=5, max_length=20, required=True)
    password = serializers.CharField(min_length=8, max_length=20, required=True)
    password_confirm = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)

    class Meta:
        model = PylerUser
        fields = ('username', 'password', 'password_confirm')

    def validate(self, attrs: dict) -> dict:
        if attrs['password'] != attrs.pop('password_confirm'):
            raise ValidationError(detail="passwords don't match")
        return attrs
