from django.contrib import admin
from django.urls import path, include
from . import views
from blog import settings
from django.conf.urls.static import static

urlpatterns = [
path("", views.index, name="index"), 
path("home", views.home, name="Home"),
path("register", views.sign_up, name="Create Account"),
path("login", views.sign_in, name="Login"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


