from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.permissions import IsAdminUser

from categories.models import Category
from categories.serializers import CategorySerializer
from core.custom_drf.generics import ListCreateAPIView, DestroyAPIView


@extend_schema_view(
    get=extend_schema(responses=CategorySerializer,
                      description="카테고리 리스트를 표시합니다."),
    post=extend_schema(request=CategorySerializer,
                       responses=CategorySerializer,
                       description="카테고리를 생성합니다"))
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    pagination_class = None


@extend_schema_view(delete=extend_schema(description="카테고리를 삭제합니다."))
class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    lookup_field = "name"
    permission_classes = [IsAdminUser]
