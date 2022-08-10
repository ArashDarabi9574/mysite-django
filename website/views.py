from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse


def index_view(response):
    return render(response, 'website/index.html')


def about_view(response):
    return render(response, 'website/about.html')


def contact_view(response):
    return render(response, 'website/contact.html')


def elemntry_view(response):
    return render(response, 'website/elements.html')
