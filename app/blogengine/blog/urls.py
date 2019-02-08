from django.urls import path
from .views import *


urlpatterns = [
    path('', post_list, name='blog_posts_list'),
    path('post/create/', PostCreate.as_view(), name='blog_post_create'),
    path('post/<str:slug>/', PostDetail.as_view(), name='blog_post_detail'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='blog_post_update'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='blog_post_delete'),
    path('tag/', TagList.as_view(), name='blog_tag_list'),
    path('tag/create/', TagCreate.as_view(), name='blog_tag_create'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='blog_tag_detail'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='blog_tag_update'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='blog_tag_delete'),
]
