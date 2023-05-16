from django.shortcuts import render, HttpResponse

# render is used for static files

# Type /static/test.txt to see the contents of test.txt in the browser


# Create your views here.
def index(request):

    # context is a dictionary that contains variables that are passed to the index.html file
    context = {
        "variable1": "I am variable1",
        "variable2": "I am variable2",
        "variable3": "I am variable3",
    }

    # Render the index.html file in the templates folder
    return render(request, "index.html", context)


def about(request):

    return render(request, "about.html")


def services(request):

    return render(request, "services.html")


def contact(request):

    return render(request, "contact.html")
