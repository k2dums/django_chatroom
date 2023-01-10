from django.urls import re_path
from . import consumer

websocket_urlpatterns=[
    re_path(r"ws/as_chat/(?P<room_name>\w+)/$",consumer.AsyncChatConsumer.as_asgi())
]