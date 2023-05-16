from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # For /, run index function in views.py
    path('', views.index, name="home"),

    # For /about, run about function in views.py
    path("about", views.about, name="about"),

    path("services", views.services, name="services"),
]
