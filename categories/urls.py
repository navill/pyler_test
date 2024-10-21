from django.urls import path

from categories import views

urlpatterns = [
    path("<str:name>/", views.CategoryDestroyAPIView.as_view(), name="category-delete"),
    path("", views.CategoryListCreateAPIView.as_view(), name="category-list-create"),
]
