from django.urls import path
from .views import *


urlpatterns = [
    path('', PostList.as_view(), name='blog_posts_list'),
    path('post/<str:slug>/', PostDetail.as_view(), name='blog_post_detail'),
    path('tag/', TagList.as_view(), name='blog_tag_list'),
    path('tag/create/', TagCreate.as_view(), name='blog_tag_create'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='blog_tag_detail'),
]
