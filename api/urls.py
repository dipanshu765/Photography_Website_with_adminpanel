from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes),
    path('content', views.getContent),
    path('team', views.getTeam),
    path('blog', views.getBlog),
    path('gallery', views.getGallery),
    path('contact', views.getContact),
]
