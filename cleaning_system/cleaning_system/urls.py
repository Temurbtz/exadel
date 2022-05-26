
from django.contrib import admin
from django.urls import path,  include
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from  django.conf  import  settings
import  debug_toolbar
schema_view = get_schema_view(
   openapi.Info(
      title="Cleaning  System API",
      default_version='v1',
      description="An  api for cleaning  system",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@cleaningsystem.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('',include('cleaning_company.urls')),
    path('',include('rating_review.urls')),
    path('',include('service_type.urls')),
     path('',include('request.urls')),

 
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   path('__debug__/', include('debug_toolbar.urls')),
]



