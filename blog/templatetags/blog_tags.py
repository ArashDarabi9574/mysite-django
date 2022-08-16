from os import stat
from django import template
from blog.models import Post
register = template.Library()

@register.simple_tag(name="totalposts")
def totalposts():
     posts = Post.objects.filter(status=1).count()
     return posts

@register.inclusion_tag('blog/blog-popular-post.html')
def latestpost():
     posts = Post.objects.filter(status=1).order_by('published_at')[:4]
     return {'posts': posts}