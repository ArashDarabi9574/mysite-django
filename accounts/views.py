from django.shortcuts import render

# Create your views here.


def login_view(response):
    return render(response, 'accounts/login.html')


# def logout_view(response):
#     pass


def signup_view(response):
    return render(response, 'accounts/signup.html')
