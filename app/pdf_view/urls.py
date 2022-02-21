# → Here are the URLs for views within pdf_view.
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('pdf_view',views.pdf_view,name='pdf_view')
]