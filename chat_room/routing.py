from django.urls import re_path
from . import consumer

websocket_patterns = [
    re_path(
        r"ws/chat/global/$",
        consumer.GlobalChatConsumer.as_asgi()
    )
]