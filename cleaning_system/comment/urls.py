from  django.urls  import path
from .views  import  CommentViewSet
urlpatterns=[
    path('company/<int:company_id>/comment/',CommentViewSet.as_view({'get':'list'})),
    path('comment/<int:pk>/', CommentViewSet.as_view({'delete':'destroy','put':'update'})),
]
