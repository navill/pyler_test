from django.db import models

from categories.managers import CategoryManager, ImageCategoryManager
from core.models import BaseModel


class Category(BaseModel):
    image_set = models.ManyToManyField(to="images.Image",
                                       through="categories.ImageCategory",
                                       related_name="category_set",
                                       verbose_name="이미지 관계 테이블")
    name = models.CharField(max_length=32, unique=True, verbose_name="카테고리 이름")

    objects = CategoryManager()


class ImageCategory(BaseModel):
    image = models.ForeignKey(to="images.Image", on_delete=models.DO_NOTHING)
    category = models.ForeignKey(to="categories.Category", on_delete=models.DO_NOTHING)

    objects = ImageCategoryManager()
