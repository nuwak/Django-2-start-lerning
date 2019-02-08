from django.contrib import admin

# Register your models here.
from .models import Post

# see https://djbook.ru/rel1.9/intro/tutorial07.html#adding-related-objects
admin.site.register(Post)

