from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .utils import *
from .forms import *


class PostList(ObjectListMixin, View):
    model = Post


class TagList(ObjectListMixin, View):
    model = Tag


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    Form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    Form = TagForm
    template = 'blog/tag_update.html'
    model = Tag
    raise_exception = True


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    Form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    Form = PostForm
    template = 'blog/post_update.html'
    model = Post
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect = 'blog_posts_list'
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect = 'blog_tag_list'
    raise_exception = True
