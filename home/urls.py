from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    # For /, run index function in views.py
    path('', views.index, name="home"),

    # For /about, run about function in views.py
    path("about", views.about, name="about"),

    # For /services, run services function in views.py
    path("services", views.services, name="services"),

    # For /contact, run contact function in views.py
    path("contact", views.contact, name="contact"),
]
