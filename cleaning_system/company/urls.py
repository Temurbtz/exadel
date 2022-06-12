from  django.urls  import path
from  .views  import CompanyViewSet,  RatingViewSet
urlpatterns=[
    path('company/<int:pk>/',CompanyViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
     path('company/',CompanyViewSet.as_view({'post':'create'})),
     path('company/<int:company_id>/rating/',RatingViewSet.as_view({'post':'create','put':'update'})),
     
    
]
