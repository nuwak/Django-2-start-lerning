from django.shortcuts import redirect
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


class TagCreate(View):
    def get(self, request):
        form = TagForm
        return render(request, 'blog/tag_create.html', {'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        try:
            new_tag = bound_form.save()
        except ValueError:
            return render(request, 'blog/tag_create.html', {'form': bound_form})

        return redirect(new_tag)
