from django.shortcuts import render

def blog_view(response):
     return render(response, 'blog/blog-home.html')

def blog_single_view(response):
     return render(response, 'blog/blog-single.html')
