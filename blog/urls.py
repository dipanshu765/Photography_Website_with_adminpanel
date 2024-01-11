from django.urls import path
from . import views

app_name = 'blog'


urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('blogs/<str:blog_id>/', views.blog_page, name='blog_page'),
]