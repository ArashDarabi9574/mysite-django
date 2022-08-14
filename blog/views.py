import datetime
from django.shortcuts import render
from blog.models import Post


def blog_view(response):
    posts = Post.objects.filter(published_at__lte=datetime.datetime.now())
    context = {'posts': posts}
    
    return render(response, 'blog/blog-home.html', context)


def blog_single_view(response):
    return render(response, 'blog/blog-single.html')
