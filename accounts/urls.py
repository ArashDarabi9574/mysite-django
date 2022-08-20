from django.urls import path
from accounts.views import *
app_name = 'accounts'
urlpatterns = [
     path('login',login_view, name='login'),
     #login
     # path('logout',views.logout_view, name='logout'),
     # #logout
     path('signup',signup_view, name='signup'),
     #signup

]
