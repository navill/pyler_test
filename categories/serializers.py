from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

    def validate_name(self, value):
        if Category.objects.filter(name=value).exists():
            raise ValidationError(f"{value}는 이미 존재하는 카테고리 입니다.")
        return value.upper()


class CategoryAddRemoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

    def validate_name(self, value):
        if not Category.objects.filter(name=value).exists():
            raise ValidationError(f"{value}는 존재하지 않는 카테고리 입니다.")
        return value
