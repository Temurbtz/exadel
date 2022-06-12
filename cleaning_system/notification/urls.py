from  django.urls import path   
from .views  import update_status
urlpatterns=[
    path('notification/<int:pk>/',update_status)
]
