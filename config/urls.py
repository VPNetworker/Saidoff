from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.static import serve

schema_view = get_schema_view(
    openapi.Info(
        title="Saidoff Portfolio API",
        default_version='v1',
        description="Swagger for getting data for saidoff.uz",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="saidoffgroup@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    url=settings.BASE_URL
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),
    # path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

