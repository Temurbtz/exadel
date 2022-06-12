from django.urls import path
from  .views  import ServiceViewSet
urlpatterns=[
    path('company/<int:company_id>/service/',ServiceViewSet.as_view({'post':'create'})),
    path('company/<int:company_id>/service/<int:service_id>/', ServiceViewSet.as_view({'put':'update','delete':'destroy','get':'retrieve'}))
]
