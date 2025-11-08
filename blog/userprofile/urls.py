from django.contrib import admin
from django.urls import path, include
from . import views as pv
from blog import settings
from django.conf.urls.static import static

urlpatterns = [


path("", pv.userprofile, name="Profile"),
path("edit", pv.edituserprofile, name="Edit Profile"),
path("editbg", pv.edituserbg, name="Edit Profile"),
path("<str:user>", pv.otheruser, name="Profile"),
path("<str:user>/liked", pv.likeview, name="Profile"),
path("<str:user>/settings", pv.settings, name="Profile"),
]