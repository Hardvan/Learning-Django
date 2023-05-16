from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, World!")


def about(request):
    return HttpResponse("Welcome to the About Page")


def services(request):
    return HttpResponse("Welcome to the Services Page")


def contact(request):
    return HttpResponse("Welcome to the Contact Page")
