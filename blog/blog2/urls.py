from django.contrib import admin
from django.urls import path, include
from . import views as v1

urlpatterns = [
path("", v1.index, name="index"), 
path("blogs", v1.projects, name="Projects"),
path("create", v1.create, name="Create Blog"),
path("<int:id>", v1.blogview, name="Create Blog"),
path("edit/<int:id>", v1.updateview, name="Update Blog"),
path("search", v1.search, name="Search"),

]
