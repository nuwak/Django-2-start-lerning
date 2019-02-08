from time import time

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db.models import Model
from django.urls import reverse
from django.utils.text import slugify
from django.forms import ModelForm


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


class ObjectCreateMixin:
    Form = None
    template = None

    def get(self, request):
        return render(request, self.template, {'form': self.Form})

    def post(self, request):
        bound_form = self.Form(request.POST)

        if bound_form.is_valid():
            new_item = bound_form.save()
            return redirect(new_item)

        return render(request, self.template, {'form': bound_form})


class ObjectUpdateMixin:
    Form = None
    template: str = None
    model: Model = None

    def get(self, request, slug):
        model = self.model.objects.get(slug__iexact=slug)
        form = self.Form(instance=model)

        return render(request, self.template, {'form': form, 'model': model})

    def post(self, request, slug):
        model = self.model.objects.get(slug__iexact=slug)
        bound_form = self.Form(request.POST, instance=model)

        if bound_form.is_valid():
            new_item = bound_form.save()
            return redirect(new_item)

        return render(request, self.template, {'form': bound_form, 'model': model})


def gen_slug(s: str) -> str:
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time() * 10000))


class ObjectDeleteMixin:
    template: str = None
    model: Model = None
    redirect: str = None

    def get(self, request, slug):
        model = get_object_or_404(self.model, slug__iexact=slug)

        return render(request, self.template, {'model': model})

    def post(self, request, slug):
        get_object_or_404(self.model, slug__iexact=slug).delete()

        return redirect(reverse(self.redirect))

