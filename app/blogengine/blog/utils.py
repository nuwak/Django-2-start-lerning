from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Model


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectListMixin:
    model: Model = None

    def get(self, request):
        model_name = self.model.__name__.lower()
        items = self.model.objects.all()
        return render(request, 'blog/{}_list.html'.format(model_name), {'items': items})
