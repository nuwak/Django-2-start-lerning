from django.shortcuts import redirect


def home(request):
    return redirect('blog_posts_list', permanent=True)
