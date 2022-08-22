from django.urls import path
from accounts.views import *
app_name = 'signup'
urlpatterns = [
     #login
     #logout
     path('signup',signup_view, name='signup'),
     #signup

]
