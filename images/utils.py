import uuid
from io import BytesIO

from PIL import Image as PillowImage
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile


def resize_image(image_file: PillowImage, width: int) -> PillowImage:
    resized_height = round(width * float(image_file.height / image_file.width))
    return image_file.resize((width, resized_height))


def rename_filename(file_name: str, prefix: str = "", postfix: str = "") -> str:
    file_name, ext = file_name.rsplit(".", 1)
    last_uuid = str(uuid.uuid4()).split("-")[-1]
    if prefix:
        file_name = f"{prefix}_{file_name}"
    if postfix:
        file_name = f"{file_name}_{postfix}"
    return f"{file_name}_{last_uuid}.{ext}"


def create_thumbnail(image_field: InMemoryUploadedFile) -> ContentFile:
    image_file = PillowImage.open(image_field)
    resized_image = resize_image(image_file, settings.THUMBNAIL_WIDTH)

    with BytesIO() as image_io:
        resized_image.save(image_io, format=image_file.format, quality=100)
        thumbnail = ContentFile(image_io.getvalue(), name=image_field.name)
    return thumbnail
