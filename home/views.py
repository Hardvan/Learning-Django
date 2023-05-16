from django.shortcuts import render, HttpResponse

# render is used for static files

# Type /static/test.txt to see the contents of test.txt in the browser


# Create your views here.
def index(request):

    # return HttpResponse("Hello, World!")

    # Render the index.html file in the templates folder
    return render(request, "index.html")


def about(request):
    return HttpResponse("Welcome to the About Page")


def services(request):
    return HttpResponse("Welcome to the Services Page")


def contact(request):
    return HttpResponse("Welcome to the Contact Page")
