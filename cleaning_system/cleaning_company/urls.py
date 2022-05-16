
from django.urls import path,  include
from  .views  import  CompanyViewSet
urlpatterns = [
   path('company/', CompanyViewSet.as_view({'get': 'list','post':'create'})),
   path('company/<int:pk>/',CompanyViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
]