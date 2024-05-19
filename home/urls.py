from django.contrib import admin
from django.urls import path
from .views import index, search
from . import views

# from django.urls import path
# from .views import search, home  

urlpatterns = [
    #path('', home, name='home'),
    path('search/', search, name='search'),
    path('', views.index, name='home')
]