from django.urls import path
from . import views
from django.conf.urls.static import static
from ..scraper import settings

urlpatterns = [
    path('', views.index ),
]

urlpatterns += static(settings.STATIC_FRONT_URL, document_root=settings.STATIC_FRONT_ROOT)
