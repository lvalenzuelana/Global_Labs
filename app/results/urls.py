# → Here are the URLs for views within results.
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('results',views.results,name='results')
]