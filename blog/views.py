import datetime
from pickle import NONE
from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_view(response, cat_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(response, 'blog/blog-home.html', context)


def blog_single_view(response, pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid, status=1)
    post.content_view +=1
    post.save()
    nextpost = Post.objects.filter(id__gt=post.pk ).order_by('pk').first()
    prevpost = Post.objects.filter(id__lt=post.pk).order_by('pk').last()
    context = {'post': post, 'nextpost': nextpost, 'prevpost': prevpost}

    return render(response, 'blog/blog-single.html', context)

def blog_category(response, cat_name):
    post = Post.objects.filter(status=1)
    post = post.filter(category__name=cat_name)
    context = {'posts': post}
    return render(response, 'blog/blog-home.html', context)
