from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("pyeler_admin/", admin.site.urls),
    path("api/categories/", include("categories.urls")),
    path("api/images/", include("images.urls")),
    path("api/users/", include("pyler_users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns.extend([
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ])
