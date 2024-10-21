from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer, \
    TokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.custom_drf.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from pyler_users.models import PylerUser
from pyler_users.serializers.requests import RegisterRequestSerializer
from pyler_users.serializers.responses import RegisterResponseSerializer, PylerUserSerializer


@extend_schema_view(post=extend_schema(request=TokenObtainSerializer, responses=TokenObtainPairSerializer))
class LoginAPIView(TokenObtainPairView):
    permission_classes = [AllowAny]


@extend_schema_view(post=extend_schema(request=RegisterRequestSerializer, responses=RegisterResponseSerializer))
class RegisterAPIView(CreateAPIView):
    request_serializer_class = RegisterRequestSerializer
    response_serializer_class = RegisterResponseSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_request_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = PylerUser.objects.create_user(**serializer.data)

        response_serializer = self.get_response_serializer(instance=user)
        headers = self.get_success_headers(response_serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@extend_schema_view(post=extend_schema(request=TokenRefreshSerializer, responses=TokenRefreshSerializer))
class RefreshTokenAPIView(TokenRefreshView):
    permission_classes = [AllowAny]


@extend_schema_view(get=extend_schema(responses=PylerUserSerializer))
class PylerUserListAPIView(ListAPIView):
    queryset = PylerUser.objects.all()
    response_serializer_class = PylerUserSerializer
    permission_classes = [IsAdminUser]


@extend_schema_view(get=extend_schema(responses=PylerUserSerializer))
class PylerUserAPIView(RetrieveAPIView):
    queryset = PylerUser.objects.all()
    response_serializer_class = PylerUserSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'identifier'
