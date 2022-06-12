from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/comment/<int:company_id>/', consumers.CommentConsumer.as_asgi()),
]
