from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
	re_path(r'ws/forum/?P<room_name>/w+)/$', consumer.as_asgi()),
]
