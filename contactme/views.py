from django.shortcuts import render
from django.contrib import messages
from .forms import ContactRequestForm


def contact_me(request):
    """
    Renders the About page
    """
    if request.method == "POST":
        contactme_form = ContactRequestForm(data=request.POST)
        if contactme_form.is_valid():
            contactme_form.save()
            messages.add_message(request, messages.SUCCESS, "Your contact request received! I endeavour to respond within 2 working days.")

    contactme_form = ContactRequestForm()


    return render(
        request,
        "contactme/contactme.html",
        {"contactme_form": contactme_form,},
    )