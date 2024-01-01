from django.urls import re_path
from . import consumers


websocket_urlpatterns = [
    re_path(r"ws/turnow/$", consumers.TurnWebSocket.as_asgi()),
]
# All conections to ws://localhost:8000/ws/chat/
# will create an instance of TurnWebSocket.
