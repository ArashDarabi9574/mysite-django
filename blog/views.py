import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_view(response):
    posts = Post.objects.filter(published_at__lte=datetime.datetime.now())
    context = {'posts': posts}
    return render(response, 'blog/blog-home.html', context)


def blog_single_view(response, pid):
    posts = Post.objects.filter(published_at__lte=datetime.datetime.now())
    post = get_object_or_404(posts, pk=pid, status=1)
    context = {'post': post}
    return render(response, 'blog/blog-single.html', context)
