from  django.urls  import path  
from  .views  import  RequestViewSet
urlpatterns=[
    path('request/company/<int:company_id>/service/<int:service_id>/', RequestViewSet.as_view({'post':'create'})),
     path('request/<int:request_id>/', RequestViewSet.as_view({'delete':'destroy','put':'update'})),
     path('request/',RequestViewSet.as_view({'get':'list'})),

]
