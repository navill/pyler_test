import uuid

from django.db import models

from core.models import BaseModel
from images.managers import ImageManager
from pyler_users.models import PylerUser


class Image(BaseModel):
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name="이미지 식별자")
    user = models.ForeignKey(to=PylerUser, on_delete=models.DO_NOTHING, verbose_name="업로더")
    image_file = models.ImageField(upload_to="images/%Y%m%d", verbose_name="이미지 파일")
    thumbnail = models.ImageField(upload_to="images/%Y%m%d/thumbnails", verbose_name="이미지 썸네일")
    description = models.TextField(null=True, blank=True, verbose_name="설명")

    objects = ImageManager()


