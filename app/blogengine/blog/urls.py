from django.urls import path
from .views import *


urlpatterns = [
    path('', posts_list, name='blog_posts_list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='blog_post_detail'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='blog_tag_detail'),
    path('tag/', tag_list, name='blog_tag_list'),
]
