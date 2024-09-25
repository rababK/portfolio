
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path("index/", views.index, name="index"),
   path("blog/<int:id>/", views.blogDetails, name="blog"),
   path("project/<int:id>/", views.projectDetails, name="project"),
  
]
