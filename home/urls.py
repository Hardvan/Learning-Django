from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # Go to views.py and run index function
    path('', views.index, name="home"),

]
