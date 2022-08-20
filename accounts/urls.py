from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
     path('login',views.login_view, 'login'),
     #login
     # path('logout',views.logout_view, 'logout'),
     # #logout
     path('signup',views.signup_view, 'signup'),
     #signup

]
