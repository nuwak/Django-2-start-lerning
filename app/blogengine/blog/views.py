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


class TagCreate(ObjectCreateMixin, View):
    Form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    Form = TagForm
    template = 'blog/tag_update.html'
    model = Tag


class PostCreate(ObjectCreateMixin, View):
    Form = PostForm
    template = 'blog/post_create.html'


class PostUpdate(ObjectUpdateMixin, View):
    Form = PostForm
    template = 'blog/post_update.html'
    model = Post


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect = 'blog_posts_list'


class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect = 'blog_tag_list'
