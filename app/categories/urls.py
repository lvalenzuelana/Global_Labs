# → Here are the URLs for views within categories.
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('categories',views.categories,name='categories')
]