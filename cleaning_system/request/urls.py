
from  django.urls  import path
from .views  import  RequestList,  RequestDetail
urlpatterns = [
    path('request/', RequestList.as_view()),
   path('request/<int:pk>/',RequestDetail.as_view() ),
]