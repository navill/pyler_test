from django.urls import path

from images import views

urlpatterns = [
    path('<uuid:identifier>/', views.ImageRetrieveDestroyAPIView.as_view(),
         name="image-detail"),
    path('<uuid:identifier>/categories/', views.ImageCategoriesAPIView.as_view(),
         name="image-categories"),
    path('<uuid:identifier>/categories/add/', views.ImageCategoryAddAPIView.as_view(),
         name="image-category-add"),
    path('<uuid:identifier>/categories/remove/', views.ImageCategoryRemoveAPIView.as_view(),
         name="image-category-remove"),
    path('', views.ImageListCreateAPIView.as_view(), name="image-list-create"),
]
