from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/<str:uuid>/', consumers.NotificationConsumer.as_asgi()),
]
