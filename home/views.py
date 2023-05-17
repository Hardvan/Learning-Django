from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# For displaying messages
from django.contrib import messages

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

    # messages.success(request, "This is a test message")

    # Render the index.html file in the templates folder
    return render(request, "index.html", context)


def about(request):

    return render(request, "about.html")


def services(request):

    return render(request, "services.html")


def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        date = datetime.today()

        contact = Contact(name=name, email=email,
                          phone=phone, desc=desc, date=date)

        # Save the contact object to the database
        contact.save()

        messages.success(request, "Your message has been sent!")

    return render(request, "contact.html")
