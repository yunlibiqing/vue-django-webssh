import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from websshapp.consumers import WebSSHService

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webssh_server.settings")

application = ProtocolTypeRouter({
  "websocket": AuthMiddlewareStack(
        URLRouter(
            [re_path(r'webssh/$', WebSSHService.as_asgi()),]
        )
    ),
})