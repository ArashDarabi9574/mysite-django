from django.http import HttpResponse
from django.http import HttpResponse

def http_test(response):
     return HttpResponse('<h1>hello django</h1>')