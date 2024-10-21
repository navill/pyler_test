from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()


class RegisterResponseSerializer(serializers.Serializer):
    identifier = serializers.UUIDField()
    username = serializers.CharField()
    token = TokenSerializer()


class PylerUserSerializer(serializers.Serializer):
    identifier = serializers.UUIDField()
    username = serializers.CharField()
    is_staff = serializers.BooleanField()
