from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]

from django.urls import path
from .views import search, home  

urlpatterns = [
    path('', home, name='home'),
    path('search/', search, name='search'),
]