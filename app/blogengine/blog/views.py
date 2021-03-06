from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import View
from .utils import *
from .forms import *


def post_list(request):
    model_name = 'post'
    search_query = request.GET.get('search', '')

    if search_query:
        items = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        items = Post.objects.all()

    return render(request, f'blog/{model_name}_list.html', {'items': items, 'search_query': search_query})


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
