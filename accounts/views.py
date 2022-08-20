from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.


def login_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'accounts/login.html')


# def logout_view(response):
#     pass


def signup_view(response):
    return render(response, 'accounts/signup.html')