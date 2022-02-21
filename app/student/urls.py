# → Here are the URLs for views within student.
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('student',views.student,name='student')
]