# → Here are the URLs for views within teacher.
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('teacher',views.teacher,name='teacher')
]