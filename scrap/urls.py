from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
   # path('', views.imagedisplay),
    path('', views.homepage),
    path("community", views.community, name="community"),
    path("register/", views.register, name="register"),
    path("actionUrl", views.comment_request),
    path("chatuser/", views.chatuser_request, name="chatuser"),
    path("comment/", views.comment_request, name="comment"),
    path("logout", views.logout_request, name="logout"), 
    path("login", views.login_request, name="login"),
    path("<single_slug>", views.single_slug, name="single_slug"),
    #path("api/item/", views.ItemListCreate.as_view() ),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
