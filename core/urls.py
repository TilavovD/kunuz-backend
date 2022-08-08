from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from news.views import CategoryNewsView, RegionNewsView


schema_view = get_schema_view(
   openapi.Info(
      title="Kun.uz API",
      default_version='v1',
      description="This is a test project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('news/', include('news.urls')),
    path("audio/", include('audio.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("api/", include('rest_framework.urls')),
    path("category/<str:slug>", CategoryNewsView.as_view()),
    path("region/<str:slug>", RegionNewsView.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),
    path("", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]