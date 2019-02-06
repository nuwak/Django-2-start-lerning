from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db import models


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectListMixin:
    model: models.Model = None

    def tag_list(self, request):
        tags = self.model.objects.all()
        return render(request, 'blog/tag_list.html', context={'tags': tags})
