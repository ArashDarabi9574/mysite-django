from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponse

def index_view(response):
     return HttpResponse('<h1>HOME</h1>')

def about_view(response):
     return HttpResponse('<h1>ABOUT</h1>')

def contact_view(response):
     return HttpResponse('<h1>CONTACT</h1>')