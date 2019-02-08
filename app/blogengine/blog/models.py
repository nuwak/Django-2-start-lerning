from django.db import models
from django.shortcuts import reverse

from .utils import gen_slug


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def get_absolute_url(self):
        return reverse('blog_post_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('blog_post_update', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.slug)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.slug)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_tag_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('blog_tag_update', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
