import pathlib
import random
from typing import Iterator

from django.core.files import File
from django.core.management.base import BaseCommand
from django.db import IntegrityError

from categories.models import Category
from images.models import Image
from pyler_users.models import PylerUser


class Command(BaseCommand):
    help = "카테고리 및 더미데이터를 마이그레이션 합니다."
    default_category_names = ["PERSON", "LANDSCAPE", "ANIMAL", "FOOD", "OTHERS"]

    def handle(self, *args, **kwargs):
        categories = self._get_or_create_categories()
        _ = self._get_or_create_admin_user()
        users = self._get_or_create_sample_users()
        for user in users:
            # 유저별 이미지 저장 후 랜덤 카테고리 2개씩 추가
            category_list = random.sample(categories, 2)
            self._create_sample_images(user, category_list)

    def _get_or_create_categories(self) -> list[Category]:
        has_categories = Category.objects.exists()
        if not has_categories:
            categories = [Category(name=name) for name in self.default_category_names]
            return Category.objects.bulk_create(categories)
        return list(Category.objects.all())

    def _get_or_create_admin_user(self) -> PylerUser:
        admin_name = "admin"
        try:
            user = PylerUser.objects.create_user(username=admin_name, password="test1234")
        except IntegrityError:
            user = PylerUser.objects.get(username=admin_name)
        return user

    def _get_or_create_sample_users(self) -> list[PylerUser]:
        users = []
        for number in range(5):
            username = f"testuser-{number}"
            try:
                user = PylerUser.objects.create_user(username=username, password="test1234")
            except IntegrityError:
                user = PylerUser.objects.get(username=username)
            users.append(user)
        return users

    def _create_sample_images(self, user: PylerUser, categories: Iterator[Category]) -> list[Image]:
        path_list = list(pathlib.Path("core/management/commands/dummy_images").glob("*"))
        image_list = []
        for path in path_list:
            if path.is_file():
                with open(path, "rb") as file:
                    image_file = File(file, name=path.name)
                    image = Image.objects.create(user=user, image_file=image_file)
                image.category_set.add(*categories)
                image_list.append(image)
        return image_list
