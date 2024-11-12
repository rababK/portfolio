
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path("index/", views.index, name="index"),
   path("blog/<int:id>/", views.blogDetails, name="blog"),
   path("project/<int:id>/", views.projectDetails, name="project"),
    path('contact/', views.contact, name='contact'),
 
  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

