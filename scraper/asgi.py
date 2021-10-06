import os
import django
#from channels.routing import ProtocolTypeRouter
#from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import forum.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraper.settings')
django.setup()
application = ProtocolTypeRouter({
	"http": get_asgi_application(),
	"websocket": AuthMiddlewareStack(
		URLRouter(
			forum.routing.websocket_urlpatterns
		)
	),
})
