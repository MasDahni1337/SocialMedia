from functools import partial
from os import name
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.masuk, name='login'),
    path('', views.index, name='index'),
    path('daftar/', views.daftar, name='signup'),
]