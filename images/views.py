from django.db.models import QuerySet
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request

from categories.serializers import CategoryAddRemoveSerializer
from core.custom_drf.generics import ListCreateAPIView, RetrieveDestroyAPIView, GenericAPIView
from core.custom_drf.mixins import RetrieveModelMixin
from core.permissions import IsOwner
from images.mixins import ModificationMixin
from images.models import Image
from images.serializers.requests import ImageUploadSerializer
from images.serializers.responses import ImageResponseSerializer, ImageCategoriesResponseSerializer, \
    ImageListResponseSerializer


@extend_schema_view(get=extend_schema(responses=ImageListResponseSerializer,
                                      description="관리자일 경우 전체 이미지가, 사용자일 경우 사용자가 올린 이미지만 표시됩니다."),
                    post=extend_schema(request=ImageUploadSerializer,
                                       responses=ImageListResponseSerializer,
                                       description="이미지를 올립니다"))
class ImageListCreateAPIView(ListCreateAPIView):
    queryset = Image.objects.all()
    request_serializer_class = ImageUploadSerializer
    response_serializer_class = ImageListResponseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) -> QuerySet:
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        return queryset.filter(user=self.request.user)


@extend_schema_view(get=extend_schema(responses=ImageResponseSerializer,
                                      description="카테고리를 포함한 이미지를 표시합니다."))
class ImageRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Image.objects.prefetch_related("category_set")
    response_serializer_class = ImageResponseSerializer
    lookup_field = "identifier"
    permission_classes = [IsOwner | IsAdminUser]


@extend_schema_view(get=extend_schema(responses=ImageCategoriesResponseSerializer,
                                      description="간단한 이미지 정보와 이미지에 포함된 카테고리를 표시합니다."))
class ImageCategoriesAPIView(RetrieveModelMixin,
                             GenericAPIView):
    queryset = Image.objects.prefetch_related("category_set")
    response_serializer_class = ImageCategoriesResponseSerializer
    lookup_field = "identifier"
    permission_classes = [IsOwner | IsAdminUser]


@extend_schema_view(post=extend_schema(request=CategoryAddRemoveSerializer,
                                       responses=ImageCategoriesResponseSerializer,
                                       description="이미지에서 카테고리를 추가합니다."))
class ImageCategoryAddAPIView(ModificationMixin, GenericAPIView):
    queryset = Image.objects.prefetch_related("category_set")
    request_serializer_class = CategoryAddRemoveSerializer
    response_serializer_class = ImageCategoriesResponseSerializer
    lookup_field = "identifier"
    permission_classes = [IsOwner | IsAdminUser]

    def post(self, request: Request, *args, **kwargs):
        return self._modify(request, "add")


@extend_schema_view(post=extend_schema(request=CategoryAddRemoveSerializer,
                                       responses=ImageCategoriesResponseSerializer,
                                       description="이미지에서 카테고리를 제거합니다."))
class ImageCategoryRemoveAPIView(ModificationMixin, GenericAPIView):
    queryset = Image.objects.prefetch_related("category_set")
    request_serializer_class = CategoryAddRemoveSerializer
    response_serializer_class = ImageCategoriesResponseSerializer
    lookup_field = "identifier"
    permission_classes = [IsOwner | IsAdminUser]

    def post(self, request: Request, *args, **kwargs):
        return self._modify(request, "remove")
