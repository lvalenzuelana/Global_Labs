# → Here are the URLs for views within signup.
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('signup',views.signup,name='signup')
]