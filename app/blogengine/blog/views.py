from django.shortcuts import render
from django.views.generic import View
from .models import *
from .utils import ObjectDetailMixin


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', context={'posts': posts})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', context={'tags': tags})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

