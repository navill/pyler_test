from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from categories.models import Category
from images.models import Image
from images.utils import rename_filename


class ImageUploadSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category_names = serializers.ListField()

    class Meta:
        model = Image
        fields = ["user", "image_file", "category_names", "description"]

    def validate_category_names(self, input_value: list[str]) -> list[str]:
        input_size = len(input_value)
        if input_size == 0:
            return input_value

        if input_size > 5:
            raise ValidationError("이미지에 추가할 수 있는 카테고리는 최대 5개 입니다")

        filtered_category_names = Category.objects.filter(name__in=input_value).values_list("name", flat=True)
        if input_size != len(filtered_category_names):
            invalid_names = set(input_value) - set(filtered_category_names)
            raise ValidationError(f"입력된 카테고리({', '.join(invalid_names)})는 존재하지 않습니다.")

        return input_value

    def validate_image_file(self, input_value: InMemoryUploadedFile) -> InMemoryUploadedFile:
        input_value.name = rename_filename(input_value.name)
        return input_value

    def create(self, validated_data: dict) -> Image:
        category_names = validated_data.pop("category_names", None)
        with transaction.atomic():
            image = Image.objects.create(**validated_data)
            if category_names:
                categories = Category.objects.filter(name__in=category_names)
                image.category_set.add(*categories)
        return image
