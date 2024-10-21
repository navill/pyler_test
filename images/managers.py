from core.managers import BaseManager
from images.utils import create_thumbnail, rename_filename


class ImageManager(BaseManager):
    def create(self, **kwargs):
        if image_file := kwargs.get("image_file"):
            image_file.name = rename_filename(image_file.name)
            kwargs["thumbnail"] = create_thumbnail(image_file)
        return super().create(**kwargs)
