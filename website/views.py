from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse

def index_view(response):
     return render(response, 'index.html')

def about_view(response):
     return render(response, 'about.html')

def contact_view(response):
     return render(response, 'contact.html')