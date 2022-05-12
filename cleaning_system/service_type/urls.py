from django.urls import path,  include
from .views  import  service_list, service_detail

urlpatterns = [
    path('service/', service_list),
    path('service/<int:pk>/',service_detail ),
]