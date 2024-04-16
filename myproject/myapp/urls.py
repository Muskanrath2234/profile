from django.urls import path
from .views import *
urlpatterns = [
  path('home/',index,name="home"),
  path('Profile/',Profile,name="Profile"),
  path('',login_user,name="login"),
  path('register/',register_user,name="register"),
  path('logout/',logout_user,name="logout"),
]