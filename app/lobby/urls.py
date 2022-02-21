# → Here are the URLs for views within lobby.
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home')
]