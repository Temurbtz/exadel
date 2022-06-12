from django.urls import  path
from  .views  import search_create
urlpatterns=[
    path('search/',search_create)
]

