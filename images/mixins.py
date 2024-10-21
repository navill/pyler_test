from typing import Literal

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from categories.models import Category
from images.models import Image


class ModificationMixin:
    def _modify(self, request: Request, func_name: Literal["add", "remove"]):
        instance: Image = self.get_object()
        serializer = self.get_request_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = Category.objects.get(name=serializer.data["name"])

        modify_func = getattr(instance, func_name)
        modify_func(category)

        instance.refresh_from_db()
        response_serializer = self.get_response_serializer(instance)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)