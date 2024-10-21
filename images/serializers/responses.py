from rest_framework import serializers

from categories.serializers import CategorySerializer


class UploaderSerializer(serializers.Serializer):
    identifier = serializers.UUIDField()
    username = serializers.CharField()


class ImageResponseSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    user = UploaderSerializer()
    category_set = CategorySerializer(many=True)
    image_file = serializers.ImageField()
    description = serializers.CharField()

    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class ImageListResponseSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    thumbnail = serializers.ImageField()

    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()


class ImageCategoriesResponseSerializer(serializers.Serializer):
    identifier = serializers.CharField()
    category_set = CategorySerializer(many=True)
