from django.urls import path

from pyler_users import views

urlpatterns = [
    path('auth/login/', views.LoginAPIView.as_view(), name='login'),
    path('auth/register/', views.RegisterAPIView.as_view(), name='join'),
    path('auth/refresh/', views.RefreshTokenAPIView.as_view(), name='refresh'),

    path('<uuid:identifier>/', views.PylerUserAPIView.as_view(), name='user'),
    path('', views.PylerUserListAPIView.as_view(), name='user_list'),
]
