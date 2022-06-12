
from django.contrib import admin
from django.urls import path,  include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from  django.conf  import  settings
schema_view = get_schema_view(
   openapi.Info(
      title="CLEANING  SYSTEM  API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.ourapp.com/policies/terms/",
      contact=openapi.Contact(email="contact@cleaning_system.local"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
   path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include('service.urls')),
    path('',include('company.urls')),
    path('', include('request.urls')),
    path('', include('comment.urls')),
     path('', include('comment.urls')),
     path('',  include('search.urls')),
     path('',  include('notification.urls')),
   
   
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
  
 
  
]



