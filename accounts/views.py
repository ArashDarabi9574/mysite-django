import email
from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.forms import SignUpForm, LoginForm
# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST) 
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        form = AuthenticationForm()
        context = {'from' : form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
