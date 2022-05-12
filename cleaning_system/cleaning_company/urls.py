
from django.urls import path,  include
from .views  import  company_list,  company_detail

urlpatterns = [
    path('company/', company_list),
   path('company/<int:pk>/',company_detail ),
]