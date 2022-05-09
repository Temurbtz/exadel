from django.urls import path
from  .views  import  ProductCreateView,  ProductListView, ProductDeleteView,  ProductUpdateView


urlpatterns = [
    path('', ProductListView.as_view(), name='read'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<pk>/delete/',ProductDeleteView.as_view(),name='delete'),
     path('<pk>/update/',ProductUpdateView.as_view(),name='update'),
]