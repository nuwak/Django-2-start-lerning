from django.urls import path
from .views import *


urlpatterns = [
    path('', posts_list, name='blog_posts_list'),
    path('post/<str:slug>/', post_detail, name='blog_post_detail'),
]
